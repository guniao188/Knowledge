---
title: "Odoo17费用报销改善点一览"
source: "http://www.thinkltd.cn/forum/1/odoo17-3833"
forum: "求助台"
author: "肖相扶"
published: 2024-04-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17费用报销改善点一览

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-04-10
> <http://www.thinkltd.cn/forum/1/odoo17-3833>

返回  [Odoo17改善点列表](http://www.thinkltd.cn/forum/1/odoo17-3808)

1.  Accounting flow revamp
    The accounting flow of expenses reports posting has been modified. An expenses report paid by an employee generates a vendor bill, and an expenses report paid by a company generates a payment instead of a purchase receipt. The synchronization between the Accounting and the Expense app has also been improved. The payment method used can now be specified for the expenses paid by the company.
2.  Default category
    Specify a default category for automatically generated expenses.
3.  Expense report: payments
    Expense reports paid by the company now generate as many payments as there are expenses in order to ease the reconciliation process.
4.  Expense report: improved PDF
    The expense report PDF has been improved, and receipts are now attached.
5.  Forced amount in company currency
    For expenses made in foreign currencies, employees can manually enter the amount they spent in company currency independently of Odoo exchange rates to match their real spendings perfectly
6.  Improve status consistency
    Improved the pipeline stages of expenses and expense reports with consistent terminology. Clarified "to submit" versus "to report" and added tooltips to the expense dashboard.

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
