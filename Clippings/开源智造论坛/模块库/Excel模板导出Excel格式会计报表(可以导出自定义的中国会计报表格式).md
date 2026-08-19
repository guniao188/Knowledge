---
title: "Excel模板导出Excel格式会计报表(可以导出自定义的中国会计报表格式)"
source: "http://www.thinkltd.cn/forum/2/excelexcel-3759"
forum: "模块库"
author: "肖相扶"
published: 2023-08-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Excel模板导出Excel格式会计报表(可以导出自定义的中国会计报表格式)

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2023-08-15
> <http://www.thinkltd.cn/forum/2/excelexcel-3759>

模块链接：OSCG_Git\extra-addons\report_account_cn_xlsx

【模块功能】

1.  在Excel导出报表模块（参考 [在线python代码下载Excel报表模块report_xlsx](http://www.thinkltd.cn/forum/2/pythonexcelreport-xlsx-3615)）中，增加会计报表相关的变量acc_codes。该变量是一个字典，包含所有以 “ a+科目编码 ”为key的科目年初余额、当前余额、当月发生额、当前发生额
```python
    acode['ncye']: 会计科目年初余额
    acode['ncye']: 会计科目当前余额
    acode['ncye']: 会计科目当月发生额
    acode['ncye']: 会计科目本年(截至当前)发生额
```

2.  Excel模板中可以直接用公式（大括号括起来）如科目100101和科目100201的当前余额相加：{a100101['dqye'] + a100201['dqye']}
3.  报表输出的python代码中，可以使用会计报表变量，输出到Excel格式中。参见模块中demo数据的报表“演示：导出会计科目年初余额、当前余额、本年发生额、本月发生额”。

【功能截图】

![[2-excelexcel-3759-387bfaa5.png]]

![[2-excelexcel-3759-1c0e20e6.png]]

![[2-excelexcel-3759-d659031c.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
