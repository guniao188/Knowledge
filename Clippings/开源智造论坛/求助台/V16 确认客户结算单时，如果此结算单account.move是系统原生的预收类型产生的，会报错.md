---
title: "V16 确认客户结算单时，如果此结算单account.move是系统原生的预收类型产生的，会报错"
source: "http://www.thinkltd.cn/forum/1/v16-account-move-3860"
forum: "求助台"
author: "葛忠彪"
published: 2024-01-17
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# V16 确认客户结算单时，如果此结算单account.move是系统原生的预收类型产生的，会报错

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:葛忠彪 | 2024-01-17
> <http://www.thinkltd.cn/forum/1/v16-account-move-3860>

![[1-v16-account-move-3860-876c3d61.png]]

报错如上截图，原理分析如下

销售订单行sale.order.line的name字段是一个计算型字段，调用了 _compute_name方法，此方法里系统判断这行是预收款的话，且对应的结算单状态是草稿和取消时，会在原name的算法基础上，增加客户结算单的状态，例如   预收/预付款（草稿），如果结算单状态确认则沿用原来计算名称的方法

当客户结算单确认action_post时，会触发销售订单行的 _compute_name 方法， _compute_name 方法既然是赋值自然会触发wirte方法，而write方法里面有个黑名单方法

_get_protected_fields，返回不允许修改的字段

建议改造思路是对于上述 account_move的 action_post  或者sale.order.line的_compute_name 计算型方法传个上下文，然后在sale.order.line的黑名单方法 _get_protected_fields 里，如果拿到上下文，就把name字段pop掉

以上内容施老大调查

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
