---
title: "OCA Many2one字段更多选项设置web_m2x_options"
source: "http://www.thinkltd.cn/forum/2/oca-many2oneweb-m2x-options-2839"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA Many2one字段更多选项设置web_m2x_options

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-many2oneweb-m2x-options-2839>

模块链接：

12.0模块：

This modules modifies "many2one" and "many2manytags" form widgets so as to add some new display control options.

Options provided includes possibility to remove "Create..." and/or "Create and Edit..." entries from many2one drop down. You can also change default number of proposition appearing in the drop-down. Or prevent the dialog box poping in case of validation error.

If not specified, the module will avoid proposing any of the create options if the current user has no permission rights to create the related object.

### [in the field's options dict](https://github.com/OCA/web/tree/11.0/web_m2x_options#id2)

`create` *boolean* (Default: depends if user have create rights)

> Whether to display the "Create..." entry in dropdown panel.

`create_edit` *boolean* (Default: depends if user have create rights)

> Whether to display "Create and Edit..." entry in dropdown panel

`m2o_dialog` *boolean* (Default: depends if user have create rights)

> Whether to display the many2one dialog in case of validation error.

`limit` *int* (Default: openerp default value is `7`)

> Number of displayed record in drop-down panel

`search_more` *boolean*

> Used to force disable/enable search more button.

`field_color` *string*

> A string to define the field used to define color. This option has to be used with colors.

`colors` *dictionary*

> A dictionary to link field value with a HTML color. This option has to be used with field_color.

`no_open_edit` *boolean* (Default: value of `no_open` which is `False` if not set)

> Causes a many2one not to offer to click through in edit mode, but well in read mode

`open` *boolean* (Default: `False`)

> Makes many2many_tags buttons that open the linked resource

`no_color_picker` *boolean* (Default: `False`)

> Deactivates the color picker on many2many_tags buttons to do nothing (ignored if open is set)

###

### [ir.config_parameter options](https://github.com/OCA/web/tree/11.0/web_m2x_options#id3)

Now you can disable "Create..." and "Create and Edit..." entry for all widgets in the odoo instance. If you disable one option, you can enable it for particular field by setting "create: True" option directly on the field definition.

`web_m2x_options.create` *boolean* (Default: depends if user have create rights)

> Whether to display the "Create..." entry in dropdown panel for all fields in the odoo instance.

`web_m2x_options.create_edit` *boolean* (Default: depends if user have create rights)

> Whether to display "Create and Edit..." entry in dropdown panel for all fields in the odoo instance.

`web_m2x_options.m2o_dialog` *boolean* (Default: depends if user have create rights)

> Whether to display the many2one dialog in case of validation error for all fields in the odoo instance.

`web_m2x_options.limit` *int* (Default: openerp default value is `7`)

> Number of displayed record in drop-down panel for all fields in the odoo instance

`web_m2x_options.search_more` *boolean* (Default: default value is `False`)

> Whether the field should always show "Search more..." entry or not.

To add these parameters go to Configuration -> Technical -> Parameters -> System Parameters and add new parameters like:

- web_m2x_options.create: False
- web_m2x_options.create_edit: False
- web_m2x_options.m2o_dialog: False
- web_m2x_options.limit: 10
- web_m2x_options.search_more: True

###

### [Example](https://github.com/OCA/web/tree/11.0/web_m2x_options#id4)

Your XML form view definition could contain:

```python
    ...

    ...
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
