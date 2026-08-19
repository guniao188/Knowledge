---
title: "OCA扫码触发指定动作barcode_action"
source: "http://www.thinkltd.cn/forum/2/ocabarcode-action-2572"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA扫码触发指定动作barcode_action

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocabarcode-action-2572>

模块链接：

This module allows to use barcodes as launchers of actions.

The action will launch a function that uses the barcode in order to return an action.

Actions must be configured with the following data in the context: * model: Model where we can find the method (required) * method: Method to execute (required) * res_id: Id as base (optional)

The method must return an action. Installing this module with demo data will install a demo application that allows the system administrator to find a partner by the external reference encoded in a barcode.

Go to *Settings / Find partners* and scan a barcode that contains the internal reference of an existing partner. As soon as you read the barcode the system will redirect you to that partner's form view.

Technical implementation of this example:

Action:

Python code:

```python
    import json
    from odoo import api, models, _
    from odoo.tools.safe_eval import safe_eval
    class ResPartner(models.Model):
        _inherit = 'res.partner'
        @api.multi
        def find_res_partner_by_ref_using_barcode(self, barcode):
            partner = self.search([('ref', '=', barcode)], limit=1)
            if not partner:
                action = self.env.ref('res_partner_find')
                result = action.read()[0]
                context = safe_eval(result['context'])
                context.update({
                    'default_state': 'warning',
                    'default_status': _('Partner with Internal Reference '
                                        '%s cannot be found') % barcode
                })
                result['context'] = json.dumps(context)
                return result
            action = self.env.ref('base.action_partner_form')
            result = action.read()[0]
            res = self.env.ref('base.view_partner_form', False)
            result['views'] = [(res and res.id or False, 'form')]
            result['res_id'] = partner.id
            return result
```

##


## 原帖外链配图

![[2-ocabarcode-action-2572-x194038c2.png]]
<small>原始地址: /web/image/861/snipaste_20190119_224435.png?access_token=4db9823e-549a-4263-b59b-7c0b0d79edca</small>

![[2-ocabarcode-action-2572-x194038c2.png]]
<small>原始地址: /web/image/863/snipaste_20190119_224617.png?access_token=d8e62c38-c971-48ea-9cc6-8fce6bd05fb1</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
