---
title: "多公司property属性值问题"
source: "http://www.thinkltd.cn/forum/1/property-3783"
forum: "求助台"
author: "肖相扶"
published: 2023-10-11
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 多公司property属性值问题

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-10-11
> <http://www.thinkltd.cn/forum/1/property-3783>

【问题背景】

客户帆特的系统，非Admin登录，发票上点击左下角“添加”，核销预付账款，总是核销不了。

![[1-property-3783-59ff4e89.png]]

经调查，原因在于，点击“添加”按钮核销时候，系统从客户上取预付账款科目时候，按当前用户所属公司取科目。当前用户所属公司不同于该单据的公司时候，取出来的科目，和单据上的科目总是不匹配，因而核销不了。

【程序Bug】

预收预付模块account_advance_payment，存在下述有Bug的代码行。 self.commercial_partner_id.property_account_receivable_advance_id 默认按当前用户所属公司取属性值 property_account_receivable_advance_id，而不是按当前用户所操作的公司（右上角切换而成的公司）取属性值。

因而下述代码有可能错误： self.commercial_partner_id.property_account_receivable_advance_id按当前用户所属公司取值，如果当前用户所属公司不同于 单据 line_id上的公司，则下述if语句可能不成立。应该增加一行代码：self = self.with_company(self.company_id)，如此，确保属性值按单据上的公司的属性值取值。

lines = self.env['account.move.line'].browse(line_id)
if lines.account_id == self.commercial_partner_id.property_account_receivable_advance_id:

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
