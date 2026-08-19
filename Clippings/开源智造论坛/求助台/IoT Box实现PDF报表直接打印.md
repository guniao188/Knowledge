---
title: "IoT Box实现PDF报表直接打印"
source: "http://www.thinkltd.cn/forum/1/iot-boxpdf-258"
forum: "求助台"
author: "肖相扶"
published: 2022-12-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# IoT Box实现PDF报表直接打印

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-16
> <http://www.thinkltd.cn/forum/1/iot-boxpdf-258>

Odoo 12.0企业版模块 iot，在报表对象 ir.actions.report 上增加了打印设备，新增了方法 iot_render 。当设置了打印设备后，PDF打印时候，系统调用方法iot_render 获得PDF文件数据，以及IoT Box的打印设备的URL（本地连接URL），js中将获得的PDF数据发送给本地打印URL直打出来。

参考知识：[IoT Box如何添加打印机 /forum/1/question/iot-box-260](http://www.thinkltd.cn/forum/1/question/iot-box-260)

[Odoo如何连接IoT Box: /forum/1/question/odooiot-box-259](http://www.thinkltd.cn/forum/1/question/odooiot-box-259)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
