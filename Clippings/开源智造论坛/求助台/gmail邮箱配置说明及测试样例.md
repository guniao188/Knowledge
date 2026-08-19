---
title: "gmail邮箱配置说明及测试样例"
source: "http://www.thinkltd.cn/forum/1/gmail-3915"
forum: "求助台"
author: "符赛红"
published: 2024-04-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# gmail邮箱配置说明及测试样例

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2024-04-10
> <http://www.thinkltd.cn/forum/1/gmail-3915>

需要odoo里设置和gmail账号里设置开通

odoo官方针对gmail邮箱的配置说明参考链接：[https://www.odoo.com/documentation/17.0/applications/general/email_communication/google_oauth.html](https://www.odoo.com/documentation/17.0/applications/general/email_communication/google_oauth.htmlhttps://www.odoo.com/documentation/17.0/applications/general/email_communication/google_oauth.html)

针对gmail的设置，smtp及Pop的设置参考说明：

[https://support.google.com/mail/answer/7104828?hl=en&amp;sjid=1390837046509351710-NC](https://support.google.com/mail/answer/7104828?hl=en&amp;sjid=1390837046509351710-NC)

如果要开通google用户授权登录，需要

创建一个项目地址

针对gmail里面的设置及odoo里的设置可以查看视频头，需要VPN打开

[https://www.youtube.com/watch?v=9Ni3WW6FeZg](https://www.youtube.com/watch?v=9Ni3WW6FeZg)视频设置google邮箱解说

在google账户里登录进入后，需要设置开启：

登录该gmail账号，目前示例是免费的个人gmail邮箱，可以连通，连的示例是V17版本。

[https://mail.google.com/mail/u/0/#inbox/FMfcgzGxSbnRcjPNsBPTlbGdpxZfBPMQ](https://mail.google.com/mail/u/0/#inbox/FMfcgzGxSbnRcjPNsBPTlbGdpxZfBPMQ)

然后进到我的账户里，搜索打开app passwords

进入设置页面里[https://myaccount.google.com/security?hl=en&amp;utm_source=my-activity&amp;utm_medium=logo](https://myaccount.google.com/security?hl=en&amp;utm_source=my-activity&amp;utm_medium=logo)然后直接搜索app passwords

![[1-gmail-3915-6401bfe3.png]]

然后设置填写app名字，再获得一个密钥：

![[1-gmail-3915-fe00eacb.png]]

将密钥填写在odoo的邮箱服务器里面。

![[1-gmail-3915-d4b109a3.png]]

![[1-gmail-3915-03e0d178.png]]

![[1-gmail-3915-4d712fbb.png]]

![[1-gmail-3915-be909ed0.png]]

![[1-gmail-3915-85814f6a.png]]

![[1-gmail-3915-dafe13fc.png]]

测试验证文档参考：


## 附件

- [[附件/forum/1-gmail-3915-邮箱收发测试验证.docx|邮箱收发测试验证.docx]] (1.7 MB)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
