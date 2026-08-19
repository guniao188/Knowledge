---
title: "Smile数据库日志模块smile_log"
source: "http://www.thinkltd.cn/forum/2/smilesmile-log-3047"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile数据库日志模块smile_log

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smilesmile-log-3047>

模块链接：

This module adds a logs handler writing to database.

Notice

> - Following code will create a log in db with a unique pid per logger:
>   import logging logger = SmileLogger(dbname, model_name, res_id, uid) logger.info(your_message)

Features :

- Create logs when executing an action.
- Archive and delete old logs from database.
- Give users access right to see logs.
-

## [Configuration](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_log#id1)

- Developer adds `import logging` to his python file.
- Developer must add following code to his action and specify the database, the model name, the res_id, and uid. Then give a message to log for information:

    logger = SmileLogger(dbname, model_name, res_id, uid)
    logger.info(your_message)

- Administrator must create a `Scheduled Action` to call the function `archive_and_delete_old_logs`, configure archiving path and the number of days to archive and delete logs.

##

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_log#id2)

To add Logs handler to an action :

> 1.  Import SmileDBLogger to your python code and add code lines as shown in following example :

>     >
>     >
>     >
>     >
>     >

> 2.  Add `smile_log` to your module dependence:

>     >
>     >
>     >
>     >
>     >

> 3.  Now execute the action.:

>     >
>     >
>     >
>     >
>     >

> 4.  Go to `Settings > Technical > Logging`> Logs menu to see logs.

>     >
>     >
>     >
>     >
>     >

Administrator can give access right to users, to see logs, by checking `Smile Logs / User`.

To create the scheduled action:
1.  Go to `Settings > Technical > Automation > Scheduled Actions` and fill fields as follow:

    >
    >
    >
    >
    >
    >
    > `(Make sure that the given folder has a write access!)`

2.  After running the action, the extracted logs file in csv format is as shown in next figure:

    >
    >
    >
    >
    >


## 原帖外链配图

![[2-smilesmile-log-3047-xcdef94f9.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_log/static/description/scheduled_action.png</small>

![[2-smilesmile-log-3047-x92d1c247.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_log/static/description/exported_log.png</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
