---
title: "Odoo17销售改善点一览"
source: "http://www.thinkltd.cn/forum/1/odoo17-3815"
forum: "求助台"
author: "肖相扶"
published: 2024-04-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17销售改善点一览

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-04-10
> <http://www.thinkltd.cn/forum/1/odoo17-3815>

返回  [Odoo17改善点列表](http://www.thinkltd.cn/forum/1/odoo17-3808)

1.  从产品目录批量添加产品
    销售订单SO、采购订单PO上，支持按产品目录批量添加多个产品明细行。 

![[1-odoo17-3815-f54f597a.png]]

2.  Amazon Connector
    Manually launch the synchronization of an Amazon order based on its Amazon reference. Shipping confirmations statuses sent to Amazon are now synchronized.
3.  Amazon synchronization
    Update the quantities available for 'Fulfilled by Merchant' (FBM) offers on Amazon depending on inventory levels.
4.  Confirmation on down payment
    Ask for a down payment from your customers to validate their quotation.
5.  预收款描述
    销售订单预收款明细行上，描述信息里，预收款发票确认后，预收发票号码自动添加到描述信息里。

![[1-odoo17-3815-ab0c5b92.png]]

6.  Events: support quotation templates
    Include event tickets in quotation templates.
7.  整单折扣
    销售订单上增加整单折扣功能。

![[1-odoo17-3815-5d2099e3.png]]

8.  积分条件增加价格表
    积分程序上增加价格表条件。

![[1-odoo17-3815-97575b04.png]]

9.  积分条件增加开始日期
    积分条件设置上增加“Start Date”字段，标记积分规则什么时候开始生效。
10. No tax on fixed discounts
    Taxes are not applied on fixed discounts anymore.
11. Partial payments
    The partial payment flow was improved: it's easier to create payment links and quotations are automatically confirmed when a partial payment completes the total amount.
12. PDF quote builder
    Send attractive quotations to improve your conversion rate. Upload your own PDF files and insert them as header pages, product pages, and footer pages.
13. PDF报表:忽略数量为零的明细行
    PDF打印报表，数量为零的变体不再出现在销售订单的PDF打印报表上。
14. 价格表：聊天区
    价格表的Form视图，下方增加Message区域（聊天区域），方便调价沟通记录。
15. Product documents
    Share documents with your customers automatically when sending a quotation or once the order is confirmed by linking documents to your products.
16. 报价单批量取消
    报价单列表视图上，增加批量取消报价单功能。
17. 销售订单锁定
    可以在任何阶段锁定销售订单（锁定后不可编辑）。
18. 无价格表的销售订单
    不配置价格表，销售流程也可以往下走。
19. 客户表单增加积分查询
    客户表单上增加快捷按钮，一键查看客户积分情况。

![[1-odoo17-3815-3a88aeee.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
