---
title: "Odoo18企业版模块降级使用办法（汇总）"
source: "http://www.thinkltd.cn/forum/1/odoo18-3983"
forum: "求助台"
author: "肖相扶"
published: 2025-10-29
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo18企业版模块降级使用办法（汇总）

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2025-10-29
> <http://www.thinkltd.cn/forum/1/odoo18-3983>

1.  会计及会计报表模块。模块accountant及会计报表模块account_reports ，移到社区版安装，方法如下（比Odoo17方法中多了一个模块 accountant）：同时移动下述五个模块（account_reports_cash_basis可以不要）： accountant, account_accountant，account_reports，mail_enterprise，web_mobile，account_auto_transfer。模块 web_mobile的文件__manifest__.py 中，web_enterprise的依赖修改成 web 。
2.  扫码模块stock_barcode降级使用方法和Odoo16完全一样，参考  [Odoo16 stock_barcode模块社区版安装方法](http://www.thinkltd.cn/forum/1/odoo16-stock-barcode-3656)
3.  工单模块mrp_workorder的降级使用方法和Odoo17一样，参考  [Odoo17企业版模块降级使用办法（汇总） | Odoo技术服务管理平台 - 上海开源智造软件有限公司](http://www.thinkltd.cn/forum/1/odoo17-3816)

## 补充/答案 1

有几个客户出现了:Service home menu is not available 报错

经测试是 mail_enterprise 引起的，去掉 mail_enterprise模块以及对他的依赖，会计也能正常使用

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
