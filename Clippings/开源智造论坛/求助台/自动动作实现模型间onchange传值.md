---
title: "自动动作实现模型间onchange传值"
source: "http://www.thinkltd.cn/forum/1/onchange-606"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 自动动作实现模型间onchange传值

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/onchange-606>

【需求背景】

1.  通过界面配置方式，在产品上增加了一些字段(x_ 开头)

2.  通样通过界面配置的方式，在生产单上也增加了一些几乎同样的字段

3.  生产单上选择产品时候，希望将产品上的字段值自动带到生产单上对应字段上（自动触发 产品的 onchange 事件）

【实现方法】

1.  Odoo 13.0的自动动作（安装模块 base_automation），可以配置onchang 的python代码

2.  onchang 代码形式如下（通过 action 返回 value, warning, domain  三个onchang 值）：

# Available variables:
#  - env: Odoo Environment on which the action is triggered
#  - model: Odoo Model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - Warning: Warning Exception to use with raise
# To return an action, assign: action = {...}

```python
action = {
  "value": {
      'x_zhuzi': record.product_id.x_zhuzi,
      'x_drawing': record.product_id.product_drawing.id,
      'x_mm_product_id': record.product_id.x_mm_product_id.id,
      'x_maokou': record.product_id.x_maokou,
      'x_jiaokou': record.product_id.x_jiaokou,
    },
  "warning":{
    "title":"Warning",
    "message": "Are you OK?",
  },
  "domain": {
    "sale_order_id": [('id', 'in', sale_orders.ids)],
  },
}
```

【示例截图】

![[1-onchange-606-92f69f3e.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
