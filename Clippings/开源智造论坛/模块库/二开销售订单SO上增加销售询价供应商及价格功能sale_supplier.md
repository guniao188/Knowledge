---
title: "二开销售订单SO上增加销售询价供应商及价格功能sale_supplier"
source: "http://www.thinkltd.cn/forum/2/sosale-supplier-3303"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开销售订单SO上增加销售询价供应商及价格功能sale_supplier

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/sosale-supplier-3303>

模块链接：OSCG_SVN\odoo_ecommerce\13.0SRC\外贸跟单\sale_supplier

11.0版：[/forum/2/question/sale-merchandiser-2496](http://www.thinkltd.cn/forum/2/question/sale-merchandiser-2496)

* 应用场景：贸易公司，原则上没有库存，都是MTO订单，且经常有新产品销售（第一次销售的产品）。此类产品在给客人SO的同时，需要临时找供应商询价。此种场景，SO上需要有供应商询价功能。
* 本模块在SO Line上增加三个字段：供应商、采购说明、采购价格。
* 选择产品时候，系统自动带出上述三个字段，SO确认时候，系统将产品供应商、采购价格、采购说明自动更新到产品档案上。

## 补充/答案 1

是否一定要将产品设置为MTO按订单生成才能与PO关联呢？

## 补充/答案 2

不管是不是MTO，都是，SO确认时候，系统将产品供应商、采购价格、采购说明自动更新到产品档案上。但如果不是mto，so确认时候不会有po产生，po和so自然没关联。

## 补充/答案 3

可以在销售报价单状态，能同步去生成采购询价单吗？点个按钮就能跳转生成一张相同产品项的采购询价单，右上角并与so相关联吗？这样就不用设mto了，再确认SO也不用关联再产生有采购了，可以明细行与采购有关联字段的话，可以同步抓取已确认为真的信息，然后再采购也能再接着往下走流程，确认相应的询价单为采购订单了，多的询价单取消掉。

实际业务中，在尚未接到销售订单时，就有询价要求，如果是在销售界面去完成采购询价，有缺陷：

1、无法一对多询价，

2、涉及销售上的权限问题，

3、采购询价如果需要每个单找供应商咨询，还不能引用门户供应商进行供应商自行填补采购价格。

## 补充/答案 4

【功能截图】

![[2-sosale-supplier-3303-cc23ebcc.png]]

## 补充/答案 5

bug修正：这个代码没有考虑多公司问题：

![[2-sosale-supplier-3303-33f549a1.png]]

加上 with_company(self.company_id)

![[2-sosale-supplier-3303-a00ccf81.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
