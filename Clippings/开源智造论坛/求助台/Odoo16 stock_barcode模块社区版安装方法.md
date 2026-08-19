---
title: "Odoo16 stock_barcode模块社区版安装方法"
source: "http://www.thinkltd.cn/forum/1/odoo16-stock-barcode-3656"
forum: "求助台"
author: "肖相扶"
published: 2025-02-25
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo16 stock_barcode模块社区版安装方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2025-02-25
> <http://www.thinkltd.cn/forum/1/odoo16-stock-barcode-3656>

做以下三处修改即可：

1.  依赖的修改：web_mobile的依赖中，去掉对 web_enterprise 的依赖（ web_mobile 模块的文件__manifest__.py 中， web_enterprise的依赖修改成 web ）
2.  代码文件 stock_barcode\static\src\main_menu.js 中，注释代码行 this.home = useService("home_menu");  

![[1-odoo16-stock-barcode-3656-a7da42a4.png]]

3.  条码模块返回到主菜单的修改。代码文件 stock_barcode\static\src\main_menu.xml 改成 t-on-click="() => window.location.assign('/web')"  

![[1-odoo16-stock-barcode-3656-7dae767d.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
