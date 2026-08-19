---
title: "Odoo14质检管理功能原理"
source: "http://www.thinkltd.cn/forum/1/odoo14-699"
forum: "求助台"
author: "肖相扶"
published: 2023-10-25
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo14质检管理功能原理

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-10-25
> <http://www.thinkltd.cn/forum/1/odoo14-699>

【质检功能概述】

1.  QCP: Quality Control Point，质量控制点，可以定义哪些产品，哪些作业类型（Picking Type），进行什么样的质检（Type），是全检还是抽检(Control Type)，哪个质检小组负责（Team），连接哪个设备质检（需要IoT Box）

2.  QC: Quality Check，质检单。如果作业单（Picking或mrp Production）上的产品、作业类型有关联的QCP，作业单Confirm时候，系统自动基于QCP创建质检单。作业单上可以一键跳到质检单质检操作。

3.  QA: Quality Alerts，质量告警。作业单上，基于质检情况，可以针对某些质量问题发起QA单，让QA部门介入，深入分析问题原因，制定根治办法。

4.  系统内部实现原理是，Stock Move Confirm的时候，检查Stock Move的产品、作业类型是否有关联的QCP，如果有则自动创建QC单。参考代码：odoo\enterprise\quality_control\models\stock_move.py

 【功能截图】

![[1-odoo14-699-463128e7.png]]

![[1-odoo14-699-47c83b1b.png]]

![[1-odoo14-699-93e8d876.png]]

![[1-odoo14-699-b6637e85.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
