---
title: "外协加工/委外生产方案详解及外协加工模块 mrp_wo_subcontracting"
source: "http://www.thinkltd.cn/forum/2/mrp-wo-subcontracting-3355"
forum: "模块库"
author: "肖相扶"
published: 2025-02-21
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 外协加工/委外生产方案详解及外协加工模块 mrp_wo_subcontracting

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2025-02-21
> <http://www.thinkltd.cn/forum/2/mrp-wo-subcontracting-3355>

【2024年09月13日备注】Odoo17对应的模块参考  [Odoo17工序外协采购模块mrp_subcontracting_operation](http://www.thinkltd.cn/forum/2/odoo17mrp-subcontracting-operation-3974)

【业务背景】

1.      外协加工有两种情况，一种是成品/部件的委外生产，就是提供原料，委外商加工成部件/成品；一种是某道工序的外协加工，例如电镀工序。工序外协加工的情况，外协加工不改变产品，出去和回来的都是同一个产品。

2.      在SAP R3中，前者叫库存外协（委外加工），后者叫工序外协。参考学习：

3.  在用友NC中，前者叫带料委外，后者叫工序外协。参考学习：

4.  Odoo13\.0中，前者有现成功能模块[/forum/2/question/odoo13-0-mrp-subcontractingmrp-subcontracting-account-3183](http://www.thinkltd.cn/forum/2/question/odoo13%5C%5C%5C%5C-0%5C%5C%5C%5C-mrp%5C%5C%5C%5C-subcontractingmrp%5C%5C%5C%5C-subcontracting%5C%5C%5C%5C-account%5C%5C%5C%5C-786)，后者有第三方插件\\

5.  产能不足时候才外协，处理方法参考：[/forum/2/question/mo-mrp-not-confirm-3369](http://www.thinkltd.cn/forum/2/question/mo%5C%5C%5C%5C-mrp%5C%5C%5C%5C-not%5C%5C%5C%5C-confirm%5C%5C%5C%5C-1255)

【外协加工功能设计】

1.  新开发工序外协模块mrp_wo_subcontracting

2.  工作中心上增加一个勾选项“外协”，如果勾选，填写外协供应商、外协产品（Service产品）、单价、发料Picking\\ Type、收料Picking\\ Type

3.  工序单（WO）上增加按钮“外协”，当WO的工作中心上勾选了外协，显示“外协”按钮，点击按钮，自动创建外协PO，外协发料Picking、外协收料Picking

4.  实现界面参考第三方插件\\ [https://apps.odoo.com/apps/modules/12.0/de_mrp_subcontracting/](https://apps%5C%5C%5C%5C.odoo%5C%5C%5C%5C.com/apps/modules/12%5C%5C%5C%5C.0/de_mrp_subcontracting/)

【svn路径】

    SVN\odoo_ecommerce\13.0SRC\mrp_wo_subcontracting

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
