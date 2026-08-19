---
title: "OCA Partner增加地图显示partner_external_map"
source: "http://www.thinkltd.cn/forum/2/oca-partnerpartner-external-map-2711"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA Partner增加地图显示partner_external_map

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-partnerpartner-external-map-2711>

模块链接：

In the old days of Odoo/OpenERP, back in version 6.1, there was an official *google_map* module ; this module added a *Map* button on the partner form view and, when the user clicked on that button, it would open a new tab on its web browser and go to Google Map with a search on the address of the partner.

This module aims at restoring this feature with several improvements:

- Each user can select the map website he wants to use in its preferences
- There are now two buttons on the partner form view: one to open a regular map on the address of the partner, and another one to open an itinerary map from the start address configured in the preferences of the user to the address of the partner.

This module supports several map websites:

- Google Maps
- OpenStreetMap
- Bing Maps
- Here Maps
- MapQuest

If the module *base_geolocalize* from the official addons is installed on the system, it will use the latitude and longitude to localize the partner (instead of the address) if this information is present on the partner.

## [Configuration](https://github.com/OCA/partner-contact/tree/12.0/partner_external_map#id1)

If you want to create additional map websites, go to the menu *Settings > Technical > Map Websites > Map Websites*. You are invited to send the configuration information of your additional map websites to one of the authors of the module, so that the module can be updated with more pre-configured map websites.

##

## [Usage](https://github.com/OCA/partner-contact/tree/12.0/partner_external_map#id2)

First, you need to configure in your preferences:

- The map website to use for the regular maps,
- The map website to use for the route maps,
- The start address for the route maps.

Then you can use the two new buttons on the partner form to open a regular map or a route map.


## 原帖外链配图

![[2-oca-partnerpartner-external-map-2711-x194038c2.png]]
<small>原始地址: /web/image/1130/snipaste_20190126_220212.png?access_token=b43fbedb-4db5-4e80-b67c-f31b2c2470da</small>

![[2-oca-partnerpartner-external-map-2711-x194038c2.png]]
<small>原始地址: /web/image/1132/snipaste_20190126_220256.png?access_token=8ff11f3a-0c31-4512-a6b1-2cbe5b282c33</small>

![[2-oca-partnerpartner-external-map-2711-x194038c2.png]]
<small>原始地址: /web/image/1134/snipaste_20190126_220235.png?access_token=0e535b6a-03e1-4cf7-8af7-b0fe178581c7</small>

![[2-oca-partnerpartner-external-map-2711-x194038c2.png]]
<small>原始地址: /web/image/1136/snipaste_20190126_220507.png?access_token=1fd6ebc2-dab0-4839-9532-9ea3e8bf5d5e</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
