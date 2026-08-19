---
title: "Odoo邮箱配置若干问题解析"
source: "http://www.thinkltd.cn/forum/1/odoo-295"
forum: "求助台"
author: "肖相扶"
published: 2024-07-31
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo邮箱配置若干问题解析

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-07-31
> <http://www.thinkltd.cn/forum/1/odoo-295>

【万能邮箱配置方法】
1) 企业邮箱管理员创建postmaster-odoo邮箱（例postmaster-odoo@oscg.biz）；
2) Odoo中设置postmaster-odoo作为发送邮件服务器；
3) 同时系统参数中不设置mail.bounce.alias ，但要设置 mail.catchall.domain 为邮箱域名。
腾讯企业邮箱，163企业邮箱，各类企业邮箱，此方法都有效。

4）正式解决365不允许代发的问题的说明，请参考附件SVN地址：D:\svn\SVN\odoo_ecommerce\03.R&D\**365邮箱设置中断代发配置**

【问题1】Odoo SMTP服务器设置为QQ邮箱，邮件发送失败：
邮件投递失败
通过SMTP发送邮件失败 'smtp.qq.com'.
SMTPSenderRefused: 501
mail from address must be same as authorization user
help@odoo.com

同样的Odoo环境，换成263收费邮箱，或者腾讯企业收费邮箱，发送正常。什么原因呢？

【问题2】163企业邮箱，发送报错，如下。From和Sender用的同一个邮箱。

邮件发送失败 通过SMTP发送邮件失败 'None'.
SMTPSenderRefused: 550

5.8.1 Local user only.
postmaster-odoo@maxcess-china.com

【问题3】腾讯企业邮箱

邮件发送失败
通过SMTP发送邮件失败 'None'.
SMTPSenderRefused: 501
mail from address must be same as authorization user
postmaster-odoo@oscg.biz

【问题4】office365企业邮箱

Mail Delivery Failed Mail delivery failed via SMTP server 'None'. SMTPDataError: 554 5.2.0 STOREDRV.Submission.Exception:SendAsDeniedException.MapiExceptionSendAsDenied; Failed to process message due to a permanent exception with message Cannot submit

经查，office365要求From和Sender用的同一个邮箱（Office365不允许代发邮件）。下述链接的最后，Office365表明不希望通过Office365代发邮件，但下述链接中，Office365也提供了代发邮件的设置方法（选项三），设置比较繁琐。
有客户案例调通过，主要是要邮箱管理员修改这个选项，需要开通发送权限。

![[1-odoo-295-a4f0eb0a.png]]

