---
title: "Odoo15、Odoo16的会计模块account_accountant社区版安装说明"
source: "http://www.thinkltd.cn/forum/1/odoo15odoo16account-accountant-812"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo15、Odoo16的会计模块account_accountant社区版安装说明

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo15odoo16account-accountant-812>

**Odoo16.0**中，，企业版模块account_accountant及会计报表模块account_reports ，移到社区版安装，方法如下：

1.  同时移动下述四个模块（account_reports_cash_basis可以不要）：account_accountant，account_reports，mail_enterprise，web_mobile，account_auto_transfer

2.  模块 web_mobile的文件__manifest__.py 中，web_enterprise的依赖修改成 web 。如下截图所示。

![[1-odoo15odoo16account-accountant-812-f90defbf.png]]

**Odoo 15.0**中，企业版模块account_accountant ，移到社区版安装，只要删除文件 __manifest__.py 中的依赖模块 mail_enterprise  即可正常安装。

![[1-odoo15odoo16account-accountant-812-4978ff26.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
