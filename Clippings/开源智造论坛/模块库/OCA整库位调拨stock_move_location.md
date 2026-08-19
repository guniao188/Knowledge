---
title: "OCA整库位调拨stock_move_location"
source: "http://www.thinkltd.cn/forum/2/ocastock-move-location-2893"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA整库位调拨stock_move_location

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastock-move-location-2893>

模块链接：

- A new menuitem Stock > Move from location... opens a wizard where 2 location ca be specified.
- Select origin and destination locations and press "IMMEDIATE TRANSFER" or "PLANNED TRANSFER"
- Press ADD ALL button to add all products available
- Those lines can be edited. Move quantity can't be more than a max available quantity
- Move doesn't care about the reservations and will move stuff anyway
- If during your operation with the wizard the real quantity will change it will move only the available quantity at the button press
- Products will be moved and a form view of picking that did that will show up
- If "PLANNED TRANSFER" is used - the picking won't be validated automatically
-


## 原帖外链配图

![[2-ocastock-move-location-2893-x194038c2.png]]
<small>原始地址: /web/image/1407/snipaste_20190217_231940.png?access_token=0cc5e921-0653-45bc-848d-7db24fdc8a3c</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
