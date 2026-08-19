---
title: "Odoo15新特性开发之触发display_notification气泡消息链接跳转的开发技巧"
source: "http://www.thinkltd.cn/forum/1/odoo15display-notification-936"
forum: "求助台"
author: "杨浔波"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo15新特性开发之触发display_notification气泡消息链接跳转的开发技巧

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:杨浔波 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo15display-notification-936>

实现类似场景应用：

![[1-odoo15display-notification-936-16cdfece.png]]

![[1-odoo15display-notification-936-018853da.png]]

按钮内部的python代码定义如下：

![[1-odoo15display-notification-936-ed8f9526.png]]

```python
    def action_notification(self):
        action = self.env.ref('om_hospital.action_hospital_patient_view')
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': 'Button click %s successfull ',
                'title': _('Click to open the patient record'),
                'type': 'success',
                'links': [{
                    'label': "patient "+self.patient_id.name,
                    'url': f'#action={action.id}&id={self.patient_id.id}&model=hospital.patient&view_type=form'
                }],
                'sticky': False,
            }
        }
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
