---
title: "Odoo17企业版模块降级使用办法（汇总）"
source: "http://www.thinkltd.cn/forum/1/odoo17-3816"
forum: "求助台"
author: "肖相扶"
published: 2024-12-02
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17企业版模块降级使用办法（汇总）

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-12-02
> <http://www.thinkltd.cn/forum/1/odoo17-3816>

1.  模块account_accountant及会计报表模块account_reports ，移到社区版安装，方法如下（和Odoo16方法完全一样）：同时移动下述四个模块（account_reports_cash_basis可以不要）：account_accountant，account_reports，mail_enterprise，web_mobile，account_auto_transfer。模块 web_mobile的文件__manifest__.py 中，web_enterprise的依赖修改成 web 。
2.  扫码模块stock_barcode降级使用方法和Odoo16完全一样，参考  [Odoo16 stock_barcode模块社区版安装方法](http://www%5C%5C.thinkltd%5C%5C.cn/forum/1/odoo16%5C%5C-stock%5C%5C-barcode%5C%5C-3656)
3.  工单模块mrp_workorder的降级使用方法（修改下述两点）：一、文件OSCGODOO17\myaddons2\mrp_workorder\static\src\mrp_display\mrp_display.js ，setup()方法中，注释代码行(代码行前面加 // )this.homeMenu = useService("home_menu");   二、close()方法中，代码行 this.homeMenu.toggle(); 改成 history.back();

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
