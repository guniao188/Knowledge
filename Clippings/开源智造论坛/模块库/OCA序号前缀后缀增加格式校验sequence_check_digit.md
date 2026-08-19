---
title: "OCA序号前缀后缀增加格式校验sequence_check_digit"
source: "http://www.thinkltd.cn/forum/2/ocasequence-check-digit-2583"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA序号前缀后缀增加格式校验sequence_check_digit

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocasequence-check-digit-2583>

模块链接：

This module was written to configure check digits on sequences added on the end. It is useful as a control of the number on visual validation.

It is useful when some manual checks are required or on integrations. The implemented codes can avoid modification of one character and flip of two consecutive characters.

###

### Usage

- Access sequences and configurate the model to use.

- The model will check if the format of prefix, suffix and number is valid

- Implemented algorithms
  - Luhn: [0-9]*
  - Damm: [0-9]*
  - Verhoeff: [0-9]*
  - ISO 7064 Mod 11, 2: [0-9]*
  - ISO 7064 Mod 11, 10: [0-9]*
  - ISO 7064 Mod 37, 2: [0-9A-Z]*
  - ISO 7064 Mod 37, 36: [0-9A-Z]*
  - ISO 7064 Mod 97, 10: [0-9A-Z]*


## 原帖外链配图

![[2-ocasequence-check-digit-2583-x194038c2.png]]
<small>原始地址: /web/image/871/snipaste_20190120_002122.png?access_token=12ad61fb-914a-4529-9a66-f606136deb14</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
