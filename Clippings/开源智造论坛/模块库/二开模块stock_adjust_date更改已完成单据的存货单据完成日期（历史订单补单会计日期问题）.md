---
title: "二开模块stock_adjust_date更改已完成单据的存货单据完成日期（历史订单补单会计日期问题）"
source: "http://www.thinkltd.cn/forum/2/stock-adjust-date-3220"
forum: "模块库"
author: "符赛红"
published: 2023-06-26
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开模块stock_adjust_date更改已完成单据的存货单据完成日期（历史订单补单会计日期问题）

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:符赛红 | 2023-06-26
> <http://www.thinkltd.cn/forum/2/stock-adjust-date-3220>

V15.0版本：OSCG_SVN\odoo_ecommerce\15.0SRC\存货核算\stock_adjust_date

V14升级版本存放位置：SVN\odoo_ecommerce\06.Customization\polymaker聚复\addons\stock_adjust_date

V13版本存放位置： oscg_svn\13.0SRC\存货核算

操作说明请参考聚复的测试报告，存放位置：SVN\odoo_ecommerce\06.Customization\polymaker聚复\技术配置\补单更改会计日期测试说明.doc

模块里少一个访问控制列表的权限，需要补充：stock.adjust.wizard 增加内部用户的访问权限，数据表。

![[2-stock-adjust-date-3220-07d174fc.png]]

V12模块存放位置：

F:\SVN\odoo_ecommerce\06.Customization\菲尔\190917\addons\stock_adjust_date

业务场景：

在实际业务中，往往会出现销售发货，或者采购入库，在系统中操作【验证】完成时，会有补单的情况，以及跨月的问题，比如实际业务发生在上月末，但实际操作系统时已经是本月初了，就会出现会计上的存货期间需要调整的情况，有可能客户发票会计日期，供应商账单的会计日期都有调过，但存货的picking及move上的日期会计期间与会计账单上不一致，就需要调整已完成的存货日期。

这个模块主要解决的是：

在picking单上点按钮adjust，可以修改move及move.line的完成日期以及picking单的调拔日期；

在盘点单上点按钮adjust，可以修改move的完成日期及盘点单的完成日期；

在生产单上点按钮adjust，可以修改原料扣减库存的move以及成品入库的move以及报废单上的move的完成日期。

这些改动都会留下该单据下面的log日志。

具体截图示例：

![[2-stock-adjust-date-3220-b27fa522.png]]

![[2-stock-adjust-date-3220-02e92cda.png]]

![[2-stock-adjust-date-3220-bb9c7838.png]]

![[2-stock-adjust-date-3220-1e107ab0.png]]

![[2-stock-adjust-date-3220-58b393b2.png]]

![[2-stock-adjust-date-3220-8df701b3.png]]

这个按钮，可以设权限由会计控制。尤其是全月加权平均核算或是非永续自动的情况下需要先调好相应的会计期间，再进行核算。

如果是永续自动的，则这个按钮实际操作单据的用户操作修改会比较好，但没有测试不确定放在【完成】之前就adjust修改，会不会在【验证】单据时，日期仍会被覆盖。

实际系统也有accounting_date日期，但完成日期放出来手动改，点【验证】会报错。后来就推荐给了客户这个adjust的模块插件来解决已完成单据的日期修改。

备注：这个模块不会改动quants。

## 补充/答案 1

这个模块，目前 有菲尔，suto，以及睿思凯都有用到。

## 补充/答案 2

改版成V14版本，需要将picking或move关联的会计赁证的日期也一起同步更改掉。

## 补充/答案 3

V14版本代码以及操作手册测试报告说明，请参考目录：

D:\svn\SVN\odoo_ecommerce\06.Customization\suto\V14 addons\customaddons\stock_adjust_date

以及测试文档【补单更改会计日期测试说明.docx】

## 补充/答案 4

15版本部署后，会计凭证的重排序会报错，经排查是sequence.mixin文件下面代码导致的
暂时注释掉后没有发现什么问题

# def _get_sequence_format_param(self, previous):

    #        format, format_value = super()._get_sequence_format_param(previous=previous)

    #        format_value.update({

    #            'year': self.date.year,

    #            'month':self.date.month

    #        })

    #        return format, format_value

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
