---
title: "Odoo18分类汇总创建存货/出入库会计凭证stock_account_subtotal"
source: "http://www.thinkltd.cn/forum/2/odoo18-stock-account-subtotal-4028"
forum: "模块库"
author: "肖相扶"
published: 2025-01-07
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo18分类汇总创建存货/出入库会计凭证stock_account_subtotal

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2025-01-07
> <http://www.thinkltd.cn/forum/2/odoo18-stock-account-subtotal-4028>

模块链接：OSCG_Git\18.0\extra-addons\stock_account_subtotal

【模块功能】

1.  库存计价的分类（参考 [库存计价上增加业务分类功能模块stock_account_category](http://www.thinkltd.cn/forum/2/stock-account-category-4022)）上增加凭证类型字段，用于汇总创建存货变动(出入库)的会计凭证。同一类型的库存变动(库存计价)，汇总到同一个会计凭证。常见凭证类型如：分采购入库、销售出库、生产领料，等等
2.  新增菜单“会计 --> 存货 --> 存货会计凭证”。新增分类汇总凭证生成的计算表单。
3.  汇总库存计价（但不包括到岸成本分摊、采购发票价格差异分摊产生的库存计价）。系统按库存计价的凭证类别汇总当期的所有库存计价(stock.valuation.layer)。系统按凭证类别、产品分类、产品、借方科目、贷方科目，汇总当期库存计价的总价值，生成凭证行。每一个凭证行再生成会计凭证。
4.  汇总到岸成本分摊单。当期的所有到岸成本分摊单，系统汇总其计价调整明细行(stock.valuation.adjust.lines)，根据在库数量、已出库数量，拆分分摊金额，生成不同凭证行（此部分凭证类别为“费用分摊”）。
5.  借方科目和贷方科目的取法和Odoo本来逻辑是一样的。即先取虚拟库位上的科目，再取产品上的科目，再取产品分类上的科目。
6.  实施时候，需要补全“存货凭证分类”。

【功能截图】

![[2-odoo18-stock-account-subtotal-4028-205a37d5.png]]

![[2-odoo18-stock-account-subtotal-4028-6ff332a8.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
