---
title: "零售扫码支付: pos_enhance, payment_alipay, payment_weixin"
source: "http://www.thinkltd.cn/forum/2/pos-enhance-payment-alipay-payment-weixin-3370"
forum: "模块库"
author: "施叶寒"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 零售扫码支付: pos_enhance, payment_alipay, payment_weixin

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:施叶寒 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/pos-enhance-payment-alipay-payment-weixin-3370>

【背景】

    零售的支付界面需要支持常用的第三方扫码支付，如 支付宝、微信的付款码支付。

【svn路径】

```python
    SVN\odoo_ecommerce\13.0SRC\零售

    其中，需要首先安装pos_enhance及其依赖模块；payment_weixin、oscg_payment_alipay视情况而定。
```

【POS配置方法】

1. 创建**支付的日记账（account.journal）；

2. 把日记账（account.journal）绑定到支付方式上（payment.acquirer）；
3. 创建一个POS的付款方式（pos.payment.method），绑定这个日记账（account.journal）。

【实际操作】

    在付款界面，选择 支付方式， 输入金额， 扫码。

![[2-pos-enhance-payment-alipay-payment-weixin-3370-cccf56a7.png]]

【微信支付配置】

稍后补充

【支付宝配置】

支付宝需要配置四个信息：

1、APP ID：

APPID位置在：开放平台密钥=》APPID

2、应用私钥：

下载密钥工具生成应用私钥

支付宝私钥生成参考：\https://opendocs.alipay.com/open/291/105971

ODOO上填写应用私钥格式：

-----BEGIN RSA PRIVATE KEY-----
应用私钥
-----END RSA PRIVATE KEY-----
 3、支付公钥：

当生成支付应用私钥并绑定后系统会生成支付公钥

支付公钥格式：

-----BEGIN PUBLIC KEY-----
支付公钥
-----END PUBLIC KEY-----

4、合作伙伴ID：

合作伙伴ID位置在：老版wap支付密钥=》合作伙伴身份（PID）

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
