---
title: "企业版地图视图模块web_map、web_map_amap"
source: "http://www.thinkltd.cn/forum/2/web-mapweb-map-amap-3180"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 企业版地图视图模块web_map、web_map_amap

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/web-mapweb-map-amap-3180>

Odoo 13.0中，新增加地图视图。

Odoo 14中地图视图改成高德地图的模块链接：OSCG_SVN\odoo_ecommerce\14.0SRC\地图视图，各个模块功能说明如下：

1.  base_geolocalize_amap ：根据Partner地址获取Partner经纬度。系统原本是调用 openstreetmap.org获取经纬度，中国的地址精度很差，本模块换成高德地图获取经纬度，精度高很多。

2.  website_amap ：网站上联系我们页面上显示公司地址的地图，原本是Google地图，此模块改成高德地图显示

3.  web_map_amap ：Odoo原本的地图视图（web_map模块）中，如果设置了系统参数 web_map.token_map_box，则使用https://www.mapbox.com/ 作地图，否则使用 https://www.openstreetmap.org/ 作为地图。路径规划和导航则使用Google地图。这几个都是国外地图，访问速度慢（Google则不能访问），地址精度差。本模块使用高德地图替换mapbox、openstreetmap、以及Google地图。

【地图视图使用方法】

1.  Partner上维护完整正确的地址，而后点击获取经纬度按钮，自动获取Partner的经纬度。修改Partner地址，系统自动将经纬度清空，需要重新获取。可以编写一个服务器动作，批量刷新Partner的经纬度。如果没有获取Partner的经纬度，地图视图显示不出来。

2.  任何还有Partner字段的表单（如销售订单、采购订单、发货单等），都可以显示地图视图（Map）。

3.  视图XML格式是，res_partner 表示当前表单上Partner字段的字段名，hide_address和hide_name表示，点击目标点，弹窗中是否隐藏详细地址和单据名称。默认为false，true则表示隐藏。地图视图中的field表示在弹窗中显示哪些字段内容。

![[2-web-mapweb-map-amap-3180-e98df5af.png]]

![[2-web-mapweb-map-amap-3180-71dc96dc.png]]

## 补充/答案 1

该模块默认用 openstreet 显示位置，Google地图导航。如果要改成中国的地图(高德地图)，按下述步骤修改。参考技术文章

1) 此文件 https://raw.githubusercontent.com/htoooth/Leaflet.ChineseTmsProviders/master/src/leaflet.ChineseTmsProviders.js 另存到目录 Odoo13\source\enterprise\web_map\static\lib 下面

2) 文件 web_map\static\src\js\map_view.js   jsLibs 处增加依赖  '/web_map/static/lib/leaflet.ChineseTmsProviders.js',

3) 文件web_map\static\src\js\map_renderer.js 方法 _initializeMap ，如下修改：

```python
            var gaode = L.tileLayer.chinaProvider('GaoDe.Normal.Map', {
                maxZoom: 19,
                minZoom: 2
            });
            this.leafletMap = L.map(mapContainer, {
                maxBounds: [L.latLng(180, -180), L.latLng(-180, 180)],
                center: [39.5427,116.2317],
                zoom: 15,
                layers: [gaode],
                zoomControl: true,
            });
```

4) 文件web_map\static\src\js\map_renderer.js 方法 _addMakers ，如下修改：

```python
                    //'https://uri.amap.com/marker?position=121.51920,31.19744&name=开源智造&src=Odoo&callnative=1'
                    //popup.url = 'https://www.google.com/maps/dir/?api=1&destination=' + record.partner.partner_latitude + ',' + record.partner.partner_longitude;
                    popup.url = 'https://uri.amap.com/marker?src=Odoo&callnative=1&position=' + record.partner.partner_longitude + ',' + record.partner.partner_latitude;
```

![[2-web-mapweb-map-amap-3180-67cfaa44.png]]

![[2-web-mapweb-map-amap-3180-c312d45c.png]]

![[2-web-mapweb-map-amap-3180-a5fb8fdb.png]]

## 补充/答案 2

仓库单据的显示，出发地和目的地址是如何定义的呢？字段取值界面上能默认指定吗

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
