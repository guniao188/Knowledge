---
title: "Odoo17工作记录（hr.work.entry）的内部实现原理"
source: "http://www.thinkltd.cn/forum/5/odoo17-hr-work-entry-3852"
forum: "专家库"
author: "刘祥海"
published: 2024-02-28
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/专家库
---

# Odoo17工作记录（hr.work.entry）的内部实现原理

> [!info] 来源
> 开源智造论坛 · 专家库 | 作者:刘祥海 | 2024-02-28
> <http://www.thinkltd.cn/forum/5/odoo17-hr-work-entry-3852>

【问题列表】

说明在哪些情况下系统自动产生工作记录（hr.work.entry），工作记录时长（Duration）的计算原理（工作日、休息日、加班日分别如何计算，工作日历(resource.calendar)如何影响时长计算）

【业务实现示例】

1.   Odoo17中如何实现三班倒，如早班8点到16点，晚班16点到24点，夜班0点到8点。
2.  Odoo17中如何实现加班。注意考虑平日晚上加班、周末或国定节假日加班，以及三班倒情况下的加班处理。
3.  参考  [Odoo17加班单及节假日调班模块hr_holidays_legal_ot](http://www.thinkltd.cn/forum/2/odoo17hr-holidays-legal-ot-3879)

## 补充/答案 1

【方案补充】

1.  Odoo工作出勤（resource.calendar.attendance）、休假（resource.calendar.leaves）、工作记录（hr.work.entry），几个模型用法及关系，参考  [Odoo17加班单及节假日调班模块hr_holidays_legal_ot](http://www.thinkltd.cn/forum/2/odoo17hr-holidays-legal-ot-3879)
2.  排班及三班倒的方案参考：[Odoo17基于计划模块的排班/三班倒实施方案](http://www.thinkltd.cn/forum/1/odoo17-3882)


## 附件

- [[附件/forum/5-odoo17-hr-work-entry-3852-工作分录.doc|工作分录.doc]] (1.6 MB)


## 原帖外链配图

![[5-odoo17-hr-work-entry-3852-x481047fe.png]]
<small>原始地址: /web/image/7180-481047fe/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_17041858401629.png</small>

---

相关:[[Clippings/开源智造论坛/专家库/00-专家库索引.md|← 专家库索引]]
