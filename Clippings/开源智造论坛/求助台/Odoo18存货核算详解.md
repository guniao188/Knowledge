---
title: "Odoo18存货核算详解"
source: "http://www.thinkltd.cn/forum/1/odoo18-4027"
forum: "求助台"
author: "肖相扶"
published: 2025-01-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo18存货核算详解

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2025-01-10
> <http://www.thinkltd.cn/forum/1/odoo18-4027>

【Odoo功能】

1.  存货核算核心是解决两个问题，其一是成本价格如何计算，其二是存货相关会计凭证如何记账（入库、出库相关的会计凭证）。
2.  成本价格计算问题，中国会计上，成本价格计算有五种方法：计划法，月末一次加权平均法，移动加权平均法，先进先出法，个别计价法。
3.  计划法对应Odoo的“标准价格”法，移动加权平均法对应Odoo的“平均成本(AVCO)”、先进先出法对应Odoo的“先进先出(FIFO)”。个别计价法在Odoo中用先进先出法+批次/序列号管理，即每一批次/序列号，其成本价格都是其入库价格，每一批次、或者每一件(序列号)，其成本价格都是唯一的。月末一次加权平均法参考 [Odoo18月末一次加权平均生产成本计价mrp_cost_month_end](http://www.thinkltd.cn/forum/2/odoo18mrp-cost-month-end-4026)及 [Odoo18月末一次加权平均成本计价方法stock_costs_month_end](http://www.thinkltd.cn/forum/2/odoo18stock-costs-month-end-4025)
4.  影响存货成本价格的因素主要有：入库成本（采购入库和生产入库，销售退货、盘盈入库等通常不认为影响成本）、费用分摊（采购费用分摊、制造费用分摊）、采购发票价格差异。
5.  出库时候，以设定的成本计价方法计算出的成本，作为出库成本。不同企业可以设置不同成本计价方法，但一旦设定，在一个会计期间(通常一年)不得修改。
6.  Odoo的费用分摊逻辑参考  [Odoo18到岸成本分摊逻辑](http://www.thinkltd.cn/forum/1/odoo18-4014)，制造费用分摊参考  [全月制造费用分摊模块mrp_landed_costs_cn](http://www.thinkltd.cn/forum/2/mrp-landed-costs-cn-4019)，制造品的料工费分析参考  [生产成本料工费分析模块mrp_cost_analytic](http://www.thinkltd.cn/forum/2/mrp-cost-analytic-4023)
7.  Odoo采购发票差异价格分摊参考  [Odoo18自动处理采购发票价格差异的逻辑](http://www.thinkltd.cn/forum/1/odoo18-4012)
8.  存货变动的会计凭证生成，Odoo中有两种方法，即永续盘存制和实地盘存制。参考  [永续盘存制‌和实地盘存制‌](http://www.thinkltd.cn/forum/1/4029)
9.  在中国会计环境下，选择永续盘存制，又希望解决会计凭证过多过细，难以打印存档的问题。参考  [会计记账凭证合并打印功能模块account_move_merge](http://www.thinkltd.cn/forum/2/account-move-merge-3607)
10. 在中国会计环境下，如果选择实地盘存制，系统不会自动生成存货相关会计凭证。此种情况下，会计凭证有两种解决方法：
11. 一种是，系统出具“收发存报表”，会计基于收发存报表自己计算当月成本价格，手工录入存货会计凭证。当仅把Odoo当作库存管理系统，财务在别的系统时候，这不失为一种好办法。收发存报表参考  [Odoo18进销存/收发存报表模块stock_report_sfc](http://www.thinkltd.cn/forum/2/odoo18-stock-report-sfc-4024)
12. 另外一种是，分类汇总自动生成存货会计凭证，参考  [Odoo18分类汇总创建存货/出入库会计凭证stock_account_subtotal](http://www.thinkltd.cn/forum/2/odoo18-stock-account-subtotal-4028)
13. 影响存货变动的会计凭证，还有一个重要设置是 盎格鲁撒克逊会计体系 anglo_saxon_accounting。参考  [盎格鲁撒克逊会计anglo_saxon_accounting与大陆会计体系](http://www.thinkltd.cn/forum/1/anglo-saxon-accounting-4030)

【功能截图】

![[1-odoo18-4027-8ca3bb57.png]]

【 中国会计环境下的实施建议】

1.  总是开启 盎格鲁撒克逊会计体系 anglo_saxon_accounting。参考  [盎格鲁撒克逊会计anglo_saxon_accounting与大陆会计体系](http://www.thinkltd.cn/forum/1/anglo-saxon-accounting-4030)
2.  如果作为内账使用，可以开启永续。参考  [永续盘存制‌和实地盘存制‌](http://www.thinkltd.cn/forum/1/4029)
3.  下面几种情况，不应该开启永续：a) Odoo财务作为外帐，需要打印存档会计凭证；b) 采用月末一次加权平均成本计价方法；c) Odoo仅作业务系统使用，不做财务系统使用。
4.  采用月末一次加权平均成本计价法的情况，需要安装的模块参考：[Odoo18月末一次加权平均成本计价方法stock_costs_month_end](http://www.thinkltd.cn/forum/2/odoo18stock-costs-month-end-4025)、 如果是生产型企业，还需要 [Odoo18月末一次加权平均生产成本计价mrp_cost_month_end](http://www.thinkltd.cn/forum/2/odoo18mrp-cost-month-end-4026)、[全月制造费用分摊模块mrp_landed_costs_cn](http://www.thinkltd.cn/forum/2/mrp-landed-costs-cn-4019)。可能需要 [生产成本料工费分析模块mrp_cost_analytic](http://www.thinkltd.cn/forum/2/mrp-cost-analytic-4023)
5.  不开启永续的情况下，可以安装模块[Odoo18分类汇总创建存货/出入库会计凭证stock_account_subtotal](http://www.thinkltd.cn/forum/2/odoo18-stock-account-subtotal-4028)，批量汇总生成存货变动的会计凭证。无论用哪种成本计价方法，本模块都适用。
6.  不开启永续的情况下，供应商账单可以正常确认。如果采用标准价格、移动平均、先进先出、个别计价成本计价法的话，客户发票可以正常确认。
7.  Odoo仅作业务系统使用的情况下，建议从Odoo导出收发存报表交给成本会计。i) 成本会计基于收发存报表的数据，在其他会计系统手工填制存货会计凭证。ii) 如果采用月末一次加权平均成本计价方法的话，可以在Odoo中完成月末成本的计算，再导出收发存报表。如此，会计人员直接填制凭证即可。iii) 也可以不在Odoo中做成本计算，直接导出收发存报表，成本会计基于收发存报表的期间入库数量和金额，自己计算月末成本价格，再填制会计凭证。此种情况，收发存报表的期初金额、期间出库金额、期末金额都是不准确的，没有参考价值。但期初数量、期间入库数量和金额、期间出库数量、期末数量是准确的，具备参考价值。 收发存报表参考 [Odoo18进销存/收发存报表模块stock_report_sfc](http://www.thinkltd.cn/forum/2/odoo18-stock-report-sfc-4024)

【配置截图】

会计科目典型配置：

![[1-odoo18-4027-1679d741.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
