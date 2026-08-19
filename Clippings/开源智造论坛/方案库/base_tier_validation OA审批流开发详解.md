---
title: "base_tier_validation OA审批流开发详解"
source: "http://www.thinkltd.cn/forum/3/base-tier-validation-oa-3602"
forum: "方案库"
author: "肖相扶"
published: 2022-12-18
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# base_tier_validation OA审批流开发详解

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:肖相扶 | 2022-12-18
> <http://www.thinkltd.cn/forum/3/base-tier-validation-oa-3602>

所有待审批的单据，如purchase.order都必须继承自模型tier.validation，模型tier.validation 中增加了一些和OA审批流相关的方法、字段、属性。

模型tier.validation的重要属性：

```python
        _tier_validation_buttons_xpath = "/form/header/button[last()]"
        _tier_validation_manual_config = True

        _state_field = "state"
        _state_from = ["draft"]
        _state_to = ["confirmed"]
        _cancel_state = "cancel"
```

1.  _tier_validation_manual_config：如果为False，系统通过继承Odoo方法def get_view自动在待审批表单的Form视图上增加审批控制元素。 注意，Odoo15.0及之前的版本，方法是def  fields_view_get 。Form表单上增加的审批控制元素有：按钮”提交审批“、”重置审批“，审批标签”同意“、”驳回“、”审批意见“，审批记录列表。如下截图。 _tier_validation_manual_config 为True的情况（默认为True），则需要自己编写XML继承视图，在Form视图上添加审批控制元素。

![[3-base-tier-validation-oa-3602-96c79605.png]]

2.  截图中的OA审批控制元素，模板id分别为 tier_validation_buttons，tier_validation_label，tier_validation_reviews 。如果希望改变其显示样式，可以在Odoo技术设置的视图中修改。
3.  _tier_validation_buttons_xpath：设置待审批单据的Form视图上，审批按钮（提交和重置）添加位置（自动添加到该参数指定的位置后面），默认是添加到Form上的按钮行的右边。
4.  _state_field, _cancel_state： _state_field 指定待审批表单的状态字段的字段名， _cancel_state指定取消状态是哪个值。
5.  _state_from, _state_to：从哪些状态（ _state_from 指定），跳转到哪些状态（ _state_to 指定），需要审批通过。即，当状态从 _state_from跳转到  _state_to时候，系统检查该表单有没有审批流程，如果有，则提示必须先审批通过，才能跳转状态。跳转时候，系统会以当前用户身份自动提交和审批，自动审批后，还没审批完的情况，系统报错（必须审批通过才能跳转状态）。例如，点击销售订单的确认按钮，如果当前用户是最后一道审批人，则自动审批，自动确认销售订单。

模型tier.validation的重要字段：

1.  review_ids：审批记录列表。根据该表单配置的审批流程，系统自动创建的审批记录。
2.  validated：如果所有的审批记录（ review_ids ）都审批通过，则此值为True
3.  rejected： 如果审批记录（ review_ids ）中，有一个为驳回，则此值为True
4.  can_review：如果当前用户是当前审批人，则此值为True。可用此字段过滤“ 待我审批 ”的单据
5.  next_review：下一条待审批记录的说明（name字段值）
6.  reviewer_ids：当前待审批记录的审批人

模型tier.validation的重要方法：

1.  request_validation：点击“提交审批”按钮对应的方法，此时系统发送base_tier_validation.mt_tier_validation_requested 子类型的通知消息。审批流程节点上勾选了“创建时通知”（字段 notify_on_create ）的节点的审批人都会收到此消息。收到消息的审批人同时自动关注该单据，因而所有审批人会收到该单据随后的各种审批通知（同意、驳回、重置）。
2.  validate_tier：点击“同意”按钮对应的方法，此时系统发送base_tier_validation.mt_tier_validation_accepted子类型的通知消息。单据的关注者都会收到此消息。
3.  reject_tier： 点击“驳回”按钮对应的方法，此时系统发送base_tier_validation.mt_tier_validation_rejected子类型的通知消息。单据的关注者都会收到此消息。
4.  restart_validation： 点击“重置审批”按钮对应的方法，此时系统发送base_tier_validation.mt_tier_validation_restarted子类型的通知消息。单据的关注者都会收到此消息。
5.  _get_under_validation_exceptions： 模型tier.validation 继承了Odoo的write方法，审批中的单据，默认不允许修改任何字段值。但是， 方法 _get_under_validation_exceptions  可以返回允许修改的字段。待审批单据可以继承此方法，增加需要允许修改的字段。当在单据上做某些操作时候，例如上传附件，Odoo背后可能会更新单据的某些字段，如果这些字段未加入到 _get_under_validation_exceptions，则系统报错“The operation is under validation.”，操作失败。此时可以查Odoo日志文件，日志中会输出形如“tier validation: 字段[%s]不在允许修改的字段列表[%s]”的Warning日志，显示试图修改哪个字段而报错，将该字段加入 _get_under_validation_exceptions 即可。

## 补充/答案 1

采购订单(purchase.order)审批代码开发示例，一些关键开发要点，参见代码中注释。

    # -*- coding: utf-8 -*-
```python
    from odoo import models, api

    class TierDefinition(models.Model):
        _inherit = "tier.definition"

        @api.model
        def _get_tier_validation_model_names(self):
            """继承此方法，追加待审批单据的模型名。
            如此，在审批流配置的画面上，才可以选择此模型，配置审批节点
            """
            res = super(TierDefinition, self)._get_tier_validation_model_names()
            res.append("purchase.order")
            return res

    class PurchaseOrder(models.Model):
        _name = "purchase.order"
        _inherit = ["purchase.order", "tier.validation"]

        _state_from = ["draft", "sent", "to approve"]
        _state_to = ["purchase", "done"]
```

        #让系统自动在Form视图上添加审批控制元素
        _tier_validation_manual_config = False
        #_tier_validation_buttons_xpath = "/form/header/button[last()]"
        #_state_field = "state"
        #_cancel_state = "cancel"

        def _get_under_validation_exceptions(self):
            #["message_follower_ids", "access_token"]
            res = super()._get_under_validation_exceptions()
            #此处添加需要在审批过程中修改的字段
            #res.append("state")
```python
            return res

        def request_validation(self):
            res = super().request_validation()
```

            #此处添加提交审批时候的额外处理
```python
            return res

        def validate_tier(self):
            res = super().validate_tier()
```

            #此处添加审批通过时候的额外处理
```python
            return res

        def reject_tier(self):
            res = super().reject_tier()
```

            #此处添加审批驳回时候的额外处理
```python
            return res

        def restart_validation(self):
            res = super().restart_validation()
```

            #此处添加审批重置时候的额外处理
            return res

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
