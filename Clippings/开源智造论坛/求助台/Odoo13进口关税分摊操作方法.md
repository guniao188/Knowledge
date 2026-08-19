---
title: "Odoo13进口关税分摊操作方法"
source: "http://www.thinkltd.cn/forum/1/odoo13-486"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo13进口关税分摊操作方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo13-486>

【操作方法】

1.  Odoo标准模块stock_landed_costs 可以实现进口海运费、关税等分摊到库存商品价值上。其处理原理是，进口商品到达海关港口，报关，收到海关关税发票，系统中录入一个关税的供应商账单，从供应商账单上可以点击按钮直接创建一个 Landed Cost单据，系统自动将关税金额带入Landed Cost表单。

2.  关税供应商账单可以有两个明细行，一个是“关税”，科目“应付暂估”，一个是“海关增值税”，科目“应交税费”。如此，可以实现关税和进口增值税会计核算。

3.  Odoo 13的模块stock_landed_costs， 不仅 FIFO 成本计算方法可以分摊，移动加权平均的成本方法也可以分摊。此外，安装这个模块 OSCG_SVN\odoo_ecommerce\13.0SRC\存货核算\stock_landed_costs_fix ，非实时存货核算的情况，也可以应用该模块进行费用分摊。

4.  进口报关业务知识参考[：https://baike.baidu.com/item/%E8%BF%9B%E5%8F%A3%E6%8A%A5%E5%85%B3%E6%B5%81%E7%A8%8B/1686728?fr=aladdin](https://baike.baidu.com/item/%E8%BF%9B%E5%8F%A3%E6%8A%A5%E5%85%B3%E6%B5%81%E7%A8%8B/1686728?fr=aladdin)

5.

## 补充/答案 1

【操作截图】

关税账单：

![[1-odoo13-486-b2e8f67e.png]]

关税分摊单：

![[1-odoo13-486-1da4ce86.png]]

分摊单验证后自动产生会计凭证：

![[1-odoo13-486-f193d657.png]]

## 补充/答案 2

开启Saxon，入库商品10个，销售出库4个，而后分摊关税100元，系统自动产生的会计凭证如下：

![[1-odoo13-486-fca5315f.png]]

## 补充/答案 3

![[1-odoo13-486-3440494d.png]]

![[1-odoo13-486-3440494d.png]]

分摊成本时若产品已出库，stock.valuation.layer将不再产生存货明细变动，会将分摊的成本结转到“主营业务成本”。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
