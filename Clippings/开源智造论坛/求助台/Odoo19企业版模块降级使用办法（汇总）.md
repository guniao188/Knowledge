---
title: "Odoo19企业版模块降级使用办法（汇总）"
source: "http://www.thinkltd.cn/forum/1/odoo19-4075"
forum: "求助台"
author: "肖相扶"
published: 2025-10-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo19企业版模块降级使用办法（汇总）

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2025-10-16
> <http://www.thinkltd.cn/forum/1/odoo19-4075>

1.   会计及会计报表模块。模块accountant及会计报表模块account_reports ，移到社区版安装，方法和Odoo18一样，参考 [Odoo18企业版模块降级使用办法（汇总）](http://www.thinkltd.cn/forum/1/odoo18-3983)
2.  扫码模块stock_barcode降级使用方法和Odoo16一样，参考  [Odoo16 stock_barcode模块社区版安装方法](http://www.thinkltd.cn/forum/1/odoo16-stock-barcode-3656) 。不过注意两点，一是Odoo19的依赖从web_enterprise改成了web_mobile，因此需要带上 web_mobile 模块，并且修改 web_mobile 模块中__manifest__.py对企业版的web_enterprise的依赖，改成web 。二是， main_menu.js、 main_menu.xml  两个文件所在目录换成了stock_barcode\static\src\main_menu\
3.

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
