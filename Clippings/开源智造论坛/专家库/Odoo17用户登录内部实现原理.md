---
title: "Odoo17用户登录内部实现原理"
source: "http://www.thinkltd.cn/forum/5/odoo17-3850"
forum: "专家库"
author: "吴键"
published: 2024-02-28
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/专家库
---

# Odoo17用户登录内部实现原理

> [!info] 来源
> 开源智造论坛 · 专家库 | 作者:吴键 | 2024-02-28
> <http://www.thinkltd.cn/forum/5/odoo17-3850>

【问题列表】
请说明Odoo用户登录的内部实现逻辑，依次说明下述登录验证模块的功能auth_ldap、auth_oauth、auth_password_policy、auth_password_policy_portal、auth_password_policy_signup、auth_signup、auth_totp、auth_totp_mail、auth_totp_mail_enforce、auth_totp_portal。

参考： [auth_ldap 实施方法](http://www%5C%5C.thinkltd%5C%5C.cn/forum/1/auth%5C%5C-ldap%5C%5C-621)、 [Odoo14企业微信登录验证auth_oauth_wechat](http://www%5C%5C.thinkltd%5C%5C.cn/forum/2/odoo14auth%5C%5C-oauth%5C%5C-wechat%5C%5C-3496)\\\\

【业务实现示例】
深圳网易优客户，他们销售随身Wifi等流量卡设备。消费者购买设备后，微信扫描设备上的二维码（二维码有用户注册/登录URL及设备号），输入手机号码、短信验证码，完成用户注册、用户和设备号的绑定。二维码内容示例：[http://tiot.ud0.com.cn/imei/erwema/info/d2dbdf56c5b06383fbc605fbd3edfd26/w/869069064352268](http://tiot%5C%5C%5C.ud0%5C%5C%5C.com%5C%5C%5C.cn/imei/erwema/info/d2dbdf56c5b06383fbc605fbd3edfd26/w/869069064352268) 。请说明，上述功能如何实现。

参考  [二开短信发送模块sms_zhutong](http://www%5C%5C.thinkltd%5C%5C.cn/forum/2/sms%5C%5C-zhutong%5C%5C-3276)、[手机号注册及短信验证auth_signup_sms](http://www%5C%5C.thinkltd%5C%5C.cn/forum/2/auth%5C%5C-signup%5C%5C-sms%5C%5C-3275)

![[5-odoo17-3850-fc597a86.png]]


## 附件

- [[附件/forum/5-odoo17-3850-IOT Box & Odoo说明文档.docx|IOT Box & Odoo说明文档.docx]] (6.8 MB)
- [[附件/forum/5-odoo17-3850-login.docx|login.docx]] (2.2 MB)

---

相关:[[Clippings/开源智造论坛/专家库/00-专家库索引.md|← 专家库索引]]
