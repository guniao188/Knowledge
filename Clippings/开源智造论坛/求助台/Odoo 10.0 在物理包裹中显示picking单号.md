---
title: "Odoo 10.0 在物理包裹中显示picking单号"
source: "http://www.thinkltd.cn/forum/1/odoo-10-0-picking-335"
forum: "求助台"
author: "沙正武"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo 10.0 在物理包裹中显示picking单号

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:沙正武 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo-10-0-picking-335>

1 需求：天津市蜂潮商贸有限公司 需要在 包裹（stock.quant.package）中打印唛头，唛头信息有箱号、条码、尺寸、毛重、发件人和收件人地址。
   其中收件人信息在stock.picking中，从stock.quant.package 上不能直接获取

## 补充/答案 1

2 解决方法：通过 打包作业（stock.pack.operation）可以找到拣货的picking_id 和目的包裹（result_package_id）
   在stock.quant.package创建一个计算型字段x_picking_id，通过在stock.pack.operation中查找包裹等于目的包裹（result_package_id）的拣货作业，然后把其对应的picking_id赋值给x_picking_id。这样即可在stock.quant.package关联到它的拣货单。

![[1-odoo-10-0-picking-335-6416d2c7.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
