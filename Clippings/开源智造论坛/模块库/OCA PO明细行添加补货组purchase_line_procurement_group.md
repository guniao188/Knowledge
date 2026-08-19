---
title: "OCA PO明细行添加补货组purchase_line_procurement_group"
source: "http://www.thinkltd.cn/forum/2/oca-popurchase-line-procurement-group-2564"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA PO明细行添加补货组purchase_line_procurement_group

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-popurchase-line-procurement-group-2564>

模块链接：

12.0版：OSCG_SVN\odoo_ecommerce\12.0SRC\purchase_line_procurement_group_odoo12

OCA12.0版：
Odoo13.0版：

Odoo14.0版：OSCG_SVN\odoo_ecommerce\14.0SRC\仓库物流\purchase_line_procurement_group

OSCG_SVN\odoo_ecommerce\14.0SRC\仓库物流\purchase_line_procurement_group_sale

Odoo14.0版功能改善：1） 如果购买规则的“补货组传播”设置为“传播”，则补货组不仅传播到PO的group_id，也传播到PO Order Line的补货组上。2）PO确认生成入库单时候，同一个PO，不同补货组的明细行，归集到不同入库单（一个PO，多个入库单）[
](https://github.com/OCA/purchase-workflow/tree/13.0/purchase_line_procurement_group)

1.  PO Line上增加补货组字段

2.  增加逻辑，PO Line合并采购时候，如果补货组不同则不合并到一个Line

3.  PO Line产生Stock Move时候，补货组写入Stock Move，从而不同补货组归集到不同Picking（Odoo原本逻辑）

4.  purchase_line_procurement_group_sale 此模块在SO上显示SO补货组关联的PO：如果补货组的sale_id 字段为该SO，则显示PO Line的补货组为该补货组的所有PO

## 补充/答案 1

【功能截图】

PO Line上增加补货组字段

![[2-oca-popurchase-line-procurement-group-2564-669de4e0.png]]

SO上增加通过PO Line上补货组关联的PO：

![[2-oca-popurchase-line-procurement-group-2564-c24f74d9.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
