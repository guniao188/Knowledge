---
title: "供应商询价功能增加比价功能purchase_requisition_listprices"
source: "http://www.thinkltd.cn/forum/2/purchase-requisition-listprices-3419"
forum: "模块库"
author: "肖相扶"
published: 2024-07-26
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 供应商询价功能增加比价功能purchase_requisition_listprices

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-07-26
> <http://www.thinkltd.cn/forum/2/purchase-requisition-listprices-3419>

模块位置：OSCG_SVN\odoo_ecommerce\14.0SRC\询报价\purchase_requisition_listprices

【业务背景】

Odoo现有的供应商询价功能模块purchase_requisition，该模块可以创建多个RFQ向多个供应商询价。但该模块缺乏比价功能，例如，同时向10个供应商询价10种商品，供应商报价回来后，需要比较100个价格，而后挑选最优供应商。Odoo现有功能缺乏方便的比价视图。

【解决方案】

1) 新开发模块purchase_requisition_listprice，在purchase.requisition表单上增加页签，列示RFQ中各个供应商的价格对比，如下图样式，一个供应商显示一行，方便比对。

2) 增加供应商直接在线提交报价（而不是邮件发送空白Excel让供应商填写），参考这个模块：[供应商门户/在线询价报价website_vendor_portal_app](http://www.thinkltd.cn/forum/2/question/website%5C-vendor%5C-portal%5C-app%5C-3449) 或者\[https://apps.odoo.com/apps/modules/14.0/purchase_rfq_online/](https://apps%5C.odoo%5C.com/apps/modules/14%5C.0/purchase_rfq_online/)

![[2-purchase-requisition-listprices-3419-1ff330d1.png]]

## 补充/答案 1

【功能截图】

![[2-purchase-requisition-listprices-3419-1bb3bb0a.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
