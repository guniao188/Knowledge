---
title: "CRM/销售实施痛点及方案"
source: "http://www.thinkltd.cn/forum/3/crm-3590"
forum: "方案库"
author: "肖相扶"
published: 2022-12-26
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# CRM/销售实施痛点及方案

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:肖相扶 | 2022-12-26
> <http://www.thinkltd.cn/forum/3/crm-3590>

【业务痛点】

1.  客户资料维护
2.  1.  (Q1.1)客户档案重复：新增或者修改客户时候，系统缺乏重复客户校验，导致客户档案重复。参考  [重复Email、电话手机的Partner检测（重复客户联系人检测）](http://www.thinkltd.cn/forum/2/emailpartner-3612)
    2.  (Q1.2) 客户分级管理：如区分未成交客户、成交客户、重要客户。参考  [重复Email、电话手机的Partner检测（重复客户联系人检测）](http://www.thinkltd.cn/forum/2/emailpartner-3612)
3.  大客户跟单策略（需要线下关系互动）
4.  1.  工业类客户，一旦拓客成功，客户会长期购买服务。如工业设备或工业原料的销售企业，或者项目型销售企业（项目销售后还要长期技术服务）。此类客户决策人多，决策周期长。
```python
    2.  (Q2.1)销售漏斗：制定合理的销售阶段，以及阶段间演进条件。参考  [商机上增加行动计划（跟单/待办事项）页签crm_opportunity_activities](http://www.thinkltd.cn/forum/2/crm-opportunity-activities-3508)
    3.  (Q2.2)关系人分析：客户方决策人管理，有哪些决策人，在项目中的角色，对项目的态度，个人性格特点，爱好动机等。参考  [商机上增加客户关系分析页签crm_opportunity_contacts](http://www.thinkltd.cn/forum/2/crm-opportunity-contacts-3509)
    4.  (Q2.3)竞品分析：客户可能需要哪些品类的产品，这些品类产品，竞争对手有什么优劣势，我方有什么优劣势。 [商机上增加推荐给客户的产品明细页签crm_lead_product](http://www.thinkltd.cn/forum/2/crm-lead-product-3466)
```

5.  小客户跟单策略（电销和在线销售为主）
6.  客户报价管理
7.  1.  Odoo价格表原理，参考  [Odoo产品销售价格表原理](http://www.thinkltd.cn/forum/1/odoo-3613)
```python
    2.  行情价：案例一，电脑配件价格，基于市场行情，定期（每日）维护本公司各产品价格表，每日自动发给合作伙伴。案例二，不锈钢价格。基于钢种的市场行情价，按一定加价规则，自动计算不同厚度的不锈钢的价格（越薄越贵）。
    3.  定制报价：例如，机加工行业，基于客户给定的加工图纸，估算加工价格。又如，OEM行业，按客户要求贴牌定制，可能要基于样品试制，估算报价。参考  [客户询价/供应商询价/客户报价模块crm_quotation](http://www.thinkltd.cn/forum/2/crm-quotation-3408)
    4.  方案报价：如大型设备定制，或建筑项目报价。此类报价需要报价版本管理。参考  [SO订单取消及版本管理、报价和订单分开管理sale_order_revision、sale_isolated_quotation](http://www.thinkltd.cn/forum/2/sosale-order-revisionsale-isolated-quotation-2674)
    5.  报价单发送和打印：系统导出清晰美观的客户报价文档
```

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
