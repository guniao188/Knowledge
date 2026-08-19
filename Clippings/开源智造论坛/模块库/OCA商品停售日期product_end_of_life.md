---
title: "OCA商品停售日期product_end_of_life"
source: "http://www.thinkltd.cn/forum/2/ocaproduct-end-of-life-2651"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA商品停售日期product_end_of_life

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaproduct-end-of-life-2651>

模块链接：

### 安装报错，未进一步测试

## Product alert when close to End-of-Life(Eol) Date

This module allows you to set the End of Life Date of a Product.

Products with EoL Date in the past are excluded from the list of Products in Purchase Order so the product can not be ordered.

A scheduled action is created to know in advance the list of products whose EoL Date is approaching. An email will be sent to the members of the Discussion Channel for Product Eol Notification Group.

###

### Configuration

####

#### Discuss Channel

- Look for the the Private Channel > Product End-Of-Life Channel.
- Click settings and add members on this channel.

####

#### Scheduled Action

- The scheduled action is already configured to check if a product is about to reach its end-of-life
- The interval is automatically configured using the notification delay setting

####

#### Notification Delay

- The delay before a notification is sent for a product about to reach its end-of-life can be configured in Inventory > Configuration > Settings

###

### Usage

####

#### Products

- Go to Inventory > Master Data > Products
- Create or edit a product
- Enter the End of Life Date and save

###

### Bug Tracker

Bugs are tracked on [GitHub Issues](https://github.com/OCA/product-attribute/issues). In case of trouble, please check there if your issue has already been reported. If you spotted it first, help us smash it by providing detailed and welcomed feedback.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
