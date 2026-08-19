---
title: "Smile基础设置模块smile_base"
source: "http://www.thinkltd.cn/forum/2/smilesmile-base-3045"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile基础设置模块smile_base

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smilesmile-base-3045>

模块链接：

- Make French the default language if installed
- Disable the scheduled action "Update Notification" which sends companies and users info to Odoo S.A.
- Correct date and time format for French language
- Review the menu "Applications"
- Remove the menu "App store" and "Update modules" from apps.odoo.com.
- Add sequence and display window actions in IrValues
- Force to call unlink method at removal of remote object linked by a fields.many2one with ondelete='cascade'
- Add BaseModel.store_set_values and BaseModel._compute_store_set
- Improve BaseModel.load method performance
- Disable email sending/fetching by default
-

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_base#id1)

Add this module to your addons, it will auto install.

To enable email sending, add in your configuration file:
- enable_email_sending = True

To enable email fetching, add in your configuration file:
- enable_email_fetching = True

To enable sending of companies and users info to Odoo S.A., add in your configuration file:
- enable_publisher_warranty_contract_notification = True

## 补充/答案 1

1.  应用菜单中去除了 应用商店，右上角登录用户下拉菜单中去除了 Odoo相关的几个链接

2.  report Action 和 Server action的定义上，增加了 在哪些Action里面显示的配置项

3.  默认不允许收和发邮件，需要在conf文件中增加配置项目打开：

```python
        enable_email_sending = True
        enable_email_fetching = True
        enable_publisher_warranty_contract_notification = True
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
