---
title: "OCA用户即时通知消息web_notify"
source: "http://www.thinkltd.cn/forum/2/ocaweb-notify-2833"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA用户即时通知消息web_notify

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaweb-notify-2833>

模块链接：

Send instant notification messages to the user in live.

This technical module allows you to send instant notification messages from the server to the user in live. Two kinds of notification are supported.

- Warning: Displayed in a red flying popup div
- Information: Displayed in a light yellow flying popup div
-

## [Installation](https://github.com/OCA/web/tree/12.0/web_notify#id1)

This module is based on the Instant Messaging Bus. To work properly, the server must be launched in gevent mode.

##

## [Usage](https://github.com/OCA/web/tree/12.0/web_notify#id2)

To send a notification to the user you just need to call one of the new methods defined on res.users:

    self.env.user.notify_info(message='My information message')

or

    self.env.user.notify_warning(message='My marning message')

You can test the behaviour of the notifications by installing this module in a demo database. Access the users form through Settings -> Users & Companies. You'll see a tab called "Test web notify", here you'll find two buttons that'll allow you test the module.


## 原帖外链配图

![[2-ocaweb-notify-2833-xc821c6d5.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/web/12.0/web_notify/static/description/test_notifications_demo.png</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
