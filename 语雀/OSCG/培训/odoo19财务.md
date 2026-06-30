---
title: "odoo19财务"
type: 培训材料
phase: 上线期
yuque_url: "https://www.yuque.com/xinsuixiaoyao-degek/klxky6/dbwtbkmrf45wiuui"
yuque_slug: "dbwtbkmrf45wiuui"
tags: [Odoo, 上线期, 培训, 财务]
created_at: "2025-11-17T13:05:50.000Z"
updated_at: "2025-11-17T13:20:30.000Z"
published_at: "2025-11-17T13:20:30.000Z"
---
# odoo19财务

1、公司上的anglo_saxon_accounting字段放出来，标记为true,account_stock_journal_id配置成库存计价

<field name="anglo_saxon_accounting"/>

<field name="account_stock_journal_id"/>

2、库存-位置，把供应商位置、客户位置的类型先设置成损失，此时会显示科目配置，供应商配置成应付暂估，客户配置成发出商品，配置完科目后再把类型改回供应商、客户

3、产品类别上设置库存商品科目

4、修改代码

stock_account\models\[account_move.py](https://account_move.py/) 114行左右，saxon环境下客户结算单结转成本时的贷方分录科目
stock_account = line.move_id.partner_id.property_stock_customer.valuation_account_id
# accounts['stock_valuation']

stock_account\models\[account_move_line.py](https://account_move_line.py/) 27行左右，saxon环境下供应商账单借方分录
line.account_id = [line.move_id.partner_id.property_stock_supplier.valuation_account_id.id](https://line.move_id.partner_id.property_stock_supplier.valuation_account_id.id/)
# accounts['stock_valuation']
