---
title: "Odoo16仓库作业类型Picking Type新设置项用法说明"
source: "http://www.thinkltd.cn/forum/1/odoo16picking-type-3820"
forum: "求助台"
author: "肖相扶"
published: 2023-12-09
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo16仓库作业类型Picking Type新设置项用法说明

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-12-09
> <http://www.thinkltd.cn/forum/1/odoo16picking-type-3820>

Odoo16的仓库作业类型(stock.picking.type)新增了下面一些设置字段，用法说明如下。

1.  print_label：对应的Picking上是否显示标签打印按钮
2.  reservation_method：保留（锁货）方法，有 at_confirm, manual, by_date三个选项。by_date表示，在Stock Move的计划日期(date字段)的前若干天，系统自动保留。
3.  reservation_days_before：如果  reservation_method 是 by_date, 此设置表示提前此天数自动保留。
4.  reservation_days_before_priority： reservation_method 是 by_date，Picking上的优先级字段 priority为True时候，提前此天数自动保留。
5.  restrict_put_in_pack：是否强制要求产品必须扫码放入目标包裹，三个选项，mandatory表示每扫描一个产品码，就必须扫描包裹码表示放入此包裹。optional 表示，可以扫描多个产品码，再扫包裹码，表示多个产品，一起放入包裹。no表示不扫包裹码（不放入包裹）
6.  restrict_scan_dest_location： 是否强制要求产品必须扫码放入目标库位，三个选项，mandatory表示每扫描一个产品码，就必须扫描目标库位码表示放入此库位。optional 表示，可以扫描多个产品码，再扫目标库位码，表示多个产品，一起放入库位。no表示不扫目标库位码（不管理目标库位）
7.  restrict_scan_product：为True表示，不行先扫描产品码，定位到此产品行，才可以编辑此产品行（如输入数量）。
8.  restrict_scan_source_location：两个选项，no表示不必扫描源库位码，mandatory表示必须扫描源库位码
9.  restrict_scan_tracking_number：两个选项，mandatory和optional，前者表示扫完产品码后，必须扫描批次/序列码，后者表示，可以不扫描批次/序列码。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
