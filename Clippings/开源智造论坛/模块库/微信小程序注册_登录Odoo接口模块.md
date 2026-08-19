---
title: "微信小程序注册/登录Odoo接口模块"
source: "http://www.thinkltd.cn/forum/2/odoo-3577"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 微信小程序注册/登录Odoo接口模块

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoo-3577>

模块链接：OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\auth_oauth_wxapplet

【模块功能】

1.  微信小程序以手机号码、昵称、openid自动注册Odoo用户的接口

2.  微信小程序以openid、session_key自动登录Odoo的接口

3.  增加用户角色表单，微信小程序注册时候可以指定用户角色，用户角色上可以配置该角色的模板用户，注册该角色时候，系统自动复制模板用户创建新用户。

【微信小程序调用方法】

1.  调用链接 /auth_oauth/wxapplet；

2.  kw参数说明：applet_code：登录（login）小程序时候的code；openid: 待注册用户的openid；session_key: 待注册用户的session_key、mobile_code：授权获取用户手机号码时候的code、user_role：用户的角色，默认是portal；name：用户姓名或昵称

3.  调用步骤：先传applet_code，如果对应的openid的用户存在，则系统返回Odoo登录成功的session_info；如果对应的用户不存在，返回openid、session_key给到微信小程序端； 用户不存在的情况，微信小程序端应该授权获取微信用户的手机号码、姓名，而后再次调用本接口注册新用户。注册成功后自动登录Odoo，返回session_info

4.

【微信小程序代码示例】

参考 OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\auth_oauth_wxapplet\微信小程序示例代码\miniprogram-1.zip

【功能截图】

![[2-odoo-3577-38c50398.png]]

【参考资料】

1.  测试用微信小程序申请：[申请测试号 | 微信开放文档 (qq.com)](https://developers.weixin.qq.com/miniprogram/dev/devtools/sandbox.html)

2.  微信小程序开发文档：[基础 | 微信开放文档 (qq.com)](https://developers.weixin.qq.com/miniprogram/dev/api/)

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
