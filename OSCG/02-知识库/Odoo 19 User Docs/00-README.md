---
title: Odoo 19 User Docs 知识库总览
type: 索引
module: 通用
tags: [Odoo, 索引, 通用, Odoo19, UserDocs]
source: https://www.odoo.com/documentation/19.0/applications.html
created: 2026-07-03
---

# Odoo 19 User Docs 知识库总览

> 📎 来源：Odoo 官方 [User Docs](https://www.odoo.com/documentation/19.0/applications.html)
> 🎯 目标：把 Odoo 19 官方 39 个模块梳理成实施顾问视角的速查手册，每个模块含官方链接、核心功能、OSCG 实施要点、常见坑、相关文档。

## 一、模块地图（5 大类 · 39 模块）

### 📦 [[01-Essentials/00-README|Essentials 基础能力]]（10）
- [[01-Essentials/Stages]] · [[01-Essentials/Activities]] · [[01-Essentials/Reporting]] · [[01-Essentials/HTML Editor]] · [[01-Essentials/Contacts]]
- [[01-Essentials/Export Import Data]] · [[01-Essentials/In-app Purchases]] · [[01-Essentials/Keyboard Shortcuts]] · [[01-Essentials/Property Fields]] · [[01-Essentials/Product Catalog]]

### 👥 [[02-HR/00-README|HR 人力资源]]（10）
- [[02-HR/Attendances]] · [[02-HR/Employees]] · [[02-HR/Appraisals]] · [[02-HR/Frontdesk]] · [[02-HR/Fleet]]
- [[02-HR/Payroll]] · [[02-HR/Time off]] · [[02-HR/Recruitment]] · [[02-HR/Referrals]] · [[02-HR/Lunch]]

### 🛠 [[03-Services/00-README|Services 服务运营]]（5）
- [[03-Services/Project]] · [[03-Services/Timesheets]] · [[03-Services/Planning]] · [[03-Services/Field Service]] · [[03-Services/Helpdesk]]

### 🚀 [[04-Productivity/00-README|Productivity 生产力工具]]（13）
- [[04-Productivity/Documents]] · [[04-Productivity/Sign]] · [[04-Productivity/Spreadsheet]] · [[04-Productivity/Dashboards]] · [[04-Productivity/Knowledge]]
- [[04-Productivity/Calendar]] · [[04-Productivity/Appointments]] · [[04-Productivity/Discuss]] · [[04-Productivity/Data Cleaning]] · [[04-Productivity/WhatsApp]]
- [[04-Productivity/Phone]] · [[04-Productivity/To-do]] · [[04-Productivity/AI]]

### 🎨 [[05-Studio/00-README|Studio 无代码定制]]（1）
- [[05-Studio/Studio]]

## 二、按实施场景速查

| 场景 | 涉及模块 |
|------|----------|
| **客户接触** | Contacts · Discuss · WhatsApp · Phone |
| **销售前中后** | Contacts · Documents · Sign · Helpdesk · Field Service |
| **内部协作** | Discuss · Calendar · Appointments · Knowledge · To-do · Documents · Sign |
| **人力全流程** | Employees → Recruitment · Referrals · Appraisals · Time off · Attendances · Payroll · Fleet · Frontdesk · Lunch |
| **项目/服务** | Project · Timesheets · Planning · Field Service · Helpdesk |
| **数据基础设施** | Property Fields · Export/Import Data · Product Catalog · Data Cleaning · Spreadsheet · Dashboards · Reporting |
| **AI 与自动化** | AI · Studio · Data Cleaning |
| **系统自定义** | Studio · Property Fields · Stages · Activities |

## 三、OSCG 实施顾问视角

- **必装底座**：Contacts、Discuss、Calendar、Knowledge、Documents —— 客户上线前置。
- **横向扩展项**（几乎每个客户都会碰）：Stages（看板阶段）、Activities（跟进任务）、Reporting（透视图）、Export/Import（数据迁移）、Property Fields（不改代码扩字段）。
- **可替代第三方工具**：Sign（DocuSign）· Spreadsheet（Excel/Google Sheets）· Knowledge（Confluence/Notion）· WhatsApp（企微/Line）· AI（ChatGPT 集成）。
- **易被忽略但高价值**：Data Cleaning（重复数据清理）、Property Fields（客户自定义字段）、Product Catalog（销售/采购下单场景）。
- **和二开边界**：Studio 能盖住 60% 的字段/视图/自动化诉求，超出再走 Python/OWL。

## 四、维护约定

- 每篇模块页保持"骨架 → 使用中补充"的迭代风格。
- OSCG 实施要点、常见坑段落逐步在项目里回填（写完一个客户就回来沉淀）。
- 有新的 Odoo 版本，重新 Clip 一份 User Docs 列表，与本索引 diff 出增删。
- 补充实施案例时优先链回 [[../实施案例/]] 目录。

## 五、相关知识

- [[../../../Clippings/User Docs — Odoo 19.0 documentation|原文 Clipping]]
- [[../../../Clippings/Odoo 文档索引|Odoo 官方文档索引]]
- [[../../../Odoo 19.0 操作手册/00. 目录与总览|Odoo 19.0 操作手册（按业务流程）]]
