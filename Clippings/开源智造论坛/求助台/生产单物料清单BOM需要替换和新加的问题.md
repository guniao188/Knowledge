---
title: "生产单物料清单BOM需要替换和新加的问题"
source: "http://www.thinkltd.cn/forum/1/bom-236"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 生产单物料清单BOM需要替换和新加的问题

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/bom-236>

业务背景：

针对一些生产企业，实际业务中，尤其是定制化的产品，且有启用变体，存在多种属性参数，在配置BOM物料清单时，需要至少配好主物料的比例，但主物料明细选择具体的SKU，当这个BOM中只能明确到需要SKU的某些参数，而其他参数需要等到生产时，才能明确时，就需要用到物料的替换。物料清单虽在V12版本中，可以在MO生产单上再解锁新增，但并不能替换原来BOM的主物料。

比如：要生产一个双开门的柜子，主物料BOM中需要至少告诉生产单位，这个尺寸的柜子用到的门板是多长多宽，即门板是主物料，同时，因为颜色等变量属性是有很多选择的，颜色这些属性需要在实际生产这个产品时才能明确。

如果笼统的，全部到MO生产单时再加，就会导致做这张MO生产单，还得一个个去查这个产品是要配多少尺寸的，非常麻烦，而且生产部门的人与整理BOM的人是不同岗位的，且这个门板还是属于BOM的基础物料。

求解决方案，哪怕是二开。

## 补充/答案 1

研究一下OCA模块 BOM替代料：

可行的话截图加入模块库中。

This module allows the user to specify non-equivalent products to a part on a BOM.

Other modules can assume that products in the same category are equivalent and can be used in a Manufacturing Order if the main part is not available. Those non-equivalent products can be excluded.

这个模块看上去也不错，一起测试一下：

This module adds the location field to the Bill of Materials and its components. This may be useful to distinguish between different BoMs for the same product or to highlight the preferred locations to fetch the components from.

The location appears in the BOM Structure Report.

## 补充/答案 2

解决思路1：是改MO的解锁逻辑，允许修改已经自动带出来的BOM明细，即替换原来的物料；目前是不可调整的，只能新增，是否改下这个逻辑，放开允许修改原料的产品，改动量有多少？

解决思路2：将BOM中需要用到的这种无法固定到全部参数的产品，新加一个虚拟产品，为可消耗类型这个产品不固定的属性都可以配在这个可消耗的产品里面，在MO下单时，自动能带出来有些什么基础物料，因消耗类是不管理库存的，故可以再加实际需要的具体SKU。但这个方案会导致产品管理难度上升，而且容易出错，SKU也会特别多，相当于要翻倍了。

解决思路3：将BOM配置时，配一个该尺寸相应的SKU，但颜色先任意指定一个，待实际生产时，再去MO上新加实际的，但需要放开限制，需要允许删除明细行的物料，可以将原来的某行点【删除】。

或者研发还有更好的其他解决思路吗？

如果以上也可行，那哪一种最方便省力？

## 补充/答案 3

190714更新

新的解决方案：

V12企业版MO允许部分生产入库，部完已完成的，可以发布库存

同时，在操作【记录生产】时，填写多少完工成品数量，底下物料原料明细行，会随着成品数量依BOM配比自动变动，

对于替换问题，可以有个最简单的处理办法，即在【记录生产】时弹窗页面视图，将【初始数量】【保留数量】【完成数量】可以将未使用到的料件数量改成0，且也只是针对这个已可完工的成品使用到的原料数量进行编辑修改，同时允许【添加明细】，即实现将需要被替换的料件改为0取消，新加替换的新物料即可实现替换。

改这张视图：数量可供编辑修改即可。

    MRP Product Produce
    外部ID：mrp.view_mrp_product_produce_wizard

## 补充/答案 4

至于针对批量想更新某个料件成新的物料，比如A原料，在N多个BOM中都有用到，如何批量更新？

更新后的bom只对新生成的MO生效。

简单解决方案：

将bom.line明细单独放菜单出来，用户界面搜索A原料名称或产品编码，可以快速过滤出全部用到该原料的所有BOM，全部勾选，点中间【动作/批量更改料件】，弹窗，显示【替换新料件产品】，【配比数量】，点【确认】按钮，即执行，批量将该新选择的产品，全部替换到所勾选到的这些bom明细行中。

简单开发增加按钮。

---

不过，这么简单处理仍然解决不了一个问题：即同一颜色同成本的产品在BOM中可以任意选择，到mo时能快速的更改同一品种及价位的产品替换。而需要全部统统在bom中先指定好。

OCA的模块待测试。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
