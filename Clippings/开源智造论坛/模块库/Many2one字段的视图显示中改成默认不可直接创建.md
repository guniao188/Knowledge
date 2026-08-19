---
title: "Many2one字段的视图显示中改成默认不可直接创建"
source: "http://www.thinkltd.cn/forum/2/many2one-3691"
forum: "模块库"
author: "肖相扶"
published: 2023-04-18
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Many2one字段的视图显示中改成默认不可直接创建

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2023-04-18
> <http://www.thinkltd.cn/forum/2/many2one-3691>

【问题】

Many2one字段的xml视图显示中，默认是可以直接创建新对象，如果希望去掉直接创建功能，字段定义的XML中需要设置 options="{'no_create': True, 'no_create_edit': True}"。

希望改成默认禁用直接创建功能，即需要xml中设置  options="{'no_create': False, 'no_create_edit': False}" 才能启用直接创建功能。

【解决方案】

二开增加下述js代码

import { Many2OneField } from '@web/views/fields/many2one/many2one_field';
import { Many2ManyTagsField } from '@web/views/fields/many2many_tags/many2many_tags_field';

const { markup } = owl;

/* no_create, no_create_edit默认值设置为True
*/
const extractProps = Many2OneField.extractProps;
Many2OneField.extractProps = ({ attrs, field }) => {
if(attrs.options.no_create === undefined){
attrs.options.no_create = true;
}
if(attrs.options.no_create_edit === undefined){
attrs.options.no_create_edit = true;
```python
}
var props = extractProps({ attrs, field });
return props;
};
```

完整实现的功能模块下载 web_no_create_true.zip


## 附件

- [[附件/forum/2-many2one-3691-web_no_create_true.zip|web_no_create_true.zip]] (2 KB)

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
