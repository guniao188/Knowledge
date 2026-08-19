---
title: "Odoo14、15、16、18新版收发存报表stock_report_sfc"
source: "http://www.thinkltd.cn/forum/2/odoo14151618stock-report-sfc-3531"
forum: "模块库"
author: "肖相扶"
published: 2025-05-28
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo14、15、16、18新版收发存报表stock_report_sfc

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2025-05-28
> <http://www.thinkltd.cn/forum/2/odoo14151618stock-report-sfc-3531>

18.0版位置：OOdoo18以后参考这个改善版本： [Odoo18进销存/收发存报表模块stock_report_sfc](http://www.thinkltd.cn/forum/2/odoo18-stock-report-sfc-4024)

16.0版位置：https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/stock_report_sfc

模块位置： OSCG_SVN\odoo_ecommerce\15.0SRC\存货核算\stock_report_sfc

【20220331修改】

1.  第一列产品名称中，增加产品编码的显示

2.  增加期间出入库类型的显示选项，期间入库类型包括：采购入库、生产入库、销售退货、盘盈、其他；期间出库类型包括：销售出库、生产领料、采购退货、盘亏、其他。库间调拨同时归属于“其他入库”和“其他出库”

3.  期间出入库类型的实现方法是：Stock Move上增加了一个“期间类型”的字段 mtype ，需要事先运行服务器动作，给Stock Move的“期间类型”自动填值。本模块自带一个默认的服务器动作“计算收发存报表期间类型”，可以根据实际情况修改此服务器动作（例如贸易型企业，没有安装生产模块的情况，必须去掉服务器动作中生产相关的出库、入库）。

【模块功能】

1.  在财务报表中增加 进销存/收发存 报表。

2.  该报表基于库存移动Stock Move获取各库位的期初、期间入库、期间出库、期末数量；

3.  根据库存计价模型（stock.valuation.layer）计算每个产品的期初总价值、期间出库总价值、期末总价值，总价值除以产品的期初、期间出库、期末总数量，得到产品的期初单价、期间出库单价、期末单价；

4.  每个库位的产品期初数量 乘以 期初单价，得到该库位的期初价值，同理计算库位的期间出库价值、期末价值，该库位的期末价值 + 期间出库价值 - 期初价值，得到该库位的期间入库价值（倒轧得到入库价值）。

5.  需要纳入收发存报表的库位，库位上有个“收发存报表”字段，需要勾选该字段。

6.  202220129改善：第一列（产品名称）固定宽度，宽度设定参考模块文件 stock_report_sfc\static\src\scss\stock_report_sfc.scss，默认值 22em。产品名称过长的情况，显示不完全的文字以 ... 表示。同一分类下面，如果数据量太大，一次默认只加载80条，而后显示 “Load More...”，点击Load More 再加载80条。

【功能截图】

![[2-odoo14151618stock-report-sfc-3531-4d5fb6f9.png]]

![[2-odoo14151618stock-report-sfc-3531-3b66f275.png]]

![[2-odoo14151618stock-report-sfc-3531-fd4049b8.png]]

**202220129改善**：第一列（产品名称）固定宽度(22em)，产品名称过长的情况，显示不完全的文字以 ... 表示。同一分类下面，如果数据量太大，一次默认只加载80条，而后显示 “Load More...”，点击Load More 再加载80条。如下图

![[2-odoo14151618stock-report-sfc-3531-a066e518.png]]

## 补充/答案 1

【20220331新增期间出入库类型功能截图】

![[2-odoo14151618stock-report-sfc-3531-fc01dd52.png]]

## 补充/答案 2

第一列名称，希望可以同时显示产品的default_code，因为同名的产品很多，default_code往往唯一，这样可以导出Excel后用default_code字段做数据处理

临时解决方案 在py文件的第314行调整name的取值，拼上了default_code

            select distinct SM.product_id as id, Concat(PT.default_code,'-',PT.name) as name, pc.name as categ_name

## 补充/答案 3

咋没有最后的所有产品的合计呢？

另外产品分类维度和产品维度，可以自由选择吗？比如全部只看产品，不需要产品分类的时候，目前导出成excel后，因每一个分类也有小计，还有产品也有值，算合计的时候，还得要将分类和产品剔出来，才能汇总。

还有上面小计的分类，和下面的产品行的因为底色都是白色，很容易看混淆，要是能有底色不同字大小或底色区分，体验上会好一些。

还有期间类型的方式的样式叠字了，有些数据值看不到

![[2-odoo14151618stock-report-sfc-3531-e8469d18.png]]

![[2-odoo14151618stock-report-sfc-3531-beb170b6.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
