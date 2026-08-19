---
title: "Stock Picking的出入库时间更改"
source: "http://www.thinkltd.cn/forum/2/stock-picking-3920"
forum: "模块库"
author: "周鸿飞"
published: 2024-04-28
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Stock Picking的出入库时间更改

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:周鸿飞 | 2024-04-28
> <http://www.thinkltd.cn/forum/2/stock-picking-3920>

【开发背景】

1.  Picking单验证时候，它将当前时间当作是入库/出库时间，但实际情况，有可能是昨天入库/出库的，今天点验证按钮。
2.  希望是Picking上可以填写实际入库/出库时间，验证时候，如果填写了，则以填写的时间作为入库/出库时间。

【开发思路】

1.  首先 picking 验证的时候 内部会调用_action_done方法去将date_done的值设置为当前时间，接下来执行到move的_action_done的方法将date也设置为当前时间。
2.  所以我们只需要将这两个赋值的地方重写一下，同时在界面上date done可以手动填入
3.  在action done的上下文里 传入  force_period_date

![[2-stock-picking-3920-14072ed6.png]]

【功能截图】

![[2-stock-picking-3920-67632ae8.png]]

模块地址：OSCG_Git\17.0\extra-addons\stock_date_done

## 补充/答案 1

如此一来，库存计价应该也会是按照手动录入的 日期 准，进而凭证上的日期也是手动设置的 日期 ，那么过往凭证编号的顺序就不符合 日期 顺序了，所以实施的时候应该有个弹框提示，提示用户输入的日期不等于当前日期，要使用系统自带的凭证重排序功能，对凭证编号重新排序

## 补充/答案 2

在创建凭证时候 系统会先去判断上下文有没有传一个 force_period_date 如果有 就用 force_period_date的日期来创建凭证

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
