---
title: "Odoo17条码改善点一览"
source: "http://www.thinkltd.cn/forum/1/odoo17-3813"
forum: "求助台"
author: "肖相扶"
published: 2024-04-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17条码改善点一览

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-04-10
> <http://www.thinkltd.cn/forum/1/odoo17-3813>

返回  [Odoo17改善点列表](http://www.thinkltd.cn/forum/1/odoo17-3808)

1.  库存调整
    要求批次/序列号管理的产品，库存扫码盘点界面，扫产品码，系统自动带出该产品在盘点库位的所有批次/序列号。下图是序列号管理的产品扫码盘点截图，扫序列码后，对应序列码行自动打勾，不存在的序列码可以点击打叉。 

![[1-odoo17-3813-7ce38dea.png]]

2.  条码手工输入
    扫码界面增加了手工条码输入的功能。

![[1-odoo17-3813-989c4d15.png]]

3.  扫码模块支持生产订单操作
    扫码模块增加了生产订单的扫码支持。

![[1-odoo17-3813-607be1be.png]]

4.  Product picture
    Display a picture of the product in the details to ensure the correct product is picked.
5.  Returns from barcodes
    Create returns in barcode format and conveniently scan barcodes to identify returns. Additionally, the visibility of returns in the portal has been improved, and the return default operation type has been removed for better handling of purchase returns.
6.  扫码源库位
    扫码出库的过程中，可以随时扫描库位码，切换拣选产品的源库位。老版本功能是，按源库位不同，自动分成了几个Page，操作完一个Page，切换到下一个Page继续操作。

![[1-odoo17-3813-7109644d.png]]

7.  Smooth handling of reserved quantities
    Better handling of reserved quantities with on-the-fly reservation changes when picking from a different location.
8.  扫码错误时候增加音效提示
    扫了一个不存在/不认识的条码，除了右上角弹框消息提示之外，还增加了“哐...”的音效提示。正确条码的情况下，只有弹框消息，没有声音。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
