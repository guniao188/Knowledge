---
title: "Smile允许按单据上的公司取会计科目而不是按当前用户所在公司smile_multi_company_base"
source: "http://www.thinkltd.cn/forum/2/smilesmile-multi-company-base-3073"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile允许按单据上的公司取会计科目而不是按当前用户所在公司smile_multi_company_base

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smilesmile-multi-company-base-3073>

模块链接：

This module allows managing connection to companies in case of multi company. It also changes the behavior of company_dependent fields. Instead of being calculated natively from the connected user's company, they are calculated from the company carried by the record.

Features:

- Allows to log in or not to a company.
- Select with which companies it is possible to connect.
- For example in invoicing module, it makes possible to validate an invoice for a company different from that of the connected user, and this invoice will be registered in account by attached company and not that of connected user.
-

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_multi_company_base#id1)

1.  Go to `Settings > Companies` and use the boolean toggle to allow or not logging in to a company.

    >
    >
    >
    >
    >

2.  In users interface, the system shows companies which it is possible to connect.

    >
    >
    >
    >
    >

3.  Example of application in `Invoicing` module:

    - Considering two companies `YourCompany` and `A1`, knowing that `YourCompany` is a parent company of `A1`.

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
    >
    > - Considering a user `user01` connected to `YourCompany` company and a second user `user02` connected to child company `A1`.
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
    >
    >
    > - Even if the user `user01` has created the invoice attached to his company `A1`, the user `user02` from the parent company can validate this invoice by keeping the company A1 already attached.
    >
    >
    >
    >
    >
    >
    >
    > - The invoice will be added to `Journal Items` with attached company `A1` and not the company of the connected user who validate it.
    >
    >
    >
    >
    >
    >

##

-

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
