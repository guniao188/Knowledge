---
title: "account_move_line_add_cost客户发票上的成本毛利计算V14"
source: "http://www.thinkltd.cn/forum/2/account-move-line-add-costv14-3544"
forum: "模块库"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# account_move_line_add_cost客户发票上的成本毛利计算V14

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/account-move-line-add-costv14-3544>

对于已经开票的产品清单，发票明细行，需要知道毛利及成本情况

开发模块：account_move_line_add_cost

V14版本存储目录：D:\svn\SVN\odoo_ecommerce\06.Customization\fortune living\addons\account_move_line_add_cost

功能开发点：

1、客户发票增加按钮【更新明细行成本】方法；

2、明细行增加了：成本单价、成本金额、利润

成本单价取值逻辑：如果发票明细行关联的so订单明细行有值并且关联的move已完成，数量不等于0，则取该明细行关联的库存计价的合计金额/合计数量得到（避免有成本分摊数量为0的情况来合并计算）

如果订单明细行关联的MOVE的库存计价数量为0，则默认取产品上的当前成本值；

有特别修复问题：成本金额的计算，如果关联的SO订单明细行同一行有多次发货，则用发票上的数量来计算；

如果有外币，则计算利润时，有加上汇率的换算；同时有考虑move_type的类型，如果是红冲退款客户发票，则计算利润的公式略有不同。

*再次修复，多计量单位的情况下，仓库的成本和产品上的成本均是以产品上的基础计量单位来计算，但INVOICE上的计量单位有可能与产品上的计量单位不一致，故还需要考虑产品的计量单位间的换算。

##增补功能：因到岸成本分摊时，有些已出货的产品的成本，是不会再生成库存计价的，故这种算成本的方法只能算到有库存计价的金额，那么就需要将到岸成本的产生的这部分已出货的补生成的会计分录，其中是【收入成本】分类的会计赁证明细行，也要计入到这张毛利清单表中，这样方便查看每个产品每个订单发票及产品最终的毛利情况。

故代码上有增加这个if判断，当是属于到岸成本分摊的类型时，让成本和毛利就等于balance的金额，不过需要将这个货币型转成float类型

另外，如果用户有成本限制需求，则需要用户自行在界面上配置该菜单明细行的汇总表，以及字段的【成本权限组】相关的限制。

界面配置：

1、增加了菜单：Margin Report

菜单动作domain限制条件：['|','&',('exclude_from_invoice_tab','=',False),('move_id.move_type','in',['out_invoice','out_refund','out_receipt']),'&',('x_is_land_cost','=',True),('account_id.user_type_id','=',17)]

意思是：只显示属于客户发票、客户退款、客户收据类型的account move line并且是属于发票明细行，而且会计赁证分录的行（系统是用exclude_from_invoice_tab这个字段来区分是这行account move line是属于发票明细行还是赁证明细行的），

或者是属于【到岸成本】分摊产生的会计分录明细行并且该行的科目类型ID为17的，即【收入成本】科目。

3、做这个限制实际上是为了找到明细行是属于到岸成本分摊产生的数据，系统原生的is_landed_costs_line只是判断供应商发票是否要分摊用的，所以在本例中有界面另外加了【布尔型字段x_is_land_cost】

![[2-account-move-line-add-costv14-3544-190f443b.png]]

4、加了该字段x_is_land_cost的自动动作来自动赋值

```python
for p in records:
  for x in p.account_move_id.line_ids:
    x.write({'x_is_land_cost':True})
```

![[2-account-move-line-add-costv14-3544-124f7252.png]]

5、有在Margin Report的菜单里，设置默认过滤器，因在菜单动作中写太复杂的并且或者关系较难，故第1点中的菜单过滤中还没有排除掉明细行是【节】或【便签】的记录，故通过默认过滤器，排除即可，叉掉过滤器也不会有什么金额上的影响

![[2-account-move-line-add-costv14-3544-0e553f62.png]]

![[2-account-move-line-add-costv14-3544-f1f195ae.png]]

条件：不等于便签类型或节类型

["|",["display_type","!=","line_section"],["display_type","!=","line_note"]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
