---
title: "odoo_auto_logout无操作XX时间后自动退出登录"
source: "http://www.thinkltd.cn/forum/2/odoo-auto-logoutxx-3546"
forum: "模块库"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# odoo_auto_logout无操作XX时间后自动退出登录

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoo-auto-logoutxx-3546>

方案一：

-修改源码记录 /opt/odoo/odoo14/odoo-server/odoo下的http.py文件中： STATIC_CACHE = 3600 * 24 * 1参数，由7天改成了1天（用户登录缓存） 还调整了第1168行的参数： if random.random() < 0.1: # we keep session one week last_week = time.time() - 60*60*12
但是这个方案有个问题，是固定的时间退出登录，而不是监控用户操作状态而休眠退出；

方案二：第三方应用插件功能odoo_auto_logout

改善后的模块参见（每个用户都可以单独设置登出时间）：[一定时间无操作后自动Logout登出Odoo模块base_auto_logout](http://www.thinkltd.cn/forum/2/question/logoutodoobase-auto-logout-3576)

官方查看和购买链接：https://apps.odoo.com/apps/modules/15.0/odoo_auto_logout/

![[2-odoo-auto-logoutxx-3546-8956e44e.png]]

King已购买V14版本

下载链接：

https://apps.odoo.com/loempia/download/tmp/odoo_auto_logout/2022-06-06/27592/0f451edc70c5d01d4bdb54b2498ea2b9400bdb16a5df8a7a931b398ffd3ca476.zip?deps#

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
