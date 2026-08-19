---
title: "Odoo13 searchpanel实现原理"
source: "http://www.thinkltd.cn/forum/1/odoo13-searchpanel-437"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo13 searchpanel实现原理

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo13-searchpanel-437>

如下图，在Odoo 13的会计科目列表视图中，左边有一个快速搜索工具 searchpanel :

![[1-odoo13-searchpanel-437-73fcb0e1.png]]

## 补充/答案 1

searchpanel的字段 root_id 是关联到一个上下级关系的搜索表，界面上显示的 1,10,11等是该搜索表里面的记录。以本例说明，account.root是一个数据库视图，其第一级记录值构成是，id是会计科目code的第一位，name也是会计科目的第一位，parent_id为NULL。其第二级记录值构成是，id是会计科目code的第一位乘以1000 加上 会计科目第二位构成，其name 字段是会计科目code的前两位，其parent_id则是对应的第一级记录（会计科目code第一位的account.root记录）

root_id = fields.Many2one('account.root', compute='_compute_account_root', store=True)

```python
class AccountRoot(models.Model):
    _name = 'account.root'
    _description = 'Account codes first 2 digits'
    _auto = False

    name = fields.Char()
    parent_id = fields.Many2one('account.root')
    company_id = fields.Many2one('res.company')

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute('''
            CREATE OR REPLACE VIEW %s AS (
            SELECT DISTINCT ASCII(code) * 1000 + ASCII(SUBSTRING(code,2,1)) AS id,
                   LEFT(code,2) AS name,
                   ASCII(code) AS parent_id,
                   company_id
            FROM account_account WHERE code IS NOT NULL
            UNION ALL
            SELECT DISTINCT ASCII(code) AS id,
                   LEFT(code,1) AS name,
                   NULL::int AS parent_id,
                   company_id
            FROM account_account WHERE code IS NOT NULL
            )''' % (self._table,)
        )
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
