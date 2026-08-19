---
title: "Odoo15模块project_enterprise、timesheet_grid移植到社区版的修改"
source: "http://www.thinkltd.cn/forum/1/odoo15project-enterprisetimesheet-grid-856"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo15模块project_enterprise、timesheet_grid移植到社区版的修改

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo15project-enterprisetimesheet-grid-856>

1.  文件 OSCGODOO15\myaddons2\project_enterprise\\_manifest__.py 中模块依赖去掉 web_enterprise ，'project.webclient' 中注释含有 web_enterprise 的两行

2.  文件 OSCGODOO15\myaddons2\project_enterprise\static\src\project_control_panel\project_control_panel.xml中的web_enterprise替换成web、同时注释下面一段：

3.  文件 OSCGODOO15\myaddons2\project_enterprise\static\src\xml\project_enterprise.xml 中的 web_enterprise 都替换成 web，同时注释下面一段：

4.  文件 OSCGODOO15\myaddons2\project_enterprise\views\project_sharing_templates.xml 中注释 含有 web_enterprise 的三行

## 补充/答案 1

【参考截图】

![[1-odoo15project-enterprisetimesheet-grid-856-e7ac5c9d.png]]

![[1-odoo15project-enterprisetimesheet-grid-856-85a979e7.png]]

![[1-odoo15project-enterprisetimesheet-grid-856-c67d5e47.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
