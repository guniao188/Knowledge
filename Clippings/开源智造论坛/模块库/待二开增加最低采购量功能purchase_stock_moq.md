---
title: "待二开增加最低采购量功能purchase_stock_moq"
source: "http://www.thinkltd.cn/forum/2/purchase-stock-moq-3302"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 待二开增加最低采购量功能purchase_stock_moq

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/purchase-stock-moq-3302>

【业务背景】

1.  有些供应商有最低采购数量（MoQ，minimum of quantity）要求，Odoo现有功能，有阶梯价格（不同数量，不同采购价格），没有最低采购数量功能。

2.  如果产品供应商(product.supplierinfo)中，设定的最低数量是100，如果需求数量为30（低于100），系统目前的功能是匹配不到供应商，如果是MTO产生PO的情况，直接报错: There is no matching vendor price to generate the purchase order for product MOQ测试 (no vendor defined, minimum quantity not reached, dates not valid, ...). Go on the product form and complete the list of vendors. 。如果是MTS（例如安全库存）的情况，没有报错，也不产生PO。

3.  MoQ问题的一个补救方法是，设定一条最小数量为0.0 的product.supplierinfo，价格奇高（例如 999999）。如此，系统可以产生PO，但采购价格明显不对，以此提醒采购处理人员手工修改采购数量、采购价格。

4.  MoQ的一个更好的处理方法是，系统基于Buy的规则查找供应商时候，先比较一下需求数量，和product.supplierinfo最小的数量，如果需求数量低于最小数量，则自动调整需求数量到最小数量。

5.  关联模块“[MTO补货整数倍及经济生产批量处理](http://www.thinkltd.cn/forum/2/question/odoo13-mtostock-mto-qty-multi-3271)”  [/forum/2/question/odoo13-mtostock-mto-qty-multi-3271](http://www.thinkltd.cn/forum/2/question/odoo13-mtostock-mto-qty-multi-3271)

【模块设计】

1.  系统基于Buy的规则查找供应商，产生PO时候，先取出该产品、该供应商的product.supplierinfo 记录的最小的数量，该数量和需求数量比较，如果需求数量低于该最小数量，则自动调整需求数量到最小数量。如此自动处理MoQ问题。

2.  参考代码 Odoo13\source\odoo\addons\purchase_stock\models\stock_rule.py  方法 def _prepare_purchase_order_line

```python
    def _prepare_purchase_order_line(self, product_id, product_qty, product_uom, company_id, values, po):
        partner = values['supplier'].name
        moq_seller = product_id.seller_ids.filtered(lambda s: s.name.active and s.name == partner and s.company_id == company_id).sorted(lambda s: (s.min_qty))
        moq = moq_seller and moq_seller[0].min_qty or 0.0
        if moq > product_qty:
            return super(StockRule, self)._prepare_purchase_order_line(product_id, moq, product_uom, company_id, values, po)
        else:
            return super(StockRule, self)._prepare_purchase_order_line(product_id, product_qty, product_uom, company_id, values, po)
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
