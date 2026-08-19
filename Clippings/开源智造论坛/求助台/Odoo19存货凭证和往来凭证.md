---
title: "Odoo19存货凭证和往来凭证"
source: "http://www.thinkltd.cn/forum/1/odoo19-4090"
forum: "求助台"
author: "葛忠彪"
published: 2026-01-18
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo19存货凭证和往来凭证

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:葛忠彪 | 2026-01-18
> <http://www.thinkltd.cn/forum/1/odoo19-4090>

Odoo19简化了存货凭证，同时延迟了采购定价，即采购入库无需先计入暂估再结转到应付，而是创建供应商账单时借 库存 贷 应付（同时以此金额更新stock.move上的value），以及销售出库无需先计入发出商品再结转主营业务成本，而是确认客户结算单时直接 借主营业务成本 贷 库存商品，这样一来会带来以下问题

国内制造型企业，往往收到货后，物权发生了转移，但是迟迟不和供应商对账、不让供应商开票，而是等物料投入生产，发货前成品验收，此时才和供应商对账，距入库往往可能已经过去几个月甚至将近1年，这段时间内没有任何存货凭证

从审计角度上述做法是会出现问题的，DTT已经初步确认

经过调查，odoo19存货凭证，是基于stock.move产生 代码在 addons\stock_account\models\[stock_move.py](https://stock_move.py) 第156 方法 _get_account_move_line_vals，当源位置上配置了科目时 借 产品大类上的存货科目 贷 源位置上的科目；当源位置上没有配置科目时（这里直接else而没有判断目的位置是否配置科目） 借 目的位置上配置的科目 贷 产品大类上的存货科目，同时还调查了供应商账单、客户结算单上科目取值方法（参考下文）
所以可以尝试以下改动，凭证效果和18以前开启saxon是一致的，因为只改动了科目取值逻辑没有修改金额取值逻辑，所以应该风险不大（仅供参考）

1.公司上把saxon显示出来，打钩，或者服务器动作刷成True
2.公司上库存日记账显示出来，配置成库存计价
3.库存-位置，把供应商位置、客户位置的类型先设置成损失，此时会显示科目配置，供应商配置成应付暂估，客户配置成发出商品，配置完科目后再把类型改回供应商、客户
4.代码修改
stock_account\models\[account_move.py](https://account_move.py) 114行左右，saxon环境下客户结算单结转成本时的贷方分录科目
stock_account = line.move_id.partner_id.property_stock_customer.valuation_account_id
# accounts['stock_valuation']

stock_account\models\[account_move_line.py](https://account_move_line.py) 27行左右，saxon环境下供应商账单借方分录
line.account_id = [line.move_id.partner_id.property_stock_supplier.valuation_account_id.id](https://line.move_id.partner_id.property_stock_supplier.valuation_account_id.id)
# accounts['stock_valuation']

## 补充/答案 1

可以不用改代码的方式实施，具体如下：

![[1-odoo19-4090-d08c0797.png]]

产品类别上【stock varilation】可以统一配置暂估存货

![[1-odoo19-4090-113cdeb0.png]]

开启永续方式，在会计/审计/库存计价的菜单下，可以看到如下的结果：

![[1-odoo19-4090-8ff644ec.png]]

会计里针对这些中间科目的账，可以按月到会计【审计】里面去跑这些中间科目的挂账即可：

![[1-odoo19-4090-633012d2.png]]

![[1-odoo19-4090-a29ca068.png]]

![[1-odoo19-4090-ee666841.png]]

该报表可以按月跑相关的存货分录：

![[1-odoo19-4090-bc70cd01.png]]

![[1-odoo19-4090-d9ecf95f.png]]

当客户发票确认时，再看这张报表，发出商品科目就会余额减少，同理，供应商账单如果正常开具后，应付暂估在图上是暂收存货科目中会减少。

![[1-odoo19-4090-65043da4.png]]

![[1-odoo19-4090-e9b020d1.png]]

当启用的标准的中国会计准则，并且开启了永续自动的存货计价模式，会自动按以前版本的saxson模式在客户发票节点结转主营业务成本，并且又不会产生多余的发出商品和应付暂估中间科目的会计账，这些中间科目仅在存货库存估值报表里体现。

而且在【会计/配置/设置】里库存计价开启了永续自动的情况下，存货比如MO的消耗原材料的凭证，不再是以前版本的一个产品一张凭证，而是合在一张单据上，同时也有按产品分开计算，很清晰。

![[1-odoo19-4090-251ed4ef.png]]

![[1-odoo19-4090-c0f518b1.png]]

如果有生产人工费用，也会在月凭证时汇总生成：

![[1-odoo19-4090-bee71b26.png]]

需要特别注意的是：

如果MO完成了，事后解锁修改过消耗的原料数量，导致产成品或原料消耗的价值有变动的情况下，需要人工在改动的产品相关的【库存移动】记录里，同步调整操作一下【调整估值】，这样在会计库存计价报表上及再结转生成的存货凭证里才能更新这些价值，客户发票再确认过账结转的主营业务成本才会是用的修正后的成本价值，这样一来，比以前的版本改进了很多，至少出现错误，可以由人工进一步干预处理即可。

![[1-odoo19-4090-ae7c9a1b.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
