---
title: "二开采购发票差异金额分摊模块stock_landed_costs_improved"
source: "http://www.thinkltd.cn/forum/2/stock-landed-costs-improved-3295"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开采购发票差异金额分摊模块stock_landed_costs_improved

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/stock-landed-costs-improved-3295>

模块链接：OSCG_SVN\odoo_ecommerce\13.0SRC\存货核算\stock_landed_costs_improved

**2021/12/04更新**

模块升级到了Odoo 14.0：OSCG_SVN\odoo_ecommerce\14.0SRC\存货核算\stock_landed_costs_improved

1.  新增功能：采购退货时候，如果是移动加权平均，则重新计算产品成本价格（退回到采购入库前的价格）

2.  Bug修正：发票差异的分摊单，验证时候，自动产生会计分录，借记/贷记 库存商品，贷记/贷记 材料差异，如果分摊的商品已经销售出库，还产生出库分录（如 借记 主营业务成本 或 发出商品）

【模块功能】

1) 成本分摊单上增加分摊类型字段，常见类型包括：采购发票差异金额分摊，进口关税分摊，个别分摊/包裹分摊，其他分摊
2) 供应商账单上增加发票价格和采购价格差异判断，如果有差异，允许创建差异分摊单（显示成本分摊单创建按钮），点击按钮，自动计算差异金额，添加到成本分摊单。
3) 成本分摊单上，如果是采购差异金额分摊，系统自动载入差异发票行对应的Stock Move，进行差异金额分摊。
4) 注意：采购发票差异金额分摊功能，仅对移动加权平均，和FIFO成本法有效。

## 补充/答案 1

【功能截图】

![[2-stock-landed-costs-improved-3295-d1895d60.png]]

![[2-stock-landed-costs-improved-3295-0e1827de.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
