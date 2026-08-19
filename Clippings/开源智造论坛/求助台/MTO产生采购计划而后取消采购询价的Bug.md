---
title: "MTO产生采购计划而后取消采购询价的Bug"
source: "http://www.thinkltd.cn/forum/1/mtobug-796"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# MTO产生采购计划而后取消采购询价的Bug

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/mtobug-796>

【问题现象】

1）安装采购计划模块，产品上设置为“提出申请”，而不是创建采购询价（如下图）。

![[1-mtobug-796-0cab434b.png]]

2）产品补货路线设置为MTO，购买规则上不勾选“取消下一移动”，如下图。

![[1-mtobug-796-dc353107.png]]

3）做一个SO，销售产品1，产品1缺货，系统自动创建了采购计划，基于采购计划创建了两个询价单（不同供应商），先创建的是PO1，后创建的是PO2。询价结束，如果取消PO2，发现系统连带把产生采购计划的销售出库Stock Move也取消了。如果取消PO1则没这个问题。如果确认PO1（但不取消PO2），则PO1的采购入库Stock Move，和销售出库的Stock Move之间并没有建立MTO关系。如果确认PO2则有MTO关系。

【问题原因】

1) OSCGODOO14\source\addons\purchase_requisition_stock\models\purchase_requisition.py  文件中：

```python
    方法 def _prepare_tender_values()  中，没有把rule上的propagate_cancel 字段值传递到采购计划

    方法 def _prepare_purchase_order_line() 中，也没有设置采购明细行的字段 propagate_cancel，因而采购明细行的字段propagate_cancel总是取默认值True
```

2) OSCGODOO14\source\addons\purchase_stock\models\purchase.py 中，

```python
    方法 def button_cancel() ，因为采购明细行的字段propagate_cancel总是True，因而会取消目的Stock Move（MTO产生此采购询价的Stock Move）

    方法 def button_cancel() 中，正确的做法应该是，取消目的Stock Move之前，应该判断一下该明细行对应的PO的采购计划（requisition_id字段关联），如果有采购计划，则不应该取消目的Stock Move。因为采购计划还可能创建新的PO来满足该Stock Move。只有当采购计划取消时候，才应该取消该目的Stock Move。如果有采购计划且该产品还有同一采购计划产生的询价单，应该把目的Stock Move移到该询价单（同一个采购计划同一产品的未取消的采购询价明细行）。
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
