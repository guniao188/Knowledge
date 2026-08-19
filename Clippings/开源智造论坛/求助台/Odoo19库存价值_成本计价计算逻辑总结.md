---
title: "Odoo19库存价值/成本计价计算逻辑总结"
source: "http://www.thinkltd.cn/forum/1/odoo19-4095"
forum: "求助台"
author: "肖相扶"
published: 2025-12-12
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo19库存价值/成本计价计算逻辑总结

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2025-12-12
> <http://www.thinkltd.cn/forum/1/odoo19-4095>

Odoo19的库存价值、成本计价方法的内部实现逻辑有较大变化，最大的变化是去掉了库存计价模型(stock.layer.valuation)，因而产品的库存价值、入库stock move的剩余数量、剩余价值的计算方法完全不一样了。本帖总结Odoo19新的成本/价值相关计算逻辑。

1.  库位存货是否计算库存价值(stock.location的方法 _should_be_valued() )的判断条件：库位设置了公司，且类型为内部库位或在途库位
2.  Stock Move属于入库(is_in)、出库(is_out)、直发(dropship)、退货的判断条件：
3.  1.  入库(is_in)：目标库位要计算库存价值，但源库位不要计算库位价值，且有stock move line（排除实际入出库数量为零的情况），且不是dropship
```python
    2.  出库(is_out)：源库位要计算库存价值，但目标库位不要计算库位价值，且有stock move line（排除实际入出库数量为零的情况），且不是dropship
    3.  直发(dropship)：源库位类型为 供应商或者没有设置公司的在途库位，目标库位类型为 客户或者没有设置公司的在途库位
    4.  退货：stock move的字段origin_returned_move_id有值则为退货stock move，origin_returned_move_id是退货前的stock move，即如果sm1有退货，则退货的stock move的origin_returned_move_id字段记录sm1的id。
```

4.  产品库存数量的计算逻辑：
5.  1.  产品库存数量的字段：在手库存(qty_available)，可用库存(free_qty)，预期库存(virtual_available)，在途库存(incoming_qty)，待发库存(outgoing_qty)
```python
    2.  产品库存数量计算时候可用的上下文关键字：指定库位(location)，指定仓库(warehouse_id)，指定产品批次(lot_id)，指定产品属有者(owner_id)，指定产品包裹(package_id)，指定实际/预计入库/出库日期(from_date、to_date)
    3.  在手库存(qty_available)：系统中所有stock quant上的数量的汇总，如果指定了上下文关键字，则是用关键字筛选后的库存数量。
    4.  待发库存(outgoing_qty)：状态非done、cancel的出库stock move的数量汇总，即，将要出库但还没出库的数量
    5.  在途库存(incoming_qty)：状态非done、cancel的入库stock move的数量汇总，即，将要入库但还没入库的数量
    6.  可用库存(free_qty)：在手库存，减去待发库存后的数量
    7.  预期库存(virtual_available)：在手库存，加上在途库存，减去待发库存后的数量
    8.  参考代码 OSCGODOO19\source\addons\stock\models\product.py 方法 _compute_quantities()
```

6.  Stock Move验证完成时候，自动产生入库出库会计分录的条件：
7.  1.  Stock Move的产品是可库存的(勾选了字段 is_storable)
```python
    2.  入库或出库Stock Move。注意 dropship的Stock Move不产生会计分录
    3.  源库位或目标库位上设置了库存价值科目（字段 valuation_account_id）
    4.  产品或分类上设置为自动计价(real_time)
```

8.  入库/出库Stock Move验证完成时候，自动产生会计分录的科目取值方法：
9.  1.  入库Stock Move，目标库位要计算库存价值，但源库位不要计算库位价值。系统借方科目取自产品或分类上设置的库存计价科目(字段 property_stock_valuation_account_id)，贷方科目取自源库位的库存价值科目(字段 valuation_account_id)
```python
    2.  出库Stock Move，源库位要计算库存价值，但目标库位不要计算库位价值。系统借方科目取自源库位上设置的库存计价科目(字段 valuation_account_id)，贷方科目取自产品或分类上设置的库存计价科目(字段 property_stock_valuation_account_id)
    3.  注意，如果希望自动产生入库、出库会计分录，入库的源库位、出库的目标库位一定要设置会计科目，不设置，系统不会生成会计分录
    4.  相关代码参考：OSCGODOO19\source\addons\stock_account\models\stock_move.py 方法 _get_account_move_line_vals()
```

