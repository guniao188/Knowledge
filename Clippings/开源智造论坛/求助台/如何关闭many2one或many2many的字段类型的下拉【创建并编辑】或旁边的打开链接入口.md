---
title: "如何关闭many2one或many2many的字段类型的下拉【创建并编辑】或旁边的打开链接入口"
source: "http://www.thinkltd.cn/forum/1/many2onemany2many-828"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 如何关闭many2one或many2many的字段类型的下拉【创建并编辑】或旁边的打开链接入口

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/many2onemany2many-828>

关闭many2one或many2many的字段类型的下拉【创建并编辑】或旁边的打开链接入口，操作方法：

系统自带的很多这种字段，原生的只要一回车就会创建新的产品或新的位置，导致系统产生很多脏的基础数据，这些地方包括so订单的客户，明细行的产品，产品模板，计量单位；采购订单的供应商，明细行的产品，计量单位，以及仓库内部调拔的明细行的产品，来源位置，目的位置，及调拔单的Move上的产品及位置，picking表头的位置，以及盘点表上的产品及位置及盘点明细上的产品入口，还有bom及mo，及会计的Invoice及bill及payment等常见表单上的这些产品、业务伙伴的数据，很容易用户操作错误产生不必要的数据，故一般在上线之前，都会关闭这些入口。

继承视图示例：针对报废菜单的下拉产品界面Odoo Studio: stock.scrap.form customization

    {"no_create":true,"no_edit":true}

对于picking单上关闭Picking及move和move line的示例：

继承视图的写法：Odoo Studio: stock.picking.form customization

    {"no_create":true,"no_edit":true}

实际控制这个入口的主要参数：options="{'no_create': True, 'no_edit': True}" 如果还要控制不能链接打开，尤其是涉及外部用户权限时，为了防止链接点入，还可以加上options="{'no_create': True, 'no_edit': True,'no_open': True}"

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
