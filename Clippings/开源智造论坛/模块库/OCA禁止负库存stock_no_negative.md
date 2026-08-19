---
title: "OCA禁止负库存stock_no_negative"
source: "http://www.thinkltd.cn/forum/2/ocastock-no-negative-2544"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA禁止负库存stock_no_negative

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastock-no-negative-2544>

【**20221207升级到16.0**】https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/stock_no_negative

模块链接：

此模块在产品及产品分类上增加是否允许负库存的配置项“Allow Negative Stock”，默认为不允许负库存。当发送负库存出库时候，系统报错，不允许出库。

By default, Odoo allows negative stock. The advantage of negative stock is that, if some stock levels are wrong in the ERP, you will not be blocked when validating the picking for a customer... so you will still be able to ship the products on time (it's an example !). The problem is that, after you forced the stock level to negative, you are supposed to fix the stock level later via an inventory ; but this action is often forgotten by users, so you end up with negative stock levels in your ERP and it can stay like this forever (or at least until the next full inventory).

If you disallow negative stock in Odoo with this module, you will be blocked when trying to validate a stock operation that will set the stock level of a product as negative. So you will have to fix the wrong stock level of that product without delay, in order to validate the stock operation in Odoo... you can't forget it anymore !

###

### Configuration

By default, the stockable products will not be allowed to have a negative stock. If you want to make some exceptions for some products or some product categories, you can activate the option *Allow Negative Stock* on some products or some products categories.

## 补充/答案 1

【功能截图】

![[2-ocastock-no-negative-2544-9f3335ad.png]]

![[2-ocastock-no-negative-2544-62b3dd87.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