10. 入库Stock Move验证完成时候，自动产生会计分录的金额取值方法：
11. 1.  入库Stock Move的价值计算方法。场景一，采购入库，例如采购100件，入库前收到采购发票80件，实际入库105件。此种情况，入库105件的stock move的入库价值应该如何计算呢？从会计上讲，其中80件应该从采购发票上取得单价计算价值，20件应该从采购单上取得单价计算价值，剩下5件应该取产品上设置的成本单价计算价值。
```python
    2.  场景二，销售退库，销售出库100件，退货20件。此种情况，退货20件的stock move的入库价值应该如何计算？应该从当初销售出库的stock move上取得成本价值，计算方法是，取得销售出库的stock move的总价值(stock move的字段 value)，乘以退货的占比，即20/100，得到退货部分的价值。
    3.  场景三，采购入库，加到岸成本分摊。例如采购100件，单价10元(不含税)，入库后，又到岸成本分摊，每件分摊了2元。Odoo19的处理，分摊验证时候，产生分摊的会计分录，同时重算入库stock move的入库价值(更新stock move的字段 value)，加上分摊的成本。参考代码 OSCGODOO19\source\addons\stock_landed_costs\models\stock_landed_cost.py 方法 button_validate()
    4.  Odoo19入库stock move的价值即按上述方法计算()，先取已开采购发票的金额，再取采购订单的金额，再取退货入库的金额，最后取产品上的成本单价计算金额。
        参考代码：OSCGODOO19\source\addons\stock_account\models\stock_move.py 方法 _set_value() 及方法 _get_value_data()
    5.  注意，stock move价值计算方法 _get_value_data() 提供了一个参数   ignore_manual_update，该参数为True的情况，表示取指定时间点的产品上的成本价格乘以数量作为价值，即标准价格成本法的入库价值算法。
```

12. 出库Stock Move验证完成时候，自动产生会计分录的金额取值方法：
13. 1.  出库Stock Move的价值计算方法，如果是先进先出成本计价方法，按先进先出方法，排序入库stock move，依次取得出库数量和价值，作为出库stock move的出库价值(字段 value)。参考代码：OSCGODOO19\source\addons\stock_account\models\product.py 方法 _run_fifo()
    2.  非先进先出计价方法的情况，直接取产品上的成本价格(字段 standard_price)乘以数量作为出库价值。
14. Odoo19先进先出(FIFO)成本计价原理：
15. 1.  场景：在指定日期，从某库位中取得某产品N件，按FIFO成本计价方法，计算该N件产品的成本价值。例如，今天取得N件，其成本价值是多少；去年的今天取得N件，其成本价值又是多少。Odoo19中，系统可以计算过去时间的N件产品的成本价值
```python
    2.  取得指定日期、指定库位、指定产品的在手库存数量(qty_available)；
    3.  取得尚在库的入库stock move
        在Odoo19以前的版本，每一笔入库，系统在SVL中记录该笔入库的入库数量、入库价值、剩余数量、剩余价值。每次出库，系统按FIFO顺序，取得剩余数量大于零的SVL，依次从最早入库的stock move上减少数量，减少价值，即减少其SVL的剩余数量、剩余价值。
        但Odoo19中，去除了SVL模型，尚在库的入库stock move的计算原理是：取得最近的入库stock move，按入库日期降序排列(最近的在前面)。从qty_available中，依次减去入库stock move的入库数量，直到减完。如此，得到的即为尚在库的入库stock move列表。该列表反序排列，即最早入库的排前面。
        从入库stock move列表中，依次取得入库数量和价值，直到取满N件产品。
    4.  参考代码 OSCGODOO19\source\addons\stock_account\models\product.py 方法 _run_fifo()
```

16. stock move的剩余数量(字段remaining_qty)计算逻辑：
17. 1.  以前的版本，因为有SVL，SVL上记录了stock move的剩余数量。Odoo19没有了SVL，但stock move上仍有剩余数量字段 remaining_qty，该字段可以计算而得。
    2.  参照FIFO的计算原理，从最近的入库stock move开始，依次减在手库存，减到零的时候，对应那条入库stock move。在它之后的入库stock move，剩余数量等于入库数量，在它之前的入库stock move，剩余数量为零。它本身，剩余数量为入库数量减去在手库存后的数量。
    3.  参考代码 OSCGODOO19\source\addons\stock_account\models\stock_move.py 方法 _compute_remaining_qty()
