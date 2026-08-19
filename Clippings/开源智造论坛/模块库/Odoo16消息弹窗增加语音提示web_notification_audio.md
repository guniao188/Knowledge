---
title: "Odoo16消息弹窗增加语音提示web_notification_audio"
source: "http://www.thinkltd.cn/forum/2/odoo16web-notification-audio-3824"
forum: "模块库"
author: "肖相扶"
published: 2023-12-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo16消息弹窗增加语音提示web_notification_audio

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2023-12-10
> <http://www.thinkltd.cn/forum/2/odoo16web-notification-audio-3824>

模块链接（16.0版本）： OSCG_Git\extra-addons\web_notification_audio

1.  Odoo右上角的消息弹窗提示，没有语音。在仓库扫码的场景下面，扫码错误的情况下，消息显示一下，4秒以后自动消失。没有语音提示，扫码人员容易忽略扫码错误，而继续往下扫。
2.  本模块为success, warning, danger三种类型的消息增加语音提示，即显示消息的同时，带不同的语音提示。语音提示文件参见本模块文件夹web_notification_audio\static\description下面的语音文件：success.mp3、warning.mp3、danger.mp3
3.  Odoo16消息实现机制参考 [Odoo16消息通知实现原理](http://www.thinkltd.cn/forum/1/odoo16-3823)

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
