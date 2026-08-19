---
title: "Odoo企业版模块mrp_account功能介绍"
source: "http://www.thinkltd.cn/forum/2/odoomrp-account-2463"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo企业版模块mrp_account功能介绍

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoomrp-account-2463>

生产订单MO的生产成本核算，根据产成品的成本计算方法不同，核算方法如下：

**标准成本法：产成品的入库成本价格直接取自产品上的成本价格**

** 移动平均及先进先出法：产成品的入库成本计算公式是如下：**

1.      产成品入库价格 =（MO原料Stock Move的总值 + 生产工时总额）/ MO上产成品的数量

2.      产成品入库总值 =（MO原料Stock Move的总值 + 生产工时总额

3.      生产工时总额 = MO的Work Order的工时 * 工时单价

4.      工时单价在Work Order的Work Center上设置

 **全月平均法：**MO的原料Stock Move总值，加上工时、制造费用，除以产成品总数，得到入库成本价格

 **案例分析：**生产单MO生产桌子10个，需要原料桌面、桌腿、螺丝套、螺丝钉，工单（Work Order）工时510分钟，工作中心上工时单价34.59 。产成品入库成本如下：原料消耗17000元，工时总额294.01元，产成品入库17294.01元，如下图。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
