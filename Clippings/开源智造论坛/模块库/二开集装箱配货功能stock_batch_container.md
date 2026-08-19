---
title: "二开集装箱配货功能stock_batch_container"
source: "http://www.thinkltd.cn/forum/2/stock-batch-container-3161"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开集装箱配货功能stock_batch_container

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/stock-batch-container-3161>

【模块设计】

svn路径：odoo_ecommerce/12.0SRC/stock_batch_container

1) 本模块依赖模块stock_package_volum ：[/forum/2/question/stock-package-volume-3157](http://www.thinkltd.cn/forum/2/question/stock-package-volume-3157)
2) 批量拣货(stock.picking.batch)上增加字段：集装箱号(container), 仓库作业明细(one2many 到 stock.move.line)，集装箱体积(container_volum, 手工输入),产品体积(product_volum, 汇总stock.move.line之体积)，剩余体积(left_volum，集装箱体积 - 产品体积)
3）stock.picking.batch上增加按钮“添加明细”，点击按钮，弹窗多选明细。弹窗上三个字段：move_lines（many2many 到 stock.move.line）,体积、重量，体积和重量是选择的stock.move.line的体积和重量之和。
4）多选明细时候，在多选窗口上，显示就绪状态的stock.move.line，显示所勾选的明细的体积
5）弹窗上“确定”时候，自动添加所选明细到stock.picking.batch，并且自动将“保留数量”填写到“完成数量”列
6）批量拣货(stock.picking.batch)上点击“完成”按钮时候，自动“验证”stock.move.line对应的Picking，注意有拆分Picking的情况（选了Picking的一部分作业明细，或者作业明细上的完成数少于初始数）。

## 补充/答案 1

【功能截图】

![[2-stock-batch-container-3161-136ed835.png]]

![[2-stock-batch-container-3161-932a95e7.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
