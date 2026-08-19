---
title: "Odoo V16废除了fields_view_get方法，替换为get_view方法"
source: "http://www.thinkltd.cn/forum/1/odoo-v16fields-view-get-get-view-3630"
forum: "求助台"
author: "杨浔波"
published: 2023-01-25
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo V16废除了fields_view_get方法，替换为get_view方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:杨浔波 | 2023-01-25
> <http://www.thinkltd.cn/forum/1/odoo-v16fields-view-get-get-view-3630>

get_view方法示例如下，建议第一次使用保留print，控制台查看输出变化：

```python
    @api.model
    def get_view(self, view_id=None, view_type='form', **options):
        res = super(SchoolStudent, self).get_view(view_id, view_type, **options)
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            address_field = doc.xpath("//field[@name='school_address']")
            if address_field:
                address_field[0].set("string", "School Address For GetView Method")
                address_field[0].set("nolabel", "0")

            res['arch'] = etree.tostring(doc, encoding='unicode')

        if view_type == 'tree':
            doc = etree.XML(res['arch'])
            school_field = doc.xpath("//field[@name='school_id']")
            print("res1----->", etree.tostring(doc, encoding='unicode'))
            if school_field:
                school_field[0].addnext(etree.Element('field', {'string': 'Total Fees',
                                                                'name': 'total_fees'}))

            print("res2----->", etree.tostring(doc, encoding='unicode'))
            res['arch'] = etree.tostring(doc, encoding='unicode')

        print("res----->", res)
        return res
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
