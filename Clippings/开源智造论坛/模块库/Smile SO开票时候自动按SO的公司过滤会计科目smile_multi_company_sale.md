---
title: "Smile SO开票时候自动按SO的公司过滤会计科目smile_multi_company_sale"
source: "http://www.thinkltd.cn/forum/2/smile-sososmile-multi-company-sale-3075"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile SO开票时候自动按SO的公司过滤会计科目smile_multi_company_sale

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smile-sososmile-multi-company-sale-3075>

模块链接：

This module forces filter in `Income Account` and `Customer Taxes` by invoicing company attached to SO, when creating an invoice order of this corresponding SO.

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_multi_company_sale#id1)

- Create a sale order from a company `My Company, Morocco` which has a moroccan chart of account:

- Confirm the SO and create the invoice, the system will pass the company corresponding to this SO in the context of the invoice, then filter the `Income Account` and the `Customer Taxes` using this context:

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
