---
title: Odoo AI Copilot
type: project
status: 开发调试中
updated: 2026-08-04
tags: [Odoo19, AI, 报表]
---

# Odoo AI Copilot

## 产品目标

- AI 运维问答：根据用户的业务需求和系统上下文解释、诊断并给出操作建议。
- 自然语言报表：将用户问题转换为受控的数据查询和结构化报表。
- Odoo 19 工作台：在原生前端中展示会话、结果、报表与诊断信息。

## 当前实现上下文

- 工作区源码：`/Users/yaodaidi/Documents/New project/odoo_ai_copilot`
- 实际 addons：`/Users/yaodaidi/odoo19/custom_addons/odoo_ai_copilot`
- 近期修复：OWL 模板不能直接依赖上下文未暴露的浏览器全局 `JSON`；序列化逻辑已移到组件 JavaScript 方法。

## 长期设计约束

- 自然语言不得直接生成并执行无限制 SQL；需要模型/字段白名单、权限继承、行数限制与审计。
- AI 回答必须区分系统事实、推断和建议，并可追溯查询依据。
- 工作区与实际 addons 的同步必须纳入交付检查，防止两份代码漂移。

## 下一步

- 完成资源重编译与浏览器回归验证。
- 固化可执行报表的安全策略、异常提示和审计日志。
- 形成最小可用场景与验收清单。

