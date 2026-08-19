---
title: "二开集成高德地图模块base_geolocalize_amap、website_amap"
source: "http://www.thinkltd.cn/forum/2/base-geolocalize-amapwebsite-amap-3179"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开集成高德地图模块base_geolocalize_amap、website_amap

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/base-geolocalize-amapwebsite-amap-3179>

模块链接：OSCG_SVN\odoo_ecommerce\13.0SRC\base_geolocalize_amap

OSCG_SVN\odoo_ecommerce\13.0SRC\website_amap

【模块功能】

Odoo标准模块base_geolocalize在Partner上显示地址经纬度，该模块默认调用Google或者Open Street获取partner地址的经纬度。模块base_geolocalize_amap增加了高德地图获取经纬度功能。

Odoo标准模块website提供了“联系我们（Contact us）”网页上显示公司位置地图的功能，点击地图跳转到Google地图。但在中国，Google地图用不了。模块website_amap将Google地图替换为高德地图，显示公司位置地图。

【模块配置】

base_geolocalize_amap

![[2-base-geolocalize-amapwebsite-amap-3179-8532f03a.png]]

website_amap：注意，显示地图之前，需要先通过模块base_geolocalize_amap 获取公司对应的业务伙伴的经纬度，高德地图是通过经纬度定位。

![[2-base-geolocalize-amapwebsite-amap-3179-b07fac7d.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
