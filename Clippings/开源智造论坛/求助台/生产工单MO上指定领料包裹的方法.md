---
title: "生产工单MO上指定领料包裹的方法"
source: "http://www.thinkltd.cn/forum/1/mo-3774"
forum: "求助台"
author: "肖相扶"
published: 2023-09-08
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 生产工单MO上指定领料包裹的方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-09-08
> <http://www.thinkltd.cn/forum/1/mo-3774>

【业务背景】

1.  台湾TSGS公司，生产冲锋衣防水贴条。防水贴条的生产步骤，先是生产1米宽的大卷，客人要货时候，按客户要求，切成1cm、2cm、3cm等宽度的小卷。切完以后，仓库里面总是剩下很多宽度不等的残卷。
2.  接到新的订单时候，希望可以指定残卷领料（优先消耗残卷）。Odoo中如何实现此需求？
3.  在不锈钢卷加工贸易中，也存在类似问题，即指定加工哪个不修钢卷。
4.  印刷行业中，纸卷也存在类似问题。例如某宽幅的纸卷缺货，指定用宽幅更大的纸卷替代生产。

【操作截图】

1.  安装模块：stock_quant_manual_assign，参考 [Picking上指定批次/包裹/Quant锁货stock_quant_manual_assign](http://www.thinkltd.cn/forum/2/picking-quantstock-quant-manual-assign-2870)
2.  MO的原料明细行上添加按钮“Manual Quants”，参考代码 。点击按钮，弹窗选择包裹/批次，指定锁货。

![[1-mo-3774-d492cd55.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
