---
title: "OA审批流程推荐方案base_tier_validation"
source: "http://www.thinkltd.cn/forum/2/oabase-tier-validation-3498"
forum: "模块库"
author: "肖相扶"
published: 2024-11-26
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OA审批流程推荐方案base_tier_validation

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-11-26
> <http://www.thinkltd.cn/forum/2/oabase-tier-validation-3498>

【20241025】吴键，模块升级到了Odoo 18.0： [https://gitlab.com/oscg-china/extra-addons/-/tree/18.0](https://gitlab%5C.com/oscg%5C-china/extra%5C-addons/%5C-/tree/18%5C.0)

【20231209】模块升级到了Odoo 17.0：[https://gitlab.com/oscg-china/extra-addons/-/tree/17.0](https://gitlab%5C.com/oscg%5C-china/extra%5C-addons/%5C-/tree/17%5C.0)

【20221217】模块升级到了Odoo16\\0：[https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/base_tier_validation](https://gitlab%5C.com/oscg%5C-china/extra%5C-addons/%5C-/tree/16%5C.0/base_tier_validation)\\gitlab上升级好的模块有

base_tier_validation
base_tier_validation_formula
base_tier_validation_forward
base_tier_validation_server_action
purchase_tier_validation
sale_tier_validation
hr_expense_tier_validation
holiday_tier_validation
approvals2_tier_validation
purchase_request_tier_validation
purchase_requisition_tier_validation

【20220929Bug修正】模块\\OSCG_SVN\odoo_ecommerce\15\\0SRC\审批模块\base_tier_validation_forward，如果待审批的单据上有name字段，提交审批时候，会用单据的name字段覆盖审批层级定义（tier\\definition）的name字段，导致该单据的所有审批记录（包括历史的）的审批说明都变成了待审单据的name值。另外还修正了一个问题：如果修改了审批层级定义（tier\\definition）的name字段值，所有该层级对应的审批记录（包括历史记录）的审批说明值都变成了新的name字段值，更合理的逻辑应该是，历史审批记录不变，（tier\\definition）的修改只对将来的审批记录生效。

【模块链接】

1.  [https://github\\com/OCA/server\\ux/tree/14\\0/base_tier_validation](https://github%5C.com/OCA/server%5C-ux/tree/14%5C.0/base_tier_validation)\\\\ \\配置审批节点

2.  [https://github\\com/OCA/server\\ux/tree/14\\0/base_tier_validation_formula](https://github%5C.com/OCA/server%5C-ux/tree/14%5C.0/base_tier_validation_formula)\\\\ 在审批节点上增加审批人选项：自定义python代码计算审批人

3.  [https://github\\com/OCA/server\\ux/tree/14\\0/base_tier_validation_forward](https://github%5C.com/OCA/server%5C-ux/tree/14%5C.0/base_tier_validation_forward)\\ 在审批节点上增加代签/转签功能

4.  [https://github\\com/OCA/server\\ux/tree/14\\0/base_tier_validation_server_action](https://github%5C.com/OCA/server%5C-ux/tree/14%5C.0/base_tier_validation_server_action)\\\\ 审批节点上增加服务器动作配置，审批通过/拒绝时候，自动执行服务器动作

5.  [https://github\\com/OCA/sale\\workflow/tree/14\\0/sale_tier_validation](https://github%5C.com/OCA/sale%5C-workflow/tree/14%5C.0/sale_tier_validation)\\\\ 销售订单上增加审批流程配置功能

6.  [https://github\\com/OCA/purchase\\workflow/tree/14\\0/purchase_tier_validation](https://github%5C.com/OCA/purchase%5C-workflow/tree/14%5C.0/purchase_tier_validation)\\\\ \\采购订单上增加审批流程配置功能

7.  [https://github\\com/OCA/hr\\expense/tree/14\\0/hr_expense_tier_validation](https://github%5C.com/OCA/hr%5C-expense/tree/14%5C.0/hr_expense_tier_validation)\\\\ \\费用报销单上增加审批流程配置功能

8.  [https://github\\com/OCA/purchase\\workflow/tree/14\\0/purchase_requisition_tier_validation](https://github%5C.com/OCA/purchase%5C-workflow/tree/14%5C.0/purchase_requisition_tier_validation)\\\\ Odoo自带的采购计划上增加审批功能

9.  [https://github.com/OCA/purchase-workflow/tree/14.0/purchase_request_tier_validation](https://github%5C.com/OCA/purchase%5C-workflow/tree/14%5C.0/purchase_request_tier_validation)  OCA的采购申请表单增加审批功能

10. **Odoo15的base_tier_validation已升级好**，参见 OSCG_SVN\odoo_ecommerce\15.0SRC\审批模块

11. 产品表的tier审批功能  https://github.com/OCA/product-attribute/tree/14.0/product_tier_validation

12. 会计赁证的tier审批功能参考：https://github.com/OCA/account-invoicing/tree/14.0/account_move_tier_validation

【模块功能】

1.  自定义审批节点，一个模型（单据）可以定义多个审批节点。可以定义审批节点的适用条件（不符合条件自动跳过该审批节点）。 审批节点上可以按条件指定审批人。审批节点之间的关系，支持：窜签、会签、或签、代签/转签。

2.  模型（单据）上增加OA审批功能（同意/拒绝），显示审批节点列表

【审批节点配置】

![[2-oabase-tier-validation-3498-6575f1ee.png]]

- validated by：本审批节点的审批人。可以是指定的User，指定的权限组（该审批组里面任何一个人审批即通过），被审单据上指定的User字段，自定义python代码指定审批人

- Sequence：审批顺序，数字大的节点先审批，数字小的节点后审批

- Approve by sequence：按Sequence顺序串行审批，即Seqence大的节点审批完了，本节点才可以审批。

- Allow Forward：本节点允许代签/转签。勾选后，表单审批界面上，Validate、Reject两个按钮之外，还可以增加一个“Forward”按钮。点击Foward弹窗，填写转签人。

- Definition Domain：本节点适用的条件：Domain表达式指定条件

- Tier Definition Expression：本节点适用的条件：python关系表达式指定的条件（表达式结果为True or False）

![[2-oabase-tier-validation-3498-e0fb6718.png]]

- Notify Reviewers on Create：勾选的话，提交审批时候，自动发消息及邮件通知该节点的所有审批者。注意，如果勾选了，不管该节点是不是第一级审批，提交审批时候都会收到邮件通知。**注意**，本模块自带的几个审批通知消息，如下图，不要勾选“隐藏”，则系统自动关注此几个审批通知消息。

- 

![[2-oabase-tier-validation-3498-9c02d4a4.png]]

-

- Comment：勾选的话，审批（同意或拒绝）时候，弹窗填写审批意见。

- Post Approve Action：审批同意时候，调用指定的服务器动作

- Post Reject Action：审批拒绝的时候，调用指定的服务器动作

- Auto Validate：计划任务自动审批本节点。如果该节点没有审批人，默认以计划动作执行的用户作为审批人，如果有一个审批人，默认以该审批人审批，如果有多个审批人，不自动审批。

【实施指南】

参见跟帖

【功能截图】

参见跟帖

## 补充/答案 1

【配置示例】

审批条件写法示例，销售报价单所在的小组组长为当前用户的，条件写法：rec.team_id.user_id.id == rec.env.user.id  如下图所示。

但这个条件不太恰当，系统逻辑是，销售订单创建时候，根据此条件判断，该审批节点是否附加到刚创建的销售订单上。正确的做法是：为每个销售小组组长配置一条审批节点，条件是订单的组长是 该组组长（写死User ID）

![[2-oabase-tier-validation-3498-daded682.png]]

## 补充/答案 2

为每个销售小组组长配置一条审批节点，条件是订单的组长是 该组组长（写死User ID）------------------------复：这样一来，是不是就变成多条节点审批，成了多级审批了？

## 补充/答案 3

例如，配置了5条审批，订单创建时候，订单上的组长是张三，则订单审批节点只会留下张三那条，其他四条不符合条件，不会出现在订单审批流程里面。

## 补充/答案 4

V15版的给用户的操作说明，参考写法【辰海】，给其他客户的话，记得去掉客户相关的敏感信息和目录。

SVN存放：D:\svn\SVN\odoo_ecommerce\06.Customization\辰海智能\addons 文件【灵活审批工作流增加model的扩展操作方法说明.docx】

压缩包文件下载

## 补充/答案 5

【实施指南-开发】

1.  如果希望某表单具有OA审批功能，需要开发一个功能模块，为该表单添加审批功能。开发要点：

2.  继承tier.definition模型的方法 _get_tier_validation_model_names，使得审批节点配置时候，可以选择该表单；

3.  继承表单模型，填写    _state_from、_state_to，表示从_state_from指定的状态跳转到_state_to指定的状态，必须先通过审批流程。控制审批流状态的几个关键字段（可以使用这些字段控制视图上按钮的显示/隐藏）：need_validation（为True表示需要审批，但尚未提交审批），validated（为True表示已经审批通过），rejected（为True表示审批被拒），review_ids（提交审批后，此字段表示审批节点/审批步骤，提交审批前，此字段为空值），reviewer_ids（当前的待审用户ID列表）

4.  继承表单的Form视图，添加审批相关按钮，包括“审批提交”、“审批重置”，以及“同意”、“拒绝”、“转签" 按钮，以及审批步骤列表显示。

5.  开发示例参考 sale_tier_validation

6.  表单Form视图中添加转签按钮的代码如下图示例（注意模块要添加对转签模块base_tier_validation_forward 的依赖）：

![[2-oabase-tier-validation-3498-ded31a88.png]]

【实施指南-配置】

1.  串签：审批人1先审，审过后审批人2再审

2.  会签：审批人1、审批人2不分先后，可以同时审，但两个人都要审

3.  或签：审批人1、审批人2不分先后，但两个人任何一个审了就算过

4.  转签：审批时候，指定另外一个人审批（另外一个人或收到审批请求），而不是自己审。

5.  串签实现方法，各个节点勾选“Approve by sequence”即可，其中Sequence指定审批顺序，数字小的后审。

6.  会签实现方法，不勾选节点的“Approve by sequence“即为会签

7.  或签实现方法，Validated by中指定权限组，参与或签的人都属于该权限组即可

8.  转签实现方法，审批节点勾选“Allow Forward”，表单审批模块中，继承表单Form视图，添加“转签”按钮（参见上述开发篇）

9.  下图示例是销售订单的审批流程配置，主管1和主管2是会签，两人都批过以后，流程到Admin审批（串签）

10. 【已知Bug】文件 base_tier_validation\models\tier_validation.py  方法  def write(self, vals)    该方法中，系统检查，如果没有审批，修改不允许修改的字段则报错。但有一点Bug，导致，即使审批过了，系统仍作检查，使得审批了的单据，修改时候也报错。此Bug修复方法是，上述文件、上述方法中，增加代码 and not rec.validated ，如下面截图

![[2-oabase-tier-validation-3498-0db73e83.png]]

![[2-oabase-tier-validation-3498-cba7ae4d.png]]

【审批效果】

![[2-oabase-tier-validation-3498-98d458d4.png]]

![[2-oabase-tier-validation-3498-d186fc6e.png]]

## 补充/答案 6

![[2-oabase-tier-validation-3498-778e764b.png]]

需要增配一条访问控制权限，否则普通用户无法填写审批意见。

## 补充/答案 7

审批完成时自动执行服务器动作时会报错，提示该单据不存在，需要将层级定义中的审批意见的勾去掉。

![[2-oabase-tier-validation-3498-74acdfe9.png]]

## 补充/答案 8

审批节点设置项注意：

**如果遇到客户有要开启了多公司，请节点设置按公司抬头分开，尤其注意不要按权限组来审批，否则多公司的话，会导致一张单据会有全部这个组内的用户都关注和收到消息提醒，而且有多公司的权限问题。**

## 补充/答案 9

如果开启了多公司间交易的情况下

除了审批层级需要区分公司，还要在单据的过滤条件里加上公司

因为A公司下采购单确认的时候，自动推出的B公司的销售单据B，虽然B单据company_id是B，但是当前用户还在A环境下，所以还是会触发A公司的审批层级

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
