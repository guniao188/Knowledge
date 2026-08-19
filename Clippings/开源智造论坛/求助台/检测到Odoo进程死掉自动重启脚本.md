---
title: "检测到Odoo进程死掉自动重启脚本"
source: "http://www.thinkltd.cn/forum/1/odoo-309"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 检测到Odoo进程死掉自动重启脚本

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo-309>

1) 脚本参见附件文件（另存为.sh文件），上传到服务器，增加执行权限：chmod +x 。**注意修改脚本中字样 odoo-20170926  为 自己服务器上的Odoo进程标志字样。**上传到服务器，修改好脚本，手动执行一下看看效果。手动执行OK了，再设置到crontab 中 **。**

2) crontab -e ，添加类似下面的命令行。该命令行每5分钟检测一下Odoo进程是否存在，不存在就自动重启。**注意按上传的实际路径修改脚本openerp-ctrl.sh的目录。**

*/5 * * * * /opt/openerp/oscg/openerp-ctrl.sh oe_start

3) 脚本命令参数：openerp-ctrl oe_stop|oe_start|restart|pcheck|oe_check|oe_dropdb

oe_stop：停止Odoo进程，尤其是多进程模式下，该命令比手工杀进程方便很多

oe_start：检测Odoo进程是否在，不在就自动启动

restart：重启Odoo进程

pcheck：以telnet方式检测Odoo端口，看是否可以访问，不可以访问则重启Odoo。有时候会出现Odoo进程在，但就是不能访问的情况，重启Odoo又好了。尤其多进程模式下，这个问题出现概率高。此命令检测此种情况。

oe_check：以wget命令访问Odoo网站，如果返回500错误，则重启Odoo。有时候会出现不知道的原因，Odoo进程在，但网页500错误，重启Odoo又OK了

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
