---
title: "Odoo18二维码收款功能解析"
source: "http://www.thinkltd.cn/forum/1/odoo18-3984"
forum: "求助台"
author: "肖相扶"
published: 2024-10-12
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo18二维码收款功能解析

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-10-12
> <http://www.thinkltd.cn/forum/1/odoo18-3984>

【功能解析】

1.  客户发票上，可以选择二维码收款方式（qr_code_method）。如此，发票预览画面，以及发票打印的PDF上，系统显示收款二维码。客户用二维码对应的APP扫码即可发起支付。
2.  POS零售模块中，POS的支付方式设置上，也可以选择二维码收款方式 （qr_code_method）。如此，POS收款时候，系统可以显示收款二维码，客户扫码支付。
3.  二维码收款方式，目前系统支持两种，一种是SEPA（安装模块 account_qr_code_sepa），一种是EMV（安装模块account_qr_code_emv）。
4.  二维码收款功能配置，以SEPA为例。安装模块 account_qr_code_sepa ，配置一个银行（res.partner.bank），该银行的银行账号必须是IBAN格式的银行账号，例如 BE68 5390 0754 7034 。客户发票上的币种选择欧元（SEPA只支持欧元支付）。
5.  参照系统的实现，可以开发中国支付宝、微信、银联的二维码收款功能。

【功能截图】

发票预览的收款二维码 

![[1-odoo18-3984-35da899d.png]]

POS收银界面的二维码收款 

![[1-odoo18-3984-0b32ad9c.png]]

客户发票上的设置 

![[1-odoo18-3984-37768240.png]]

POS收款方式配置 

![[1-odoo18-3984-52dfbc1e.png]]

【技术实现原理】

1.  继承文件 addons\account\models\res_partner_bank.py 方法 _get_available_qr_methods，增加一种新的二维码收款方式。
2.  继承文件 addons\account\models\res_partner_bank.py 方法 _get_qr_code_generation_params，该方法中返回二维码的参数信息。系统基于该参数生成二维码图像。代码参考示例 addons\account_qr_code_emv\models\res_bank.py
3.  继承文件 addons\account\models\res_partner_bank.py 方法 _get_error_messages_for_qr 及 _check_for_qr_code_errors，这两个方法在返回二维码参数前，先检查一下系统配置等有无错误。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
