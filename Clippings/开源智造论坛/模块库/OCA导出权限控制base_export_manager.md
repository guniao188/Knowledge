---
title: "OCA导出权限控制base_export_manager"
source: "http://www.thinkltd.cn/forum/2/ocabase-export-manager-2573"
forum: "模块库"
author: "肖相扶"
published: 2022-12-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA导出权限控制base_export_manager

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-16
> <http://www.thinkltd.cn/forum/2/ocabase-export-manager-2573>

1.  **【问题背景】**Odoo的导出功能，在14.0以前的版本，导出功能没有权限设置，只要有权限查看表单，就可以导出该表单的数据。Odoo14开始，提供了导出权限组，可以设置是否有导出权限。但此权限设置是全局的，一旦设置则是全局不可导出，不能设置某些表单允许导出，某些表单不允许导出。

2.  如果是控制是否可以导出，Odoo14预制了导出权限组（之前版本没有，需要下面链接的模块提供此功），勾选该权限组则可以看见“导出”动作。

3.  如果还希望控制可以导出哪些表单，不可以导出哪些表单，则需要下面链接的模块 base_export_manager

OSCG_SVN\odoo_ecommerce\14.0SRC\base_export_manager

Odoo 15.0版本 OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\base_export_manager

20221211增加Odoo16.0版本：https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/base_export_manager

注意OCA上该模块的版本（[server-ux/base_export_manager at 14.0 · OCA/server-ux · GitHub](https://github.com/OCA/server-ux/tree/14.0/base_export_manager)）有Bug，不起作用，上述SVN的版本修改了Bug。

Odoo14导出权限组：

![[2-ocabase-export-manager-2573-3c1ebab9.png]]

**模块base_export_manager功能**：在表单的权限设置上，增加了是否允许导出的勾选项；其次，增加了导出模板设置的菜单

![[2-ocabase-export-manager-2573-1b3f12f7.png]]

![[2-ocabase-export-manager-2573-84613283.png]]

模块链接：

####

此模块不好用，建议下面两个替代模块（此二个模块都是增加了一个导入、导出的权限组，属于该权限组的用户才可以导入、导出。但此二个模块不能指定哪个模型可以导入导出，哪个模型不可以导入导出。）：

[/forum/2/question/smilesmile-web-impex-3057](http://www.thinkltd.cn/forum/2/question/smilesmile-web-impex-522)

[/forum/2/question/ocaweb-disable-export-group-2829](http://www.thinkltd.cn/forum/2/question/ocaweb-disable-export-group-334)

This module extends the export capability:

1.  It allows an admin to manage export profiles (`ir.exports`) that Odoo stores internally but does not show anywhere.
2.  It also adds a new column to access rights to enable/disable export and override the export method to check if the user is allowed to export. Export is enabled by default.
3.

## [Configuration](https://github.com/OCA/server-ux/tree/11.0/base_export_manager#id1)

- Activate the developer mode
- Go to Settings > Users > Groups to select a user group
- Edit the group and go to the Access Rights tab
- Uncheck the "Export Access" box on the object of your choice and save

You can also go to Settings > Technical > Security > Access Rights.

##

## [Usage](https://github.com/OCA/server-ux/tree/11.0/base_export_manager#id2)

You can create the export profiles as you are used to:

- Go to any list view.
- Check some records.
- Press *More > Export*.
- Use the wizard to choose the columns to export.
- Press *Save fields list*.
- Give it a name.
- Press *OK*.

To manage export profiles, you need to:

- Go to *Settings > Technical > User Interface > Export Profiles*.
- Create a new one.
- Choose a name.
- Choose a model (table in the database).
- Choose the fields to export.
  - If you choose a related field, you can choose also up to 4 levels of subfields.
  - You can drag & drop to reorder the fields.

To use one of those profiles, you need to:

- Go to any list view.
- Check some records.
- Press *More > Export*.
- Choose your saved export from *Saved exports*.
- Press *Export to file*.

Once you have configured groups who cannot export an object:

- Connect as a user of this group
- Go to the list view of the object you disabled the export
- Select records and open the Action menu. The "Export" is not there.

## 补充/答案 1

我们SVN上有V10版本的，应当是有做过改动，是生效的。有V10的客户已用上。

## 补充/答案 2

V14版本功能模块链接：

https://apps.odoo.com/apps/modules/14.0/base_export_manager/

## 补充/答案 3

V15不能直接使用，需要另外升级处理

![[2-ocabase-export-manager-2573-0faf71c5.png]]

## 补充/答案 4

OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\base_export_manager

## 补充/答案 5

对应odoo应用链接

https://apps.odoo.com/apps/modules/13.0/base_export_manager/


## 原帖外链配图

![[2-ocabase-export-manager-2573-x194038c2.png]]
<small>原始地址: /web/image/865/snipaste_20190119_234233.png?access_token=33544d14-3485-4cfe-a768-9151eb461682</small>

![[2-ocabase-export-manager-2573-x194038c2.png]]
<small>原始地址: /web/image/867/snipaste_20190119_234500.png?access_token=fc4585e5-997d-4833-a35b-8eb54be7a250</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
