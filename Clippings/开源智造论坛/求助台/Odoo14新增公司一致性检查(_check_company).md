---
title: "Odoo14新增公司一致性检查(_check_company)"
source: "http://www.thinkltd.cn/forum/1/odoo14-check-company-767"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo14新增公司一致性检查(_check_company)

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo14-check-company-767>

1.  多公司情况下，Odoo以前的版本中，一个大的销售订单，订单属于A公司，该订单明细行也应该属于A公司，但由于输入错误等原因，可能存在某个明细行不属于A公司。此种情况，会导致订单确认时候报错，或者创建发票时候报错。

2.  Odoo14中，表单保存时候，增加了此种情况的检查功能：如果一个表单上，关联字段（many2one, 或 one2many 的关联）指向的数据是否和表单在同一个公司。如果不是同一个公司，系统报错“Incompatible companies on records:”

![[1-odoo14-check-company-767-fa287976.png]]

【公司一致性检查】

模型定义时候，新增了一个模型属性：_check_company_auto = False，一个字段属性：check_company=True。如果_check_company_auto = True，则该模型表单保存时候，对于设置有check_company=True 属性的所有字段，系统自动检查该字段指向数据的公司，和表单是否同一个公司（公司一致性检查）。该属性默认为False，即保存时候不自动检查公司一致性。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
