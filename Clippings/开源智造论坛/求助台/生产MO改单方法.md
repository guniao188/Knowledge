---
title: "生产MO改单方法"
source: "http://www.thinkltd.cn/forum/1/mo-762"
forum: "求助台"
author: "肖相扶"
published: 2022-12-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 生产MO改单方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-16
> <http://www.thinkltd.cn/forum/1/mo-762>

【业务背景】

SO MTO引发生产MO，MO引发缺料采购。此过程中，由于种种以外，可能要求修改生产用料。触发修改的节点可能有：

1.  生产计划时候发现BoM有错误，要求修改MO

2.  采购过程中，市场因素，某些原料不好采购，要求替换成别的原料

3.  生产过程中，发现某些原料不合适，要求修改成别的原料

上述生产改单情况，系统如何处理？

【操作方法】

1.  生产计划时候要求修改MO用料。此种情况，由于SO确认时候，系统自动创建生产MO，且自动确认此MO。实际业务，系统创建好MO后，不应自动确认，而是留给生产计划人员（PMC）计划排好后再手工确认。因为没有确认，生产计划时候可以任意修改MO。系统创建MO后不自动确认，需要安装此插件：[/forum/2/question/mo-mrp-not-confirm-3369](http://www.thinkltd.cn/forum/2/question/mo-mrp-not-confirm-3369)

2.  缺料采购时候要求修改MO用料。此插件（参照：[/forum/2/question/mrp-substitionspurchase-split-substitions-3396](http://www.thinkltd.cn/forum/2/question/mrp-substitionspurchase-split-substitions-3396)）提供了采购明细行分拆功能，可以按替代组分拆采购，分拆后，系统自动修改MO上的投料明细（Stock Move），以及生产领料Picking的Stock Move。具体操作方法是，需要修改原料时候，创建一个替代组，将原来的原料、要替换的新原料，都加入该替代组，而后分拆采购明细，将原来的采购原料数量改为0，替代料数量改为采购数量。如此，系统会自动在MO、生产领料Picking上添加替代料的Stock Move。

3.  生产过程中要求修改MO用料。已确认的MO上，可以添加投料明细行，系统会自动确认新添加的Stock Move，自动触发生产领料和缺料采购，但系统不支持减少数量，或删除原来明细。减少数量、被替换的原料的处理，可以在生产领料，或生产报工时候，原来的料（被替代的料），生产实际消耗数量填写0，再退回仓库。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
