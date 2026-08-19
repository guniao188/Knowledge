---
title: "OCA用户角色base_user_role"
source: "http://www.thinkltd.cn/forum/2/ocabase-user-role-2754"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA用户角色base_user_role

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocabase-user-role-2754>

模块链接：

- 定义用户角色概念，一个角色包含多个权限组，一个用户可以同时属于多个角色。

- 角色实现原理：系统自动为每个Role自动创建一个Group，该Group继承该Role设定好的Group

This module was written to extend the standard functionality regarding users and groups management. It helps creating well-defined user roles and associating them to users.

It can become very hard to maintain a large number of user profiles over time, juggling with many technical groups. For this purpose, this module will help you to:

> - define functional roles by aggregating low-level groups,
> - set user accounts with the predefined roles (roles are cumulative),
> - update groups of all relevant user accounts (all at once),
> - ensure that user accounts will have the groups defined in their roles (nothing more, nothing less). In other words, you can not set groups manually on a user as long as there is roles configured on it,
> - activate/deactivate roles depending on the date (useful to plan holidays, etc)
> - get a quick overview of roles and the related user accounts.

That way you make clear the different responsabilities within a company, and are able to add and update user accounts in a scalable and reliable way.

## [Configuration](https://github.com/OCA/server-backend/tree/12.0/base_user_role#id2)

To configure this module, you need to go to *Configuration / Users / Roles*, and create a new role. From there, you can add groups to compose your role, and then associate users to it.

You can also define default roles for a new user by editing the user called "Default User".

Roles:

Add groups:

Add users (with dates or not):


## 原帖外链配图

![[2-ocabase-user-role-2754-x194038c2.png]]
<small>原始地址: /web/image/1233/snipaste_20190129_155643.png?access_token=09186da5-9d13-4116-81e0-602ae0ff9166</small>

![[2-ocabase-user-role-2754-x194038c2.png]]
<small>原始地址: /web/image/1235/snipaste_20190129_155143.png?access_token=d9d24270-b1ce-4899-90ad-4f1ec2a9628d</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
