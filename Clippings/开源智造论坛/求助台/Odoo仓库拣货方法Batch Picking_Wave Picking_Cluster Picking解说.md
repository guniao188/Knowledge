---
title: "Odoo仓库拣货方法Batch Picking/Wave Picking/Cluster Picking解说"
source: "http://www.thinkltd.cn/forum/1/odoobatch-picking-wave-picking-cluster-picking-3989"
forum: "求助台"
author: "肖相扶"
published: 2024-10-21
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo仓库拣货方法Batch Picking/Wave Picking/Cluster Picking解说

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-10-21
> <http://www.thinkltd.cn/forum/1/odoobatch-picking-wave-picking-cluster-picking-3989>

仓库各种拣货方法的业务解说参考： [免费开源Odoo软件如何实现电商仓库高效发货](http://www.thinkltd.cn/forum/4/odoo-3990)

【Batch Picking】

1.  多个仓库单据合并拣货，称之为Batch Picking。对应到中文说法，可以称之为“按订单的波次拣货”。以发货单为例，Odoo中勾选多个发货单，合并为一个Batch。
2.  Batch单打印的PDF上，显示被合并的发货单的作业明细(stock.move.line)，仓库作业员可以按此单一次性拣选多个发货单。
3.  扫码模块中，打开Batch单，界面上显示被合并的发货单的作业明细，仓库作业员可以一次性完成多个发货单的拣货。
4.  Batch的典型应用场景：将多个单合并为一个Batch，按Batch分配拣货员。

【Wave Picking】

1.  从多个仓库单据的作业明细(stock.move.line)中，勾选部分明细，归集到一个Wave。对应到中文说法，可以称之为“按作业明细的波次拣货”。
2.  在Odoo中，归集到Wave的时候，系统会自动拆分作业单。例如，作业单OUT/0001上有两个明细行，当其中一个明细行归集到Wave的时候，系统自动将OUT/0001拆分为OUT/0001和 OUT/0002两个作业单。
3.  Wave的典型应用场景：大面积仓库中，分区域拣货。例如张三负责A区货架的拣货，李四负责B区货架的拣货。将多个发货单中，源库位为A区的归为一个Wave，张三负责拣货；源库位为B区的归为另一个Wave，由李四负责拣货。

【Cluster Picking】

1.  在Batch的基础上，增加按订单分拣的操作，称之为Cluster Picking。操作方法上，例如，将8个发货单合并为Batch，分配给张三负责拣货。张三推着拣货车开始拣货，如果拣货车上只有一个大容器，8个订单的货都混在大容器里面，这个是Batch Picking。如果拣货车上放8个容器，一个容器对应一个发货单，张三拣货到拣货车的时候，按发货单把货分别放入8个容器，这个是Cluster Picking。
2.  在Odoo中，Cluster Picking的操作方法是：
3.  1.  预定义一些可重复使用的包裹（对应到现实中的容器，包裹号即为容器编号）；
```python
    2.  发货单合并为Batch后，Batch上的每个明细行，按发货单分配目的包裹，即同一个发货单的明细行分配同一个包裹；
    3.  拣货时候，根据打印的PDF拣货单，或者手持的PDA上显示的包裹号，将货物放入对应的容器（包裹号和现实中的容器编号相同）
    4.  拣货车拣满后，推到打包台，打包作业员逐个容器装箱打包。
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
