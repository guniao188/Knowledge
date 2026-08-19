---
title: "待二开微信账号授权登录Odoo模块auth_wechat"
source: "http://www.thinkltd.cn/forum/2/odooauth-wechat-3154"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 待二开微信账号授权登录Odoo模块auth_wechat

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odooauth-wechat-3154>

【模块设计】

1.  本模块依赖模块 auth_oauth

2.  Odoo 登录界面增加“微信登录/绑定微信”链接。文字首先显示“微信登录”。用户输入了用户名和密码，文字显示“绑定微信”。

3.  点击“微信登录/绑定微信”链接，系统判断是非移动设备浏览器，调用微信扫码授权界面。如果是移动设备浏览器，调用微信免扫码授权接口。如果是微信浏览器，调用微信免授权接口。

4.  微信授权后，如果输入了用户名和密码（绑定微信），系统以用户名和密码登录系统，登录成功，将微信openid写入该用户的oauth_uid字段。

5.  如果没输入用户名和密码，或输入不全（微信登录），系统以微信openid 匹配 res.users 的 oauth_uid字段，匹配到则取该用户的微信授权令牌（字段oauth_access_token），调用微信接口验证授权是否有效，无效则获取新令牌，并保存到oauth_access_token 。

6.  未匹配到res.users，则以 wx_openid 为login，自动创建一个Portal User，oauth_uid中存放openid ，获取微信授权token到字段oauth_access_token 。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
