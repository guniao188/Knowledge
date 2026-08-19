---
title: "15版本中，财务在登记员工报销时系统提示没有 HR模块的bank_account_id权限的解决方法"
source: "http://www.thinkltd.cn/forum/1/15-hrbank-account-id-900"
forum: "求助台"
author: "葛忠彪"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 15版本中，财务在登记员工报销时系统提示没有 HR模块的bank_account_id权限的解决方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:葛忠彪 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/15-hrbank-account-id-900>

经调查，源码里定义了Hr模型的  bank_account_id 字段需要有 员工/主管 群组的权限
```python
    而这个群组的权限非常大，几乎可以看到员工模块的所有信息，例如工资等
    可以通过写继承的方式，重新定义这个字段只要是内部用户都可以编辑
     class HrEmployee(models.Model):
        _inherit = "hr.employee"
        bank_account_id = fields.Many2one(
            'res.partner.bank', 'Bank Account Number',
            domain="[('partner_id', '=', address_home_id), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",
            groups="base.group_user",
            tracking=True,
            help='Employee bank salary account')

    需要在manifest文件中依赖 hr模型
    "depends": ["hr"],
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
