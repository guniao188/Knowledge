---
title: "OCA库存盘点申请stock_inventory_verification_request"
source: "http://www.thinkltd.cn/forum/2/ocastock-inventory-verification-request-2889"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA库存盘点申请stock_inventory_verification_request

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastock-inventory-verification-request-2889>

模块链接：

Adds the capability to request a Slot Verification when an inventory is 'Pending to Approve'. When asked from an inventory adjustment, which have discrepancies over the threshold for the location, a Slot Verification Request will be created for each line that exceed the maximum discrepancy allowed.

A SVR must be created when warehouse operation (e.g. an inventory adjustment, a cycle count...) uncovers a count discrepancy within a slot (a small stock location), and the discrepancy is greater than the pre-defined acceptable variance threshold. It is a stock manager's task to confirm the SVR and assign it to someone to perform it.

The aim of SVR is to find and fix errors before they are transferred to another location, so they will not be found again in similar stock operations. In other words, a SVR helps to correct an already existing error in our stock records the earliest possible. Many times, a SVR will likely lead to manual actions (before being marked as solved) in order to fix the problems uncovered.

## [Usage](https://github.com/OCA/stock-logistics-warehouse/tree/11.0/stock_inventory_verification_request#id1)

In order to use this module act as follow:

- From a Inventory Adjustment in state 'Pending to Approve' click in the button 'Request Verification'. This will create all the Slot Verification Request needed.
- Go to 'Inventory / Inventory Control / Slot Verification Request'
- Go to a Slot Verification Request 'Waiting Actions' and confirm it.
- You can now check the involved lines and moves to help you.
- Once you have found the problem and you have fixed it 'Mark as Solved' the Verification.

https://github.com/OCA/stock-logistics-warehouse/tree/11.0/stock_inventory_verification_request


## 原帖外链配图

![[2-ocastock-inventory-verification-requ-x194038c2.png]]
<small>原始地址: /web/image/1401/snipaste_20190217_230321.png?access_token=d8f11337-b570-4405-8aba-a2a800c36ad1</small>

![[2-ocastock-inventory-verification-requ-x194038c2.png]]
<small>原始地址: /web/image/1403/snipaste_20190217_230357.png?access_token=4e31baf4-d2e6-4944-850d-297d92d4ebac</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
