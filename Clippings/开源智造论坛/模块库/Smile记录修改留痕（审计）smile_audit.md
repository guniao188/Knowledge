---
title: "Smile记录修改留痕（审计）smile_audit"
source: "http://www.thinkltd.cn/forum/2/smile-smile-audit-3053"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile记录修改留痕（审计）smile_audit

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smile-smile-audit-3053>

模块链接：

This module lets administrator track every user's operation on all the objects of the system (for the moment, only create, write and unlink methods). Each rule for tracking user's operation on data through the Odoo's interface is called audit rule.

Features:

- The administrator creates an audit rule by specifying the name and the module on which the rule will be applied,
- The administrator ticks the operations he wants to follow (creation and/or modification and/or deletion),
- The administrator selects the group of users concerned by the audit.
- A rule can be disabled if the administrator does not want to follow its logs anymore.
- Operations performed by a user will be automatically recorded in the list of logs according to the pre-defined rule.
- The log view contains details about each operation: date, name, the module, the user, old and new values of each modified field, etc.
- The module also allows a history revision of each operation.
- The administrator can delete audit rules but logs can't be deleted.
- Users can view a list of current model logs.
-

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_audit#id1)

To create a new rule:

1.  Go to `Settings > Audit > Rules` menu.

2.  Press the button `Create`.

3.  Insert the name of the rule, the model and the user group. Then check operations you want to audit.

    >
    >
    >
    >
    >

To show the list of logs and edit a log:

1.  Go to `Settings > Audit > Logs` menu.

    >
    >
    >
    >
    >

2.  Display the log by clicking on a line to see more details about the operation and changes.

    >
    >
    >
    >
    >

To view different versions of the object:

1.  Click on the smart button `History Revision`.

    >
    >
    >
    >
    >

2.  Corresponding history:

    >
    >
    >
    >
    >

To view logs of displayed model:

1.  Select one or multiple lines from the list view.

2.  Go to `Action > View audit logs`.

    >
    >
    >
    >
    >

##

-


## 原帖外链配图

![[2-smile-smile-audit-3053-x6ec384d5.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_audit/static/description/create_audit_rules.png</small>

![[2-smile-smile-audit-3053-xced612f9.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_audit/static/description/show_list_logs.png</small>

![[2-smile-smile-audit-3053-x1cc774d0.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_audit/static/description/display_operation_log.png</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
