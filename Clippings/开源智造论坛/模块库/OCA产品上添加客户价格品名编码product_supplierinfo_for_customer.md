---
title: "OCA产品上添加客户价格品名编码product_supplierinfo_for_customer"
source: "http://www.thinkltd.cn/forum/2/ocaproduct-supplierinfo-for-customer-2659"
forum: "模块库"
author: "肖相扶"
published: 2024-11-29
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA产品上添加客户价格品名编码product_supplierinfo_for_customer

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-11-29
> <http://www.thinkltd.cn/forum/2/ocaproduct-supplierinfo-for-customer-2659>

V17改善及改过bug后的模块参考：git华霆里面：[https://gitlab.com/oscg-china/chint_shanghai_v17.git](https://gitlab.com/oscg-china/chint_shanghai_v17.git)

这个功能对应的模块名字为： product_supplierinfo_for_customer和product_supplierinfo_for_customer_sale

示例效果图如下：

![[2-ocaproduct-supplierinfo-for-customer-2659-42be1716.png]]

![[2-ocaproduct-supplierinfo-for-customer-2659-08b4d137.png]]

![[2-ocaproduct-supplierinfo-for-customer-2659-16c25426.png]]

产品上添加客户价格、产品编码及名称：

12.0版本：

15.0版本：[product-attribute/product_supplierinfo_for_customer at 15.0 · OCA/product-attribute · GitHub](https://github.com/OCA/product-attribute/tree/15.0/product_supplierinfo_for_customer)

Odoo17.0版本： [product-attribute/product_supplierinfo_for_customer at 17.0 · OCA/product-attribute · GitHub](https://github.com/OCA/product-attribute/tree/17.0/product_supplierinfo_for_customer)

SO上录入客户产品编码及名称：

14.0版本： [sale-workflow/product_supplierinfo_for_customer_sale at 14.0 · OCA/sale-workflow · GitHub](https://github.com/OCA/sale-workflow/tree/14.0/product_supplierinfo_for_customer_sale)

【注意事项】

安装本模块后，价格表上，价格计算公式的 计价基础 base 设置为基于客户（Partner），电商网站上价格显示时候，系统报错“KeyError: 'partner'”。原因查明是因为，1) 电商价格计算调用的是product.template的方法 price_compute， 在该方法中，处理patner的计价基础时候，报错。2) 本模块继承重写了 product.product 的方法price_compute，对partner的情况做了特殊处理，因而SO上价格计算没问题。但没继承重写product.template的方法 price_compute，因而电商上价格计算报错。3) 解决方法是，参照重写product.product 的方法price_compute，重写一下product.template 的方法price_compute 即可。

This modules allows to use supplier info structure, available in *Inventory* tab of the product form, also for defining customer information, allowing to define prices per customer and product.

## [Configuration](https://github.com/OCA/product-attribute/tree/11.0/product_supplierinfo_for_customer#id1)

For these prices to be used in sale prices calculations, you will have to create a pricelist with a rule with option "Based on" with the value "Partner Prices: Take the price from the customer info on the 'product form')".

##

## [Usage](https://github.com/OCA/product-attribute/tree/11.0/product_supplierinfo_for_customer#id2)

There's a new section on *Sales* tab of the product form called "Customers", where you can define records for customers with the same structure of the suppliers.

There's a new option on pricelist items that allows to get the prices from the supplierinfo at the product form.

## 补充/答案 1

V17版本改善及处理过bug之后的版本模块：模块名字，product_supplierinfo_for_customer和product_supplierinfo_for_customer_sale参考华霆上海v17版本。

## 补充/答案 2

使用注意要点：

1、这个模块使用时，注意这个关联的对象与供应商价格表是同一个对象product.supplierinfo

2、在导入或提供模板（不管 是产品批量导入还是单独这个菜单下去导入都需要考虑到）时，如果导入供应商价格表，菜单增加限制[('supplierinfo_type','=','supplier')]，需要必须导入一列为supplierinfo_type为supplier，否则二边会窜，混乱

导入客户产品编码表时，需要菜单加限制：[('supplierinfo_type','=','customer')]

3、oscg_customer_code_action这个模块依赖于：
sale和search_customer_product
4、有遇到当客户产品编码记录数量非常大时，搜索或创建时，会导致CPU占用率到300%几倍，卡死系统；当时这里也有调查，后来是有拿掉了产品搜索空格代表通配符的功能，才有缓解；

5、示例客户：华霆、平湖机械 V13版本都已有上线在使用中；

6、也有踩过坑，当产品有开变体时，到SO订单行上，无法正常显示这个客户产品编码，故有加强了模块和补丁，具体经手人蔺辉；华霆addons上有最新的；

7、另外，当跑安全库存或MTO时，因为客户产品编码和供应商产品编码都是同一个对象，所以自动跑出来的供应商采购询价单上的【供应商】会出现不对，如果客户产品编码里绑的客户上的【序号】是1，就会导致这个问题

解决方法：将客户产品编码里的记录的【序号】设置得大一些，比如默认设成客户产品编码记录序号统一是1000

而供应商价格表记录序号是按系统原有的，这样跑出来的询价单才是正确的。

可以在客户产品编码表的菜单动作中，设置上下文默认值：'default_sequence':'1000',

即{'default_supplierinfo_type':'customer','default_sequence':'1000', 'default_search_supplierinfo_type':'customer',                'tree_view_ref':'oscg_customer_code_action.oscg_product_supplierinfo_tree_view',                'form_view_ref':'oscg_customer_code_action.oscg_product_supplierinfo_form_view'}

![[2-ocaproduct-supplierinfo-for-customer-2659-918e61e7.png]]

## 补充/答案 3

odoo12升级方法：

product_supplierinfo_for_customer_sale/views/sale_view.xml

```python
    中的

    中的
```

xpath expr="//search/group" position="inside">

    中的

替换为

## 补充/答案 4

需要V12的版本

还要有发货单上体现客户编码


## 评论

> [!quote] 符赛红 · 2024-11-29
> V17版本改善及处理过bug之后的版本模块：模块名字，product_supplierinfo_for_customer和product_supplierinfo_for_customer_sale参考华霆上海v17版本。


## 原帖外链配图

![[2-ocaproduct-supplierinfo-for-customer-x194038c2.png]]
<small>原始地址: /web/image/996/snipaste_20190120_234041.png?access_token=4d2c226e-2602-4ead-add8-a2e3708fbb20</small>

![[2-ocaproduct-supplierinfo-for-customer-x194038c2.png]]
<small>原始地址: /web/image/998/snipaste_20190120_234156.png?access_token=022930e1-8f4e-4c8c-a5fc-0343be6eb897</small>

![[2-ocaproduct-supplierinfo-for-customer-x194038c2.png]]
<small>原始地址: /web/image/990/snipaste_20190120_231913.png?access_token=380b36c9-3a8d-46a9-8900-83652fbcb861</small>

![[2-ocaproduct-supplierinfo-for-customer-x194038c2.png]]
<small>原始地址: /web/image/992/snipaste_20190120_231904.png?access_token=967eca6b-83bb-4426-ac6b-006346da711e</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
