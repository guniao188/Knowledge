---
title: "Odoo16企业版模块降级办法(汇总)"
source: "http://www.thinkltd.cn/forum/1/odoo16-3655"
forum: "求助台"
author: "肖相扶"
published: 2024-10-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo16企业版模块降级办法(汇总)

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-10-15
> <http://www.thinkltd.cn/forum/1/odoo16-3655>

1.  会计模块(account_accountant)： [Odoo15、Odoo16的会计模块account_accountant社区版安装说明](http://www%5C.thinkltd%5C.cn/forum/1/odoo15odoo16account%5C-accountant%5C-812)
2.  扫码模块(stock_barcode)： [Odoo16 stock_barcode模块社区版安装方法](http://www%5C.thinkltd%5C.cn/forum/1/odoo16%5C-stock%5C-barcode%5C-3656)
3.  质量相关模块(quality, quality_control, quality_mrp, quality_mrp_workorder等)：直接安装即可
4.  其他扫码相关模块(stock_barcode_quality_control等)：直接安装即可
5.  主生产计划 模块(mrp_mps)，产品生命周期模块(mrp_plm)：直接安装即可
6.  文档管理 模块(documents)：文件__manifest__.py中，对 web_enterprise 的依赖，改成 web 即可直接安装。
7.  文档签署模块(sign)： 文件__manifest__.py中，注释代码行（加#号） 'web_enterprise/static/src/scss/primary_variables.scss' 重启Odoo即可。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
