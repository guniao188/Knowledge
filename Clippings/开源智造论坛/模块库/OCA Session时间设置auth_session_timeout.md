---
title: "OCA Session时间设置auth_session_timeout"
source: "http://www.thinkltd.cn/forum/2/oca-sessionauth-session-timeout-3035"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA Session时间设置auth_session_timeout

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-sessionauth-session-timeout-3035>

模块链接：

This module was written to be able to kill(logout) all inactive sessions since a given delay. On each request the server checks if the session is yet valid regarding the expiration delay. If not a clean logout is operated.

Two system parameters are available:

- `inactive_session_time_out_delay`: validity of a session in seconds (default = 2 Hours)
- `inactive_session_time_out_ignored_url`: technical urls where the check does not occur
-

## 补充/答案 1

http://www.odoo.com/apps/modules/12.0/auth_session_timeout/

 V12版本链接。

## 补充/答案 2

![[2-oca-sessionauth-session-timeout-3035-335ee941.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
