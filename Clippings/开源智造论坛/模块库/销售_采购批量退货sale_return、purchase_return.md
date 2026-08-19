---
title: "销售/采购批量退货sale_return、purchase_return"
source: "http://www.thinkltd.cn/forum/2/sale-returnpurchase-return-3226"
forum: "模块库"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 销售/采购批量退货sale_return、purchase_return

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/sale-returnpurchase-return-3226>

【**20221207升级到了16.0**】

- https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/purchase_return

- https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/sale_return

- https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/sale_return_mrp

【**20211224升级到15.0**】采购退货位置：OSCG_SVN\odoo_ecommerce\15.0SRC\采购\purchase_return

【20220628增加】支持套件BoM的销售退货模块：OSCG_SVN\odoo_ecommerce\15.0SRC\销售\sale_return_mrp

经测试，14.0版的销售退货 sale_return 直接可以在15.0上应用

销售退货模块位置：OSCG_SVN\odoo_ecommerce\13.0SRC\sale_return

采购退货模块位置：OSCG_SVN\odoo_ecommerce\13.0SRC\purchase_return

采购退货有新补增加供应商价格的取值，原来版本负数量总会是0单价。V13版本可以参考目录D:\svn\SVN\odoo_ecommerce\06.Customization\纵微\addons\新版采购退货

以及这个目录下还有D:\svn\SVN\odoo_ecommerce\06.Customization\纵微\addons【纵微采购批量集中退货操作说明.docx】参考。

Odoo 14.0版本位置：

OSCG_SVN\odoo_ecommerce\14.0SRC\销售采购对账\sale_return
OSCG_SVN\odoo_ecommerce\14.0SRC\销售采购对账\\purchase_return

【业务背景】

1.  Odoo现有退货处理功能，是按单退货，不能处理打包退货。以销售退货为例，需要在原来的销售出库单上点击退货按钮，系统生成待退货单，仓库操作退货。采购退货也类似，需要在原来的采购入库单上点击退货按钮，仓库操作退货。

2.  如果涉及红字发票/退款问题，以销售退货为例，会计线下开具红字发票（数量为负数），系统上找到原来的客户发票，点击按钮，创建红字发票。采购退货也同理，供应商开具红字发票过来，系统里面找到原来的供应商账单，点击按钮，创建红字账单。

3.  代理商的情况，销售退货、采购退货，通常是批量退货。以销售退货为例，下级代理商，不定期地把过去一段时间有问题或滞销的商品一次性打包退回。这种退货操作，没法对应到过去的哪个销售出库单。同理，不定期打包退货（采购退货）给上级代理商或厂商。

4.  打包退货时候，不一定按原价退货，可能有协商价格，或者折损价格。相应的要开红字发票，冲销之前的应收/应付。

【模块设计】

1.  销售模块新增“销售退货”菜单，该菜单中创建销售订单，销售明细行上，系统默认带出“销售退货” 路线，数量要求填写 负数。

2.  销售订单确认时候，系统判断数量为负数，则按“销售退货” 路线，自动创建销售退货仓库作业单。销售订单确认时候，系统会判断，不允许订单上有正数、负数混杂的情况。

3.  采购模块新增“采购退货”菜单，该菜单中创建采购退货单，明细行上，要求填写负数数量。采购订单确认时候，系统判断数量为负数，则按退货处理。生成的退货单，取采购入库作业类型上的退货作业类型；生成供应商账单时候，也按红字账单处理。

## 补充/答案 1

再发现一个bug，采购退货的问题：

同一个产品正向的采购订单的单价是正常的，但做采购退货时，带出来的单价会自动的刨掉了税金

![[2-sale-returnpurchase-return-3226-82f9c8d1.png]]

## 补充/答案 2

原因是，产品上的供应商的最低采购数量默认是0。采购退货时候，数量是负数，小于0，导致系统匹配不到该供应商，取不到该供应商价格。此种情况，系统取产品上的成本价格（并不是不含税的供应商价格）作为采购价格。

将产品上的供应商的最低采购量修改为负数（低于退货数量），即可正确取到供应商价格。如下下图：

