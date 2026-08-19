---
title: "MPS（主生产计划 ）模块详解"
source: "http://www.thinkltd.cn/forum/2/mps-3721"
forum: "模块库"
author: "周鸿飞"
published: 2023-05-24
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# MPS（主生产计划 ）模块详解

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:周鸿飞 | 2023-05-24
> <http://www.thinkltd.cn/forum/2/mps-3721>

在Odoo中，Master Production Schedule（MPS，主生产计划）是一个用于制定生产计划的关键工具。MPS是基于市场需求和销售预测的生产计划，它帮助企业预测所需的产量，并规划生产过程中所需的原材料和资源。

当打开菜单 Master Production Schedule时，系统会去调用一个mrp_mps_client_action的client action,而这个mrp_mps_client_action的action中，用到一个名字为MainComponent的组件，

MainComponent中最主要的组件是MpsLineComponent，它渲染了主要的明细行

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
