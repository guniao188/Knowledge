---
title: "二开销售对账/客户对账/采购对账/供应商对账模块sale_fapiao、purchase_fapiao"
source: "http://www.thinkltd.cn/forum/2/sale-fapiaopurchase-fapiao-3422"
forum: "模块库"
author: "肖相扶"
published: 2024-11-13
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开销售对账/客户对账/采购对账/供应商对账模块sale_fapiao、purchase_fapiao

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-11-13
> <http://www.thinkltd.cn/forum/2/sale-fapiaopurchase-fapiao-3422>

模块链接：

销售对账 OSCG_SVN\odoo_ecommerce\14.0SRC\销售采购对账\sale_fapiao

采购对账 OSCG_SVN\odoo_ecommerce\14.0SRC\销售采购对账\purchase_fapiao

18版本链接：

[采购对账    https://gitlab.com/oscg-china/extra-addons/-/tree/18.0/purchase_fapiao](https://gitlab.com/oscg-china/extra-addons/-/tree/18.0/purchase_fapiao)销售对账    [https://gitlab.com/oscg-china/extra-addons/-/tree/18.0/sale_fapiao](https://gitlab.com/oscg-china/extra-addons/-/tree/18.0/sale_fapiao)

【业务背景/模块功能】

客户对账界面显示销售订单明细行（Sale Order Line），显示字段包括：订单号，客户，客户订单号码（默认Hide），产品（默认Hide），明细行说明，订单单价，订单数量，已经发货的数量，已开票的数量，对账数量（发给客户对账的数量，或者和客户对账确定的开票数量），开票状态，订单状态（默认Hide）

 实际操作步骤是：

1.  每月按客户筛选未开票的订单明细，按产品汇总，导出汇总值，及明细数据到Excel，手工整理成客户对账单，发给客户

2.  导出前，可以按点击服务器动作“默认对账数”，将系统的待开票数量自动复制到“对账数”，而后可以手工修改“对账数”

3.  客户确认后，勾选对应明细行，动作下面点击“对账后开票”，系统按“对账数”创建客户发票。注意一次只能勾选一个客户的明细行，不可以多个客户的销售明细混合勾选

4.  如果客户对账有疑义，和客户沟通达成一致后，修改系统的“对账数”，客户发票的备注或Message区域注明修改事项及修改原因，方便财务审核及日后备查

5.  财务复核系统的客户发票，开具实际税务发票，寄予客户

【功能截图】

![[2-sale-fapiaopurchase-fapiao-3422-10489aca.png]]

## 补充/答案 1

模块安装后，点击客户对账报错。

![[2-sale-fapiaopurchase-fapiao-3422-dc8a3c16.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
