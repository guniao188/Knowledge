---
title: "产品名称搜索功能增强product_name_search_split"
source: "http://www.thinkltd.cn/forum/2/product-name-search-split-3559"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 产品名称搜索功能增强product_name_search_split

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/product-name-search-split-3559>

模块位置：OSCG_SVN\odoo_ecommerce\15.0SRC\销售\product_name_search_split

【业务背景】

1.  工业品经销商，产品规格品种几十万，一个业务员每天处理几十个客户报价，一个报价单几十个报价产品。

2.  录入客户报价单时候，要求系统可以同时按产品名称、产品编码、产品规格属性同时快速搜索产品。

3.  有些大客户有客户专属的产品名称、产品编码，录入客户产品编码、产品名称时候，系统也能查找到对应的产品。

4.  报价员产品添加时候，支持空格分开，乱序搜索。例如，输入关键字“nx 32 32 tu”，系统应该把同时含有 nx、32 32、tu的产品显示出来，支持乱序匹配。例如，关键字“nx 32 32 tu”可以匹配 NXA32-TUM-32-4-DC24。

【模块功能】

1.  销售订单明细行上，产品录入时候的产品搜索增强。1) 以空格分隔，乱序搜索产品name字段；2) 以空格分隔，按序搜索产品default_code字段；3) 以空格分隔，按序搜索客户或供应商的product_code、product_name字段。上述3个搜索条件是 OR 的关系

2.  产品列表画面上，产品搜索功能增强。1)  以空格分隔，乱序搜索产品name字段；2)  如果没有搜到合适产品，再以空格分隔，按序搜索产品default_code字段；3)  如果没有搜到合适产品，再以空格分隔，按序搜索客户或供应商的product_code、product_name字段；

【功能截图】

![[2-product-name-search-split-3559-51fbfb70.png]]

![[2-product-name-search-split-3559-9ff81b9c.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
