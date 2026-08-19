---
title: "练习：销售Excel打印格式练习"
source: "http://www.thinkltd.cn/forum/1/excel-523"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 练习：销售Excel打印格式练习

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/excel-523>

请将系统自带的PDF销售订单格式，改成Excel格式。具体练习包括：

1) 参照PDF格式，做一个Excel格式

2) 点击打印 动作，下拉框里面增加一个“销售订单(Excel)”选项

3) 点击销售订单上“打印”按钮时候，直接出来Excel格式（而不是本来的PDF格式）

4) 请研究，点击销售订单上的“邮件发送”按钮，可否发送Excel的附件（而不是系统本来的PDF附件）。

5) 上述配置内容，请做成Excel导入

## 补充/答案 1

下载安装第三方模块：D:\oscg-svn\odoo_ecommerce\13.0SRC\report_xlsx

配置：

导入模板，这里上传不了zip文件，已经更新到SVN！！

SVN路径： D:\oscg-svn\odoo_ecommerce\销售Excel打印

![[1-excel-523-dfd0e7a5.png]]

![[1-excel-523-04d887ce.png]]

![[1-excel-523-af1123e9.png]]

![[1-excel-523-e76dc817.png]]

这个为Excel打印模板：

![[1-excel-523-4bfb1e8a.png]]

此为打印结果：

![[1-excel-523-c60d1acf.png]]

5、这里以销售发送邮件为例（上传不了zip文件，所以只能截图）：

首先创建销售Excel打印，然后导入Excel修改发送附件

![[1-excel-523-d803fcca.png]]

![[1-excel-523-36b4fa3c.png]]

Excel导入内容：

![[1-excel-523-ded254e6.png]]

![[1-excel-523-3c7f4436.png]]

![[1-excel-523-98769b39.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
