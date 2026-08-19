---
title: "手机号注册及短信验证auth_signup_sms"
source: "http://www.thinkltd.cn/forum/2/auth-signup-sms-3275"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 手机号注册及短信验证auth_signup_sms

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/auth-signup-sms-3275>

模块链接：OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\auth_signup_sms

【模块功能】

1.  Odoo注册页面，增加手机号码作为注册账号（login）的 选项。选择手机号码注册时候，注册页面增加短信验证码功能

2.  手机号作为账号注册时候，login写入mobile字段，不写入 email字段

3.  密码重置时候，除了系统自带的密码重置邮件，如果用户有mobile，增加短信方式发送密码重置链接

4.  增加系统参数，sms.validate.minutes，配置短信验证码的有效时间（分钟）

5.  增加“手机验证码”、“密码重置”的短信模板

6.  已知问题，模块安装后，查找“手机短信登录验证”的视图，修改继承模式为“扩展”，如下面截图

7.  手机短信发送模块参考 [二开短信发送模块sms_zhutong](http://www.thinkltd.cn/forum/2/question/sms-zhutong-3276)

【功能截图】

![[2-auth-signup-sms-3275-ff4e66e0.png]]

![[2-auth-signup-sms-3275-82a183a3.png]]

![[2-auth-signup-sms-3275-7897ffec.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
