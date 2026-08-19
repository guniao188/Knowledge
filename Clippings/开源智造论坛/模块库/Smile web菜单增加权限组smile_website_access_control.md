---
title: "Smile web菜单增加权限组smile_website_access_control"
source: "http://www.thinkltd.cn/forum/2/smile-websmile-website-access-control-3070"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile web菜单增加权限组smile_website_access_control

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smile-websmile-website-access-control-3070>

模块链接：

## Website Access Control

This module is used to hide website menus depending on whether the user is part of a group or not.

##

## Usage

Once installed, the module creates a list on the groups where you can add the menus of the website, if the connected user has this group, he will have access or not to the menu.

Example :

- I create a test web page
- I create a user test with 'Hidden features' group
- Add the webpage 'test' to the group

If I am connected with the user "test" on the website, I have access to the test menu, but it disappears if I disconnect

Add user to group:

Add menu to group:

Example without user logged in:

Without having the rights on the menu, you can't access it, even by typing the url directly.

Example with user logged in:


## 原帖外链配图

![[2-smile-websmile-website-access-contro-x7cbbb815.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_website_access_control/static/description/add_user_to_g</small>

![[2-smile-websmile-website-access-contro-x2c5e9682.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_website_access_control/static/description/add_menu_to_g</small>

![[2-smile-websmile-website-access-contro-x42d36c0e.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_website_access_control/static/description/website_witho</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
