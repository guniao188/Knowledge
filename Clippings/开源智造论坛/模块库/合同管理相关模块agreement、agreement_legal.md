---
title: "合同管理相关模块agreement、agreement_legal"
source: "http://www.thinkltd.cn/forum/2/agreementagreement-legal-3539"
forum: "模块库"
author: "肖相扶"
published: 2025-12-04
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 合同管理相关模块agreement、agreement_legal

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2025-12-04
> <http://www.thinkltd.cn/forum/2/agreementagreement-legal-3539>

17版本 模块位置：[https://gitlab.com/oscg-china/extra-addons/-/tree/17.0/%E5%90%88%E5%90%8C%E7%AE%A1%E7%90%86](https://gitlab.com/oscg-china/extra-addons/-/tree/17.0/%E5%90%88%E5%90%8C%E7%AE%A1%E7%90%86)

【2024-11-13升级到17版本】

模块位置：原始位置

OSCG_SVN\odoo_ecommerce\15.0SRC\合同管理

OCA模块中，合同审批及条文管理模块 agreement_legal，功能较为杂乱，SVN上的版本重写了该模块，删减了一些功能，增加了基于 tier_validation 的合同审批功能，增加了基于report_docx 的Word合同模板输出示例。

【20220320新增】1) 合同电子签章(参考 [电子签章接口模块base_eseal](http://www.thinkltd.cn/forum/2/question/base%5C-eseal%5C-3551))功能模块：agreement_esign；2) 双方签署后的合同归档（自动创建document）：agreement_document

【业务背景】

1.  服务型行业、项目型行业，销售合同的修改、审批、签订是一个复杂的过程。

2.  销售合同的修改：多数客户愿意接受标准合同条款，少数客户在标准条款上，会要求做一些修改。如何保证每位销售人员，每次销售都使用了最新版本的、统一格式的标准条款合同，如果标准条款上有修改，改了哪些条款，如何防止销售人员无原则地修改合同条款

3.  本模块在合同表单上维护合同条款（初始值从合同模板拷贝形成新合同），直接打印输出Word档的合同。如果客户对条款有修改，直接修改合同表单，再次输出给客户确认。

4.  销售合同的审批，合同审批一般要走OA流程，本模块开发了基于\\ base_tier_validation的OA审批流程。

5.  合同签章，可以打印系统输出的Word合同，盖章，扫描，上传合同表单，完成电子合同存档。也可以支持在线电子签章（待开发），直接从系统输出盖好章的合同，发与客户盖章，再扫描上传。

6.  Word合同打印模板参考这里 [二开Excel/Docx word打印报表模块report_xlsx、report_docx | 开源智造服务管理平台 (thinktech.ltd](http://www.thinkltd.cn/forum/2/question/excel%5C-docx%5C-wordreport%5C-xlsxreport%5C-docx%5C-2987))

7.  OCA上其他一些模块关联agreement和其他单据，如模块 agreement_sale，在销售订单上增加 agreement_id, agreement_type_id字段，关联合同和销售订单。

【模块功能】

## 补充/答案 1

【功能截图】

电子签章：

![[2-agreementagreement-legal-3539-7d2cd272.png]]

合同条款：

![[2-agreementagreement-legal-3539-d7fc3cfe.png]]

Word模板：

![[2-agreementagreement-legal-3539-0f996769.png]]

Word合同输出：

![[2-agreementagreement-legal-3539-692fe30b.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
