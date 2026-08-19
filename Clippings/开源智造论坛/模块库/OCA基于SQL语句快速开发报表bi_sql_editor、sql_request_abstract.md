---
title: "OCA基于SQL语句快速开发报表bi_sql_editor、sql_request_abstract"
source: "http://www.thinkltd.cn/forum/2/ocasqlbi-sql-editorsql-request-abstract-2995"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA基于SQL语句快速开发报表bi_sql_editor、sql_request_abstract

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocasqlbi-sql-editorsql-request-abstract-2995>

可以不要该模块了，该模块功能被更好的模块替代了：[带参数SQL语句抽取数据直接导出到Excel模块sql_export](http://www.thinkltd.cn/forum/2/question/sqlexcelsql-export-3485)

模块链接：

依赖模块：

Odoo 12.0版链接：

Odoo 13.0版修改：

1.  12.0版的代码，将 .py 文件中的 @api.multi 都删除（可以批量替换）

2.  文件 bi_sql_editor\models\bi_sql_view.py 方法 def _instanciate 中， pycompat.to_native 修改成 pycompat.to_text

上述两处修改后，Odoo 13.0可以正常使用。

This module extends the functionality of reporting, to support creation of extra custom reports. It allows user to write a custom SQL request. (Generally, admin users)

Once written, a new model is generated, and user can map the selected field with odoo fields. Then user ends the process, creating new menu, action and graph view.

Technically, the module create SQL View (or materialized view, if option is checked). Materialized view duplicates datas, but request are fastest. If materialized view is enabled, this module will create a cron task to refresh the data).

By default, users member of 'SQL Request / User' can see all the views. You can specify extra groups that have the right to access to a specific view.

###

### Warning

This module is intended for technician people in a company and for Odoo integrators.

It requires the user to know SQL syntax and Odoo models.

If you don't have such skills, do not try to use this module specially on a production environment.

###

### Use Cases

this module is interesting for the following use cases

- You want to realize technical SQL requests, that Odoo framework doesn't allow (For exemple, UNION with many SELECT) A typical use case is if you want to have Sale Orders and PoS Orders datas in a same table
- You want to customize an Odoo report, removing some useless fields and adding some custom ones. In that case, you can simply select the fields of the original report (sale.report model for exemple), and add your custom fields
- You have a lot of data, and classical SQL Views have very bad performance. In that case, MATERIALIZED VIEW will be a good solution to reduce display duration

####

#### Installation

- You must put this module as server_wide_modules in your odoo configuration file or add '--load=bi_sql_editor' if you start odoo in command line.

####

#### Configuration

To configure this module, you need to:

- Go to Settings / Technical / Database Structure / SQL Views

- tip your SQL request

- Select the group(s) that could have access to the view

- Click on the button 'Clean and Check Request'

- Once the sql request checked, the module analyses the column of the view, and propose field mapping. For each field, you can decide to create an index and set if it will be displayed on the pivot graph as a column, a row or a measure.

- Click on the button 'Create SQL View, Indexes and Models'. (this step could take a while, if view is materialized)

- If it's a MATERIALIZED view:

  > - a cron task is created to refresh the view. You can so define the frequency of the refresh.
  > - the size of view (and the indexes is displayed)

- Finally, click on 'Create UI', to create new menu, action, graph view and search view.

####

#### Usage

To use this module, you need to:

1.  Go to 'Reporting' / 'Custom Reports'
2.  Select the desired report

- You can switch to 'Pie' chart or 'Line Chart' as any report,

## 补充/答案 1

![[2-ocasqlbi-sql-editorsql-request-abstract-2995-944e3229.png]]

这个写的查询报表的库存按位置看价值的功能，有加载更新在了哪里呢？可以直接拿来用吗？

## 补充/答案 2

需要确认一下：

这个语句依stock moves得到库存库位相应的价值，这个剩余价值，是否与会计科目的库存价值余值，理论上应当是可以相等的吧？可以这么理解的，对吧？

如果出现了差异，会计账上会补上差异，

入的和出的实时产生的凭证也是依这个move来的。

## 补充/答案 3

补充：该功能有个问题需要补充

报表数据并非实时的，而是通过【安排的动作】来操作刷新的，安排的动作不能设太密，且用户需要查看的时候，又需要admin才能来刷新，很不方便。

