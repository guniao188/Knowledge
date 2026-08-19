---
title: "MO上手工修改BoM字段而后确认MTO生成子MO报单号唯一性错误（必须在公司内唯一！）"
source: "http://www.thinkltd.cn/forum/1/mobommtomo-915"
forum: "求助台"
author: "肖相扶"
published: 2022-12-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# MO上手工修改BoM字段而后确认MTO生成子MO报单号唯一性错误（必须在公司内唯一！）

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-16
> <http://www.thinkltd.cn/forum/1/mobommtomo-915>

【问题】

Odoo15.0，创建MO，修改MO上的BoM，确认MO。系统按MTO补货规则，应该自动创建子MO，但却报下述错误。

![[1-mobommtomo-915-33a3b85e.png]]

【原因及解决办法】

1.  经调查，原因是2022年2月18日，Odoo提交的代码（）引发了此错误。此代码导致，修改MO的BoM后，MO的组件Stock Move的origin字段为空，因而导致子MO的单号（name）和父MO相同，从而报单号唯一性错误。

2.  修改方法是，修改MO的BoM字段后，确保新生成的组件Stock Move的origin字段不空（为父MO的name字段值）。

3.  模块mrp_not_confirm的15.0版本中（[生产单MO不自动确认/标记待办mrp_not_confirm](http://www.thinkltd.cn/forum/2/question/mo-mrp-not-confirm-3369)）修复了此Bug。

4.  模块mrp_procurement_fix的15.0版本（[Odoo14、15补货规则功能增强stock_procurement_fix、mrp_procurement_fix](http://www.thinkltd.cn/forum/2/question/odoo1415stock-procurement-fixmrp-procurement-fix-3394)）也针对此问题有修改

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
