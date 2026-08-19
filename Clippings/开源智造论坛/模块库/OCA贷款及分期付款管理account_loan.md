---
title: "OCA贷款及分期付款管理account_loan"
source: "http://www.thinkltd.cn/forum/2/ocaaccount-loan-2742"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA贷款及分期付款管理account_loan

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaaccount-loan-2742>

模块链接：

## Account Loan management

This module extends the functionality of accounting to support loans. It will create automatically moves or invoices for loans. Moreover, you can check the pending amount to be paid and reduce the debt.

It currently supports two kinds of debts:

- Loans: a standard debt with banks, that only creates account moves.
  Loan types info: [APR](https://en.wikipedia.org/wiki/Annual_percentage_rate), [EAR](https://en.wikipedia.org/wiki/Effective_interest_rate), [Real Rate](https://en.wikipedia.org/wiki/Real_interest_rate).

- Leases: a debt with a bank where purchase invoices are necessary

###

### Installation

To install this module, you need to:

1.  Install numpy : `pip install numpy`
2.  Follow the standard process

###

### Usage

To use this module, you need to:

1.  Go to Invoicing / Accounting > Adviser > Loans
2.  Configure a loan selecting the company, loan type, amount, rate and accounts
3.  Post the loan, it will automatically create an account move with the expected amounts
4.  Create automatically the account moves / invoices related to loans and leases before a selected date

On a posted loan you can:

- Create moves or invoices (according to the configuration)
- Modify rates when needed (only unposted lines will be modified)
- Reduce or cancel the debt of a loan / lease

## 补充/答案 1

【模块安装】本模块在12.0企业版可以安装，还款额计算时候，有三行代码需要修改一下：文件 model/account_loan.py

【贷款管理】

贷款类型（Loan Type）： 等额本息（Fixed Annuity）、等额本金(Fixed Principal)、仅利息（到期一次性还本金，Only interest）
利息计算方法（Rate Type）：年度百分率(Annual Percentage Rate,APR)，有效年利率(Effective Annual Rate，EAR)。

【分期付款】


## 原帖外链配图

![[2-ocaaccount-loan-2742-x194038c2.png]]
<small>原始地址: /web/image/1672/snipaste_20190610_122837.png?access_token=9e716bc4-1734-4b89-b53f-e5db2b628446</small>

![[2-ocaaccount-loan-2742-x194038c2.png]]
<small>原始地址: /web/image/1674/snipaste_20190610_122330.png?access_token=b6b3e46f-f183-4330-988a-7f19c7c7879b</small>

![[2-ocaaccount-loan-2742-x194038c2.png]]
<small>原始地址: /web/image/1676/snipaste_20190610_124231.png?access_token=b9f5eacd-7047-4222-85d5-d8786277cc46</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