故有补充界面配置：

增加一个服务器动作：

![[2-ocasqlbi-sql-editorsql-request-abstract-2995-8c6e084f.png]]

对象到bi.sql.view

执行代码段示例：

model.sudo()._refresh_materialized_view_cron([1]) action = { 'name': '含批次_查看历史库存', 'type': 'ir.actions.act_window', 'view_mode': 'tree', 'res_model': 'x_bi_sql_view.stock_q2', }

然后增加了一个可以配置权限或用户可以在【库存】菜单下可以点击的菜单

![[2-ocasqlbi-sql-editorsql-request-abstract-2995-b44b97d2.png]]

![[2-ocasqlbi-sql-editorsql-request-abstract-2995-2d56eec3.png]]

点这个菜单按钮就能跳转到查询批次库存的报表中。

这个只是示例的报表数据。

## 补充/答案 4

库存数量和价值在同一张表，依stock move唯度分析，内部位置剩余的数量和价值

默认取move的数量，依据来源位置类型是内部位置，数量为负，目的位置是内部位置，数量为正，金额统一取move上的value值，先绝对值再判断来源或目的的正负符号。

示例：

select stock_move.id as x_id, PP.default_code as x_code, PP.name as x_name, date as x_date, value as x_value, product_uom_qty as x_qty, stock_location.name as x_location from stock_move left join stock_location on stock_move.location_dest_id = stock_location.id left join (select product_product.id as pid, product_product.default_code, name, type, product_product.active as active from product_product left join product_template on product_product.product_tmpl_id = product_template.id ) PP on stock_move.product_id = PP.pid where state = 'done' and stock_location.usage = 'internal' and PP.type = 'product' and PP.active = 't' union select stock_move.id as x_id, PP.default_code as x_code, PP.name as x_name, date as x_date, -abs(value) as x_value, -product_uom_qty as x_qty, stock_location.name as x_location from stock_move left join stock_location on stock_move.location_id = stock_location.id left join (select product_product.id as pid, product_product.default_code, name, type, product_product.active as active from product_product left join product_template on product_product.product_tmpl_id = product_template.id ) PP on stock_move.product_id = PP.pid where state = 'done' and stock_location.usage = 'internal' and PP.type = 'product' and PP.active = 't'

![[2-ocasqlbi-sql-editorsql-request-abstract-2995-37275a5a.png]]

![[2-ocasqlbi-sql-editorsql-request-abstract-2995-c4abee78.png]]

## 补充/答案 5

11.0的模块绝大多数可以直接在12.0用。这个模块12.0我没测试过，应该可以直接安装使用。

## 补充/答案 6

这个模块11的不能直接安装在12的环境上我试过了。

但是有12版本的下载的。

select SM.location_dest_id as x_loc_id, SM.product_id as x_product_id, SM.name as x_name, SM.origin as x_origin, SM.product_uom_qty as x_qty, SM.price_unit as x_price_unit, SM.value as x_value, SM.date as x_date, LOC.company_id as x_company_id, SM.lot_id as x_lot_id, SM.categ_id as x_categ_id from stock_location LOC right join (select SM.location_id,SM.location_dest_id,SM.product_id,SM.name,SM.origin,Sl.qty_done as product_uom_qty, case when SM.price_unit is null then 0.0 else SM.price_unit end as price_unit, case when SM.price_unit is null then 0.0 else SM.price_unit * Sl.qty_done end as value, SM.date, sl.lot_id as lot_id , pt.categ_id as categ_id, pt.type as type from stock_move SM left join stock_move_line sl on sl.move_id = SM.id left join stock_production_lot lot on sl.lot_id = lot.id left join product_product pp on pp.id = SM.product_id left join product_template pt on pp.product_tmpl_id = pt.id and pt.type ='product' left join product_category pc on pc.id = pt.categ_id where SM.state='done' ) SM on (LOC.id=SM.location_dest_id) where LOC.usage = 'internal' and SM.type = 'product' union all select SM.location_id as x_loc_id, SM.product_id as x_product_id, SM.name as x_name, SM.origin as x_origin, -SM.product_uom_qty as x_qty, SM.price_unit as x_price_unit, SM.value as x_value, SM.date as x_date, LOC.company_id as x_company_id, SM.lot_id as x_lot_id, SM.categ_id as x_categ_id from stock_location LOC right join (select SM.location_id,SM.location_dest_id,SM.product_id,SM.name,SM.origin,Sl.qty_done as product_uom_qty, case when SM.price_unit is null then 0.0 else SM.price_unit end as price_unit, case when SM.price_unit is null then 0.0 else SM.price_unit * Sl.qty_done end as value, SM.date, sl.lot_id as lot_id , pt.categ_id as categ_id, pt.type as type from stock_move SM left join stock_move_line sl on sl.move_id = SM.id left join stock_production_lot lot on sl.lot_id = lot.id left join product_product pp on pp.id = SM.product_id left join product_template pt on pp.product_tmpl_id = pt.id and pt.type ='product' left join product_category pc on pc.id = pt.categ_id where SM.state='done' ) SM on (LOC.id=SM.location_id) where LOC.usage = 'internal' and SM.type = 'product'

