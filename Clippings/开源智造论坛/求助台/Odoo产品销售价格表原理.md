---
title: "Odoo产品销售价格表原理"
source: "http://www.thinkltd.cn/forum/1/odoo-3613"
forum: "求助台"
author: "肖相扶"
published: 2022-12-21
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo产品销售价格表原理

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-21
> <http://www.thinkltd.cn/forum/1/odoo-3613>

Odoo产品销售价格表（product.pricelist）价格计算逻辑是：

1.  从价格表（ product.pricelist ）中匹配产品适用的价格规则（product.pricelist.item）
2.  调用价格规则（product.pricelist.item）的价格计算方法 def _compute_price(self, product, quantity, uom, date, currency=None) ，计算产品价格。
3.  价格规则的价格计算有三种类型： ('fixed', "Fixed Price"), ('percentage', "Discount"), ('formula', "Formula") 。可以二次开发增加更多的价格计算类型，如取最近一次的销售价格，基于行情基价按加价规则计算价格。
4.  价格规则的价格计算方法 _compute_price 中，调用产品（product.product）的基价计算方法 def price_compute(self, price_type, uom=None, currency=None, company=None, date=False)，该方法取产品的成本价格字段（standard_price， price_type =='standard_price'），或者销售价格字段（list_price + price_extra， price_type ==' list_price  ' ）。如果（计算销售明细的价格的情况）上下文_context中有 no_variant_attributes_price_extra，再加上属性价格。如此计算得到产品基价。
5.  取最近一次的销售价格、采购价格作为价格表价格。参考  [二开取最近价格的销售价格表product_latest_sale_price](http://www.thinkltd.cn/forum/2/product-latest-sale-price-3435)，以及  [二开取最近价格的采购价格表product_latest_vendor_price](http://www.thinkltd.cn/forum/2/product-latest-vendor-price-3434)
6.  行情基价价格表：大宗贸易，如不锈钢贸易，行情基价上，按产品属性加价计算产品价格。行情基价是指不同钢种当天的行情价格，由公司定价部门根据市场行情每天维护。产品属性加价是指，例如越薄的钢价格越贵，以及某些特殊规格的钢单独加价。
7.  行情基价价格表的一种实现方法：
8.  1.  钢种维护为product.category, 或者 product.template
```python
    2.  价格表上为每个钢种维护一个价格规则（ product.pricelist.item ）， Formula 的价格类型，维护钢种基价
    3.  厚度作为不锈钢的一个属性，厚度加价（越薄越贵）维护在属性价格上
    4.  产品的销售价格（list_price字段）为0.0
    5.  产品价格计算时候，先匹配钢种，取得钢种基价，再加上产品的属性加价。如此计算得到产品价格
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
