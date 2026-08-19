---
title: "二开门店零售按序列码定价pos_lots_price"
source: "http://www.thinkltd.cn/forum/2/pos-lots-price-3430"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开门店零售按序列码定价pos_lots_price

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/pos-lots-price-3430>

模块链接：OSCG_SVN\odoo_ecommerce\14.0SRC\POS零售\pos_lots_price

【业务背景】

二手奢侈品零售门店，同样的商品，新旧程度不同，因而每一件商品都单独定价。

实现原理：

```python
  1）批次对象stock.production.lot 上，增加价格字段

  2)  POS数据初始化时候，加载 批次及批次价格

  3）设置序列号的方法models.js 方法 setPackLotLines，继承该方法，设置序列号的同时设置价格

  4)  如果填写了一个不存在的序列号，或者没有库存的序列号，或者序列号上没有维护价格（价格为0.0），系统不更新零售价格（仍按原来逻辑基于POS上设置的价格表计算价格）。
```

【功能截图】

![[2-pos-lots-price-3430-0a89c430.png]]

## 补充/答案 1

【增加寄卖主结算功能】

1) 增加佣金等级表

2) 批次上增加寄卖主、佣金、是否已结算、结算日期、实际售价、状态等字段

3) 批次上增加快捷按钮，跳转到关联的POS订单、销售订单、结算单（供应商账单）

4) 批次上增加两个服务器动作：寄卖主结算、寄卖主退款，以及一个计划任务：寄卖主自动结算

![[2-pos-lots-price-3430-ecba1e65.png]]

![[2-pos-lots-price-3430-d85dc059.png]]

【增加寄卖主修改价格，实时更新到POS前台功能】

实现机制参考：[Odoo的总线消息机制原理bus模块](http://www.thinkltd.cn/forum/1/question/odoobus-697)
注意，POS界面默认js没有启动 polling 线程，导致Bus消息通知机制不起作用。解决方法是增加this.call('bus_service', 'addChannel', 'pos.notification');的调用，如下：

this.call('bus_service', 'addChannel', 'pos.notification');

this.call('bus_service', 'onNotification', this, this._onNotification);

【注意事项】

经测试，Odoo的消息实时通知线程(longpolling/poll)只对浏览器的主Tab页生效（_isMasterTab）。实际测试结果，打开门店POS的浏览器，不可以开多个Odoo的Tab页面（只可以有POS页面一个Tab页，不可以再开其他的Odoo Tab页面）。测试时候修改价格要用另外一个浏览器测试。

![[2-pos-lots-price-3430-70980065.png]]

## 补充/答案 2

【Odoo14可以配置手工修改零售价格的权限】

![[2-pos-lots-price-3430-5c5ee1a1.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
