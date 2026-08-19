---
title: "res_users 创建 代码优化"
source: "http://www.thinkltd.cn/forum/1/res-users-685"
forum: "求助台"
author: "施叶寒"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# res_users 创建 代码优化

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:施叶寒 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/res-users-685>

创建res.users时，所需时间与表记录数量正相关。

当res.users表 数量达到50000以上，平均创建一条记录需要1分钟甚至更长时间；

当res.users创建每一条记录时，mail.channel会去res.users表全量更新至少4次。select id from res_users where id in (全表id列表);

优化方法：

1. 禁止过程中的全量更新

2. 所有res.users对应的create全部改成api.model_create_multi

![[1-res-users-685-67985972.png]]

![[1-res-users-685-c6f1feb4.png]]

![[1-res-users-685-c6f1feb4.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
