---
title: "OCA同时触发多个动作web_ir_actions_act_multi、web_ir_actions_act_view_reload"
source: "http://www.thinkltd.cn/forum/2/ocaweb-ir-actions-act-multiweb-ir-actions-act-view-reload-2831"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA同时触发多个动作web_ir_actions_act_multi、web_ir_actions_act_view_reload

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaweb-ir-actions-act-multiweb-ir-actions-act-view-reload-2831>

模块链接：

This module provides a way to trigger more than one action on ActionManager

To use this functionality you need to return following action with list of actions to execute:

```python
    @api.multi
    def foo():
       self.ensure_one()
       return {
          'type': 'ir.actions.act_multi',
          'actions': [
              {'type': 'ir.actions.act_window_close'},
              {'type': 'ir.actions.act_view_reload'},
          ]
       }

    https://github.com/OCA/web/tree/12.0/web_ir_actions_act_view_reload
    This module provides a way to trigger reload of the current window on ActionManager
```

To use this functionality you need to return following action:

```python
    @api.multi
    def foo():
       self.ensure_one()
       return {
          'type': 'ir.actions.act_view_reload',
       }
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
