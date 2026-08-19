---
title: "Odoo14费用报销操作流程"
source: "http://www.thinkltd.cn/forum/1/odoo14-768"
forum: "求助台"
author: "肖相扶"
published: 2023-05-26
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo14费用报销操作流程

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-05-26
> <http://www.thinkltd.cn/forum/1/odoo14-768>

【费用报销操作流程】在Odoo中，费用报销功能模块设计意图是：

1.  费用发生时候（取得费用发票等凭证时候），上传费用凭证，OCA文字识别（Odoo提供的付费服务）自动填写费用单。

2.  到了公司规定的费用报销日（例如每周四，或者每月25日），勾选平时填报的费用明细，提交费用报销单。

3.  费用报销单经主管审批，财务审批，最后出纳付款。

4.  关于上述功能详细原理，参考：[Odoo费用报销模块完善hr_expense_cn](http://www.thinkltd.cn/forum/2/question/odoohr-expense-cn-3415)

5.  但在中国，费用报销的操作习惯是，直接填写费用报销单，在费用报销单上逐行填写费用明细。在Odoo14中，这种操作模式也可以支持。如下面截图，直接创建费用包括，费用报告上在创建费用明细。

![[1-odoo14-768-aebfa26c.png]]

## 补充/答案 1

直接在费用报销单上逐行增加费用时，如何针对某笔费用添加附件呢，例如费用是高铁费，需要上传高铁发票附件

如下图所示增加按钮

方案：

经调查这个弹框调用的是费用的form视图

因此只需要对form视图写继承，增加

widget name="attach_document" string="Attach Receipt" action="attach_document" highlight="1" invisible="context.get('not_show_attach')"

而原生的费用模块已经有上传附件的按钮，再显示这个按钮就会很突兀

因此针对原生费用菜单传一个上下文，对应上面增加的按钮里通过接收上下文 invisible="context.get('not_show_attach')" 控制此按钮是否显示

![[1-odoo14-768-9f2c391c.png]]

![[1-odoo14-768-b9f976a6.png]]

、

![[1-odoo14-768-5706098a.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
