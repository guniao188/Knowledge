---
title: "Exception: bus.Bus unavailable原因分析"
source: "http://www.thinkltd.cn/forum/1/exception-bus-bus-unavailable-331"
forum: "求助台"
author: "Administrator"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Exception: bus.Bus unavailable原因分析

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:Administrator | 2022-12-15
> <http://www.thinkltd.cn/forum/1/exception-bus-bus-unavailable-331>

Odoo中，事件处理路由是 /longpolling/  ，单进程情况下，Odoo启动时候，同时启动 ImDispatch 对象负责处理 /longpolling/ 请求。

多进程情况下，只有带有 gevent 启动参数的进程会启动 ImDispatch 对象，也就是是专门的 gevent 进程处理 /longpolling/ ，其他进程不会启动 ImDispatch 对象，不应该处理/longpolling/ 请求。

带有 gevent 启动参数的Odoo进程，侦听端口为 longpolling_port ，因而，必须配置 nginx 等，将/longpolling/请求转发到  longpolling_port 端口，交由 gevent 进程处理。如果没有配置 nginx 转发 /longpolling/， 则 /longpolling/ 请求可能交由非 gevent 进程处理，而非 gevent 进程没有 启动 ImDispatch 对象，因而会报错 Exception: bus.Bus unavailable  。

gevent进程启动命令： python3 /opt/odoo/server/odoo-bin gevent -c /opt/odoo/oscg/odoo-server.conf

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
