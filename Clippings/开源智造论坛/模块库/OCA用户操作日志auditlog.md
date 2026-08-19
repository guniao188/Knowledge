---
title: "OCA用户操作日志auditlog"
source: "http://www.thinkltd.cn/forum/2/ocaauditlog-2797"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA用户操作日志auditlog

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaauditlog-2797>

模块链接：

12.0版：

14.0版：[OCA/server-tools: Tools for Odoo Administrators to improve some technical features on Odoo. (github.com)](https://github.com/OCA/server-tools/tree/14.0/auditlog)

## Audit Log - Track user operations

记录用户详细操作日志：谁，什么时间，哪个请求，哪个操作（读写删建），操作前后字段值的变化。

This module allows the administrator to log user operations performed on data models such as `create`, `read`, `write` and `delete`

###

## 补充/答案 1

【功能截图】

规则设置：记录哪个模型，读、写、删、建，哪个动作的日志，是否记录变更前的字段值（完整日志），或者只记录变更后的字段值（快速日志），记录删除前是否记录字段值（Capture Record）

![[2-ocaauditlog-2797-63876c41.png]]

操作的详细日志：哪个会话（http session）、哪个请求(http request)、哪个模型、哪个操作、哪些字段值发生了变化。

![[2-ocaauditlog-2797-90352721.png]]

## 补充/答案 2

缺点一：这个规则不能直接到字段级，而是整个数据表的变动，就是会产生很多无用的日志数据；

缺点二：普通用户无权查看这个日志，需要管理员级才能查看，除非另行调配权限。无法象系统的日志一样出现在相应的记录底下。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