18. Odoo19移动加权平均(AVCO)成本计价原理：
19. 1.  场景：指定日期，某库位中某产品，按AVCO计算其库存价值。Odoo19以前的版本中，AVCO成本计价方法，库存价值计算一直存在一些问题，如，没有产品成本价格重算功能，一旦成本价格有错，没法纠正，基本只能将错就错。也没法查看历史日期的成本价格。因为这些问题，Odoo的成本数据基本是不可信任的。Odoo19解决了这些问题。
```python
    2.  Odoo19新增模型product.value，产品上的成本价格变更时候，系统自动记录历史价格到模型product.value，因此，从product.value中，可以取得历史时间的成本价格。
        从product.value模型中，取得产品的历史成本价格列表。取得系统中截止到指定日期的所有入库(is_in)stock_move列表, 以及所有出库(is_out)的stock_move列表。直发(dropship)既算入库也算出库。
    3.  按stock move的日期顺序，从最早的开始，模拟入库、出库过程，逐笔计算成本价格。如果是入库stock move，按移动加权平均(AVCO)方法，计算成本价格，增加库存价值。如果是出库，减少库存数量，减少库存价值(出库不影响成本价格)。
    4.  参考代码 OSCGODOO19\source\addons\stock_account\models\product.py 方法 _run_avco()
```

20. 产品库存价值(产品上的计算型字段 total_value、avg_cost)的计算逻辑：
21. 1.  字段 total_value：产品当前时间点的库存总价值(在当前公司，所有库位的总价值)，不同计价方法(standard、avco、fifo)，其值计算逻辑不同。
```python
    2.  字段 avg_cost：平均价格，其值为 total_value除以在手库存(qty_available)
    3.  标准成本计价方法(standard)情况，当前在手库存数量，以及当前的产品成本价格，相乘，得到总库存价值total_value。
    4.  移动加权平均计价方法的情况，按前述AVCO计价原理，取得当前时间，在手数量的库存价值
    5.  先进先出计价方法的情况，系统取得指定日期的在手库存数量，按前述FIFO计价原理，取得在手数量的库存价值
    6.  参考代码 OSCGODOO19\source\addons\stock_account\models\product.py 方法 _compute_value()
```

22. 产品上成本价格(字段 standard_price)的更新机制：
23. 1.  入库和直发的stock move验证完成时候：标准成本计价，不更新成本价格；FIFO的情况，重新按FIFO计算产品的avg_cost，用avg_cost更新成本价格，如果avg_cost为0，则用最近一次的入库stock move的价格更新成本价格；其他情况(AVCO)则重新按AVCO计算产品的avg_cost，更新成本价格。
```python
    2.  采购发票(供应商账单)验证时候，(账单价格可能和采购价格不一致)自动重算账单关联的入库stock move的价值(value字段)，自动按入库逻辑更新成本价格。
    3.  到岸成本分摊验证时候，发生了分摊的入库和直发的stock move，系统按“入库和直发的stock move验证完成时候”的逻辑，更新成本价格。
    4.  出库stock move验证完成时候：只有FIFO的情况，系统重新按FIFO计算产品的avg_cost，更新成本价格
```

24. 产品/分类上 Inventory Valuation 选项含义：
25. 1.  periodic: 入库或出库(库存资产变化)时候，不自动生成会计分录，销售发票确认时候，也不自动产生销售成本相关的分录。
    2.  real_time:  入库或出库(库存资产变化)时候，自动生成会计分录。不过，还要注意，自动产生会计分录，还必须是可库存商品，源库位(入库情况)或目标库位(出库情况)的必须配置了库存计价科目(库位字段valuation_account_id)。 销售发票确认时候，自动产生销售成本相关的分录。
26. 采购发票(供应商账单)会计处理逻辑：
    1.  非库存商品，或者非real-time的商品，借方科目取产品/分类上配置的费用科目，贷方取业务伙伴上配置的应付科目。
    2.  库存商品，且 real-time的商品， 借方科目取产品/分类上配置的库存价值科目，贷方取业务伙伴上配置的应付科目。
27. 销售发票(客户结算单)会计处理逻辑：
28. 1.  借方科目取业务伙伴上配置的应收科目， 贷方取产品/分类上配置的收入科目。如果是 real-time的商品，还会自动生成销售成本的分录，借方取产品/分类上配置的费用科目，贷方取产品/分类上配置的库存价值科目。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
