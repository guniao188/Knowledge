---
title: "Odoo16的三大会计报表改善l10n_cn_reports"
source: "http://www.thinkltd.cn/forum/2/odoo16l10n-cn-reports-3586"
forum: "模块库"
author: "肖相扶"
published: 2023-04-21
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo16的三大会计报表改善l10n_cn_reports

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2023-04-21
> <http://www.thinkltd.cn/forum/2/odoo16l10n-cn-reports-3586>

【Git位置】

1.  https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/l10n_cn_oscg

2.  https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/l10n_cn_reports

【会计报表功能增强】

1.  增加了月末结转功能，出具资产负债表之前，需要先做月末结转，将收入、费用科目余额结转到本年利润科目

2.  资产负债表增加了“年初余额”列

3.  利润表增加了“本年累计”列

4.  现金流量表增加了“现金流量分析”功能（开发者模式下），帮助查找“哪笔现金分录，对应哪笔现金流量分录”。系统采用间接法计算现金流量表（参考 [Odoo13现金流量表原理解析](http://www.thinkltd.cn/forum/1/question/odoo13-435)）。此功能方便查找现金流量各个项目的汇总金额，包含了哪些会计分录。2023年4月23日Bug修正： “现金流量分析”功能中，现金分录也从“杂项”类日记账取数据，参考 [现金流量表的日记账不能选择杂项日记账](http://www.thinkltd.cn/forum/1/3675) 。

5.  注意事项：下面截图中Odoo自带的现金流量标签，需要从科目上删除，否则中国的现金流量表取不到中国的现金流量标签。

![[2-odoo16l10n-cn-reports-3586-0c1413af.png]]

6.

【功能截图】

![[2-odoo16l10n-cn-reports-3586-01fb01f8.png]]

![[2-odoo16l10n-cn-reports-3586-d32066aa.png]]

![[2-odoo16l10n-cn-reports-3586-6f554a8b.png]]

![[2-odoo16l10n-cn-reports-3586-2d1f5e54.png]]

![[2-odoo16l10n-cn-reports-3586-715fc962.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
