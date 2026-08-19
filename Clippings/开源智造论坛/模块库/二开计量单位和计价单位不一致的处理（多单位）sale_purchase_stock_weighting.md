---
title: "二开计量单位和计价单位不一致的处理（多单位）sale_purchase_stock_weighting"
source: "http://www.thinkltd.cn/forum/2/sale-purchase-stock-weighting-3177"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开计量单位和计价单位不一致的处理（多单位）sale_purchase_stock_weighting

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/sale-purchase-stock-weighting-3177>

svn路径：odoo_ecommerce/12.0SRC/sale_purchase_stock_weighting
【20220324新增15.0版本】位置： OSCG_SVN\odoo_ecommerce\15.0SRC\包装称重

【业务背景】

1.  业务场景1：钢管贸易。某型号的钢管，长度、内径、外径有标准值（允许一定误差），实际生产中，不同批次、不同炉号，生产出来的每根钢管的重量都可能不同（在一定误差范围之内）。采购时候，向厂家要货某型号钢管10吨，厂家实际发货可能是钢管50根，重量10.1吨（每根200公斤，有一定误差）。仓库管理时候，按根管理（按根入库、出库、盘点）。财务结算时候，按公斤结算（采购单价是每吨多少钱，销售单价是每公斤多少钱）。客人要货时候，下单要货3根，实际发货可能是610公斤，财务也是按610公斤结算。

2.  业务场景2：工厂原料采购，采购铜接头1000个。同样道理，每批次的铜接头重量都有差异，采购款结算时候，按铜的重量结算（加上每个的加工费）。生产领料时候，按个领料。库存盘点也按个盘点。

【模块功能】

1.  本模块依赖模块 sale_purchase_stock_packaging ：[/forum/2/question/sale-purchase-stock-packaging-3165](http://www.thinkltd.cn/forum/2/question/sale-purchase-stock-packaging-768)

2.  产品模板上增加Boolean型字段 "采购称重(purchase_weighing)"、"销售称重（sale_weighing）"

3.  采购明细行和销售明细行上增加字段“公斤单价”

4.  stock picking上增加 Boolean型“已称重(weighted)”字段，增加“称重”按钮。**stock move line上增加字段“称重数”**。

5.  stock picking上点击“称重”按钮，系统检查stock move line，如果是要求称重的产品，而“称重数”列或完成数量列的值为0，报错“请先填写好作业明细的重量和完成数量”。如果重量和完成数都填写了，如果是采购入库（对应的stock move 的 purchase_line_id有值），则stock move line的“称重数”乘以采购明细上的公斤单价，除以stock move line的完成数，作为每根的采购单价，更新到采购明细，同时更新对应的stock move的单价（注意去税）。如果是销售出库（对应的stock move 的 sale_line_id有值），则同理更新销售明细行上的单价（但不更新stock move的单价）。同时自动打钩“已称重(weighted)”字段

6.  stock picking上点击“验证”按钮，系统检查，如果存在称重的产品，但“已称重(weighted)”字段没有打钩，则报错“存在称重产品，请先称重再入库！”

7.  模块功能应用方法：1) 产品上定义好箱规“公斤”，以钢管为例，产品单位是“根”，箱规“公斤”的值是 0.005（200公斤一根）；2) 采购时候，采购单明细行的“箱规”填写公斤数，数量列填写“根数”，并填写“公斤单价”；3) 入库时候，stock move line上填写好“称重数”（公斤数）、实际入库数（根数）；4) stock picking上点击按钮“称重”，系统更新采购单价/入库单价/销售单价。

8.  **采购明细行和销售明细行上，增加“实重”字段，仓库称重时候，将实际重量回写到此字段（多次入库多次称重的情况，累加多次的实际重量）。**

【功能截图】

采购表单上增加公斤单价

![[2-sale-purchase-stock-weighting-3177-37e0ec0e.png]]

Picking上增加称重功能：

![[2-sale-purchase-stock-weighting-3177-612f71b9.png]]

产品上增加称重配置：

![[2-sale-purchase-stock-weighting-3177-6d6bf309.png]]

销售表单上增加称重功能

![[2-sale-purchase-stock-weighting-3177-61c9c0c6.png]]

## 补充/答案 1

V13 svn路径：odoo_ecommerce/13.0SRC/sale_purchase_stock_weighting

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
