---
title: "待二开钉钉账号授权登录Odoo模块auth_ding"
source: "http://www.thinkltd.cn/forum/2/odooauth-ding-3272"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 待二开钉钉账号授权登录Odoo模块auth_ding

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odooauth-ding-3272>

【模块设计】

1.  本模块依赖模块 auth_oauth

2.  Odoo 登录界面增加“钉钉登录”链接。

3.  点击“钉钉登录”链接，系统判断是 非移动设备浏览器，调用钉钉扫码授权界面。如果是移动设备浏览器，调用钉钉免扫码授权界面。如果是钉钉浏览器，调用钉钉免授权接口。

4.  钉钉授权后，系统以钉钉openid 匹配 res.users 的 oauth_uid字段，匹配到则取该用户的钉钉授权令牌（字段oauth_access_token），调用钉钉接口验证授权是否有效，无效则获取新令牌，并保存到oauth_access_token 。

5.  未匹配到res.users，则以获取到的钉钉手机号码或者 ding_openid 为 login，自动创建一个Portal User，oauth_uid中存放openid ，获取钉钉授权token到字段oauth_access_token 。

## 补充/答案 1

【模块用法】

钉钉接口配置说明如下：

app id：钉钉开放者平台/应用开发/移动应用接入/登录/扫码登录/appId
app secret：钉钉开放者平台/应用开发/移动应用接入/登录/扫码登录/appSecret

Corp id：钉钉开放者平台/应用开发/企业内部开发/小程序=》应用首页/应用信息/AppKey
Corp Secret：钉钉开放者平台/应用开发/企业内部开发/小程序=》应用首页/应用信息/AppSecret

身份验证网址：https://oapi.dingtalk.com/connect/qrconnect
作用域：snsapi_login
验证网址：https://oapi.dingtalk.com/sns/gettoken
数据网址：https://oapi.dingtalk.com/sns/getuserinfo

## 补充/答案 2

![[2-odooauth-ding-3272-3a16ba6b.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
