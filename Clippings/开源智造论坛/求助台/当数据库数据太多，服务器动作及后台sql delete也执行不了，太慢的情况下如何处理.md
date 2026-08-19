---
title: "当数据库数据太多，服务器动作及后台sql delete也执行不了，太慢的情况下如何处理"
source: "http://www.thinkltd.cn/forum/1/sql-delete-840"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 当数据库数据太多，服务器动作及后台sql delete也执行不了，太慢的情况下如何处理

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/sql-delete-840>

有时候我们在清理业务数据的时候，遇到原有的业务数据量非常大，执行清理业务数据的方法服务器动作根本行不通，一直在转，甚至后台使用sql命令delete也要转很久才能出结果的情况下，可以考虑采用以下的命令方法来执行清理，需要后台sql语句命令执行：

truncate table sale_order_line  CASCADE;

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
