---
title: "Odoo Qweb打印报表"
source: "http://www.thinkltd.cn/forum/3/odoo-qweb-3599"
forum: "方案库"
author: "肖相扶"
published: 2022-12-17
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# Odoo Qweb打印报表

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:肖相扶 | 2022-12-17
> <http://www.thinkltd.cn/forum/3/odoo-qweb-3599>

Odoo以qweb作为打印报表的格式标记语言。Qweb报表技术的优劣势如下：

1.  可以处理任意复杂的打印格式。Qweb标记语言的能力等同于html，可以输出各种复杂打印格式。
2.  可以处理任意复杂的数据逻辑。如果需要对数据进行复杂处理，再打印输出。此种情况，可以在对应模型上继承增加数据处理方法，Qweb中调用该方法，获取复杂处理后的结果数据。
3.  qweb-text的输出格式，可以快速输出数据报表文件（如csv格式，.txt后缀）。
4.  Qweb技术缺点是，需要有一定的HTML技术基础，复杂打印格式的情况，QWeb调试比较费时间。

Qweb打印报表处理逻辑如下：

1.  打印时候，系统根据预定义的qweb，抽取业务数据，渲染打印单据格式，生成html文件
2.  qweb中，可以做一些简单的数据逻辑处理。复杂的数据处理逻辑，可以在对应模型中添加计算型字段，或逻辑方法，qweb中调用该方法获取结果。
3.  Odoo报表支持 qweb-html、 qweb-pdf、 qweb-text三种输出格式
4.  如果报表输出格式为 qweb-html，则直接以网页形式显示打印报表
5.  如果报表输出格式为 qweb-pdf，则调用命令 wkhtmltopdf 将HRML文件转换为PDF文件输出。调用代码参见 addons\base\models\ir_actions_report.py 文件中的方法 _run_wkhtmltopdf 。必要情况下，继承改写此方法，修改  wkhtmltopdf 命令的调用参数，改善输出的 pdf 文档格式。
6.  如果报表输出格式为 qweb-text，则直接输出HTML文件。qweb-txt格式适用于无格式的数据输出的情况，如输出 csv数据文件。此种情况，业务模型中编写一个数据获取方法，qweb中以一个简单的for循环，输出类似于csv格式的数据文件。

Qweb技术资料参考：

1.  [Odoo-QWeb知识点总结_JTOOP的博客-CSDN博客_odoo qweb](https://blog.csdn.net/xiaoduu/article/details/112724947)
2.  [QWeb Reports — Odoo 16.0 documentation](https://www.odoo.com/documentation/16.0/developer/reference/backend/reports.html)
3.  [QWeb Templates — Odoo 16.0 documentation](https://www.odoo.com/documentation/16.0/developer/reference/frontend/qweb.html)
4.  [qweb.qa](https://qweb.qa)

wkhtmltopdf工具技术资料参考：

1.  [HTML 转 PDF 之 wkhtmltopdf 工具精讲 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/137469275)
2.  [wkhtmltopdf官网](https://wkhtmltopdf.org/)

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
