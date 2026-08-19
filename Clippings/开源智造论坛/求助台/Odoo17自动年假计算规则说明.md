---
title: "Odoo17自动年假计算规则说明"
source: "http://www.thinkltd.cn/forum/1/odoo17-3891"
forum: "求助台"
author: "肖相扶"
published: 2024-02-27
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17自动年假计算规则说明

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-02-27
> <http://www.thinkltd.cn/forum/1/odoo17-3891>

【】

![[1-odoo17-3891-ee993164.png]]

1.  Employee accrue：如果本条规则的条件满足，增加此字段的天数/小时数的年假。如果年假分配上的开始日期到期间末，不足一个期间(年或月)，系统按比例计算年假数量。例如整年增加年假12天，入职日期为10月1日，则实际上班时间3个月，增加 3/12 * 12 = 3天年假
2.  每年的几月几日增加，或每月的几号增加
3.  Cap accrued time: 封顶数。此按本条计算增加年假数后，如果剩余年假数量（不含已休掉的年假）超过此封顶数，则取此封顶数。
4.  milestone reached: 年假分配上设置的开始日期(date_from 字段)，加上此天数/月数/年数后，本条年假规则生效。
5.  Carry over：本条规则设置的期间到期后，未休完的年假如何处理。清零/累加/累加但不超过指定上限。
6.  系统内部计算逻辑：
7.  1.  年假分配（hr.leave.allocation）的几个重要字段：开始日期（ date_from ），最近一次年假计算日期(lastcall)，下一次年假计算日期(nextcall)
```python
    2.  年假分配第一次计算时候，以date_from + 第一条规则的 milestone reached时间，作为 lastcall日期，以第一条规则的“ 计算年假的日期 ”作为nextcall日期。
    3.  如果lastcall日期大于当前日期，退出，不计算。如果lastcall日期等于第一条规则的 “ 计算年假的日期 ”，则按第一条规则计算年假。
    4.  如果nextcall小于当前时间，系统以nextcall按sequence顺序逐条匹配年假规则（ date_from +  规则的 milestone reached时间 大于  nextcall日期 ），取最后一条匹配成功的规则，按此规则计算年假。计算后，以此规则的次一个 “ 计算年假的日期 ” 作为新的nextcall日期
```

【示例截图】

业务需求：入职日满一年的日期，年假加5天，满两年的日期，之前剩余年假清零，年假加6天，同理，满三年加7天，年假最多10天（满10天后不再按工龄增加）。

![[1-odoo17-3891-e3dcb6cd.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
