---
title: "Odoo18的PDF Builder（PDF构建器）"
source: "http://www.thinkltd.cn/forum/1/odoo18pdf-builder-pdf-3981"
forum: "求助台"
author: "肖相扶"
published: 2024-10-09
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo18的PDF Builder（PDF构建器）

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-10-09
> <http://www.thinkltd.cn/forum/1/odoo18pdf-builder-pdf-3981>

【业务场景】

1.  例如家具销售企业，给客户报价时候，希望发给客户的报价PDF文件上，不是一个简单的产品及价格明细行，而是一个图文并茂的PDF册子。例如，第一页是封面，含有公司介绍，第二页是报价明细，随后各页是报价明细中各个家具产品的图文介绍（PDF文件）。
2.  在线发给客户的报价单，希望客户可以浏览下载报价产品的图文介绍PDF文件。
3.  机加的外协采购的采购单，需要把工件的PDF图纸文件随采购单一并发给外协方。系统能不能把采购明细和图纸PDF自动合并为一个完整的PDF外协采购合同文件呢？

【实现功能】

1.  产品可以上传PDF附件，该附件可以指定如何添加到销售订单（Sale Order）上。有四个选项：Hidden，On quote, On confirmed order, Inside quote pdf 。Hidden表示该附件SO客户不可见。On quote表示该附件SO客户总是可见（客户可以从在线预览的SO上下载该附件）， On confirmed order表示该附件只有SO确认后SO客户才可见， Inside quote pdf 表示打印PDF报价单时候，该附件自动合并到报价单中。
2.  销售订单SO上增加了Quote Builder页签，该页签上，可以选择Header PDF、产品附件PDF、Footer PDF文件，系统生成PDF报价文件时候，自动合并Header PDF、产品附件PDF、报表XML生成的报价PDF、Footer PDF，形成一个多页的报价文件。
3.  系统的报价模板（ Quote Template ）上也新增了 Quote Builder页签，该页签上可以添加多个 Header PDF及 Footer PDF，SO上选择报价模板时候，这些PDF自动添加到SO的 Quote Builder页签，而后在SO上还可以选择用哪个Header，哪个Footer。
4.  Header PDF、产品附件PDF、 Footer PDF文件，可以定义“域字段”，域字段是可以在SO上填写的字段。即在SO上填写字段值，客户下载PDF文件，或者系统生成PDF报价文件时候，系统自动用SO上的字段值填写到生成的PDF文件上。
5.  域字段分两种，一种是用SO上的已有的字段值自动填写，一种是用户在SO填写好后系统合并到PDF上。前一种，域字段的name必须和SO上的字段名相同，例如域字段名为name，系统自动用SO的单号(name字段)填写。如果是SO上的关联字段，例如SO的partner_id的name(SO客户名称)，域字段name命名规则是“partner_id__name”,partner_id和name间用两个_ 。
6.  Adobe Acrobat软件的“ 表单准备 ”工具，可以给PDF文件添加域字段。

【功能截图】

产品PDF附件：

![[1-odoo18pdf-builder-pdf-3981-7dc21bff.png]]

SO上的Quote builder：

![[1-odoo18pdf-builder-pdf-3981-2079ccd9.png]]

Adobe Acrobat软件给PDF文件添加域字段：

![[1-odoo18pdf-builder-pdf-3981-bce9a599.png]]

【技术原理】

1.  报价PDF文件中合并Header、Footer的实现代码：OSCGODOO18\source\addons\sale_pdf_quote_builder\models\[ir_actions_report.py](https://ir_actions_report.py) 继承方法 _render_qweb_pdf_prepare_streams，该方法中，填写PDF的域字段，合并PDF形成多页PDF文件。
2.  SO及报价模板上的Quote Builder页签，系统单独写了一个 customContentKanbanLikeWidget 的js widget实现显示效果。参看模块sale_pdf_quote_builder的js代码文件。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
