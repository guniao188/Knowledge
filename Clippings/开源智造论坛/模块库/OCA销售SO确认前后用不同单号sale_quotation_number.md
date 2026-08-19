---
title: "OCA销售SO确认前后用不同单号sale_quotation_number"
source: "http://www.thinkltd.cn/forum/2/ocasosale-quotation-number-2678"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA销售SO确认前后用不同单号sale_quotation_number

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocasosale-quotation-number-2678>

模块链接：https://github.com/OCA/sale-workflow/tree/11.0/sale_quotation_number

## Sale quotation number

- Sale Quotation:
  - Sale process in draft stage just informing prices and element of communication.

- Sale Order:
  - Sale process confirmed, the customer already have a compromise with us in terms of pay an invoice and receive our product or service.

Originally Odoo manage only 1 sequence for this 2 documents, then the sales order won and lost manage the same sequence losing almost all lost quotations in terms of sequences, making so difficult understand with a quick view if we are good or bad in terms of logistic and sale process already confirmed.

**Technical Explanation**

When you create a quotation, it is numbered using the 'sale.quotation' sequence. When you confirm a quotation, its orginal number is saved in the 'origin' field and the sale order gets a new number, retrieving it from 'sale.order' sequence.

- With Odoo Base:

  > Sale Quotation 1 Number = SO001
  >
  > Sale Quotation 2 Number = SO002
  >
  > Sale Quotation 3 Number = SO003
  >
  > Sale Quotation 4 Number = SO004

- With Odoo + This Module:

  > Sale Quotation 1 Number = SQ001
  >
  > Sale Quotation 2 Number = SQ002
  >
  > Sale Quotation 3 Number = SQ003
  >
  > Sale Quotation 4 Number = SQ004
  >
  > Sale Quotation 2 Confirmed = Number for Sale Order SO001 from Sale Quotation SQ002
  >
  > Sale Quotation 1 Confirmed = Number for Sale Order SO002 from Sale Quotation SQ001
  >
  > Sale Quotation 4 Confirmed = Number for Sale Order SO003 from Sale Quotation SQ004

###

### Configuration

To configure this module you need to go to Sales -> Configuration and uncheck 'Use same enumeration for quotations and sale orders'.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
