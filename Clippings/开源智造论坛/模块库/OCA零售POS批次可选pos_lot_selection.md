---
title: "OCA零售POS批次可选pos_lot_selection"
source: "http://www.thinkltd.cn/forum/2/ocapospos-lot-selection-3155"
forum: "模块库"
author: "施叶寒"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA零售POS批次可选pos_lot_selection

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:施叶寒 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocapospos-lot-selection-3155>

1. 模块存放位置：
备注：odoo12可以直接安装使用

2. 使用场景： 零售带有批次号/序列号的产品

3. odoo当前的不足：odoo源码要求使用者在零售前端页面手动输入一个正确的产品批次号/序列码，如果输入错误那么对应的出库单无法自动发货。

4. 实现思路：在需要输入批次号/序列码的弹框中，增加一个下拉菜单。用户可以选择程序提供的号码，也允许系统原生的手工输入（不推荐）。
下拉可选项的取值方式：通过rpc方式获取当前POS.CONFIG对应的STOCK.LOCATION中PRODUCT.PRODUCT可用的STOCK.PRODUCTION.LOT，通过类onchange方法写到原文本框中。

5. 依赖：

模块:point_of_sale

6. 截图：

![[2-ocapospos-lot-selection-3155-8c161556.png]]

![[2-ocapospos-lot-selection-3155-99dd30c5.png]]

![[2-ocapospos-lot-selection-3155-af184b4a.png]]

## 补充/答案 1

补充：

因为只会寻找内部位置的stock.production.lot，本模块不适用前端创建退货单的情况。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
