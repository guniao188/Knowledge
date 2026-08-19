---
title: "Smile发票确认时候取发票上的公司的而不是当前用户的公司smile_multi_company_account"
source: "http://www.thinkltd.cn/forum/2/smilesmile-multi-company-account-3074"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile发票确认时候取发票上的公司的而不是当前用户的公司smile_multi_company_account

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smilesmile-multi-company-account-3074>

模块链接：

This module depends on `Multi-Company Base` module parameters. It makes invoices attached to invoicing company. Instead of attaching the invoice natively to the connected user's company, it will be registered by the invoicing company carried by the record.

Features:

- Add a filter by invoicing company in invoices.
- Automatically set `Is Invoicing Company` to true if company is an invoicing company (has a Chart of Accounts).
- Make possible to validate an invoice for a company different from that of the connected user, and this invoice will be registered in account by attached company and not that of connected user.
-

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_multi_company_account#id1)

1.  Considering two companies `YourCompany` and `A1`, knowing that `YourCompany` is a parent company of `A1`. Both companies are invoicing companies:

    >
    >
    >
    >
    >
    >
    >
    >
    >
    >
    >

2.  Considering a user `user01` connected to `YourCompany` company and a second user `user02` connected to the child company `A1`.

    >
    >
    >
    >
    >
    >
    >
    >
    >
    >
    >

3.  Even if the user `user01` has created the invoice attached to his company `A1`, the user `user02` from the parent company can validate this invoice by keeping the company A1 already attached.

    >
    >
    >
    >
    >

4.  The invoice will be added to `Journal Items` with attached company `A1` and not the company of the connected user who validate it.

    >
    >
    >
    >
    >

##

-

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
