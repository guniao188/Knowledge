---
title: "admin账号不小心拿掉了【设置】权限组权限，该如何恢复"
source: "http://www.thinkltd.cn/forum/1/admin-721"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# admin账号不小心拿掉了【设置】权限组权限，该如何恢复

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/admin-721>

调配权限显示时，如果不小心将admin账号的设置组权限拿掉了。

可能用sql语句后台恢复一下。

sql语句命令如下：

insert into res_groups_users_rel values(3,2);

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
