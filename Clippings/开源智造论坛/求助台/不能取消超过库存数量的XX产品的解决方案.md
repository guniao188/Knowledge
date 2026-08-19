---
title: "不能取消超过库存数量的XX产品的解决方案"
source: "http://www.thinkltd.cn/forum/1/xx-867"
forum: "求助台"
author: "符赛红"
published: 2025-04-29
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 不能取消超过库存数量的XX产品的解决方案

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2025-04-29
> <http://www.thinkltd.cn/forum/1/xx-867>

有实际业务中会出现一种情况，调度器异常，因存在有偶发的情况下原来有库存，而且被出库单占用锁货了，在没有库存被释放的情况下，直接盘亏了，有可能导致这张原来锁货的发货单，即不能【取消保留】，也无法验证发货，也无法取消发货单，都会提示这个信息：

![[1-xx-867-bbdca14e.png]]

用户即无法出货，也无法取消，那该如何处理呢？

经多次尝试，将该锁货的stock move line的锁货数量直接修改是行不通的，盘点单也无法验证。

正确的做法，可以用服务器动作修正：

第一步，先将这行stock move line的state状态改为【已取消】，cancel

第二步，再将这行stock move line 的state状态改回到原来的状态，并且将锁货数量改到0；

第三步，再找到这张stock picking上，左上角点按钮【取消保留】，就能正常释放出来，能正常操作了。

```python
for r in record:
  r.write({'product_uom_qty':0})--------------------第二步
  r.write({'state':'partially_available'})------------------第二步
```

  # r.write({'state':'cancel'})---------------------------第一步

![[1-xx-867-4d16632d.png]]

这样就能正常操作了。

## 补充/答案 1

此错误原因及修复方法参见：[操作Stock Picking时候"不能取消保留超过库存数量"的错误解析](http://www.thinkltd.cn/forum/1/stock-picking-871)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
