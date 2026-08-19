---
title: "Odoo13企业版审批模块approvals"
source: "http://www.thinkltd.cn/forum/2/odoo13approvals-3211"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo13企业版审批模块approvals

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoo13approvals-3211>

【设计原理】

1.  该审批模块新增了一个通用表单 approval.request ，该表单有字段：申请类型、申请人、申请时间、项目、数量、金额、说明等字段。该表单可以预设审批人列表，也可以表单申请时候，手工添加审批人。审批表单可以添加附件文档，随表单一起审批。

2.  模块新增了审批类型 approval.category 表单，该表单可以设置表单 approval.request 各字段显示/不显示，必须/不必须。也可以预设审批人列表。

3.  审批时候，各审批人不分先后顺序，前面的人没审，后面的人也可以先审。

4.  审批是否通过的判断，审批类型上可以设置最少几人审批了，才算审批通过。

## 补充/答案 1

![[2-odoo13approvals-3211-ba71c2bb.png]]

审批表单：

![[2-odoo13approvals-3211-e0c3a63c.png]]

审批类型定义：

![[2-odoo13approvals-3211-52c94d23.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
