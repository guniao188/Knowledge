---
title: "Odoo17在线表格改善点一览"
source: "http://www.thinkltd.cn/forum/1/odoo17-3838"
forum: "求助台"
author: "肖相扶"
published: 2024-04-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17在线表格改善点一览

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-04-10
> <http://www.thinkltd.cn/forum/1/odoo17-3838>

返回  [Odoo17改善点列表](http://www.thinkltd.cn/forum/1/odoo17-3808)

1.  数字和日期默认格式
    数字和日期格式按用户语言上配置的格式显示，可以在电子表格的 文件 --> 配置上选择语言配置。

![[1-odoo17-3838-67250c4a.png]]

2.  多单元格数组函数
    新增30个多单元格数组(multi-cell array)的函数(如 UNIQUE, EXPAND, FILTER, TRANSPOSE, SPLIT, 等等)。
3.  动态 pivot图表
    使用单个公式 ODOO.PIVOT.TABLE 显示完整pivot图表。
4.  智能图表charts 2.0
    智能标示显示标签/数据列。
5.  版本历史
    查看版本历史，以及复制任何一个历史版本制作新电子表格。
6.  数据校验
    输入时候可以配置数据校验规则。

![[1-odoo17-3838-baf02543.png]]

7.  按行或列分组
    按行或列分组，支持分组展开合并。
8.  移除重复行
    使用移除工具移除重复行。

![[1-odoo17-3838-8c5a968f.png]]

9.  分割文本到多个列
    使用文本分割工具，或SPLIT函数，将文本分割到多个列或单元格。

![[1-odoo17-3838-d623f6a2.png]]

10. 自动删除空格
    使用trim自动删除空格及制表符tab。
11. 电子表格共享
    分享电子表格给内部用户或外部用户。外部用户可以查看、拷贝、下载电子表格。内部用户（有相应权限的话）可以编辑电子表格。
12. 分享到仪表盘
    电子表格可以一键分享到仪表盘。
13. 新函数
    新增下述函数 SORT, RANK, ODOO.PIVOT.TABLE, TRUE/FALSE, HYPERLINK, STEYX, PEARSON, CORREL, RSQ, FORECAST, GROWTH, TREND, SLOPE, LINEST, LOGEST, INTERCEPT, POLYFIT.COEFFS, POLYFIT.FORECAST, SPEARMAN, MATTHEWS, INDEX, UNIQUE, EXPAND, FILTER, TRANSPOSE, MUNIT, RANDARRAY, FLATTEN, FREQUENCY, ARRAY.CONSTRAIN, CHOOSECOLS, CHOOSEROWS, SUMPRODUCT, MINVERSE, MDETERMs, MMULT, SUMX2MY2, SUMX2PY2, SUMXMY2, TOCOL, TOROWS, SPLIT, HSTACK, VSTACK, WRAPCOLS, WRAPROWS, and XLOOKUP
14. 高级文本格式
    新增纵向居中、自动换行功能。

![[1-odoo17-3838-6726db16.png]]

15. 自动填充
    鼠标拖动自动填值。

![[1-odoo17-3838-e6cbf736.png]]

16. 超出可视画面的自动填充
    自动填充时候，可以拖动到屏幕可视范围之外。
17. 自动清除空白工作表
    系统在24小时内自动检测新增的空白且未编辑过的工作表，自动删除。
18. 边线格式
    支持多种边线格式。
19. 单元格引用
    支持不同工作表间的单元格引用。
20. 图表分类
    聚合图表分类/标签。
21. Chart data series: header row
    Easily include or exclude a header row from a chart data series
22. Chart domain edition
    Edit the domain of charts inserted from the graph view.
23. Contextual domain import
    The contextual domain is now imported when a model is inserted into a spreadsheet.
24. Date and time formats
    Added more date and time formats.
25. Drag and drop sheets
    Move sheets in the bottom bar by drag-and-dropping them.
26. Editable font size selector
    Type in the desired font size in the font size selector.
27. Essential keyboard shortcuts
    Added plenty of keyboard shortcuts to increase usability.
28. Extend filters to match new data sources
    Field matching is now automatic for data sources already set in the global filters.
29. Format painter mode
    Double-click the format painter to stay in that mode, allowing multiple clicks.
30. Global filter: "From/To"
    Use the "From/To" time range in the global filters.
31. Global filters order
    Reorder your global filters.
32. Image insertion
    Insert images in spreadsheets.
33. Improve color picker
    Addition of color intensity in the color picker.
34. Improved date parsing
    Dates formatted as MM/YYYY are now properly recognized.
35. Insert functions
    Insert and visualize all functions from the Insert menu.
36. Insert line breaks
    Insert line breaks within a cell by pressing Alt+Enter.
37. Insert links shortcut
    Use the Ctrl+K keyboard shortcut to insert a link in a cell.
38. New functions for prediction assessments
    Added functions for prediction assessments.
39. ODOO formulas insertion
    ODOO formulas can be inserted from the function menu.
40. Search granularity
    Find and replace characters more quickly by searching all sheets, the current sheet only, or a specific range of sheets.
41. Snap to align
    Effortlessly align all graphical elements with the snap-to-align feature.
42. Text vertical alignment on import/export
    Vertical alignment is kept when importing/exporting a spreadsheet.
43. Text wrapping and vertical align
    Format your data with text wrapping and vertical alignment.
44. Text wrapping on import/export
    Text wrapping is kept when importing/exporting a spreadsheet.
45. Use cell as value
    Allow dynamic comparisons by setting a cell as the value on conditional formatting.

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
