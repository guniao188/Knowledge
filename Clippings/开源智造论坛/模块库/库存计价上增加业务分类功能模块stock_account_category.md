---
title: "库存计价上增加业务分类功能模块stock_account_category"
source: "http://www.thinkltd.cn/forum/2/stock-account-category-4022"
forum: "模块库"
author: "肖相扶"
published: 2025-01-14
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 库存计价上增加业务分类功能模块stock_account_category

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2025-01-14
> <http://www.thinkltd.cn/forum/2/stock-account-category-4022>

模块链接： OSCG_Git\18.0\extra-addons\stock_account_category

【模块功能】

1.  库存计价(stock.valuation.layer)上增加业务分类字段。库存计价的分类，常见的如：采购入库、采购费用分摊、采购发票价格差异分摊、采购退货、销售出库、销售退货、盘点盈亏、生产领料、生产入库、生产退库，等等。
2.  增加菜单“会计 --> 存货”，以及子菜单“费用分摊”（库存模块的到岸分摊菜单）、“库存计价”（库存模块的报表下的计价菜单），“配置 --> 计价分类”。
3.  新增计价分类的模型，以及自动设置计价分类的Wizard和服务器动作。
4.  计价分类是月末一次加权平均成本价格计算、存货会计凭证生成的来源数据。本模块在库存计价(SVL)上增加分类字段，方便月末价格计算、以及存货会计凭证生成功能的实现。
5.  Bug修正：只要是Anglo-Saxon会计体系，不管是否开启永续
    采购发票确认时候，费用科目都取自入库科目，而不是费用科目。系统原有功能是，开启 Anglo-Saxon会计体系且开启永续的情况下， 费用科目都取自入库科目，否则取自费用科目。参见文件 OSCGODOO18\source\addons\stock_account\models\account_move.py
    方法 def _compute_account_id(self)
6.  增加功能，如下图，盘点时候，点击“应用”按钮，检查一下如果产品的成本价格为零，弹窗警告。

![[2-stock-account-category-4022-1ad3db6a.png]]

【功能截图】

![[2-stock-account-category-4022-55b1969d.png]]

![[2-stock-account-category-4022-c5aff3ed.png]]

![[2-stock-account-category-4022-770e17c8.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
