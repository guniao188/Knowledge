---
title: "【Odoo并发修改问题】&#34;已完成的移动行被纠正&#34; Picking单Bug"
source: "http://www.thinkltd.cn/forum/1/odoo-pickingbug-389"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 【Odoo并发修改问题】&#34;已完成的移动行被纠正&#34; Picking单Bug

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo-pickingbug-389>

再现Bug操作顺序：

1.  两个浏览器，打开同一个就绪状态的Picking单据

2.  其中一个浏览器点击编辑，Picking处于编辑状态。

3.  另一个浏览器点击“验证”，完成该Picking单

4.  之前的浏览器中，完成列随便修改一下，点击“保存”。

5.  Bug出现：已经完成的Picking，初始数量和完成数量被修改。Message区域出现消息“已完成的移动行被纠正”字样。

## 补充/答案 1

评价

经调查，这个问题实际上是并发修改问题，即多人同时修改同一个单据的问题。关于并发修改问题，Odoo官方说了他们的设计决策： 。在ORM层面也有并发修改的检查（models.py方法_check_concurrency ），需要并发修改控制的Model的write方法中，加上下述代码，则该表单即开启了并发修改检查功能。

```python
    @api.multi
    def write(self, vals):
        last_update = {}
        for obj in self:
            id_ref = '%s,%s' % (obj._name, obj.id)
            last_update[id_ref] = obj.__last_update
        self = self.with_context({'__last_update': last_update})
        return super(Model, self).write(vals)
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
