---
title: "JS报错 Error: list is undefined"
source: "http://www.thinkltd.cn/forum/1/js-error-list-is-undefined-919"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# JS报错 Error: list is undefined

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/js-error-list-is-undefined-919>

【问题】

Odoo14版本，采购订单上添加预付款明细行时候，报js错误Error: list is undefined，如下面截图。

![[1-js-error-list-is-undefined-919-512d1f58.png]]

【错误原因及修复】

1.  经查，错误原因在于文件odoo14/odoo-server/addons/web/static/src/js/views/basic_model.js ，报错代码行（3311行前后） var oldResIDs = list.res_ids.slice(0);

2.  进一步调查，发现下面代码行（3300行前后），!data[fieldName]  不能判断空数组[] 的情况。某些情况下，会出现空数组，从而引发本错误。代码应该改成  !data[fieldName] || data[fieldName] == false

```python
            if (type === 'many2many' || type === 'one2many') {

                if (!data[fieldName]) {

                    // skip if this field is empty

                    continue;

                }
```

1.  经查，Odoo15.0的代码文件OSCGODOO15\source\addons\web\static\src\legacy\js\views\basic\basic_model.js 3341行前后，也存在相同潜在问题。

            if (type === 'many2many' || type === 'one2many') {

                **if (!data[fieldName]) {**

```python
                    // skip if this field is empty

                    continue;

                }
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
