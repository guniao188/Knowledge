---
title: "OCA采购成本分摊purchase_landed_cost"
source: "http://www.thinkltd.cn/forum/2/ocapurchase-landed-cost-2618"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA采购成本分摊purchase_landed_cost

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocapurchase-landed-cost-2618>

模块链接：

1.  12.0版本：

2.  此模块新开发了一个采购成本分摊单，分摊单上导入采购入库单，供应商账单

3.  分摊计算

4.  更新产品成本价格。注意，本模块只更新移动加权平均成本计算方法的产品成本价格。

The functionality of this module is to provide a way to manage your purchase costs more easily than the official module (*stock_landed_cost*) and allow to distribute them with a lot of methods.

**Main features:**

- Possibility to assign landed cost afterwards in a separate screen.
- Management of expense types with preconfigured calculation methods.
- Distribution of costs based on weight, volume, product price, etc.
- Types marked as default are automatically added to each new purchase distribution.
- Management orders shopping expenses associated with one or more entry slips.
- Upgrade cost price of products based on the costs.
- Currently only one type of upgrade cost is available: direct upgrade.

## 补充/答案 1

那如果是实时产生凭证，那么这个模块也能产生费用分摊结转的凭证吗？

如果分摊发生在销售出库之后，会不会有啥问题？还是说也必须做到分摊要实时去分摊，即一入库完成就要分摊好？

建议推荐的客户行业注意：这种方式如果客户不上制造模块，只是外采，涉及进口或是物流费用、仓储费用占成本比重较大的产品行业，比较适应这种计算方式。

## 补充/答案 2

应该会自动产生分摊的会计凭证，不过我没测试过，有空可以测试一下。

## 补充/答案 3

涉及简单加工生产的中小企业，某些产品既能外采，又能自行组装加工得到，成本的核算，参考方案：

完美的结合这个采购费用分担，加stock_production的二开加工模块，实时加工成品成本计算，再搭配全月加权平均月末批量生成会计凭证功能。

就能解决这个成本实时，以及外采和内部加工的成本加权平均。

视频参考分享：

链接：https://pan.baidu.com/s/1OgebnCyU3vuIzKoNi09zag
提取码：wxds
复制这段内容后打开百度网盘手机App，操作更方便哦


## 原帖外链配图

![[2-ocapurchase-landed-cost-2618-x194038c2.png]]
<small>原始地址: /web/image/924/snipaste_20190120_161425.png?access_token=1253ec02-a24b-447b-875f-02e94c012f3c</small>

![[2-ocapurchase-landed-cost-2618-x194038c2.png]]
<small>原始地址: /web/image/926/snipaste_20190120_161630.png?access_token=f1d3643d-e682-4284-89b5-efa5affcbdc1</small>

![[2-ocapurchase-landed-cost-2618-x194038c2.png]]
<small>原始地址: /web/image/928/snipaste_20190120_162127.png?access_token=89779417-c938-42c5-95a1-b76d4c001be1</small>

![[2-ocapurchase-landed-cost-2618-x194038c2.png]]
<small>原始地址: /web/image/930/snipaste_20190120_162807.png?access_token=ec113263-1e6b-48e4-bfff-95b9eb39bbd1</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
