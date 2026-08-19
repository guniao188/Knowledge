---
title: "Odoo企业版财务报表account_reports介绍"
source: "http://www.thinkltd.cn/forum/2/odooaccount-reports-2467"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo企业版财务报表account_reports介绍

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odooaccount-reports-2467>

Once the name is filled, there are two other parameters that need to be configured:

- **Show Credit and Debit Columns**

- **Analysis Period** :

  - Based on date ranges (eg Profit and Loss)
  - Based on a single date (eg Balance Sheet)
  - Based on date ranges with 'older' and 'total' columns and last 3 months (eg. Aged Partner Balances)
  - Bases on date ranges and cash basis method (eg Cash Flow Statement)

In the **formulas** field you can add one or more formulas to assign a value to the balance column (and debit and credit column if applicable – separated by ;)

You have several objects available in the formula :

- `Ndays` : The number of days in the selected period (for reports with a date range).
- Another report, referenced by its code. Use `.balance` to get its balance value (also available are `.credit`, `.debit` and `.amount_residual`)

A line can also be based on the sum of account move lines on a selected domain. In which case you need to fill the domain field with an Odoo domain on the account move line object. Then an extra object is available in the formulas field, namely `sum`, the sum of the account move lines in the domain. You can also use the group by field to group the account move lines by one of their columns.

Other useful fields :

- **Type** : Type of the result of the formula.
- **Is growth good when positive** : Used when computing the comparison column. Check if growth is good (displayed in green) or not.
- **Special date changer** : If a specific line in a report should not use the same dates as the rest of the report.
- **Show domain** : How the domain of a line is displayed. Can be foldable (`default`, hidden at the start but can be unfolded), `always` (always displayed) or `never` (never shown).


## 原帖外链配图

![[2-odooaccount-reports-2467-x194038c2.png]]
<small>原始地址: /web/image/606/acc_report1.png?access_token=c1f1dcf5-a19d-47d4-8432-316835c12775</small>

![[2-odooaccount-reports-2467-x194038c2.png]]
<small>原始地址: /web/image/608/acc_report2.png?access_token=90cde64c-36b2-473e-bd55-89d11232a840</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
