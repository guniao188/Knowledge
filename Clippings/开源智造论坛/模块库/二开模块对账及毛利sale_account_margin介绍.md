---
title: "二开模块对账及毛利sale_account_margin介绍"
source: "http://www.thinkltd.cn/forum/2/sale-account-margin-2505"
forum: "模块库"
author: "肖相扶"
published: 2022-12-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开模块对账及毛利sale_account_margin介绍

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-16
> <http://www.thinkltd.cn/forum/2/sale-account-margin-2505>

模块存放位置：OSCG_SVN\odoo_ecommerce\11.0SRC\进销存\sale_account_margin

Odoo14.0中，此模块废弃，拆成下面三个模块：

销售对账/采购对账：[/forum/2/question/sale-fapiaopurchase-fapiao-3422](http://www.thinkltd.cn/forum/2/question/sale-fapiaopurchase-fapiao-3422)

销售毛利：

销售对账
---
    * 开票 | 销售 | 文档 下面增加菜单“客户对账”,该菜单显示状态为['sale', 'done'] 的 sale.order.line，显示字段包括：订单号、客户、客户订单号、产品、单位、订单数量、发货数量、开票数量、发货日期、开票日期
    * 客户对账界面，导出数据到Excel（模块 web_export_view，[参考/forum/2/question/ocaweb-export-view-2508](http://www.thinkltd.cn/forum/2/question/ocaweb-export-view-2508)）作成客户对账单
    * 客户对账界面，增加功能：勾选销售明细行创建客户发票

供应商对账
---
    * 开票 | 采购 | 文档 下面增加菜单“供应商对账”,该菜单显示状态为['purchase', 'done'] 的 purchase.order.line，显示字段包括：订单号、供应商、供应商订单号、产品、单位、订单数量、收货数量、收票数量
    * 供应商对账界面，导出数据到Excel（模块 web_export_view）作成供应商对账单

销售毛利分析
---
    * 继承 sale.order.line 增加字段：成本价(cost_price)，成本金额(cost_amount)，毛利金额（margin_amount），发货日期(delivery_date)，账期(receivable_date)，到款金额(receive_amount)，到款日期(receive_date) 。
    * 开票 | 销售 | 文档 下面增加菜单“毛利分析”,该菜单显示状态为['sale', 'done'] 的 sale.order.line
    * sale.order.line 增加Wizard “销售成本更新”,该Wizard更新 sale.order.line 的下述字段：成本价(cost_price)，成本金额(cost_amount)，发货日期(delivery_date)，账期(receivable_date)，到款金额(receive_amount)，到款日期(receive_date)。更新逻辑如下：
```python
     成本价(cost_price)：取 move_ids的各个stock.move的price_unit及qty加权平均值
     成本金额(cost_amount)： cost_price 乘以发货数量
     发货日期(delivery_date)：move_ids 的最晚一条的date
     账期(receivable_date)：invoice_lines中，未paid的line的最早一条的到期日期
     到款金额(receive_amount)：invoice_lines中，所有已经paid的未税金额，如果是外币，按paid日期的汇率转为本位币金额
     到款日期(receive_date)：invoice_lines中，所有已经paid的line的最晚一条的付款日期
     毛利金额（margin_amount）：receive_amount 减去 cost_amount
```

## 补充/答案 1

【毛利分析功能截图】

- l  数量：SO的订单数量

- l  已发数量：SO的发货数量

- l  发货日期：SO对应的发货单的发货日期

- l  应收日期：SO对应的Invoice的应收日期，有多个Invoice的情况，取最近的那个应收日期

- l  到款金额：SO实际收到的金额，取已经Paid的Invoice的金额

- l  到款日期：SO到款的日期，多个到款的情况，取最近的到款日期

- l  成本价：SO发货产品的成本，取SO的发货单的Stock Move的成本价格（price_unit）。

- l  成本金额：发货数量 * 成本价

- l  毛利金额：到款金额– 成本金额，如果尚未到款，毛利金额为负数。

## 补充/答案 2

【对账功能截图】

- l  客户对账： 客户要货的时候，销售员做销售订单SO，给客户供货。月末，汇总当月发货明细，做成客户对账单，发与客户确认，客户确认后，开票给客户。Odoo标准功能中，缺乏客户对账的功能支持

- l  供应商对账：要货时候，给供应商发采购单PO，供应商送货，仓库验收入库。月末，供应商发来当月供货明细，甲方确认后，供应商开票过来。Odoo标准功能中，缺乏供应商对账的功能支持（面对供应商发来的对账单，甲方如何快速判断对账单是否无差错？）。

- l  Odoo标准功能是，直接基于SO开客户发票，财务审核发票。或者基于PO开供应商账单，财务审核。SO开客户发票之前，需要一个客户对账的功能，PO开账单之前，需要一个供应商对账的功能。

- l  模块sale_account_margin 补足了客户对账和供应商对账的缺陷

客户对账界面显示销售订单明细行（Sale Order Line），显示字段包括：订单号，客户，客户订单号码（默认Invisible），产品（默认Invisible），明细行说明，订单单价，订单数量，已经发货的数量，未开票的数量（待开数，指系统中尚未开客户发票的数量），发货日期（需要勾选明细行，动作里面点击“日期毛利更新”，系统取最后一次发货的Stock Move的Date日期字段），开票状态

 实际操作步骤是：

1)    每月按客户筛选未开票的订单明细，按产品汇总，（web_view_export）导出汇总值，及明细数据，手工整理成客户对账单，发给客户

2)    客户确认后，勾选对应明细行，动作下面点击“对账开票”，开具Invoice。此操作可以批量勾选，系统自动按客户合并开票

