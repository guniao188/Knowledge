---
title: "长捷导入bom及裁切下料使用说明"
client: 长捷
type: 项目文档
phase: 上线期
yuque_url: "https://www.yuque.com/xinsuixiaoyao-degek/klxky6/oclsswfnrhserwae"
yuque_slug: "oclsswfnrhserwae"
tags: [Odoo, 上线期, 制造, 培训, 完成实施, 客户/长捷, 导入]
created_at: "2024-11-28T07:38:30.000Z"
updated_at: "2024-11-28T07:50:11.000Z"
published_at: "2024-11-28T07:50:11.000Z"
---
# 长捷导入bom及裁切下料使用说明

1、导入原材料，原材料名称为钢材名称+规格，示例：圆钢Q235B-D20

若产品需要按批次追溯，且领料时根据图号去锁批次，则需要勾选：按批次追溯和需要图号

![image](_附件/1732779761636-41165358-33c3-4671-9f8f-36-bc8c9ccebdec2a67.png)![image](_附件/1732779774880-9b0ce608-a6e9-45e1-924c-8a-4713a70b8475ced9.png)

注：可直接在车间使用的不需要勾选图号自动锁货，仅需要下料切割的需要勾选

效果如下：![image](_附件/1732779830670-80241dd7-226e-4a1e-b613-36-948038539f1ae17c.png)


2、导入bom创建产品、bom、工序及下料切割

路径：库存--配置--导入bom

Excel File：上传附件

Server Action：选择导入excel创建产品及BOM 或选择消耗原批次、创建新产品

![image](_附件/1732779959257-02461b10-2e49-4ee3-aa3f-00-6e8e60622a30704d.png)

说明：应当在导入bom之前建立原材料产品的基础数据，且名称需要按照圆钢Q235B-D20这种示例要求。创建bom时根据名称进行匹配，若匹配不到，则创建新的产品。所以要求产品命名需要两边一致。
