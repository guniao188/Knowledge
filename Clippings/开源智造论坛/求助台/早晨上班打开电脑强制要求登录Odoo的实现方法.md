---
title: "早晨上班打开电脑强制要求登录Odoo的实现方法"
source: "http://www.thinkltd.cn/forum/1/odoo-981"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 早晨上班打开电脑强制要求登录Odoo的实现方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo-981>

【业务背景】

客户“数皆” 实施了Odoo的薪酬模块，数据保密要求高。Odoo现有功能是，登录后，7天内可以免输密码，自动登录。为了提高安全性，客户要求：1）登录一定时间后，强制登出，要求重新输入密码登录。2）关闭浏览器，或者关闭电脑后，重新打开浏览器，连接Odoo，要求重新登录。3）早晨上班，连接Odoo，强制要求登录。

【解决办法】

1.  登录一定时间后，强制登出，参考这个模块：[一定时间无操作后自动退出登录Logout登出Odoo模块base_auto_logout](http://www.thinkltd.cn/forum/2/question/logoutodoobase-auto-logout-3576)

2.  重启电脑，或重新打开浏览器后，强制要求登录，这个要求暂无解决办法。

3.  早晨上班强制要求登录Odoo的一个解决办法是，Odoo服务器配置一个cron_tab任务，半夜自动删除Odoo服务器的用户session 。Odoo session存储路径在 conf文件配置的 data_dir 文件夹内。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
