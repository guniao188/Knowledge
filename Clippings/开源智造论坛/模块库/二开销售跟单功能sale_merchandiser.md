---
title: "二开销售跟单功能sale_merchandiser"
source: "http://www.thinkltd.cn/forum/2/sale-merchandiser-3309"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开销售跟单功能sale_merchandiser

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/sale-merchandiser-3309>

模块链接：OSCG_SVN\odoo_ecommerce\13.0SRC\外贸跟单\sale_merchandiser

11.0版：[/forum/2/question/sale-merchandiser-2496](http://www.thinkltd.cn/forum/2/question/sale-merchandiser-2496)

    * SO表单右上角增加按钮“采购”，点击显示 源单据 为该SO的PO列表
    * 销售订单SO上增加字段： PO日期(po_date)，PL日期(pl_date)，CI日期(ci_date)，到款日期(payment_date)。增加服务器动作“销售跟单更新”，更新SO上此三个日期。
```python
      PO日期(po_date)：源单据为该SO的PO的确认日期，取最近的PO日期
      PL日期(pl_date)：源单据为该SO的PO的入库单完成日期，取最近的入库单日期
      CI日期(ci_date)：该SO的Invoice的确认日期，取最近的Invoice日期
      到款日期(payment_date)：该SO的Invoice的收款日期，取最近的收款日期
```

    * 销售模块增加菜单“销售跟单”，显示销售订单SO及其PO的关键节点日期
    * 销售表单增加出发港、到达港字段，销售配置中增加港口表单配置

## 补充/答案 1

![[2-sale-merchandiser-3309-89264ce7.png]]

![[2-sale-merchandiser-3309-89264ce7.png]]

安装了这个模块后，如果更改销售单数量增加会提示报错，改小则不会。

## 补充/答案 2

并不是此模块引发，是其他二开模块继承系统的这个def _action_launch_stock_rule()缺少一个previous_product_uom_qty=False这个参数

修改方法：

只要二开模块有继承def _action_launch_stock_rule(self)这个方法，修改为def _action_launch_stock_rule(self, previous_product_uom_qty=False),增加以下previous_product_uom_qty=False这个参数即可！

## 补充/答案 3

【功能截图】

![[2-sale-merchandiser-3309-5f135555.png]]

![[2-sale-merchandiser-3309-1bd0f1fb.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
