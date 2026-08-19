---
title: "Odoo如何连接IoT Box"
source: "http://www.thinkltd.cn/forum/1/odooiot-box-259"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo如何连接IoT Box

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odooiot-box-259>

1.  Odoo12.0企业版新增IoT Box模块，安装该模块，打开模块，点击 CONNECT 按钮，系统弹窗指示如何自动查找及连接IoT Box，如下图。

2.  点击 SCAN，系统js代码扫描本地网址（如 192.168.1.*），访问 /hw_proxy/hello， 如果有回应说明扫描的IP是IoT Box

3.  点击扫描到的IoT Box链接，进入Iot box配置界面，在该界面，将Server端的Token复制到IoT Box，Iot box保留该Token（存在本地conf文件中），并调用Server端IP主动上传Box及设备信息给Server，Server收到信息即创建IoT box和Device。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
