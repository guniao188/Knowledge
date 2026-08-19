---
title: "MTO改单及上下游单据关系调查"
source: "http://www.thinkltd.cn/forum/1/mto-365"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# MTO改单及上下游单据关系调查

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/mto-365>

【结论】

以仓库两步发货为例，销售出库时候，系统自动产生两个单据，一个 Stock  --> Output ， 一个  Output  --> Customer 。

如果修改其中一个单据的初始数量，不会传导到另一个单据。

如果取消下游单据（Output  --> Customer），上游单据不会自动取消。如果取消上游单据，上游单据对应的Stock Rule上勾选了“Propagate cancel and split”，则下游单据自动取消。

同理，勾选了“Propagate cancel and split”，如果上游单据分批发货，下游单据自动分批（拆分）。

如果下游单据初始数量改大了，或者上游单据初始数量改小了，则下游单据数量超出的部分永远保留不了，只能分批发货（拆单）后，取消超出的部分。如果误操作取消了上游单据，下游单据也只能取消（否则无法锁货，无法完成）。或者参考这里“重置为草稿”：[/forum/1/question/stock-picking-366](http://www.thinkltd.cn/forum/1/question/stock-picking-366)

![[1-mto-365-13f908ba.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
