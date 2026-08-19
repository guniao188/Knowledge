---
title: "Smile rpc、sql执行时间数据采集smile_perf_analyzer"
source: "http://www.thinkltd.cn/forum/2/smile-rpcsqlsmile-perf-analyzer-3068"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile rpc、sql执行时间数据采集smile_perf_analyzer

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smile-rpcsqlsmile-perf-analyzer-3068>

模块链接：

This module log in function of logging rules:

- each JSON-RPC / XML-RPC call linked to a model: db, datetime, model, method, user, total time, db time, args, result
- Python method profiling
- SQL queries stats

A logging rule is defined directly via the user interface (menu: Settings > Technical > Performance > Rules) and it's applied without restarting Odoo server.

To hide the database _perf created during the installation :

- add "dbfilter = (?!.*_perf$)" in your config file.
-

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_perf_analyzer#id1)

To create a rule :

1.  Go to `Settings > Technical > Performance> Rules` menu :

- In this example we will create a rule for Administrator account in sale.order module :

> We specify :

> > 1.  Methods,
> > 2.  Slow RPC calls - Min. duration,
> > 3.  Slow SQL requests - Min. duration,
> > 4.  Slow field's recomputation - Min. duration
> > 5.  Profile Python methods,
> > 6.  Log SQL requests

2.  The rule will be added to the rules :

3.  Then, when the Administrator executes one of the methods declared in the created rule, Performance Analyzer will record automatically :

- Date
- Method
- SQL requests time
- SQL requests count
- Total Time, etc

To show the Logs :

4.  Go to `Settings > Technical > Performance`> Logs menu :

## 补充/答案 1

1.  本模块安装时候，自动创建一个perf数据库，该数据库名称是，当前安装模块的数据库名称 + 后缀 _perf

2.  安装本模块前，数据库要安装扩展 postgres_fdw，该扩展使得Odoo可以跨库读写perf数据库的数据


## 原帖外链配图

![[2-smile-rpcsqlsmile-perf-analyzer-3068-x90046962.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_perf_analyzer/static/description/rules.png</small>

![[2-smile-rpcsqlsmile-perf-analyzer-3068-xc41e303a.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_perf_analyzer/static/description/logs.png</small>

![[2-smile-rpcsqlsmile-perf-analyzer-3068-x194038c2.png]]
<small>原始地址: /web/image/1662/snipaste_20190604_165330.png?access_token=7ef0bb59-cabf-4bff-a4f1-57a3356a81b6</small>

![[2-smile-rpcsqlsmile-perf-analyzer-3068-x194038c2.png]]
<small>原始地址: /web/image/1664/snipaste_20190604_170753.png?access_token=88351b64-de28-4d5f-9489-951765f1bb52</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
