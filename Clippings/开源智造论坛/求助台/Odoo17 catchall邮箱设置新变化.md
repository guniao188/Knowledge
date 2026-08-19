---
title: "Odoo17 catchall邮箱设置新变化"
source: "http://www.thinkltd.cn/forum/1/odoo17-catchall-3945"
forum: "求助台"
author: "肖相扶"
published: 2024-06-26
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17 catchall邮箱设置新变化

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-06-26
> <http://www.thinkltd.cn/forum/1/odoo17-catchall-3945>

1.  Odoo17支持不同域名的邮箱。例如系统中有A、B两家公司，A公司的销售邮箱是 sales@a.com, B公司的销售邮箱是 sales@b.com, 在以前的版本中，一套Odoo只能用一个邮箱后缀域名，不支持这种不同公司不同邮箱域名的情况。Odoo17可以支持这种情况了，设置示例如下图（菜单 “设置-->技术-->别名”）。

![[1-odoo17-catchall-3945-8e06cfbf.png]]

2.  发件服务器中，新增FROM过滤字段，该字段设置哪些发件人邮箱，或发件人邮箱域名走此发件服务器。例如A公司一个发件服务器，负责发送邮箱后缀域名为a.com的用户的邮件。B公司一个发件服务器，负责后缀域名b.com的邮箱。

![[1-odoo17-catchall-3945-e6cc3c1d.png]]

3.  系统参数中去除了 mail.catchall.domain 和 mail.catchall.alias的设置。改成了菜单“设置 --> 技术 --> 别名域”中设置，设置示例如下图。

![[1-odoo17-catchall-3945-25a37171.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
