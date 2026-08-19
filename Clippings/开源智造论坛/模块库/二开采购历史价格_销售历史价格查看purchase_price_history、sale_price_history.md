---
title: "二开采购历史价格/销售历史价格查看purchase_price_history、sale_price_history"
source: "http://www.thinkltd.cn/forum/2/purchase-price-historysale-price-history-3425"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开采购历史价格/销售历史价格查看purchase_price_history、sale_price_history

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/purchase-price-historysale-price-history-3425>

【20220630更新】模块 sale_price_history 换了一种技术实现方式，以使得新建的SO上也可以查看历史价格（之前的版本必须先报存，才能查看历史价格）。

【20220309升级到了15.0】位置：OSCG_SVN\odoo_ecommerce\15.0SRC\销售\sale_price_history

OSCG_SVN\odoo_ecommerce\15.0SRC\采购\purchase_price_history

【14.0模块连接】OSCG_SVN\odoo_ecommerce\14.0SRC\销售采购对账\purchase_price_history

OSCG_SVN\odoo_ecommerce\14.0SRC\销售采购对账\sale_price_history

【模块功能】

PO Order Line上增加按钮，快速查看商品的历史采购价格

![[2-purchase-price-historysale-price-history-3425-b4d422f8.png]]

销售明细行上增加历史价格查看按钮：

![[2-purchase-price-historysale-price-history-3425-d5dc8ca5.png]]

## 补充/答案 1

实施需要了解一下，这个功能未考虑res.partner模型的记录规则

场景：

权限设置：采购员只看自己的供应商

A采购员向AA供应商采购过物料

B采购员这次向BB供应商采购物料

在历史价格中，会同时记录AA和BB供应商的历史采购记录

各自打开自己的采购单，因没有权限互相看对方的供应商，因此打开单据会报错

## 补充/答案 2

这个SVN的版本问题，会显示其他客户或供应商的浮窗价格，正常是只要这个客户的即可。

## 补充/答案 3

![[2-purchase-price-historysale-price-history-3425-61699802.png]]

![[2-purchase-price-historysale-price-history-3425-61699802.png]]

安装后，打开采购报错

## 补充/答案 4

报错原因在于，安装模块前没有重新启动Odoo

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
