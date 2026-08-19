---
title: "IT行业采购硬件安装软件服务管理案例实现技术分析"
source: "http://www.thinkltd.cn/forum/3/it-3827"
forum: "方案库"
author: "肖相扶"
published: 2023-12-14
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# IT行业采购硬件安装软件服务管理案例实现技术分析

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:肖相扶 | 2023-12-14
> <http://www.thinkltd.cn/forum/3/it-3827>

【业务背景】

1.  新疆乾坤信息技术公司，IT系统机床服务。项目签订后，各技术部门负责本部门的产品交付，交付流程是：采购硬件（电脑、服务器等），安装软件，发往客户，现场安装调试。
2.  提供给客户的业务解决方案是：
3.  1.  SO明细行上销售A型电脑
```python
    2.  A型电脑有一个套件BoM，包含A型电脑(未装软件)，以及服务型产品“软件安装”。 A型电脑(未装软件)设置成MTO
    3.  如此，SO确认时候，系统展开套件BoM，生成销售发货单，发货“ A型电脑(未装软件) ”，以及采购订单，采购“ A型电脑(未装软件) ”。
    4.  但还希望，系统能够自动生成“软件安装”的项目任务（project.task），该如何实现？
```

【技术实现分析】

1.  销售带有套件BoM的产品，SO确认时候，系统背后的代码逻辑是：
2.  文件 sale_stock\models\sale_order_line.py，方法 _action_launch_stock_rule ，该方法查找产品的补货路线，运行补货路线对应的补货方法。本例中的A型电脑，补货路线是制造，对应的调用 制造的补货方法。
3.  制造补货方法参见文件 mrp\models\stock_rule.py，方法 def run 。该方法中，首先分析是套件BoM产品，展开套件BoM，调用套件BoM中每个BoM行的产品的补货方法。
4.  非套件BoM的补货方法参见文件 stock\models\stock_rule.py 方法  def run 。该方法中，首先过滤了 sevice类型的产品，只对可库存商品，和消耗型商品运行补货方法，产生Picking、Purchase、Production等类型的补货单据
5.  可以继承 文件 stock\models\stock_rule.py 方法  def run ，增加一段代码，针对服务型产品，自动创建项目任务（project.task）
6.  创建项目任务，可以参考文件 sale_project\models\sale_order_line.py 方法_timesheet_create_task
7.  附录：运行补货方法 run的参数 [(Procurement(product_id=product.product(42,), product_qty=1.0, product_uom=uom.uom(1,), location_id=stock.location(5,), name='套件产品01', origin='S00009', company_id=res.company(1,), values={'group_id': procurement.group(9,), 'sale_line_id': 13, 'date_planned': datetime.datetime(2023, 12, 14, 4, 6, 28), 'date_deadline': datetime.datetime(2023, 12, 14, 4, 6, 28), 'route_ids': stock.route(), 'warehouse_id': stock.warehouse(1,), 'partner_id': 8, 'product_description_variants': '', 'company_id': res.company(1,), 'product_packaging_id': product.packaging(), 'sequence': 10, 'bom_line_id': 1, 'priority': '0'}), stock.rule(5,))]

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
