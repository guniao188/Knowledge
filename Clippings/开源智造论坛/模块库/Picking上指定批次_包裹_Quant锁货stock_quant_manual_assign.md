---
title: "Picking上指定批次/包裹/Quant锁货stock_quant_manual_assign"
source: "http://www.thinkltd.cn/forum/2/picking-quantstock-quant-manual-assign-2870"
forum: "模块库"
author: "肖相扶"
published: 2022-12-20
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Picking上指定批次/包裹/Quant锁货stock_quant_manual_assign

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-20
> <http://www.thinkltd.cn/forum/2/picking-quantstock-quant-manual-assign-2870>

【20221220升级到16.0】

1.  模块位置：[https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/stock_quant_manual_assign](https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/stock_quant_manual_assign)
2.  产品上增加字段“不可拆包并包”，如果勾选了此字段，必须整包裹锁货，不可分包裹锁货，也不可以往包裹里增加数量。典型应用场景是钢卷贸易（把钢卷看成包裹）
3.  弹窗选择Quant锁货的界面，增加按包裹号筛选Quant

模块链接：

10.0链接：

12.0链接：

14.0模块链接：OSCG_SVN\odoo_ecommerce\14.0SRC\仓库物流\stock_quant_manual_assign

**14.0版新增了功能**：1) 作业类型上可以配置是否自动填写完成数量，如果配置了，选择Quant锁货后，系统自动用锁货数量填写到完成数。2) 指定锁货Quant的Wizard弹窗上，增加了指定批次功能。

【**12.0版本升级修改方法**】

只需要修改一行代码，如下：文件 stock_quant_manual_assign\wizard\assign_manual_quants.py， 方法 def default_get(self, fields)， Line 86行 line['qty'] = sum(move_lines.mapped('ordered_qty')) 改成 line['qty'] = move.product_qty 即可

           # line['qty'] = sum(move_lines.mapped('ordered_qty'))
            line['qty'] = move.product_qty

Stock Picking的Stock Move上增加一个手工分配Quant的按钮，点击弹窗选择Quant重新锁货。

To use this module, you need to:

1.  Click on the tags icon at the end of move line.
2.  Open the wizard with the button "Manual Quants".
3.  Select the quants to assign (reserve), then Confirm.
4.

Odoo14.0新增指定批次筛选锁货Quant功能：

![[2-picking-quantstock-quant-manual-assign-2870-111f63e0.png]]

## 补充/答案 1

vivian V14版本测试截图：

![[2-picking-quantstock-quant-manual-assign-2870-b938e24e.png]]

![[2-picking-quantstock-quant-manual-assign-2870-cd7fd25c.png]]

![[2-picking-quantstock-quant-manual-assign-2870-0d60debc.png]]

![[2-picking-quantstock-quant-manual-assign-2870-97c1c3ba.png]]

![[2-picking-quantstock-quant-manual-assign-2870-f1e6e294.png]]

## 补充/答案 2

F:\SVN\odoo_ecommerce\05.SRC\stock_quant_manual_assign

10.0版本存放位置

stock_quant_manual_assign

## 补充/答案 3

在stock.move的每条明细行上新增manual quants按钮，手工选择需要调拨的quants（库存量，位置，批次号自动带出）,数量需要填写。注意：作业需要在‘验证’前点按钮‘重新计算’才会产生。

![[2-picking-quantstock-quant-manual-assign-2870-c6c8458f.png]]

![[2-picking-quantstock-quant-manual-assign-2870-dbc6e9c2.png]]

![[2-picking-quantstock-quant-manual-assign-2870-e24eeff3.png]]

![[2-picking-quantstock-quant-manual-assign-2870-c97bed29.png]]

![[2-picking-quantstock-quant-manual-assign-2870-19782d0d.png]]


## 原帖外链配图

![[2-picking-quantstock-quant-manual-assi-x194038c2.png]]
<small>原始地址: /web/image/1365/snipaste_20190215_142506.png?access_token=124f2c91-b7e9-4c6e-b1b7-b6113016356d</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
