---
title: "通用申请表单及Tier审批模块approvals2_tier_validation"
source: "http://www.thinkltd.cn/forum/2/tierapprovals2-tier-validation-3573"
forum: "模块库"
author: "肖相扶"
published: 2024-04-07
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 通用申请表单及Tier审批模块approvals2_tier_validation

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-04-07
> <http://www.thinkltd.cn/forum/2/tierapprovals2-tier-validation-3573>

模块链接：

1.  OSCG_SVN\odoo_ecommerce\15.0SRC\HR\approvals2

2.  OSCG_SVN\odoo_ecommerce\15.0SRC\HR\approvals2_tier_validation

3.

【20221212新增16.0版本】

1.  https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/approvals2

2.  https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/approvals2_tier_validation

【业务背景】

1.  企业中的一些在线审批业务（办公自动化OA业务），例如用章申请的审批、借款申请的审批、出差申请的申请、合同文本的审批，等等。

2.  Odoo中提供了一个通用申请表单的审批模块Approvals，但该功能的审批流程配置能力很弱，不支持串审、不支持转签、不支持服务器动作、不支持审批意见。

3.  本模块提供的功能是，保留了Approvals模块中的申请表单（approvals.request）功能，去掉了审批流程功能。审批流程换成tier_validation审批（[OA审批流程推荐方案base_tier_validation](http://www.thinkltd.cn/forum/2/question/oabase-tier-validation-3498)）。

【功能截图】

## 补充/答案 1

approvals2\security\approval_security  49行左右如下文部分整段注释掉，不然不是 审批/管理员 群组的用户登录系统就会报错，因为此模型里已经没有approver_ids字段了

record id="approval_request_approvers_rule" model="ir.rule"

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
