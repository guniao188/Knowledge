---
title: "Odoo18创建产品的坑：追踪库存(is_storable)默认无值"
source: "http://www.thinkltd.cn/forum/1/odoo18-is-storable-4018"
forum: "求助台"
author: "肖相扶"
published: 2024-12-27
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo18创建产品的坑：追踪库存(is_storable)默认无值

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-12-27
> <http://www.thinkltd.cn/forum/1/odoo18-is-storable-4018>

1.  Odoo18的采购、销售模块下的产品菜单中创建产品，追踪库存(is_storable)字段默认为False，也就是不追踪库存，这使得入库、出库时候，系统不创建对应的库存计价(stock.valuation.layer)
2.  但是在 库存、制造模块下的产品菜单中创建产品，追踪库存(is_storable)字段默认为True。

## 补充/答案 1

就和老版本产品类型默认是可消耗一样，V18的不追踪其实就是消耗品，

技术创建新数据库后，实施通常都会对各环节常用的默认值进行设置

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
