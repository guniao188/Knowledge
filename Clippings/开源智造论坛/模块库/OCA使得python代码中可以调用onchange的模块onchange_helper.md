---
title: "OCA使得python代码中可以调用onchange的模块onchange_helper"
source: "http://www.thinkltd.cn/forum/2/ocapythononchangeonchange-helper-3352"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA使得python代码中可以调用onchange的模块onchange_helper

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocapythononchangeonchange-helper-3352>

模块链接：

【问题背景】

py代码中create 了一个对象后，有时候希望可以直接触发该对象上某些字段的 onchange，自动填充一些字段值。此模块正是解决了此需求。

尤其有时候，有些 onchange赋值是在界面上配置的（参考 [/forum/1/question/onchange-606](http://www.thinkltd.cn/forum/1/question/onchange-606)），create的时候无法预料时候，此模块尤其有用

【用法】

## [Usage](https://github.com/OCA/server-tools/tree/13.0/onchange_helper#id1)

To use this module, you need to:

- depend on this module
- call yourmodel.play_onchanges(values, ['field'])

Example if you want to create a sale order and you want to get the values relative to partner_id field (as if you fill the field from UI)

> vals = {'partner_id': 1}

> vals = self.env['sale.order'].play_onchanges(vals, ['partner_id'])

Then, vals will be updated with partner_invoice_id, partner_shipping_id, pricelist_id, etc...

Default values will be used to process onchange methods, if respective fields are not set in vals. You can get them if you pass fields name in the list of fields.

> vals = {'partner_id': 1}

> vals = self.env['sale.order'].play_onchanges(vals, ['partner_id', 'date_order'])

vals will contain, in addition to the changed values, the default value for date_order

You can also use it on existing record for example:

> vals = {'partner_shipping_id': 1}

> vals = sale.play_onchanges(vals, ['partner_shipping_id'])

Then the onchange will be played with the vals passed and the existing vals of the sale. vals will be updated with partner_invoice_id, pricelist_id, etc..

Behind the scene, play_onchanges will execute **all the methods** registered for the list of changed fields, so you do not have to call manually each onchange. To avoid performance issue when the method is called on a record, the record will be transformed into a memory record before calling the registered methods to avoid to trigger SQL updates command when values are assigned to the record by the onchange

Notes:

- Order in onchange_fields is very important as onchanges methods will be played in that order.
- If you use memory object in vals, be award that onchange method in base model call self.invalidate_cache() that reset it.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
