---
title: "如何去找 由tracking=True 自动生成的消息"
source: "http://www.thinkltd.cn/forum/1/tracking-true-649"
forum: "求助台"
author: "施叶寒"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 如何去找 由tracking=True 自动生成的消息

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:施叶寒 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/tracking-true-649>

state = fields.Selection([],tracking=True,**args)

当一个字段的tracking=True，在变更时将自动生成消息，格式为：旧值=》新值。

如果业务需要定向访问这些消息，并不能直接去找mail_message的body字段。

而是需要访问mail_tracking_value中mail_message_id=当前message的id；

或者访问该message的tracking_value_ids[0]（通常只会关联一个）。

mail_tracking_value表会记录 关联业务记录的目标字段 field（如：state），旧值old_value_*（如：old_value_char, old_value_float）,新值new_value_*（如：new_value_char, new_value_float），关联业务记录的消息 mail_message_id。

注意：

如果是char型字段，新值、旧值 将记录 界面展示的经翻译的值；

如果是selection型字段，新值、旧值 将记录 界面展示的经翻译的标签值。

如图所示：

![[1-tracking-true-649-7527165b.png]]

![[1-tracking-true-649-7a1dcfba.png]]

![[1-tracking-true-649-7a1dcfba.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
