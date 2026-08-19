---
title: "外贸常用的内容整合模块 sale_ci_pl"
source: "http://www.thinkltd.cn/forum/2/sale-ci-pl-3366"
forum: "模块库"
author: "符赛红"
published: 2023-06-26
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 外贸常用的内容整合模块 sale_ci_pl

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:符赛红 | 2023-06-26
> <http://www.thinkltd.cn/forum/2/sale-ci-pl-3366>

模块连接：oscg-svn\odoo_ecommerce\13.0SRC\外贸港口\sale_ci_pi

**【外贸业务背景】**

1.  外贸销售订单上，通常都要加上出发港口、到达港口信息。外贸装箱单（Packing List）知识参考：

2.  外贸CI及PL单，需要有包装信息，包装信息包括 唛头（箱标）、箱数、箱规、毛重、净重、体积。包装信息系统可以根据产品的包装规格、重量等计算默认值，而后用户可以修改（按实际装船的包装信息修改）

3.  外贸销售单（PI）上，有些外贸行业需要增加产品的包装数量、包装规格、净重、毛重信息，供销售报价时候估算运费及报价参考

**【模块设计】**

1.  新开发模块 sale_ci_pl， 该模块在销售订单上增加港口字段：1) 该模块新增一个港口模型（sale.port），该模型两个char类型字段：name、code。2) 销售模块设置菜单下增加菜单“Port” 。3) 销售订单sale.order上增加字段port_loading（PORT OF LOADING，起运港, many2one到sale.port）、port_dest（PORT OF Destination，目的港, many2one到sale.port）。4) 注意，字段标签及菜单都用英文，i18n下面做好中文翻译文件

2.  该模块在客户发票上增加CI、PL需要的字段，1) 在account.move.line上增加字段：shipping_mark（Shipping Mark，唛头，Text类型）、packages(Package, 包装数, integer)、g_weight（G.W，毛重，float）、n_weight(N.W，净重，float)、meas(Meas. ，体积，float)。2) 参照这里开发Packing List的PDF打印报表   。3) 注意，字段标签及菜单都用英文，i18n下面做好中文翻译文件。

=============================================================================

**要增加的内容：（记得所有的内容，都需要中英翻译！！！）**

1、在产品的包装设置表单product.packaging增加字段：这些表示都是单箱的相关信息

手动填写：长、宽、高、毛重、净重

自动计算：体积（依据长*宽*高计算得到）

这一点内容，请更新到模块：sale_purchase_stock_packaging 里面继承一下；

另外这个模块，再增加account.move客户**发票明细行上的箱规**（指产品上的包装名）和箱数，默认由销售订单带到发票上，箱数依这个箱规计算出来，当type类型是客户发票时，从so上拉取这个箱规，如果type类型是供应商账单时，请从po上取得这个箱规

**这些内容单独在这个sale_purchase_stock_packaging里更新，也能让其他客户单独使用这个模块哦！！**

2、产品表单上增加字段：

hs_code，海关编码，让用户在产品上维护

产品中文品名：让用户手动填写，系统自带的name让用户填写为英文，这个新加的字段填写中文，为了方便打印取值，以及批量导入，（系统自带的产品名字的翻译太麻烦了，所以添加一下，只是存在于基础资料上，供其他打印调用，出报关文件使用）

3、在销售订单表头上增加字段：sale.order

手动填写：交货时间（char文字说明）、流程方式（char填写）、客服备注（灰色预填值：比如产地证，质量证书等要求）（这个值填写的相当于订单要求，这个字段值要带到picking上）

增加新表单【港口】表，并关联到sale.order，sale.order上增加字段：出发港、目的港 （下拉选择关联到港口表），**so上增加的港口信息需要带到客户发票account.move表头上；**

付款途径：关联到account.journal日记账，并加domain条件只过滤出Type类型是银行或现金类的记录可供SO上选择；

合计体积：依据明细行的值计算得到；

合计毛重：依据明细行的值计算得到；

合计净重：依据明细行的值计算得到；

**订单上的这些信息都是供销售参考和客户参考订舱订柜使用的！**

4、销售订单明细行sale.order.line上增加字段：

单箱体积（默认由订单行上产品包装上面的单箱体积带出来，最好也能允许手动再调整）视图上默认是hide,

净重（默认由订单行上产品包装上面的单箱净重带出来，最好也能允许手动再调整）视图上默认是hide,

毛重（默认由订单行上产品包装上面的单箱毛重带出来，最好也能允许手动再调整）视图上默认是hide,

小计净重：箱数*净重 （视图上默认是显示）

小计毛重：箱数*毛重（视图上默认是显示）

小计体积：箱数*单箱体积（视图上默认是显示）

5、仓库单据stock.picking上增加字段

客服备注：通过sale_id字段从so上引入到picking上

增加以下属性页签里的packing list的所有内容字段及明细行值，参考delora的模块升级，都是手动录入填写的，（一般是给采购用户填写供应商的发货信息，供单证员参考和货贷去拼柜使用的，因为是供应商提供的，故有可能与原产品上配置的会不一样，故这个表单上是让用户手动填写的），字段默认值需要实施过程中去设置。

