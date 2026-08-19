---
title: "res.partner的记录规则限制"
source: "http://www.thinkltd.cn/forum/1/res-partner-865"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# res.partner的记录规则限制

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/res-partner-865>

通常销售和采购及其他部门，会增加一些条件限制，示例：

销售员只看自己的单据

那么系统自带的里面，是所有用户都能看到全部的客户和供应商，员工，公司等信息

故需要做记录规则的调整：

调整的时候需要考虑全面：

![[1-res-partner-865-a0656804.png]]

![[1-res-partner-865-7408f4f6.png]]

![[1-res-partner-865-cac6316c.png]]

如果只是加了规则是限制销售员，往往会导致普通用户只要使用HR或只使用费用报销的模块，而无法登录系统，报错

所以写记录规则时，需要考虑到res.user背后关联的partner的资料是否所有用户能看到！！！

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
