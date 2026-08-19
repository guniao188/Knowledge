---
title: "基于Odoo在线电子表格实现中国式会计报表"
source: "http://www.thinkltd.cn/forum/3/odoo-3737"
forum: "方案库"
author: "肖相扶"
published: 2023-07-14
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# 基于Odoo在线电子表格实现中国式会计报表

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:肖相扶 | 2023-07-14
> <http://www.thinkltd.cn/forum/3/odoo-3737>

Odoo在线电子表格功能和Excel类似。直接使用Odoo在线电子表格实现中国会计报表要点说明如下：

1.  可以直接将Excel的表格拷贝到在线电子表格（表格式样自动保留）
2.  一个在线电子表格可以插入多个数据源，分别用1, 2, 3等数字引用数据源。如下面截图的资产负债表，有两个数据源，一个是当前的科目余额，一个是去年年末（今年年初）的科目余额。
3.  表格中可以使用各种计算公式（和Excel基本一样），如  =sum(D6:D13)+D14+D16+D17
4.  引用数据源的方法，例如  =ODOO.PIVOT(3,"balance","account_id",284)+ODOO.PIVOT(3,"balance","account_id",287) 表示取数据源 3 中，科目id为284（1024 工商银行-基本户）和287（ 1026 中国银行-一般户 ）的科目余额。
5.  Odoo在线电子表格的原理和用法说明参考：[http://www.thinkltd.cn/forum/1/odoo14-715](http://www.thinkltd.cn/forum/1/odoo14-715) ，以及 [http://www.thinkltd.cn/forum/1/odoo14documents-spreadsheet-754](http://www.thinkltd.cn/forum/1/odoo14documents-spreadsheet-754)
6.  预配好的电子表格，如何快速迁移到别的数据库？可以通过在线电子表格模板导入导出的方法，参见后文跟帖。

![[3-odoo-3737-18b2ed3d.png]]

## 补充/答案 1

在线电子表格模板导入导出方法：

1.  菜单：文档 --> 配置 --> 电子表格模板，列表视图上，改成 create="1"，使得可以创建新的电子表格模板。如下图 

![[3-odoo-3737-749ec02d.png]]

2.  既有的电子表格，可以导出json数据，如下图

![[3-odoo-3737-95b36309.png]]

3.  新建一个模板，上载电子表格的json数据，制作一个新的模板。如下图。可以用本例的中国资产负债表在线表格数据导入测试（将zip包解压后上传） 。

![[3-odoo-3737-4413ecd5.png]]


## 附件

- [[附件/forum/3-odoo-3737-中国资产负债表在线表格.zip|中国资产负债表在线表格.zip]] (3 KB)

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
