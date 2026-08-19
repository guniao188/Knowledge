---
title: "Odoo中one2many、many2many的操作"
source: "http://www.thinkltd.cn/forum/1/odooone2manymany2many-432"
forum: "求助台"
author: "肖相扶"
published: 2023-11-09
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo中one2many、many2many的操作

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-11-09
> <http://www.thinkltd.cn/forum/1/odooone2manymany2many-432>

【20220103更新】Odoo15中，提供了对应方法替换下述数字命令：

from odoo import Command

1.  Command.create(cls, values: dict)  等同于 (0, 0, values)

2.  wave.picking_ids = [Command.link(picking.id)]   #等同于 [ (4, picking.id, 0) ]
    update(cls, id: int, values: dict)  等同于 (1, id, values)

3.  delete(cls, id: int)  等同于 (2, id, 0)

4.  unlink(cls, id: int) 等同于 (3, id, 0)

5.  clear(cls) 等同于 (5, 0, 0)

6.  set(cls, ids: list) 等同于 (6, 0, ids)

many2many

(0,0,{values}) 根据values里面的信息新建一个记录。

(1,ID,{values})更新id=ID的记录（写入values里面的数据）

(2,ID) 删除id=ID的数据（调用unlink方法，删除数据以及整个主从数据链接关系）

(3,ID) 切断主从数据的链接关系但是不删除这个数据

(4,ID) 为id=ID的数据添加主从链接关系。

(5) 删除所有的从数据的链接关系就是向所有的从数据调用(3,ID)

(6,0,[IDs]) 用IDs里面的记录替换原来的记录（就是先执行(5)再执行循环IDs执行（4,ID））

例子[(6, 0, [8, 5, 6, 4])] 设置 many2many to ids [8, 5, 6, 4]

one2many

(0, 0,{ values })根据values里面的信息新建一个记录。

(1,ID,{values}) 更新id=ID的记录（对id=ID的执行write 写入values里面的数据）

(2,ID) 删除id=ID的数据（调用unlink方法，删除数据以及整个主从数据链接关系）

## 补充/答案 1

二个常用的示例：

------------------------服务器动作，写many2many字段更改值，会计分析标签批量添加到银行类科目。4代表新加，1代表标签值id
for r in records:
        r.write({'analytic_tag_ids':[(4,1)]})
--------------------------------------------3代表移除，后面的是移除的id，产品上的路线批量操作。
```python
for r in records:
        r.write({'route_ids': [(3,1)]})
        r.write({'route_ids': [(3,5)]})
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
