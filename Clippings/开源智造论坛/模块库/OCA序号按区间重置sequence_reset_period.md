---
title: "OCA序号按区间重置sequence_reset_period"
source: "http://www.thinkltd.cn/forum/2/ocasequence-reset-period-2584"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA序号按区间重置sequence_reset_period

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocasequence-reset-period-2584>

模块链接：

This module was written to reset the sequences on the specified times, because by default they are reset yearly.

###

### Usage

- Access sequences and configurate the model to use.
- When sequence is computed, date_range will follow the specified rules
-

## 补充/答案 1

这个是打上勾，底下的月份及下一号码重置明细行是自动产生的吗？还是得一行行再手动加的，odoo原本是一行行加的，是不是这个模块就打勾自动化了？

## 补充/答案 2

一行行加，可以考虑批量导入。这个模块增强的功能是可以按月、按周、按天重置。Odoo原来的功能只能按年重置。

## 补充/答案 3

不是，原来打上勾，底下明细的日期，手动一行行加时，如果选择是一个月开始到月末，序号是1，就是可以按月重置的，重置是按选择的日期范围来判断的。系统原有的功能。


## 原帖外链配图

![[2-ocasequence-reset-period-2584-x194038c2.png]]
<small>原始地址: /web/image/873/snipaste_20190120_003318.png?access_token=bd7a7e27-8eee-4f06-85a5-46ecfee72d85</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
