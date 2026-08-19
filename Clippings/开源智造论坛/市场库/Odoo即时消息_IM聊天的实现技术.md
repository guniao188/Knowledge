---
title: "Odoo即时消息/IM聊天的实现技术"
source: "http://www.thinkltd.cn/forum/4/odoo-im-3942"
forum: "市场库"
author: "肖相扶"
published: 2024-06-25
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/市场库
---

# Odoo即时消息/IM聊天的实现技术

> [!info] 来源
> 开源智造论坛 · 市场库 | 作者:肖相扶 | 2024-06-25
> <http://www.thinkltd.cn/forum/4/odoo-im-3942>

Odoo是世界排名第一的免费开源ERP软件。Odoo的Discuss模块，提供了Odoo用户之间沟通和协作的工具。Odoo用户之间，可以在线聊天，语音通话，视频会议，也可以发送附件文档。

![[4-odoo-im-3942-af0eebd8.png]]

Odoo是一个网页版软件，即B/S架构的系统，网页版软件如何实现实时通信呢？Odoo的即时聊天功能，基于两个支撑技术实现，一个是HTML5中的Websocket技术，一个是PostgreSQL数据库的消息侦听机制LISTEN及NOTIFY。

【Websocket技术】HTML5新增了Websocket技术，Websocket提供了浏览器和服务器之间全双工通信，通过浏览器和服务器之间建立Websocket连接（实际上是TCP连接），在同一时间能够实现客户端到服务器和服务器到客户端的双向数据传输。

![[4-odoo-im-3942-65f49ea7.png]]

【PG的LISTEN及NOTIFY技术】Postgresql提供了客户端之间通过服务器端进行消息通信的机制，这种机制就是通过listen和notify命令完成的。相关命令如下：

- listen ：监听消息通道；例：listen topic_a
- unlisten：取消先前的监听；例：unlisten topic_a
- notify：发送消息到消息通道中；例：notify topic_a,’hello word’
- pg_notify():与notify相同的功能; 例：select pg_notify(‘topic_a’,’hello world’)
- pg_listening_channels()：查看当前session已注册了哪些消息监听。例：Select pg_listening_channels()

![[4-odoo-im-3942-41f024f9.png]]

【Odoo即时聊天技术】

1.  Odoo启动时候，建立PG消息侦听通道（listen imbus），收到消息后，从消息中取出Odoo的消息通道(channel)，查看哪些Websocket订阅了该通道，把消息发给相应的Websocket。代码参考文件 ODOO17\source\addons\bus\models\bus.py ，ImDispatch的方法 def loop()。
2.  Odoo的消息存储在模型bus.bus中，该模型的channel字段表示哪个消息通道，message字段包含 type和payload。type是指消息类别，payload是消息数据。channel、type都是任意定义的字符串。
3.  消息发送机制是，先把要发送的消息存储到bus.bus表，再调用PG的pg_notify发送消息（PG消息通道 imbus）。参考代码文件 ODOO17\source\addons\bus\models\bus.py ，ImBus的方法 def _sendmany()。

![[4-odoo-im-3942-12cfa191.png]]

---

相关:[[Clippings/开源智造论坛/市场库/00-市场库索引.md|← 市场库索引]]
