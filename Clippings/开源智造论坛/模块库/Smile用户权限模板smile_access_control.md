---
title: "Smile用户权限模板smile_access_control"
source: "http://www.thinkltd.cn/forum/2/smilesmile-access-control-3061"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile用户权限模板smile_access_control

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smilesmile-access-control-3061>

模块链接：

This module allows to manage users' rights using profiles.

Odoo's groups are a coherent set of rules that functionally consistent. Profiles allow you to combine several groups and effectively tailor users' access to each user.

Here an exemple :

- accounting group : create an invoice, modify an invoice, cancel an invoice
- business develloper group : create a lead, modify data of lead, close a deal

The CEO of an SME will probably belong to both groups. Profils allows to combine the both groups in one profil.

This is an alternative way to manage users rights by functional profiles.

Basically, a « profile » is a fictive user (res.users) tagged as a profile.

It means that like before (with the basic rules of Odoo), you can add groups to your profile.

Features:

- You can associate a profile to created users.
- You can add users by profile.
- You can set fields to update for linked users.
- You have the choice to update or not in write mode for associated users, with field 'Update users' in profiles.

## [Configuration](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_access_control#id1)

To configure this module, you need to:

- Go to new menu **Settings > Users & Companies > User Profiles** and create the profiles you need.

##

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_access_control#id2)

- Go to new menu **Settings > Users & Companies > Users** and create a new user, choose the profile and after saving you will have user access rights set.


## 原帖外链配图

![[2-smilesmile-access-control-3061-x194038c2.png]]
<small>原始地址: /web/image/1656/snipaste_20190531_211952.png?access_token=4fbc4abb-c271-4542-8478-933db8b68f0a</small>

![[2-smilesmile-access-control-3061-x194038c2.png]]
<small>原始地址: /web/image/1658/snipaste_20190531_212011.png?access_token=7b088872-03b0-4395-a95b-dbc3ad4ba28e</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
