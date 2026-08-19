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

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