[如何设置多功能设备或应用程序以使用 Microsoft 365 或 Office 365 发送电子邮件 | Microsoft Docs](https://docs.microsoft.com/zh-cn/Exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365?redirectSourcePath=%252fen-us%252farticle%252fHow-to-set-up-a-multifunction-device-or-application-to-send-email-using-Office-365-69f58e99-c550-4274-ad18-c805d654b4c4)

![[1-odoo-295-bcc21740.png]]

![[1-odoo-295-a127d667.png]]

![[1-odoo-295-4d5b7bee.png]]

[进入这个管理员设置界面的网址链接：](https://docs.microsoft.com/zh-cn/Exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365?redirectSourcePath=%252fen-us%252farticle%252fHow-to-set-up-a-multifunction-device-or-application-to-send-email-using-Office-365-69f58e99-c550-4274-ad18-c805d654b4c4)

[https://admin.microsoft.com/Adminportal/Home?source=applauncher#/homepage](https://docs.microsoft.com/zh-cn/Exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365?redirectSourcePath=%252fen-us%252farticle%252fHow-to-set-up-a-multifunction-device-or-application-to-send-email-using-Office-365-69f58e99-c550-4274-ad18-c805d654b4c4)

[

![[1-odoo-295-9417253f.png]]

](https://docs.microsoft.com/zh-cn/Exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365?redirectSourcePath=%252fen-us%252farticle%252fHow-to-set-up-a-multifunction-device-or-application-to-send-email-using-Office-365-69f58e99-c550-4274-ad18-c805d654b4c4)

![[1-odoo-295-9d3a969c.png]]

![[1-odoo-295-3a588020.png]]

![[1-odoo-295-54302d30.png]]

![[1-odoo-295-72eb6ba9.png]]

## 补充/答案 1

【问题1】

据查，邮件发送的SMTP协议中，有From、Sender两个角色，From是发件人的邮箱，Sender是登录SMTP服务器的邮箱（用户名）。如下面这个邮件源码所示，From是Eric ，Sender是zhiyunerp@oscg.cn 。QQ，163的大部分免费邮箱要求From和Sender必须是同一个邮箱（免费的Sender只能发送自己的邮件，不允许你替别人发送邮件）。

这里有一个Odoo模块修复这个问题： [https://github.com/buke/openerp-mail-server-smtp-user](https://github%5C.com/buke/openerp%5C-mail%5C-server%5C-smtp%5C-user)

但该模块有个问题，它强行将From邮箱改成Sender邮箱。安装这个模块后，邮件是可以发了，但收件方看不见是哪个人发的邮件（看到的永远是Sender）。

Received: from regular1.263xmail.com (unknown [211.150.99.137])

by newmx122.qq.com (NewMx) with SMTP id

for ; Wed, 06 Sep 2017 14:43:47 +0800

X-QQ-FEAT: XoWZfUq5xBiAOYE+f9elKHiL3EZd0BysoInWqkGmLoKzqmbt0VO1z3GiloVj/

3x2w0rT9V//aXsHqCLOEulibEiyGX5vi9V3D3TGryLVD/YB9gIa1eJ/KpsRZ4Sh/YgRVKke

Z4zYRJ64qvmnf/AcM6s7K+H84pZpIB+K8D/kPxrFMG0N3WnCtawMFcmdDQGPXFZ+jzSqluZ

IidgTWFP+08qwBSKKB6kI5//RBNg7mUdKoM9Y4soiK8IKraSfC5Tp9B+N/+7RuPaSUQW0Ml

zGJkLHPOfiq5+uMXY8A01mZkSFHYGkXye4OTEs6SCrPByH

X-QQ-MAILINFO: MjJD59SVx+LnpahJ/YkD10sHfxPylywKC4VgikUdysvFQfDfdXqa5XU1g

+pZ404WJVdgONm8E/9a8OBfgQvWtXq3hQ4a/Ng0o5cjwbpVZAeeiOjY6kApTDyfCoj5K55W

7BDXz03WSKakGUuH4ANQ0OQpSh2N68+kJqLFkTPlfwTN78IZDXh+nLrPuaJJIPsmwU2cTAo

XCOrWiv4oulCWCSawETEJMeEiRA==

X-QQ-mid: mx122t1504680228tvkb7gokk

X-QQ-CSender: zhiyunerp@oscg.cn

X-QQ-ORGSender: zhiyunerp@oscg.cn

Received: from zhiyunerp?oscg.cn (unknown [192.168.167.223])

by regular1.263xmail.com (Postfix) with ESMTP id B0B6ADC18

for ; Wed,  6 Sep 2017 14:43:45 +0800 (CST)

X-263anti-spam:KSV:0;BIG:0;

X-MAIL-GRAY:0

X-MAIL-DELIVERY:1

X-KSVirus-check:0

X-ADDR-CHECKED4:1

X-ABS-CHECKED:1

X-SKE-CHECKED:1

X-ANTISPAM-LEVEL:2

Received: from [10.135.44.76] (localhost [127.0.0.1])

by smtp.263.net (Postfix) with ESMTPA id 27FF2387

for ; Wed,  6 Sep 2017 14:43:47 +0800 (CST)

X-RL-SENDER:zhiyunerp@oscg.cn

X-FST-TO:1417063315@qq.com

X-SENDER-IP:121.40.25.211

X-LOGIN-NAME:zhiyunerp@oscg.cn

X-UNIQUE-TAG:

X-ATTACHMENT-NUM:0

X-SENDER:zhiyunerp@oscg.cn

X-DNS-TYPE:0

Received: from [10.135.44.76] (unknown [121.40.25.211])

by smtp.263.net (Postfix) whith ESMTP id 10414HMAUIN;

Wed, 06 Sep 2017 14:43:47 +0800 (CST)

Content-Type: multipart/mixed; boundary="===============2517494064163456641=="

MIME-Version: 1.0

Message-Id:

references:

Subject: =?utf-8?b?5Zue5aSNOiDmiafooYzliKDpmaTmk43kvZzml7bvvIzpg73miafooYzkuoY=?=

 =?utf-8?b?5ZOq5Lqb5pON5L2c77yf?=

From: Eric

Reply-To: =?utf-8?b?6YCg5rqQ5L+h5oGv56eR5oqAKOS4iua1tynmnInpmZDlhazlj7g=?=

To: =?utf-8?b?6IKW55u45om2?=

Date: Wed, 06 Sep 2017 06:43:46 -0000

【问题2】

经查，SMTP协议有Bounce机制：当邮件投递失败时候，“弹回”到哪个邮箱。SMTP定义的弹回情况有：

Return Code Description
0 UNDETERMINED - (ie. Recipient Reply)
10 HARD BOUNCE - (ie. User Unknown)
20 SOFT BOUNCE - General
21 SOFT BOUNCE - Dns Failure
22 SOFT BOUNCE - Mailbox Full
23 SOFT BOUNCE - Message Too Large
30 BOUNCE - NO EMAIL ADDRESS. VERY RARE!
40 GENERAL BOUNCE

Odoo中处理Bounce的机制是：如果设置了系统参数 mail.bounce.alias 和 mail.catchall.domain，Odoo自动拼接 Bounce邮箱（SMTP Header的Return-Path）的规则是，如果该邮件有对应的模型，拼接规则： '%s+%d-%s-%d@%s' % (bounce_alias, mail.id, mail.model, mail.res_id, catchall_domain) ，如果邮件没有模型，拼接规则： '%s+%d@%s' % (bounce_alias, mail.id, catchall_domain)

如果没有设置系统参数 mail.bounce.alias，Bounce固定取postmaster-odoo，邮箱拼接规则是 postmaster-odoo@catchall_domain 。

调查发现，163邮箱服务器不仅要求发送邮件的 From、Sender必须相同，且要求Bounce也必须存在，且和Sender是同一个域名（5.8.1 Local user only）

解决方法是，在163邮箱配置 postmaster-odoo邮箱，Odoo系统参数中不设置mail.bounce.alias 。

【问题3】经测试，腾讯企业邮箱是允许 From和Sender非同一个邮箱，但是，Bounce邮箱和Sender必须是同一个邮箱。因此，腾讯企业邮箱的情况，应该设置postmaster-odoo邮箱（例postmaster-odoo@oscg.biz），Odoo设置postmaster-odoo 发送邮件。同时系统参数中不设置mail.bounce.alias 。

## 补充/答案 2

分享个一次性解决odoo13邮件配置的技术方法：

1. 先配置好对应的收件服务器和发件服务器（这里采用的是阿里云的企业邮箱）：

![[1-odoo-295-b261a891.png]]

![[1-odoo-295-6af3353d.png]]

记得用这个阿里的企业邮箱的SMTP地址，然后端口用不加密的25的

![[1-odoo-295-c01dd2c0.png]]

收件的也是如此，别加密

![[1-odoo-295-7dbbf8c1.png]]

mail.catchall.alias和mail.bounce.alias两个参数改成发件箱设置的前缀名称。如果测试后发现不行使用以下大招：

进代码里修改如图所示的代码部分，然后删除mail.bounce.alias参数

![[1-odoo-295-d056befb.png]]

这里经过最终测试完成了邮件的推送和接收推送的问题

![[1-odoo-295-6883fd4b.png]]

腾讯企业邮箱，有可能会开启了安全机制，导致无法登录，一定要扫码才能登录的问题，需要用户登录进入修改安全设置：

![[1-odoo-295-908bf977.png]]

![[1-odoo-295-572bd4da.png]]

阿里上的设置检查要点：

![[1-odoo-295-d5cf251c.png]]

域名绑定解析是正常的；用邮箱管理员在【概览】中可以看到：

![[1-odoo-295-e0fef870.png]]

员工邮箱账号里需要开启POP/IMPAP服务

![[1-odoo-295-660e11ef.png]]

![[1-odoo-295-71897e7e.png]]

**所有用于odoo的公共邮箱，独立使用开通，odoo需要开通的必须要有postmaster-odoo开头和 catchall**

**其他应用下需要使用的邮箱需要在发件服务器和收件服务器中都要配置好。**

![[1-odoo-295-4f119de7.png]]

V13之后版本开始，就有后台代码强制要求发件人和当前账号要一致，故需要公共邮箱都要配好相应的邮箱服务器。

![[1-odoo-295-589abcf2.png]]

![[1-odoo-295-358914e7.png]]

## 补充/答案 3

163企业邮箱，发送报错，如下。From和Sender用的同一个邮箱。

邮件发送失败 通过SMTP发送邮件失败 'None'.
SMTPSenderRefused: 550

5.8.1 Local user only.
postmaster-odoo@maxcess-china.com

-------------请问这个要如何解决呢？

## 补充/答案 4

将From邮箱改成Sender邮箱模块已升级到V12 并上传到SVN     C:\odoo_ecommerce\12.0SRC\mail_server_smtp_user

## 补充/答案 5

如果国外客户配置Gmail邮箱，注意要客户登录邮箱，把邮箱的app access设置为On, 否则会报535的错

![[1-odoo-295-101e982f.png]]

Log in to your Google account or use this link [https://security.google.com/settings/security/apppasswords](https://security.google.com/settings/security/apppasswords)

- Go to `My Account > Sign-in & Security > App Passwords`

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
