---
title: "OCA合并重复客户及联系人crm_deduplicate_acl"
source: "http://www.thinkltd.cn/forum/2/ocacrm-deduplicate-acl-2806"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA合并重复客户及联系人crm_deduplicate_acl

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocacrm-deduplicate-acl-2806>

模块链接：

12.0版本：OSCG_SVN\odoo_ecommerce\12.0SRC\crm****

**Odoo 12.0版升级修改点**：下面三处的 crm.  修改为 base. 即可

crm_deduplicate_acl\views\base_partner_merge_view.xml(10):               action='crm.action_partner_deduplicate'
crm_deduplicate_acl\wizards\partner_merge_view.xml(11):
crm_deduplicate_acl\wizards\partner_merge_view.xml(22):

修改后，12.0的文件如下：
crm_deduplicate_acl\views\base_partner_merge_view.xml(10):               action='**base.**action_partner_deduplicate'
crm_deduplicate_acl\wizards\partner_merge_view.xml(11):
crm_deduplicate_acl\wizards\partner_merge_view.xml(22):

This module extends the functionality of the CRM contact deduplicator to add permission groups that allow the matching users to use those tools, not needing to be the sale settings manager.

###

### Configuration

To configure this module, you need to:

1.  Go to *Settings > Users > Users*.

2.  Choose a user.

3.  Choose the desired permission level(s) in *Appplication > Deduplicate Contacts*:

    - *Manually* allows him to do the manual deduplication process.

    - *Automatically* allows him to do the automatic deduplication process.

```python
      Warning

      Automatic contact deduplication can easily lead to unwanted results. Better backup before doing it.
```

    - *Without restrictions* executes the chosen deduplication method with admin rigts, to be able to update objects where the user would normally not have write rights, and to allow him to merge contacts with different email addresses.

```python
      Warning

      This is an advanced feature, be sure to train the user before enabling this permission for him.
```

###

### Usage

To use this module, you need to:

1.  Ask your admin to give you the new rights.
2.  Go to *CRM > Tools > Deduplicate Contacts* as usual.
3.


## 原帖外链配图

![[2-ocacrm-deduplicate-acl-2806-x194038c2.png]]
<small>原始地址: /web/image/1275/snipaste_20190206_080537.png?access_token=bd299bf4-c63c-4d5b-8219-47b650109115</small>

![[2-ocacrm-deduplicate-acl-2806-x194038c2.png]]
<small>原始地址: /web/image/1277/snipaste_20190206_080545.png?access_token=b2ee63dd-454f-47e6-b044-609f531327c4</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
