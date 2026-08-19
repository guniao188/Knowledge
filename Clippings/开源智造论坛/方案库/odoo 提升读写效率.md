---
title: "odoo 提升读写效率"
source: "http://www.thinkltd.cn/forum/3/odoo-3661"
forum: "方案库"
author: "施叶寒"
published: 2023-03-31
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# odoo 提升读写效率

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:施叶寒 | 2023-03-31
> <http://www.thinkltd.cn/forum/3/odoo-3661>

已创建出入库为例

1. 创建表单的同时批量创建明细
picking = self.env['stock.picking'].create(picking_values)
for line_values in line_values_list:
line_values.update({'picking_id'[:picking.id})](https://:picking.id%7D))
self.env['[stock.move.line'].create(line_values)](https://stock.move.line&#39;%5D.create(line_values))
=>
picking_values.update({
'move_line_ids': [(0,0,line_values) for line_values in line_values_list]
})
self.env['stock.picking'].create(picking_values)
------

2. 移除数据库约束
_sql_constraints = [
('name_ref_uniq', 'unique (name, product_id, company_id)', 'The combination of serial number and product must be unique across a company !'),
]
=>
alter table stock_production_lot
drop constraint stock_production_lot_name_ref_uniq
------

3. 更少地使用内存对象
code_product_dict = {
code: self._find_product(code)
for code in set(codes)}
for code in codes:
product = code_product_dict[code]
=>
for code in codes:
product = self._find_product(code)
------

4. 手写sql
lots =
self.env['[stock.production.lot'].search([('name','=','Lot1')])](https://stock.production.lot&#39;%5D.search(%5B(&#39;name&#39;,&#39;=&#39;,&#39;Lot1&#39;)%5D))
lots.write({'is_active':False})
=>
[self.env.cr.execute('''UPDATE](https://self.env.cr.execute(&#39;&#39;&#39;UPDATE) stock_production_lot SET is_active=false WHERE name='Lot1' AND company_id=1;''')
------

![[3-odoo-3661-e8552892.png]]

------

![[3-odoo-3661-4140e566.png]]

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
