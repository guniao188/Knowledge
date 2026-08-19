---
title: "二开弥补Odoo12条码模块缺陷stock_barcode_show_total"
source: "http://www.thinkltd.cn/forum/2/odoo12stock-barcode-show-total-3147"
forum: "模块库"
author: "施叶寒"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开弥补Odoo12条码模块缺陷stock_barcode_show_total

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:施叶寒 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoo12stock-barcode-show-total-3147>

1. 模块存放位置： SVN\odoo_ecommerce\12.0SRC\stock_barcode_show_total

2. 使用场景： 客户通过条码模块操作调拨单，通过扫码枪扫描的方式增加调拨明细

3. 安装条件： 依赖stock_barcode

4. odoo当前的不足/特性：

```python
    1）对于已存在的调拨明细, 支持超发：验证时没有抛错，只是弹出一个新向导供用户选择是否超发。

    2）系统锁货时，对于按批次/序列号追踪的产品，自动选择一个批次/序列号进行保留，不符合实际出/入库操作习惯。

    3）扫码入库过程中，用户无法从界面得知当前产品的 已完成/计划完成 数量。
```

5. 效果：

```python
    1）禁止用户验证超发、乱发的调拨单：

        a. 存在 完成数量>初始需求 的明细行

        b. 存在 用户手动新增的 详细明细

        c. 存在 用户手动新增的 明细行

    2）允许用户自己扫码时，自动写入新的序列号。

    3）每次扫描后，自动在表单上方更新产品当前出/入库小计
```

6. 实现思路：

```python
    1）action_done（实际验证）之前，odoo会进行大量初始化和判断的操作。_get_overprocessed_stock_moves用于检查是否存在抄送的调拨明细。

        ab. 实际验证前，并不是所有的stock.move.line都存在move_id，所以需要通过product_id对stock_move和stock_move_line进行动态分类（非数据库关联，只是运行时的一对多关联）。

        a. 如果 stock_move的product_uom_qty(趁没有改之前)小于对应stock.move.line的qty_done的总计，抛错。

        b. 如果存在 无法跟stock_move对应的stock_move_line，抛错。

        c. 如果存在origin为空的stock.move（无法在界面上为origin字段赋值），抛错。

    2）渲染页面时，按条件对数据包进行修正。如果扫码界面上的批次号为空，odoo源码会自动写入（而不是新建一行）新条码，即修改了这个明细行的批次号。随后系统将自动调用stock.move的write方法进行原批次的取消保留和新批次的保留。

    3）每次扫码时，系统一定会调用LinesWidget的incrementProduct方法。由于LinesWidget被设计为当前界面(current_page=1)的widget，因此初始化时需要先获取所有页面的数据。随后根据当前barcode进行统计，并反写当前页面。
```

7. 使用方法

```python
    3.1 安装后立即生效

    3.2：

        1）在调拨类型表中，不勾选‘自动保留序列码’（系统默认是勾选的）
```

勾选后该作业类型，在扫码界面将会清空预设条码。

![[2-odoo12stock-barcode-show-total-3147-3036a6da.png]]

```python
      2）通过扫码模块操作调拨单

        3）出库起初，明细行的批次号为空
```

 4）扫描后写入相关批次号，扫描是还会显示当前已扫面产品的数量

    3.3 安装后立即生效

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
