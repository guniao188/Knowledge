---
title: "二开仓库进销存报表及收发明细报表stock_cnreport"
source: "http://www.thinkltd.cn/forum/2/stock-cnreport-3129"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开仓库进销存报表及收发明细报表stock_cnreport

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/stock-cnreport-3129>

模块链接： OSCG_SVN\odoo_ecommerce\12.0SRC\存货核算\stock_cnreport

Odoo 13.0重写了此模块，参考： [/forum/2/question/odoo13-stock-cnreport-3197](http://www.thinkltd.cn/forum/2/question/odoo13-stock-cnreport-3197)

【仓库收发明细表】

从库存移动取数据汇总，取数条件 1) 完成状态的库存移动，2) 目标库位或源库位是指定库存及其子库位的库存移动，3) 完成日期为指定期间的库存移动 。 4) 参考SQL条件语句（MV为Stock Move表）：WHERE (MV.location_id in (%s) or MV.location_dest_id in (%s)) AND MV.date >= '%s' AND MV.date = '%s' AND MV.date = '%s' AND MV.date <= '%s' AND MV.state = 'done' GROUP BY  MV.product_id, PT.name, pu_name

![[2-stock-cnreport-3129-8d19e45a.png]]

## 补充/答案 1

请帮忙增加字段列：产品的内部编码取自defalut_code

另外请问有考虑可库存商品类型吗？

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
