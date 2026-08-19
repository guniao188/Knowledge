---
title: "IoTPay支付网关集成payment_iotpay"
source: "http://www.thinkltd.cn/forum/2/iotpaypayment-iotpay-3566"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# IoTPay支付网关集成payment_iotpay

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/iotpaypayment-iotpay-3566>

模块位置：OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\payment_iotpay

【模块功能】

增加 加拿大用的IoTPay 在线支付方式，实现了“统一下单”的支付方式，以及微信JSAPI支付集成（mobile web）的支付方式（IoTPay Channel选择“微信内网页支付”）。IoTPay相关技术资料参考如下。

1) Odoo支付网关集成技术参考 https://erpsolutions.oodles.io/blog/payment-gateway-integration/

2) IoTPay支付网关参考 https://iotpay.ca/

3) IoTPay支付网关技术参考 https://develop.iotpay.ca/zh/interface-rule.html#java-code

4) IoTPay支付网关测试页面 https://develop.iotpay.ca/newdemo/jsapi/demo.html

5) IoTPay支付网关测试账号

```python
       商户ID: 10001677

       前面Key:kSA1DVy3V8FqB0pnVOkts85BwM0lMUkX

       注意，测试页面上 Job No不要填写
```

【功能截图】

![[2-iotpaypayment-iotpay-3566-05dbc2d1.png]]

![[2-iotpaypayment-iotpay-3566-4255ba96.png]]

![[2-iotpaypayment-iotpay-3566-5217295a.png]]

## 补充/答案 1

【支付网关集成原理】

1.  点击支付按钮（Pay）时候，系统背后调用代码文件 OSCGODOO15\source\addons\payment\static\src\js\checkout_form.js 中的方法 _onClickPay 。

2.  该方法主要调用代码文件OSCGODOO15\source\addons\payment\static\src\js\payment_form_mixin.js 中的方法 _processPayment

3.  该方法调用文件OSCGODOO15\source\addons\payment\controllers\portal.py 中的方法 payment_transaction

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