![[2-sale-ci-pl-3366-51c5fceb.png]]

![[2-sale-ci-pl-3366-629b34dc.png]]

4、在客户发票account.move表单上增加的内容：这些是针对给客户的，所以记得增加的内容全部要加domain条件，**依据type的类型判断一下，只是针对于客户发票才出现，不要出现在会计凭证及供应商账单里面哦！**

表头有：出发港、目的港，这个由so_id上带过来显示，如果遇到多个订单上的值合并开票，有不同的港口信息，则默认取第一个或其中一个即可，但需要在客户发票上，还能用户手动调整；

增加属性页签上的内容：shipping/commercial invoice

![[2-sale-ci-pl-3366-d0848a8f.png]]

合计的净重

合计的毛重

合计的体积

![[2-sale-ci-pl-3366-20472184.png]]

![[2-sale-ci-pl-3366-7211e326.png]]

![[2-sale-ci-pl-3366-7211e326.png]]

****这些都是手动填写，发票上其他没框的字段，不需要增加，那是delora特有的。****

5、客户发票明细行增加字段列： （可库存商品才参考计算，服务类产品不需要，或者当产品上没有维护包装信息时，默认值为0）

净重：箱数*箱规上的单箱净重，也允许用户手动更改填写这个值（因为默认带出来的只是参考值，实际在做CI时可能会改多或改少，为了方便清关或货贷处理）

毛重：箱数*箱规上的单箱毛重，也允许用户手动更改填写这个值（因为默认带出来的只是参考值，实际在做CI时可能会改多或改少，为了方便清关或货贷处理）

体积：箱数*箱规上的单箱体积，也允许用户手动更改填写这个值（因为默认带出来的只是参考值，实际在做CI时可能会改多或改少，为了方便清关或货贷处理）

以上这些内容打包在一个模块中，除了特定的包装模块，第一点要合在一起外，其他的是在外贸模块里。

**发票上增加的这些都是为了出CI和packing list报关或清关使用。因为存在多个订单合并柜子发货的情况，以及拆开发货情况，所以多了这里也需要）**

***以上都只是外贸基础版 需要的内容，再高级一点的话，就需要有个单证员排货期及拼柜货柜，需要新开发表单去做，从so对应的尚未发货的明细，因为排柜时，有可能出现排不进去的情况，可能会有同一个订单排多次的可能，直到最终出港才不会再排到，故要最终完成的才不再进排柜表里选择），这里可以请老肖设计一下。***

**如果能单独出排柜的模块，那么在客户发票上加的内容就不需要加了，而是同样的内容要改到这个排柜的清单里面。******
**

****目前先让用户线下排，出CI是用的account发票来的。这是二个不同的方案。****
**

另外，整个外贸还需要搭配模块组合安排：（有现成的）

包装[/forum/2/question/sale-purchase-stock-packaging-3165](http://www.thinkltd.cn/forum/2/question/sale-purchase-stock-packaging-3165)

跟单二个[/forum/2/question/sale-merchandiser-2496](http://www.thinkltd.cn/forum/2/question/sale-merchandiser-2496)

[/forum/2/question/sosale-supplier-3303](http://www.thinkltd.cn/forum/2/question/sosale-supplier-3303)

订单类型[/forum/2/question/ocasosale-order-type-2676](http://www.thinkltd.cn/forum/2/question/ocasosale-order-type-2676)（V13谱源也有用到)sale_order_type)

打印excel基础功能[/forum/2/question/excelreport-xlsx-2987](http://www.thinkltd.cn/forum/2/question/excelreport-xlsx-2987)

客户产品编码模块[/forum/2/question/ocaproduct-supplierinfo-for-customer-2659](http://www.thinkltd.cn/forum/2/question/ocaproduct-supplierinfo-for-customer-2659)（这个到svn华霆下面拉最新的代码V13,有改过bug)

订单阻塞模块[/forum/2/question/ocasosale-stock-picking-blocking-2670](http://www.thinkltd.cn/forum/2/question/ocasosale-stock-picking-blocking-2670) （有需要多一个确认订单环节时增加）

等等。请结合使用。

配置上要开启：产品包装、交货方式

## 补充/答案 1

内容过于简单。出发港目的港等报关，发货通知需要用的信息应该在发票里集中体现。

产品上缺少一些外贸常用的信息：HScode，产地（现在报关，都需要提供产地），产品尺寸（装箱时需要用于计算）。

发票上，不建议净重，毛重，箱规等信息直接在发票行维护。建议开2个page页：“运输”，“包装”。

运输page用于集中填写报关，发货通知单的信息，不然信息分散在系统中，不利于操作员操作。

包装page用于维护产品的重量，箱规等信息。

下图是在做亚荷项目中，沟通的展示效果。给做参考。（亚荷家目前装箱page还没做好）

![[2-sale-ci-pl-3366-6c57b01e.png]]

![[2-sale-ci-pl-3366-20495311.png]]

## 补充/答案 2

![[2-sale-ci-pl-3366-08a677ed.png]]

模块链接：D:\oscg-svn\odoo_ecommerce\13.0SRC\外贸港口\sale_ci_pi

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
