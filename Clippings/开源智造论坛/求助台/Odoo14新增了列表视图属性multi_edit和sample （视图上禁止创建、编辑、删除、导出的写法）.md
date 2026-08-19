---
title: "Odoo14新增了列表视图属性multi_edit和sample （视图上禁止创建、编辑、删除、导出的写法）"
source: "http://www.thinkltd.cn/forum/1/odoo14multi-editsample-662"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo14新增了列表视图属性multi_edit和sample （视图上禁止创建、编辑、删除、导出的写法）

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo14multi-editsample-662>

如下图，Odoo14的视图上，可以使用的属性有 multi_edit、create、delete、duplicate、edit、export_xlsx、sample

![[1-odoo14multi-editsample-662-161b803e.png]]

各属性控制的显示效果如下图：

![[1-odoo14multi-editsample-662-4e127168.png]]

![[1-odoo14multi-editsample-662-473ac7d8.png]]

其中 multi_edit、sample是14.0版新增的。multi_edit表示，在列表视图勾选后，可以直接在列表视图上进行编辑，不勾选点击记录，则跳转到Form视图进行编辑。在以前的版本中，列表视图上定义 editable可以实现编辑，但不能跳转到Form视图。新版本既可以列表编辑，又可以跳转到Form视图编辑。

sample表示，如果该模型没有数据，则显示演示数据（Sample数据）显示效果如下图。Sample数据来自 Mock Server服务器（而不是生产服务器）。

![[1-odoo14multi-editsample-662-96b5c3b3.png]]

## 补充/答案 1

似乎导出不起作用啊

![[1-odoo14multi-editsample-662-d9ecdcbd.png]]

普通用户进入后，仍是可以导出的

![[1-odoo14multi-editsample-662-12d35654.png]]

经检查，发现是因为有一个专用的权限组，所有内部用户都有默认勾选的原因，去掉勾选就可以限制到导出功能了。

![[1-odoo14multi-editsample-662-8e2a03f1.png]]

## 补充/答案 2

records_draggable="0"   可以在看板视图中维护，然后不能进行拖拽

![[1-odoo14multi-editsample-662-dd27568b.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
