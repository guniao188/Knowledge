---
title: "二开产品图纸管理模块mrp_plm_drawing"
source: "http://www.thinkltd.cn/forum/2/mrp-plm-drawing-3338"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开产品图纸管理模块mrp_plm_drawing

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/mrp-plm-drawing-3338>

模块位置：OSCG_SVN\odoo_ecommerce\13.0SRC\产品图纸管理\mrp_plm_drawing

【模块功能】

1.  产品表单上增加图号product_drawing字段(many2one到图纸附件)；

2.  库存模块的主数据菜单下，增加图纸菜单，显示产品图纸类附件列表；图纸类附件的 res_field 字段含有字样“product_drawing”

3.  库存模块的主数据菜单下，增加文件批量上传，生成图纸附件功能；

4.  文件上传利用功能使用 fine-uploader 组件实现，该组件说明文档参考：

【功能截图】

产品上增加图纸字段，库存主数据增加图纸菜单，及图纸上传菜单

![[2-mrp-plm-drawing-3338-92bd156a.png]]

基于 fine-uploader 组件实现的多个图纸文件批量上传功能。可以多选文件，可以拖拽文件上传。上传后，系统自动以文件名作为附件名，附件res_field 字段自动填写 product_drawing:qquuid  字样，其中 qquuid将用于文件删除。即在 fine-uploader 文件上传组件上点击“删除”按钮，系统将根据该qquuid 查找附件并删除。

![[2-mrp-plm-drawing-3338-dd536a3c.png]]

## 补充/答案 1

功能存在一个问题，只有“系统管理/设置”群组的人，才能上传图纸。目前问题已由施叶寒修复，模块已跟新SVN

## 补充/答案 2

这个功能只做了一半，只能上传，不能和产品绑定自动识别啊。

还得再改造建立之间的关系

## 补充/答案 3

批量上传图纸功能有问题，上传报错。

![[2-mrp-plm-drawing-3338-866c0982.png]]

![[2-mrp-plm-drawing-3338-0d50fa13.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
