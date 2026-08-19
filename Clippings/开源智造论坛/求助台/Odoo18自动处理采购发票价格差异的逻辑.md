---
title: "Odoo18自动处理采购发票价格差异的逻辑"
source: "http://www.thinkltd.cn/forum/1/odoo18-4012"
forum: "求助台"
author: "肖相扶"
published: 2025-01-08
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo18自动处理采购发票价格差异的逻辑

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2025-01-08
> <http://www.thinkltd.cn/forum/1/odoo18-4012>

【业务背景】

1.  采购业务中，收货时候由于质量瑕疵导致的让步接收，会出现开票价格（结算价格）低于采购发票的情况。例如采购价格为10元，开票价格为9元。
2.  如果计价方式为移动加权平均，采购入库时候，系统用10元的价格计算产品成本价格（自动修改产品上的成本价格字段）。
3.  采购发票确认时候，由于实际结算价格为9元，产品的成本价格应该用9元进行修正，同时库存价值也应该用9元进行修正（减少库存价值）。
4.  经测试Odoo18会自动完成上述处理。也即，采购发票确认时候，系统一方面生成一笔差异库存计价(stock.valuation.layer)，减少库存价值。同时用差异价格重新计算产品成本价格，修正产品上的成本价格字段。
5.  如果采购发票确认时候，采购入库的数量有一部分已经出库了。例如，初始库存为零，以10元价格采购10件，采购入库10件，再销售出库2件。而后收到采购发票，单价9元，确认发票。此时系统产生一笔 -8 元的库存计价，减少8件在库商品的价值。对于已出库的2件， 如果开启了Anglo-Saxon会计体系（不管是否开启永续）， 系统在采购发票的会计凭证中直接新增一笔贷记出库科目的分录，参考下面测试截图。如果没开启 Anglo-Saxon会计体系，则对于已经出库了的2件，系统不生成会计分录。
6.  【注意系统有点Bug】对于已出库的两件，采购发票的会计分录中，如果开启了永续，一方科目取自入库科目，一方科目取自费用科目。如果没有开启永续，则两方科目都取自费用科目。正确的做法，应该一方取自出库科目，另一方取自入库科目（永续）或者费用科目（非永续）。对应修改代码文件 OSCGODOO18\source\addons\purchase_stock\models\account_move_line.py，方法 def _prepare_pdiff_aml_vals中的代码行：expense_account = self.product_id.product_tmpl_id.get_product_accounts(fiscal_pos=self.move_id.fiscal_position_id)['expense']，改成 expense_account = self.product_id.product_tmpl_id.get_product_accounts(fiscal_pos=self.move_id.fiscal_position_id)['stock_output']，即取出库科目。

【测试截图】

测试案例：1) 初始库存为零；2) 以10元价格采购10件，采购入库10件; 3) 再销售出库2件；4) 而后收到采购发票，单价9元，确认发票。

上述操作以后，系统生成的  库存计价(stock.valuation.layer)及采购发票的会计分录如下：

会计科目配置如下：

![[1-odoo18-4012-cdd44495.png]]

系统生成的库存计价如下：

![[1-odoo18-4012-cfe3220b.png]]

采购发票对应的会计凭证如下：

![[1-odoo18-4012-6f5aa43e.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
