---
title: "二开模块payment_weixin微信支付"
source: "http://www.thinkltd.cn/forum/2/payment-weixin-3150"
forum: "模块库"
author: "施叶寒"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开模块payment_weixin微信支付

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:施叶寒 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/payment-weixin-3150>

1. 模块存放位置： SVN\odoo_ecommerce\12.0SRC\payment_weixin

2. 使用场景： 客户通过微信扫码支付

3. 安装条件： 依赖payment

4. odoo当前的不足/特性：当前不支持微信支付

5. 使用方法：

    激活

1.         网站——>设置——>支付方式：

![[2-payment-weixin-3150-0d12872d.png]]

2.         微信支付配置：

![[2-payment-weixin-3150-8d25c7ee.png]]

其中：Weixin APPID、微信支付商户号、API秘钥、Weixin APPsecret为官方提供；IP Address为网站的域名

3.         基本设置——>APPID、APPsecret

![[2-payment-weixin-3150-84ca7ceb.png]]

4.         微信客户号获取：微信支付

![[2-payment-weixin-3150-2be92805.png]]

5.         Weixin Appsecret获取：

6. 配置完成之后——>发布支付方式

![[2-payment-weixin-3150-39887078.png]]

7. 登录微信公众号：

开发——>基本设置——>IP白名单

![[2-payment-weixin-3150-52c2e882.png]]

添加网站IP到IP白名单

![[2-payment-weixin-3150-5853a400.png]]

## 补充/答案 1

需要考虑下面几个应用场景：1) 电脑上浏览器打开电商网站购物，微信扫码支付；2) 直接在手机微信里面打开电商网站购物，是否有免扫码，直接输密码的支付方式；3) 手机上用浏览器打开电商网站购物（非微信浏览器），此种情况，无法扫码，如何完成支付？

## 补充/答案 2

什么时候能完善一下，能真正手机端使用呢？目前手机端还需要扫电脑上的码才能完成支付，那实际业务当中，根本不可能手机下单后还去电脑上去付款操作的。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
