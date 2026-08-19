---
title: "有什么办法能一下子过滤得出MO有哪些已最后一道工序完工了？"
source: "http://www.thinkltd.cn/forum/1/mo-352"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 有什么办法能一下子过滤得出MO有哪些已最后一道工序完工了？

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/mo-352>

生产制造订单，管理工序工艺加工过程，那么假设最后一道工序已完工了，因操作工单的是工人，与MO操作人员是不同的用户，那么下一步准备入库，操作MO的用户如何快速从系统过滤得出哪些MO是可以入库操作完成了呢？

![[1-mo-352-c83c104e.png]]

## 补充/答案 1

生产单上增加一个计算型字段即可，如下图。

计算代码：

for record in self:
        record['x_work_all_done'] = record.workorder_ids and all(x.state in ['done', 'cancel'] for x in record.workorder_ids)

![[1-mo-352-aaaa5c7d.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