3)    如果客户对账有疑义，和客户沟通达成一致后，修改系统的客户发票数量或单价，客户发票的备注或Message区域注明修改事项及修改原因，方便财务审核及日后备查

4)    财务复核系统的客户发票，开具实际税务发票，寄予客户

 按客户及产品分组显示画面：

供应商对账：

供应商对账画面显示采购单明细行（Purchase Order Line），显示字段包括：订单号，供应商，产品，明细行说明，采购单价，订单数量，已收货数量，已经开供应商账单的数量，订单金额，开票状态。

实际操作步骤如下：

1)    收到供应商对账单，按供应商分组筛选待开票的明细行，确认产品数量、产品明细、单价、总额是否一致

2)    确认无误，通知供应商对账OK，供应商寄送税票过来

3)    收到税票，“供应商账单”画面，选择PO，创建供应商账单（可以多次选择PO合并开票）

4)    如果对账有疑义，系统的供应商账单上修改数量、单价、税率等

5)    财务复核税票


## 原帖外链配图

![[2-sale-account-margin-2505-x194038c2.png]]
<small>原始地址: /web/image/716/sm5.png?access_token=4892de22-7e92-49ce-a10b-c9497aead143</small>

![[2-sale-account-margin-2505-x194038c2.png]]
<small>原始地址: /web/image/718/sm6.png?access_token=3a3efa74-94d7-4663-baa8-b5843dd3a37b</small>

![[2-sale-account-margin-2505-x194038c2.png]]
<small>原始地址: /web/image/720/sm7.png?access_token=570b2904-d4b8-4faf-8deb-f31d51082161</small>

![[2-sale-account-margin-2505-x194038c2.png]]
<small>原始地址: /web/image/722/sm8.png?access_token=12691f54-9b78-4e34-8f70-0b27dd336181</small>

![[2-sale-account-margin-2505-x194038c2.png]]
<small>原始地址: /web/image/724/sm9.png?access_token=70b564c8-1763-44f7-a76b-0d48da10927c</small>

![[2-sale-account-margin-2505-x194038c2.png]]
<small>原始地址: /web/image/726/sm10.png?access_token=11aac86f-b806-432c-80fd-55f9a66252c7</small>

![[2-sale-account-margin-2505-x194038c2.png]]
<small>原始地址: /web/image/728/sm11.png?access_token=64db17e1-767c-4dca-b4f9-44df84e645ec</small>

![[2-sale-account-margin-2505-x194038c2.png]]
<small>原始地址: /web/image/732/sm12.png?access_token=18fbb615-edd7-48d2-b921-0f51b6de12b3</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
