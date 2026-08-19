---
title: "Smile数据库备份屏蔽敏感信息smile_anonymization、smile_anonymization_hr"
source: "http://www.thinkltd.cn/forum/2/smilesmile-anonymizationsmile-anonymization-hr-3051"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile数据库备份屏蔽敏感信息smile_anonymization、smile_anonymization_hr

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smilesmile-anonymizationsmile-anonymization-hr-3051>

模块链接：

字段定义中，增加属性 data_mask ，指定数据库备份时候，如何屏蔽该字段值。主要用于电话号码等敏感字段，备份时候的屏蔽。

This module allows to anonymize automatically a database backup. To do that, you need to define data mask on model fields in Python code or via UI.

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_anonymization#id1)

A data mask is a SQL statement, e.g.:

`'partner_' || id::text WHERE is_company IS NOT TRUE`

Add such a mask on the fields containing sensitive data:

- in Python code, e.g.: `fields.Char(data_mask='NULL')`
- in UI via the menu *Settings > Technical > Database Structure > Fields*

The lock icon allows not to overload data mask at each module update if you defined it in Python code and modify via UI.

Add this module in *server_wide_modules* list in your config file or in the option *--load*.

Go to database manager and backup the desired database. You will download a anonymized backup.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
