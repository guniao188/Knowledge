---
title: "integer类型 突破上下限传值 临时解决方法"
source: "http://www.thinkltd.cn/forum/1/integer-684"
forum: "求助台"
author: "施叶寒"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# integer类型 突破上下限传值 临时解决方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:施叶寒 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/integer-684>

odoo的integer字段在postgresql的类型为写死的int4，即-2147483648~2147483647。-2**31 ~ 2**31-1

在界面给integer类型赋值时，根据当前integer字段在页面的组件(widget=integer)，调用/web/static/src/js/fields/field_utils中的parseInteger方法进行检查。

由于代码中写死的parsed  2147483647，赋值失败，返回异常。

如果绕过前端检查直接赋值，将由数据库直接抛错。

临时解决方法：

1。手动把字段改为int8类型

```python
    def post_init_hook(cr, registry):

        cr.execute('''ALTER TABLE test_order ALTER COLUMN i1 type BIGINT;''')
```

2。在xml中将int8字段的widget改成float。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
