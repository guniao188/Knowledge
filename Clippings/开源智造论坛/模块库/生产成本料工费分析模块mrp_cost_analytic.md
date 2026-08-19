---
title: "生产成本料工费分析模块mrp_cost_analytic"
source: "http://www.thinkltd.cn/forum/2/mrp-cost-analytic-4023"
forum: "模块库"
author: "肖相扶"
published: 2025-01-06
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 生产成本料工费分析模块mrp_cost_analytic

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2025-01-06
> <http://www.thinkltd.cn/forum/2/mrp-cost-analytic-4023>

模块链接：OSCG_Git\18.0\extra-addons\mrp_cost_analytic

【模块功能】

1.  分析产成品的成本价格中，其中料费、工费、其他费分别占多少。分析逻辑如下：
```python
    先计算BoM层级为2的产品的当月入库价格中的料、工、费
    再计算BoM层级为3的产品的当月入库价格中的料、工、费。产品BoM中，用到了层级2的原料时候，该原料的料、工、费分别计入上级产品(层级3产品)的料工费。
    再计算BoM层级4的产品，如此类推。
```

2.  基于当期的MO及半成品MO计算料工费。MO上投入的组件中，本级或子级BoM中，所有原材料（采购料，BoM层级为1的产品）都归集到料费中。制造费用分摊中，本级或子级BoM中，按“工时”分摊的费用，都归集到工费中， 按“机时”分摊的费用，都归集到机费中。MO上的额外费用(外协费)、工序费（工作中心价格乘以工序加工时间），都归集到其他费用。
3.  增加菜单“会计 --> 存货 --> 生产成本分析”，增加生产成本计算表单。
4.  依赖模块： [产品的BoM层级设置模块mrp_bom_level](http://www.thinkltd.cn/forum/2/bommrp-bom-level-4021)

【功能截图】

![[2-mrp-cost-analytic-4023-7cfad8c2.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