![[2-sale-returnpurchase-return-3226-aa706fe0.png]]

## 补充/答案 3

V14和V15还有一个bug，没有考虑产品是套件的情况，不能正常回写到销售订单，主要是销售退货模块。

## 补充/答案 4

支持套件BoM的销售退货模块：OSCG_SVN\odoo_ecommerce\15.0SRC\销售\sale_return_mrp

## 补充/答案 5

**当开启多公司的时候，需要创建一条路线和一条规则，不然会报多公司权限错误：**

![[2-sale-returnpurchase-return-3226-7379073f.png]]

**路线和规则配置如下：**

![[2-sale-returnpurchase-return-3226-cb56d0c3.png]]

****

![[2-sale-returnpurchase-return-3226-d10043ed.png]]

## 补充/答案 6

而销售退货，是以入库来的成本，目前测试单据上看，是取的入库时点的产品上的成本，而非销售退货单上的单价，即客户集中退货看起来问题不大。

**但采购的集中退货会有个成本和赁证问题：**

采购订单上是负数，但对于仓库的退货单来说是在出库，所以锁货逻辑及成本计算都是按占用的库存及成本计算方式得到的当时产品时点上的成本值；

而PO负数的红冲退货订单上的金额是与供应商协商的价款，故在生成红冲的供应商账单时，这里的应付暂估成本和仓库的暂估成本是不一致，一定会有差异。

这个采购集中退货的差异该如何平账的问题？这个问题即使不用这个集中退货功能，用系统原生的在原入库单上点【退回】存在同样的问题，退货系统总是按当前时点产品的成本来计算。

那么差异可以材料成本差异分摊处理，也可以直接费用成本化处理进笔总分录账中。

## 补充/答案 7

采购退货数量带到发票上的问题已经修改，具体修改如下：

在purchase_return/models/purchase_order_line.py继承方法**_prepare_account_move_line():**

```python
    def _prepare_account_move_line(self, move):
        data = super()._prepare_account_move_line(move)
        if self.order_id.purchase_return:
            data['quantity'] = -(self.product_qty - self.qty_invoiced)
        return data
```

修改之后的效果如下：

![[2-sale-returnpurchase-return-3226-67c059a9.png]]

![[2-sale-returnpurchase-return-3226-bd9a8f6c.png]]

分批开发票也是没有问题：

![[2-sale-returnpurchase-return-3226-d3d80d87.png]]

![[2-sale-returnpurchase-return-3226-31fcf381.png]]

![[2-sale-returnpurchase-return-3226-72b13090.png]]

## 补充/答案 8

问题反馈：

1、采购退货，没有强校验为负数量

![[2-sale-returnpurchase-return-3226-d8587979.png]]

2、PO退货单退货完成后，开具供应商账单，是红冲类型是对的，但数量为何是0呢？

![[2-sale-returnpurchase-return-3226-1d9011fd.png]]

![[2-sale-returnpurchase-return-3226-2445eeb1.png]]

3、销售退货，数量一列值，应当也要强校验填写负数量吧，不然，很容易用户填错

4、销售退货单，仓库入库完成了，但却没有回写到SO退货单上，导致无法开具红冲的SO红冲invoice

![[2-sale-returnpurchase-return-3226-c1ca9bf3.png]]

![[2-sale-returnpurchase-return-3226-37a339f7.png]]

## 补充/答案 9

订单确认的时候会校验是不是负数，红票时候，数字0 是要自己手工修改的。销售退货的已发送我测试是有值的（见我之前的截图）。

## 补充/答案 10

可以完善一下吗？数量自动按系统逻辑负数的数量即待开红冲票的数量生成带到invoice上？而不需要再手动人工一行一行比对填写呢？

## 补充/答案 11

采购、销售退货模块：包含省份、市区等地址的导入Excel

V13版本链接：OSCG_SVN\odoo_ecommerce\13.0SRC\采购销售退货

 初步测试没有问题！

## 补充/答案 12

【功能截图】

销售退货单

![[2-sale-returnpurchase-return-3226-b4b54aaa.png]]

采购退货单

![[2-sale-returnpurchase-return-3226-8d227cdf.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
