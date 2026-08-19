---
title: "二开手工修改MO原料模块mrp_manual_production"
source: "http://www.thinkltd.cn/forum/2/momrp-manual-production-3106"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开手工修改MO原料模块mrp_manual_production

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/momrp-manual-production-3106>

模块链接：OSCG_SVN\odoo_ecommerce\11.0SRC\mrp_manual_production

12.0版：OSCG_SVN\odoo_ecommerce\12.0SRC\mrp_manual_production   12.0版将“原料确认”按钮改名成“计划下达”，去掉了原料明细修改功能，而是改成利用Odoo自带的原料明细修改功能。

1）Bug修正，参考：https://www.zhiyunerp.com/forum/erp-1/question/534 此Bug摘录如下（不确定是否12.0依旧存在此Bug）：

一个成品有三个部件，三个部件需要分别生产。成品MO保存时候，系统自动创建三个部件的MO，并根据配置好的物流路径同时生成领料单。但有个问题，生成的领料单的group_id都是成品MO的单号，结果成品和三个部件的领料单都被合并成一个大领料单了。三个部件是依次生产，因而领料也需要分开依次领，应该可以通过配置决定是合并（BoM小，生产周期短的MO），还是不合并（生产周期长，依次生产的MO）。

经查，Odoo此处有Bug，物流路径的字段group_propagation_option本可以配置是否自动传递group_id，但系统创建部件MO的时候，没有查看该字段，而是简单地将group_id传递下去了。下述代码修正此Bug（文件 addons\mrp\models\procurement.py）。

```python
    def _prepare_mo_vals(self, bom):
        """Bug修正：
        应该根据Procurement Order上的Rule规则的设置，决定是否传递group_id给MO
        """
        group_id = self.group_id and self.group_id.id or False
        if self.rule_id:
            if self.rule_id.group_propagation_option == 'fixed' and self.rule_id.group_id:
                group_id = self.rule_id.group_id.id
            elif self.rule_id.group_propagation_option == 'none':
                group_id = False
```

2）Odoo在MO保存时候，自动根据BoM展开原料Stock Move，并自动Confirm Stock Move
3）实际生产中，有时候需要按标准BoM展开原料后，需要手工修改（修改、增加、删除原料Stock Move），而后再Confirm原料Stock Move。
4）本模块在BoM上增加了一个“原料自动确认”标志，该标志默认值为True，如果设置为False，则MO保存时候，系统会展开MO的原料，但不会自动确认原料Stock Move，而是要另外点击按钮“原料确认”。如此，因而有机会对原料Stock Move进行增删改。
5）MO的投料明细上，增加按钮“添加原料”，可以添加BoM上没有的原料


## 原帖外链配图

![[2-momrp-manual-production-3106-x194038c2.png]]
<small>原始地址: /web/image/1924/mo1.png?access_token=912a271c-01da-43f8-a091-83a9f4f219d8</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
