---
title: "OCA报价SO有效期sale_validity"
source: "http://www.thinkltd.cn/forum/2/ocasosale-validity-2675"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA报价SO有效期sale_validity

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocasosale-validity-2675>

模块链接：https://github.com/OCA/sale-workflow/tree/11.0/sale_validity

SO上增加Validity Date字段，公司上配置报价有效期的默认天数。系统自动计算Validity Date：订单日期 + 默认有效天数。

## Default Quotation Validity

With this module, you will be able to configure a default validity delay on quotations.

###

### Configuration

Go to the menu *Sale > Configuration > Settings*, in the section *Quotations & Sales*, set the *Default Validity of Sale Orders* in days.

###

### Usage

When you create a new quotation, the *Expiration Date* will be set by default to today's date plus the number of days configured in *Sale Settings* page. If you modify the *Order Date* field, the *Expiration Date* will be updated accordingly.


## 原帖外链配图

![[2-ocasosale-validity-2675-x194038c2.png]]
<small>原始地址: /web/image/1024/snipaste_20190121_110347.png?access_token=a5610e7f-1b9c-448c-b786-257c15f5ac2b</small>

![[2-ocasosale-validity-2675-x194038c2.png]]
<small>原始地址: /web/image/1026/snipaste_20190121_110531.png?access_token=28b7a692-5fa0-4ceb-8aee-2f85f80eea1e</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
