---
title: "产品分类新建时候会计科目默认值不生效（兼论默认值/属性property字段生效原理）"
source: "http://www.thinkltd.cn/forum/1/property-954"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 产品分类新建时候会计科目默认值不生效（兼论默认值/属性property字段生效原理）

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/property-954>

【问题背景】

最近有些客户的Odoo新建产品分类时候，库存计价选择“自动”，入库科目、出库科目、计价科目默认值都不生效。有些客户环境又是好的。

【原因调查】

经查，2022年5月20日，Odoo提交的代码（参考 [x[FIX] stock_account: wrong accounts for manual valuation · odoo/odoo@656348c (github.com)](https://github.com/odoo/odoo/commit/656348c06868faf216c57bef0f3056e062ee8f8f)），本来是想修复Bug：库存计价选择“手动”时候，自动清除入库科目、出库科目、计价科目值，但修复代码中，文件 stock_account\models\product.py，方法 onchange_property_valuation()  中，画蛇添足多了一段代码，库存计价选择“自动”时候，入库科目、出库科目、计价科目从公司上取对应科目值（company_id.property_stock_account_input_categ_id、company_id.property_stock_account_output_categ_id、company_id.property_stock_valuation_account_id），这使得公司上设置的科目值替代了本来的默认值，但默认情况下，公司上对应科目值又是空值，导致最终取不到科目值。

【问题修复】

1.  方法一是，公司表单的XML视图上，显示出字段property_stock_account_input_categ_id、property_stock_account_output_categ_id、property_stock_valuation_account_id，设置合适的科目值，如此，产品分类上库存计价选择“自动”时候，会自动将此值设置到产品分类上；

2.  方法二是，文件 stock_account\models\product.py，方法 onchange_property_valuation()  中，注释下面几行代码。

3.

![[1-property-954-43b7659e.png]]

## 补充/答案 1

【默认值/属性property字段取值原理】

1.  默认值设置：菜单“设置 --> 技术 --> 动作 --> 用户定义的缺省值”

2.  属性property字段值设置：菜单“设置 --> 技术 --> 参数 --> 公司属性”

3.  属性property字段（字段定义上company_dependent=True）的默认值，系统首先找 用户定义的缺省值，没找到再找 公司属性 里设置的默认值

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
