---
title: "公司错配：公司属性字段关联到其他公司记录导致的无权访问错误的查错SQL"
source: "http://www.thinkltd.cn/forum/1/sql-850"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 公司错配：公司属性字段关联到其他公司记录导致的无权访问错误的查错SQL

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/sql-850>

【业务背景】

1.  Vital家，业务伙伴Partner 上配置的价格表，存在一些公司错配的数据： A公司的价格表属性字段，配置的却是B公司的价格表；

2.  下面SQL语句，基于公司属性表(ir_property)，查询属性字段的公司、价格表的公司不一致的记录

3.  实际应用时候，查找的模型不同，或者属性字段不同的时候，需要适当修改一下SQL才能使用。

-- Partner上的公司，价格表上的公司，属性表上的公司，三者不一致的数据抓取。三者不一致会导致Odoo多公司权限错误

select IP.id, IP.res_id, IP.value_reference, RP.company_id as partner_company, IP.company_id as property_company, PR.company_id as price_company

from ir_property IP

left join res_partner RP on (RP.id = cast(split_part(IP.res_id, ',', 2) as integer) )

left join product_pricelist PR on (PR.id = cast(split_part(IP.value_reference, ',', 2) as integer) )

where IP.name = 'property_product_pricelist' and

-- 情况一：Partner上有公司，但价格表上的公司不同于Partner的公司

(not RP.company_id is null and not PR.company_id is null and RP.company_id <> PR.company_id);

-- 情况二：Partner上有公司，但属性表上的公司不同于Partner的公司

(not RP.company_id is null and not IP.company_id is null and RP.company_id <> IP.company_id);

-- 情况三：Partner上没有公司，价格表上有公司，属性表上有公司，但价格表上的公司不同于属性表的公司

(RP.company_id is null and not PR.company_id is null and not IP.company_id is null and IP.company_id <> PR.company_id);

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
