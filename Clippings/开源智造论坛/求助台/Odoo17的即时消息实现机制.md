---
title: "Odoo17的即时消息实现机制"
source: "http://www.thinkltd.cn/forum/1/odoo17-3932"
forum: "求助台"
author: "肖相扶"
published: 2024-05-23
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17的即时消息实现机制

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-05-23
> <http://www.thinkltd.cn/forum/1/odoo17-3932>

Odoo的即时消息实现原理大致如下：

1.  Odoo消息机制建立在PG的消息侦听机制之上，参考 [PG的消息侦听机制 LISTEN及NOTIFY](http://www.thinkltd.cn/forum/1/pg-listennotify-3931)
2.  建立PG消息侦听通道（listen imbus），收到消息后，从消息中取出Odoo的消息通道(channel)，查看哪些Websocket订阅了该通道，把消息发给相应的Websocket。代码参考文件 OSCGODOO17\source\addons\bus\models\bus.py ，ImDispatch的方法 def loop()。
3.  Odoo的消息存储在模型bus.bus中，该模型的channel字段表示哪个消息通道，message字段包含 type和payload。type是指消息类别，payload是消息数据。channel、type都是任意定义的字符串。
4.  消息发送机制是，先把要发送的消息存储到bus.bus表，再调用PG的pg_notify发送消息（PG消息通道 imbus）。参考代码文件  OSCGODOO17\source\addons\bus\models\bus.py ，ImBus的方法 def _sendmany()。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
