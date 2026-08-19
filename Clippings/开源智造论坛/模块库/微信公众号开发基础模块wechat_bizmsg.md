---
title: "微信公众号开发基础模块wechat_bizmsg"
source: "http://www.thinkltd.cn/forum/2/wechat-bizmsg-3568"
forum: "模块库"
author: "肖相扶"
published: 2024-06-12
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 微信公众号开发基础模块wechat_bizmsg

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-06-12
> <http://www.thinkltd.cn/forum/2/wechat-bizmsg-3568>

模块位置：OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\wechat_bizmsg

【20040612本模块的功能增强版参见】 [Odoo聊天和微信公众号聊天的功能连通模块wechat_bizmsg](http://www.thinkltd.cn/forum/2/odoowechat-bizmsg-3936)

【模块功能】

1.  微信公众号接口参数设置，三个参数：appid, secret, token

2.  微信公众号后台管理中，“设置与开发” --> “基本配置” 中，服务器地址(URL)的处理功能：设置此URL时候，处理微信的回调消息

3.  微信公众号中，消息或事件发生时候，接收消息/事件，回复消息“Received.” 。此功能为消息处理的示范代码，参照此功能，根据实际业务需求，开发更多的微信公众号消息/事件处理功能。

4.  微信公众号中，点击Odoo页面链接，或者微信公众号的菜单链接到Odoo页面，自动以微信用户授权登录Odoo。如果是第一次登录（Odoo中还不存在此用户），自动跳转到Odoo的注册页面（/web/signup）。用户注册后，创建的Odoo User上，自动写入用户的微信openid （Odoo User模型上增加了一个字段 wx_openid）。

5.  注意事项：技术设置 --> 客户账号中，开启“免费注册”功能，否则第一次登录，系统跳转到注册页面时候会报 404 页面找不到错误

6.  此模块 [手机号注册及短信验证auth_signup_sms](http://www.thinkltd.cn/forum/2/question/auth-signup-sms-3275) 扩展了Odoo注册页面，增加了手机注册及短信验证码功能。

7.  微信公众号菜单链接到Odoo页面的URL设置方法（以电商购物页面 /shop 为例）：Odoo页面链接是

 http://erp1060.s1.oscg.cn/shop， 微信公众号中链接设置成：https://open.weixin.qq.com/connect/oauth2/authorize?appid=**YourAppid**&redirect_uri=http://**YourOdooServer**/wechat/signin&response_type=code&scope=snsapi_base&state=**/shop**#wechat_redirect  。粗体字的 YourAppid是微信公众号后台管理中的AppID；YourOdooServer是Odoo服务器访问域名，必须是公网可以访问的域名，因为微信要从公网回调该域名；/Shop是要设置的Odoo页面。
最后，还要将链接中的 : 替换成%3A，/替换成%2F，替换后的示例链接如下：https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxce445cb0c44564a1&redirect_uri=http%3A%2F%2Ferp1060.s1.oscg.cn%2Fwechat%2Fsignin&response_type=code&scope=snsapi_base&state=%2Fshop#wechat_redirect

【功能截图】

wechatpy技术文档：[安装与升级 - wechatpy 2.0.0.alpha25 文档](https://wechatpy.readthedocs.io/zh_CN/master/install.html)

微信公众号测试账号获取页面：[微信公众平台 (qq.com)](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login)

微信公众号开发技术参考文档：[微信公众平台开发概述 | 微信开放文档 (qq.com)](https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Overview.html)

微信公众号管理后台的设置

![[2-wechat-bizmsg-3568-90dbd9f1.png]]

微信公众号后台网页授权用的回调域名设置：

![[2-wechat-bizmsg-3568-05da09ce.png]]

Odoo后台微信公众号接口参数设置：

![[2-wechat-bizmsg-3568-c8a27ebc.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