## 补充/答案 7

该方法中导致的问题，比较典型的异常：

![[2-ocasqlbi-sql-editorsql-request-abstract-2995-dcc0804f.png]]

而move上是正数：

![[2-ocasqlbi-sql-editorsql-request-abstract-2995-6bad4f3a.png]]

实际上这张sql拼写的报表的value金额应当直接取move上的value，而不应当另外计算，但正负符号是否也能直接拿Move的呢？


## 原帖外链配图

![[2-ocasqlbi-sql-editorsql-request-abstr-xa050826d.png]]
<small>原始地址: https://github.com/OCA/reporting-engine/raw/11.0/bi_sql_editor/static/description/01_sql_request.png</small>

![[2-ocasqlbi-sql-editorsql-request-abstr-x3531b6c6.png]]
<small>原始地址: https://github.com/OCA/reporting-engine/raw/11.0/bi_sql_editor/static/description/02_security_access.png</small>

![[2-ocasqlbi-sql-editorsql-request-abstr-xdb0904d7.png]]
<small>原始地址: https://github.com/OCA/reporting-engine/raw/11.0/bi_sql_editor/static/description/03_field_mapping.png</small>

![[2-ocasqlbi-sql-editorsql-request-abstr-x5637d81b.png]]
<small>原始地址: https://github.com/OCA/reporting-engine/raw/11.0/bi_sql_editor/static/description/04_materialized_view_setting</small>

![[2-ocasqlbi-sql-editorsql-request-abstr-x5e82e0fc.png]]
<small>原始地址: https://github.com/OCA/reporting-engine/raw/11.0/bi_sql_editor/static/description/05_reporting_pivot.png</small>

![[2-ocasqlbi-sql-editorsql-request-abstr-x33f1f104.png]]
<small>原始地址: https://github.com/OCA/reporting-engine/raw/11.0/bi_sql_editor/static/description/05_reporting_pie.png</small>

![[2-ocasqlbi-sql-editorsql-request-abstr-x194038c2.png]]
<small>原始地址: /web/image/1421/snipaste_20190303_161425.png?access_token=90531882-e414-4de8-bf6e-0f0acfba40e4</small>

![[2-ocasqlbi-sql-editorsql-request-abstr-x194038c2.png]]
<small>原始地址: /web/image/1423/snipaste_20190303_162006.png?access_token=4acb57c3-b263-4459-a590-53f4a46a20f5</small>

![[2-ocasqlbi-sql-editorsql-request-abstr-x194038c2.png]]
<small>原始地址: /web/image/1425/snipaste_20190303_162058.png?access_token=eac36c01-fcd6-4db3-9a3f-18fb3de70844</small>

![[2-ocasqlbi-sql-editorsql-request-abstr-x194038c2.png]]
<small>原始地址: /web/image/1427/snipaste_20190303_162542.png?access_token=f1ace21e-c148-4df2-ada7-f252713eb8b8</small>

![[2-ocasqlbi-sql-editorsql-request-abstr-x194038c2.png]]
<small>原始地址: /web/image/1429/snipaste_20190303_162741.png?access_token=1a95e1c3-cf34-49b6-b6ef-dcfc176b0e46</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
