---
title: "OCA仓库波次作业stock_batch_picking"
source: "http://www.thinkltd.cn/forum/2/ocastock-batch-picking-2533"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA仓库波次作业stock_batch_picking

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastock-batch-picking-2533>

13版本存放位置：OSCG_SVN\odoo_ecommerce\13.0SRC\stock_batch_picking

模块链接：\https://github.com/OCA/stock-logistics-workflow/tree/11.0/stock_batch_picking

该模块比Odoo标准的波次管理模块实用。将多个Picking归集到一个波次（batch），而后可以在波次上批量检查可用、批量验证完成、批量部分发货、汇总打印拣货单。还可以将波次分配给某位作业人员负责

Batch picking allows you to manage several pickings at the same time. After having created a batch with a list of stock picking, you can:

- Check availability and reserve quants for all pickings
- Mark all pickings as done when delivery is done.
- Make partial delivery by filling done quantities in pack operations tab.
- Print a report to pick the proper goods at once

## 补充/答案 1

该模块升级至V12测试使用。发现有如下问题：1.选中汇总的picking单如还在进行中，不可以重复选，那如果操作错误，既不可以重复选择，取消当前的汇总单，则对应的picking单状态也被取消了。  2.汇总的operation页，如果有批次号的产品填写完成数量，没批次的明细行不填完成数量，点验证只自动验证了有批次号的。   3.operation上的done 始终不可编辑，去掉字段readonly的限制也不行。


## 原帖外链配图

![[2-ocastock-batch-picking-2533-x2d9709ba.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/stock-logistics-workflow/11.0/stock_batch_picking/static/stock_picking_l</small>

![[2-ocastock-batch-picking-2533-xd4e56143.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/stock-logistics-workflow/11.0/stock_batch_picking/static/batch_wizard.pn</small>

![[2-ocastock-batch-picking-2533-x07f016e8.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/stock-logistics-workflow/11.0/stock_batch_picking/static/batch_form.png?</small>

![[2-ocastock-batch-picking-2533-x194038c2.png]]
<small>原始地址: /web/image/835/snipaste_20190119_195032.png?access_token=686e6794-c94b-4da4-9a1e-f70e7ca0d8cc</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
