---
title: "通过SO贯穿生产MO/领料Picking/采购PO/入库Picking的解决办法"
source: "http://www.thinkltd.cn/forum/1/somo-picking-po-picking-757"
forum: "求助台"
author: "肖相扶"
published: 2024-05-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 通过SO贯穿生产MO/领料Picking/采购PO/入库Picking的解决办法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-05-10
> <http://www.thinkltd.cn/forum/1/somo-picking-po-picking-757>

下述SO跟单自动动作写入了模块： OSCG_SVN\odoo_ecommerce\14.0SRC\仓库物流\stock_mrp_tracking_so

【20240510周鸿飞升级到17.0版】17.0版位置：OSCG_GIT\extra-addons\17.0\stock_mrp_tracking_so

【模块功能】

1.      增加自动动作，补货组创建时候，如果有sale_id字段，则取销售订单的仓库的库位的下架库位中，“空闲”的库位写入此补货组。“空闲“是指，没被其他未完成的补货组占用的库位

2.      增加自动动作，生产MO创建时候，自动创建以 SO + 产品编码 为名的补货组，作为MO的补货组。且补货组的库位设置为SO的补货组库位

3.     将购买规则的补货组传播字段值改成 “传播” 选项

【业务背景】

按客人要求定制化生产行业，如杭州迅得电子、深圳五洲行，希望通过销售订单号（SO）贯穿整个生产和供应链，具体来说就是：

1) 因SO而产生的MO及其子MO上，都可以查看对应的SO

2) 生产领料单上可以查看对应的SO

3) 原料采购单上可以查看对应的SO

4) 原料采购入库单上可以查看对应的SO

【解决方案】

在Odoo14.0中测试，SO确认时候，MTO产生的MO的补货组默认是SO单号，该补货组又可以传递到子MO及生产领料单上（参考：[/forum/1/question/bommo-755](http://www.thinkltd.cn/forum/1/question/bommo-755)），原料采购PO的源文档上也会显示SO单号。但采购入库的Picking上没有任何SO单号信息（源文档和补货组显示的都是PO单号）。解决上述业务问题，可以考虑下面一些二开改造：

1) SO确认时候，生成的MO的补货组，用“SO单号 + 产品编码”，如此不仅可以追溯SO，还可以追溯SO上的哪个产品。此项需求可以创建一个自动动作实现，MO（模型mrp.production）创建时候触发该自动动作，自动动作原理是：如果MO的补货组上又销售订单(sale_id字段)，且MO的产品在该sale_id的产品明细行上，则说明该MO直接来自该SO，MO的补货组替换成新补货组“SO单号+产品ID”。参考代码如下：

```python
if record.procurement_group_id and record.procurement_group_id.sale_id:

  prt = record.product_id

  for line in record.procurement_group_id.sale_id.order_line:

    if line.product_id == prt:

      nm = "%s-%s" % (record.procurement_group_id.sale_id.name, prt.id)

      procurement = record.procurement_group_id.copy(default={

        'name': nm,

        'move_type': 'one',

      })

      record.write({'procurement_group_id': procurement.id})

      break
```

2) "购买"规则上的“补货组的传播”字段设置为“传播”，如此，不同补货组的MO引发的缺货采购单，因补货组不同，系统不合并PO，且PO上的补货组(group_id)字段值和MO的补货组相同。本例中也即，同一个SO上的不同产品，产生的MO的补货组（“SO单号 + 产品编码”）不同，采购PO也不同，采购PO上也有补货组“SO单号 + 产品编码”。

## 补充/答案 1

补充：

1、如果没有多库存的，安装此模块，需要先安装模块自动动作规则base_automation，

2、另外要补充模块mrp_procurement_fix，

3、然后到自动动作里失效“SO确认时候自动分配出库库位”，

4、修改自动动作“SO确认创建生产MO时候补货组以 SO+产品编码 为名”， 注释其中两行代码

5、生产单视图上修改，添加字段显示”补货组“

![[1-somo-picking-po-picking-757-591f650e.png]]

![[1-somo-picking-po-picking-757-ad175f81.png]]

![[1-somo-picking-po-picking-757-7ac8f866.png]]

================================================================================================================================================================================================================

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
