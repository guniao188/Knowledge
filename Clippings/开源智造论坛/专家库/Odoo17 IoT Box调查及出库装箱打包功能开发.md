---
title: "Odoo17 IoT Box调查及出库装箱打包功能开发"
source: "http://www.thinkltd.cn/forum/5/odoo17-iot-box-3890"
forum: "专家库"
author: "吴键"
published: 2024-02-23
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/专家库
---

# Odoo17 IoT Box调查及出库装箱打包功能开发

> [!info] 来源
> 开源智造论坛 · 专家库 | 作者:吴键 | 2024-02-23
> <http://www.thinkltd.cn/forum/5/odoo17-iot-box-3890>

【出库打包功能研发】

参考资料：

1.   [IoT | Overview | Odoo](https://www.odoo.com/app/iot)
2.   [IoT Box &amp; Odoo说明文档](http://www.thinkltd.cn/forum/1/iot-box-odoo-3848)
3.   [Internet of Things (IoT) — Odoo 17.0 documentation](https://www.odoo.com/documentation/17.0/applications/productivity/iot.html)

业务场景：

1.  扫码出库单，界面显示出库单内容
2.  扫码商品，界面高亮显示出库单上商品明细行，出库数量加1，商品装入箱子（箱子预先放于电子秤上）。
3.  箱子装满，点击按钮“打包”，系统自动 从电子秤上获取箱重，打包（创建包裹），箱重写入包裹。
4.  换空箱，继续扫码商品，装箱，打包。
5.  整单装箱完成，点击“箱标打印”，系统自动打印该出库单的包裹标签，按包裹号顺序打印，有几个包裹打印几个标签。箱标上要显示箱子内容（产品、数量）、箱重、箱号(第几箱/总箱数)。箱标通过IoT Box直接打印（而不是先生成PDF再点击打印）。

技术方案：

1.  硬件配置：树莓派五代、USB扫码枪、标签打印机、电子秤
2.  安装Odoo 17版本，以及扫码模块(stock_barcode)
3.  树莓派上安装Odoo IoT相关功能模块，安装电子秤驱动、标签打印机驱动
4.  打包时候，Odoo操作页面连接IoT Box，从电子秤上获取包裹重量；调用Odoo后台代码创建包裹
5.  箱标打印时候，调用包裹标签打印功能，标签通过IoT Box连接打印机打印标签。

---

相关:[[Clippings/开源智造论坛/专家库/00-专家库索引.md|← 专家库索引]]
