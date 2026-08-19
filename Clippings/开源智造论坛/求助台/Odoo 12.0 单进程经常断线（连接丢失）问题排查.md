---
title: "Odoo 12.0 单进程经常断线（连接丢失）问题排查"
source: "http://www.thinkltd.cn/forum/1/odoo-12-0-324"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo 12.0 单进程经常断线（连接丢失）问题排查

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo-12-0-324>

经调查，Odoo 12.0代码文件 odoo\service\server.py  class ThreadedServer  方法 start（）中，增加了内存上限设置（limit_memory_hard）。在以前的版本中，只会在多进程情况下设置该限制，单进程不设置。因为这个设置，系统经常报内存达到上限，进程终止，从而发生断线重连现象。

## 补充/答案 1

limit_memory_soft 系统默认设置是 2 G，limit_memory_hard默认设置是2.2G 。改成4G和4.5G似乎问题减少很多。
limit_memory_soft的意思是，如果某个请求（事务）内存消耗达到limit_memory_soft，则该请求处理结束，立即终止该Odoo进程。
limit_memory_hard的意思是，如果某个请求（事务）内存消耗达到limit_memory_hard，则立即终止该Odoo进程(不会等待该请求处理结束)。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
