---
title: "Odoo锁货（保留）原理"
source: "http://www.thinkltd.cn/forum/3/odoo-3609"
forum: "方案库"
author: "肖相扶"
published: 2022-12-20
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# Odoo锁货（保留）原理

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:肖相扶 | 2022-12-20
> <http://www.thinkltd.cn/forum/3/odoo-3609>

Stock Picking上点击“检查可用”按钮，系统背后完成锁货（保留）动作。其内部原理如下：

1.  逐条调用stock.move的方法 _action_assign 锁货
2.  如果stock.move的源库位不要做库存管理的库位，或者不是可库存商品，则直接创建stock.move.line完成锁货
3.  不要做库存管理的库位 包括：虚拟库位 'supplier', 'customer', 'inventory', 'production'，报废库位，没有设置公司的transit 库位
4.  如果是按包装规格发货，且产品分类上“ 预留包装（ packaging_reserve_method ）”设置的是full（整包装出货），则自动调整锁货数量到该产品的整包装的整数倍。
5.  按下架策略锁定出货的Quant（方法 _update_reserved_quantity） 。方法 _update_reserved_quantity 的重要参数说明如下：
6.  1.  lot_id：锁货批次
```python
        package_id：锁货包裹
    2.  owner_id：锁货货主
    3.  strict：True表示只出源库位的库存（不含子库位库存），False则包含子库位库存。默认为False
```

7.  实际上，stock.move上没有批次字段，因而系统实际上没法按批次锁货。但可以设置stock.move上的 package_level_id 字段，实现按包裹锁货。

指定包裹、批次、货主 锁货的参考代码（服务器动作中测试）

```python
    mv = env['stock.move'].browse(126)
    mv._do_unreserve()

    lot_id = env['stock.lot'].browse(4)
    package_id = False
    owner_id = False

    available_quantity = mv._get_available_quantity(mv.location_id, lot_id=lot_id, package_id=package_id, owner_id=owner_id)
    if available_quantity > 0.00001:
      mv._update_reserved_quantity(mv.product_uom_qty, available_quantity, mv.location_id, lot_id=lot_id, package_id=package_id, owner_id=owner_id, strict=False)
      mv._recompute_state()
```

      #mv.mapped('picking_id')._compute_state()

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
