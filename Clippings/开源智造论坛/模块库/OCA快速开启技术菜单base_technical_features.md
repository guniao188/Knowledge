---
title: "OCA快速开启技术菜单base_technical_features"
source: "http://www.thinkltd.cn/forum/2/ocabase-technical-features-2570"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA快速开启技术菜单base_technical_features

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocabase-technical-features-2570>

模块链接：

该模块在用户偏好里增加了一个"Technical Features"字段，勾选该字段，立即可以看见所有技术菜单（无需开Debug模式）。系统原本是要求Debug模式下面才显示技术菜单。

After installation of this module, every employee can still access technical features for the applications that they have access to by enabling debug mode. Additionally, users can check the *Technical feature* field in their preferences to gain permanent access to the menus and views that fall under this category.

Upon installation of this module, this preference is already set for the administrator user of the database.

In the background, this preference is mapped to the *Technical feature (w/o debug mode)* group that this module adds. As an administrator, you can therefore manage this preference from the regular Users and Groups menu items. f it's not unique.


## 原帖外链配图

![[2-ocabase-technical-features-2570-x7c3b279e.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/server-ux/12.0/base_technical_features/static/description/user_preferenc</small>

![[2-ocabase-technical-features-2570-x194038c2.png]]
<small>原始地址: /web/image/849/snipaste_20190119_221957.png?access_token=6a9d8706-2e7a-4836-9e6d-dde09f50b61b</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
