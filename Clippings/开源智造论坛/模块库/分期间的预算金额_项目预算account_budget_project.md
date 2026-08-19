---
title: "分期间的预算金额/项目预算account_budget_project"
source: "http://www.thinkltd.cn/forum/2/account-budget-project-3543"
forum: "模块库"
author: "肖相扶"
published: 2023-10-20
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 分期间的预算金额/项目预算account_budget_project

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2023-10-20
> <http://www.thinkltd.cn/forum/2/account-budget-project-3543>

模块链接：OSCG_SVN\odoo_ecommerce\15.0SRC\项目管理\account_budget_project

【业务背景】

1.  Odoo自带的预算管理模块account_budget （功能说明 [Odoo15预算管理功能说明](http://www.thinkltd.cn/forum/1/question/odoo15-876)），每一个预算类别（预算状况），只能设定一个计划金额。

2.  实际业务中，例如项目预算的情况，项目期间（例如为期一年），每个月的计划预算并不是一样的，有的月份多，有的月份少。相应的，理论金额的计算，已经过去的月份的计划预算直接累加作为理论金额。

【模块功能】

1.  本模块在预算表单上增加项目字段，在预算明细行上增加分月份的预算明细

2.  理论金额的计算：已经过去的月份，累加该月计划金额，当前月份，用已经过去的秒数，除以当月的秒数，再乘以当月的计划金额。如此计算理论金额

【功能截图】

![[2-account-budget-project-3543-6560bac0.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
