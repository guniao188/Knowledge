---
title: "二开增加合并采购的条件purchase_stock_group"
source: "http://www.thinkltd.cn/forum/2/purchase-stock-group-3299"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开增加合并采购的条件purchase_stock_group

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/purchase-stock-group-3299>

SVN地址：SVN\odoo_ecommerce\13.0SRC\stock_rule_make_po

【业务背景】

1.  Odoo中，系统基于Buy的规则(Stock Rule)生成采购单时候，系统自动查找 相同供应商、状态为Draft、相同Picking Type、相同Group 的PO，如果找到了，则追加产品到该采购单，合并采购；

2.  但实际业务中，有一种需求是，外协采购。同一个SO购买了A、B、C三个产品，三个产品都是定制品，下单给供应商定制生产。定制周期各不相同，质检方法各不相同。为了便于定制采购的管理，希望A、B、C三个不要合并采购。

3.  还有一种情况，生产原料的采购，同一个供应商，供应A、B、C 三种原料。生产车间，A、B、C三种原料的需求时点不同，例如A用在底层BoM上，需求时间较早，B用在总装BoM上，需求时间较晚。此种情况，Odoo现有功能是，生成A的PO单时候，需求日期减去采购提前期，倒算PO的下单日期(date_order字段)。需求B的时候，自动合并到A的采购单上，B的计划到料日期（Order Line 的 date_planned 字段）是PO下单日期 + B的采购提前期。但B的实际需料日期并不是系统计算出来的到料日期。

4.  上述几种情况的一个解决办法是，不让系统自动合并PO，A、B、C三个料三个PO，由采购员去决定是否需要合并采购。可以提供一个服务器动作，需要合并的时候，方便采购人员合并采购。

![[2-purchase-stock-group-3299-516c0c50.png]]

【模块设计】

1.  Buy的路线规则上增加“合并采购”条件字段 group_buy_method，三个选项：('default','合并采购'),('product','不合并'),('date_planned','按日期合并')。默认值是 合并采购。不合并采购 则，基于本规则生成PO时候，总是不合并。按日期合并 则，基于本规则生成PO时候，增加下单日期 相同的条件。相同供应商、状态为Draft、相同Picking Type、相同Group，**相同下单日期** 的PO 。

2.  实现逻辑，代码文件 Odoo13\source\odoo\addons\purchase_stock\models\stock_rule.py  方法 def _make_po_get_domain

3.  参考实现代码：

```python
    def _make_po_get_domain(self, company_id, values, partner):
        if self.group_buy_method == 'group_buy':
            return super(StockRule, self)._make_po_get_domain(company_id, values, partner)
        elif self.group_buy_method == 'not_group_buy':
            return [('state', '=', False)]
        else:
            domain = super(StockRule, self)._make_po_get_domain(company_id, values, partner)
            procurement_date_planned = fields.Datetime.from_string(values['date_planned'])
            schedule_date = procurement_date_planned - relativedelta(days=company_id.po_lead)
            schedule_date = schedule_date - relativedelta(days=int(values['supplier'].delay))
            schedule_date1 = schedule_date - relativedelta(days=1)
            schedule_date2 = schedule_date + relativedelta(days=1)
            date_domain = (('date_order', '>=', schedule_date1),('date_order', '<=', schedule_date2))
            return domain + date_domain
```

![[2-purchase-stock-group-3299-637d4de4.png]]

## 补充/答案 1

【功能截图】

![[2-purchase-stock-group-3299-4c906008.png]]

![[2-purchase-stock-group-3299-c3cfe950.png]]

## 补充/答案 2

这个是在自动跑出单据之前就先按规则合并了。

那还有手动人工干预的方式吗？

另外还得测试一下，如果是MTO的方式，那么跑出来的单据，合并后，是否能销售出库时能正常锁货出库吗？还是一直无法保留？

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
