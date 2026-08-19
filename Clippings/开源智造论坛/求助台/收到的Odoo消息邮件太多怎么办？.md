---
title: "收到的Odoo消息邮件太多怎么办？"
source: "http://www.thinkltd.cn/forum/1/odoo-3644"
forum: "求助台"
author: "肖相扶"
published: 2023-03-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 收到的Odoo消息邮件太多怎么办？

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-03-16
> <http://www.thinkltd.cn/forum/1/odoo-3644>

【问题背景】

Odoo系统上线，数皆的领导抱怨，Odoo垃圾邮件太多，她不想看那么多。

【解决办法】

1.  如图一，单据的消息区域可以选择订阅什么消息，不订阅什么消息，不订阅的消息，系统不会自动发邮件
2.  其次，如图二，在消息子类型中，可以设置，关注单据时候，是否自动订阅该类型消息。如果不自动订阅则默认不订阅，自然不会收到邮件。

![[1-odoo-3644-2813e63a.png]]

![[1-odoo-3644-7940d218.png]]

## 补充/答案 1

图2批量取消订阅后，历史单据中已订阅不会消失

补充一个服务器动作，效果是清除历史单据里关注者的所有订阅信息

for record in records:
  [record.message_follower_ids.write({'subtype_ids':[(6,0,[])]})](https://record.message_follower_ids.write(%7B&#39;subtype_ids&#39;:%5B(6,0,%5B%5D)%5D%7D))

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
