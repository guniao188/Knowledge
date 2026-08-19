---
title: "Partner地址增加中国省市区模块base_cn_address"
source: "http://www.thinkltd.cn/forum/2/partnerbase-cn-address-3286"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Partner地址增加中国省市区模块base_cn_address

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/partnerbase-cn-address-3286>

模块位置：  OSCG_SVN\odoo_ecommerce\13.0SRC\base_cn_address

OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\base_cn_address

【模块功能】

1.  该模块增加了中国省市区维护表，模块下面有文件“2019行政区划数据库”可以导入到系统

2.  在Partner上，如果国家选择中国，则显示省市区三个字段，填写省的时候，系统背后字段补填Odoo自带的省份字段（state_id），填写市的时候，系统背后自动补填Odoo 城市 city 字段，填写区的时候，系统自动补填 Street字段。如果选择其他国家，则显示Odoo原有的地址格式（不显示省市区三个联动字段）。方便中国地址填写的同时，保留Odoo的国际兼容性。

【功能截图】

![[2-partnerbase-cn-address-3286-76092588.png]]

![[2-partnerbase-cn-address-3286-710bb576.png]]

![[2-partnerbase-cn-address-3286-de86f1f8.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
