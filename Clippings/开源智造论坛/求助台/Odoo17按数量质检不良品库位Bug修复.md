---
title: "Odoo17按数量质检不良品库位Bug修复"
source: "http://www.thinkltd.cn/forum/1/odoo17bug-3832"
forum: "求助台"
author: "肖相扶"
published: 2023-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17按数量质检不良品库位Bug修复

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-12-15
> <http://www.thinkltd.cn/forum/1/odoo17bug-3832>

【Bug现象】

Odoo17质检模块新增功能：按数量质检，质检不通过自动入不良品库位。不过此功能有点Bug，导致质检Wizard上的不良品库位不能传递到系统后台，因而系统后台拆分入库明细时候，取不到不良品库位，因而虽然拆分了，但都是入库到正常库位。

![[1-odoo17bug-3832-70394da6.png]]

【修改方法】

视图  quality.check.wizard.form.failure， 代码行   改成如下：

![[1-odoo17bug-3832-984328dc.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
