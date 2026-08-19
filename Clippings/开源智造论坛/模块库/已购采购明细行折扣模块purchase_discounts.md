---
title: "已购采购明细行折扣模块purchase_discounts"
source: "http://www.thinkltd.cn/forum/2/purchase-discounts-2783"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 已购采购明细行折扣模块purchase_discounts

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/purchase-discounts-2783>

模块介绍链接：

模块下载链接（如果链接过期请找购买人 King 重发下载链接）：

## 补充/答案 1

已开发改版，因考虑到PO折扣的话， 会导致PO入库的成本价值的计算是折扣前的，而非折扣后的实际成本。

故重新有改版和开发处理，更新后的模块代码存放在：V14版本，这个改后的版本有考虑到了成本的影响，所以控制在折扣后，来吻合系统原生的计算逻辑。供应商价格表有相互反算供应商原有的单价。

D:\svn\SVN\odoo_ecommerce\06.Customization\fortune living\addons

更改成系统原有的【单价】字段为折扣后的值，增加【原价】【折扣】的计算，通过供应商价格表带出原价和折扣。

![[2-purchase-discounts-2783-1b0f0833.png]]

![[2-purchase-discounts-2783-ce32d6c2.png]]

![[2-purchase-discounts-2783-f15e15d6.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
