---
title: "PG的消息侦听机制 LISTEN及NOTIFY"
source: "http://www.thinkltd.cn/forum/1/pg-listennotify-3931"
forum: "求助台"
author: "肖相扶"
published: 2024-05-23
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# PG的消息侦听机制 LISTEN及NOTIFY

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-05-23
> <http://www.thinkltd.cn/forum/1/pg-listennotify-3931>

Postgresql提供了客户端之间通过服务器端进行消息通信的机制，这种机制就是通过listen和notify命令完成的。

相关命令：
listen ：监听消息通道；例：listen topic_a
unlisten：取消先前的监听；例：unlisten topic_a
notify：发送消息到消息通道中；例：notify topic_a,’hello word’
pg_notify():与notify相同的功能; 例：select pg_notify(‘topic_a’,’hello world’)
pg_listening_channels()：查看当前session已注册了哪些消息监听。Select pg_listening_channels()

用法示例参考下面截图：

![[1-pg-listennotify-3931-41f024f9.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
