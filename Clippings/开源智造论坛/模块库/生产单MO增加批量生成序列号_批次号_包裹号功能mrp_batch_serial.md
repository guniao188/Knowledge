---
title: "生产单MO增加批量生成序列号/批次号/包裹号功能mrp_batch_serial"
source: "http://www.thinkltd.cn/forum/2/mo-mrp-batch-serial-3490"
forum: "模块库"
author: "肖相扶"
published: 2024-07-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 生产单MO增加批量生成序列号/批次号/包裹号功能mrp_batch_serial

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-07-16
> <http://www.thinkltd.cn/forum/2/mo-mrp-batch-serial-3490>

模块链接：OSCG_SVN\odoo_ecommerce\14.0SRC\生产制造\mrp_batch_serial

【版本升级】2023年3月16日，升级到16.0版本：OSCG_Git\extra-addons\mrp_batch_serial

同时新增功能：不仅可以批量产生入库的序列号码，也可以批量产生批次号码以及包裹号码，批量生成的包裹/批次数量可以再次修改。如下截图。

【20240709葛忠彪修正16.0版本Bug】

【20240711葛忠彪升级到17.0】链接：OSCG_Git\17.0\extra-addons\mrp_batch_serial

![[2-mo-mrp-batch-serial-3490-5da1723b.png]]

【业务背景】

1.  Odoo14生产单MO上的产成品序列号自动生成功能，每次点击“序列号”按钮生成一个序列号，而后必须验证完成MO，系统拆分MO。在拆出的新MO上再次重复操作。如果生产100件商品，要重复操作100次，这个操作难以接受。

2.  其次，系统产生产品序列号时候，用的是系统默认的批次/序列号的序号器（Sequence），希望生产产品的序列号有一个独立的序号器。

3.  MO产品有序列号管理，且组件中原料有批次管理，此种情况，MO组件的完成数量需要手工填写好，才能报工。希望可以自动填写完成数量，一次报工多个序列号产品。

【模块功能】

1.  本模块在MO上新增批量序列号生成的按钮，点击按钮弹窗批量生成序列号，生成的序列号可以编辑。

2.  MO验证完成时候，如果MO上有多个序列号，系统自动完工多个序列号产品（一个MO多个序列号）。

3.  如果组件中有批次管理产品，报工时候，系统自动填写组件的完成数，而不需要手工逐个填写。

4.  【2021年10月12日】序列号生成的Wizard上，增加首序列号字段，如果填写了，基于首序列号自动生成后续序列号。另外。序列号应用时候，新增功能：检查生成的序列号是否已经存在。

5.  【2021年10月14日】问题修正：带序列号的MO产生欠单时候，Odoo原本功能会自动设置欠单的待生产数 1，且自动按待产数量1填写原料的完成数量。这导致了一个问题：修改欠单的待产数量，验证完成时候，系统不会自动根据完工数量重新计算原料消耗数量。修改Odoo原来逻辑，安装本模块后，欠单时候，不自动填写欠单数量1 。

【功能截图】

![[2-mo-mrp-batch-serial-3490-472da204.png]]

## 补充/答案 1

这个功能和MO上的拆解功能冲突，拆解单上无法赋值序列号导致无法完成拆解单

建议直接手工创建拆解单

## 补充/答案 2

客户希望采用更简单点的方式来处理，有一个第三方app

https://apps.odoo.com/apps/modules/14.0/app_product_lot_auto_mrp/

经测试，官方作者的版本无法落地使用，有很多功能缺陷和问题。

请用肖总改造后的自研的版本。

## 补充/答案 3

肖总改造后的版本测试结果如下：
底下组件原料其中有一个有开启批次，产成品是用的序列号。

![[2-mo-mrp-batch-serial-3490-72a87f56.png]]

![[2-mo-mrp-batch-serial-3490-2636ae83.png]]

![[2-mo-mrp-batch-serial-3490-ff8b92ae.png]]

![[2-mo-mrp-batch-serial-3490-8ace3c74.png]]

![[2-mo-mrp-batch-serial-3490-031868e5.png]]

![[2-mo-mrp-batch-serial-3490-b4b8ead2.png]]

![[2-mo-mrp-batch-serial-3490-bb13ea65.png]]

![[2-mo-mrp-batch-serial-3490-69fd1749.png]]

支持分批的批量完成，并创建欠单，也支持整批入库完成。

同时支持明细行有开启批次序列号的功能。


## 附件

- [[附件/forum/2-mo-mrp-batch-serial-3490-V16-mrp_batch_serial.doc|V16-mrp_batch_serial.doc]] (276 KB)

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
