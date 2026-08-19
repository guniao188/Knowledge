---
title: "IoT Box检测USB摄像头"
source: "http://www.thinkltd.cn/forum/1/iot-boxusb-262"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# IoT Box检测USB摄像头

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/iot-boxusb-262>

查看摄像设备命令： v4l2-ctl --list-devices

获取摄像头分辨率： v4l2-ctl --list-formats-ext|grep 'Size'|awk '{print $3}'|sort -rn|awk NR==1

拍照命令：sudo fswebcam -d /dev/video0 -r 352x288 /home/pi/1.jpg


## 原帖外链配图

![[1-iot-boxusb-262-x194038c2.png]]
<small>原始地址: /web/image/1516/snipaste_20190316_235650.png?access_token=2bfac466-a02b-430b-8d6d-f4b0a3f7d46e</small>

![[1-iot-boxusb-262-x194038c2.png]]
<small>原始地址: /web/image/1518/snipaste_20190316_235618.png?access_token=d51fa1fc-c016-40a5-9489-8350b4e6b84a</small>

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
