---
title: "SQL示例报表模块Dashboard Ninja Advance"
source: "http://www.thinkltd.cn/forum/2/sqldashboard-ninja-advance-3791"
forum: "模块库"
author: "赵晨"
published: 2023-11-01
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# SQL示例报表模块Dashboard Ninja Advance

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:赵晨 | 2023-11-01
> <http://www.thinkltd.cn/forum/2/sqldashboard-ninja-advance-3791>

背景：客户需要一个以班级为单位的订奶率报表，需要支持报表信息EXCEL导出

下图为客户提供示例

![[2-sqldashboard-ninja-advance-3791-1162229e.png]]

报表模块高级版支持SQL语句生成，结合odoo自身模块与字段的易配置性，可以相对轻松的做出SQL语句报表，以下为SQL示例：

SELECT school_info.name AS 网点,grade_info.name AS 年级, class_info.name AS 班级, class_info.class_size::varchar(4) AS 人数, count(so)::varchar(4) AS 订奶数,count(so)*100/class_size::float8 AS 订奶率
FROM sale_order so
LEFT JOIN class_info ON [class_info.id](https://class_info.id) = so.class_id AND class_info.class_size > 0 AND class_info.class_size NOTNULL
LEFT JOIN school_info ON [school_info.id](https://school_info.id) = so.school_id
LEFT JOIN grade_info ON [grade_info.id](https://grade_info.id) = so.grade_id
WHERE class_size NOTNULL AND so.company_id='1'
GROUP BY so.class_id, 班级, 人数, 网点, 年级,class_info.class_size
ORDER BY 网点, 年级, 班级

SQL语句解析（部分）：

SELECT 部分为主展示结果，头部内容。 ::varchar(4)为强制转换文本，不然会显示30.00。:: float8为强转float类型，不然会显示整数。

FROM 取表以及给so定义，后续可以用so定义sale_order。

LEFT JOIN 负责取别的模型表信息，以左边表so为主表插入，细节解释不清楚，待大佬补充

WHERE 取值范围，取值条件

GROUP BY  不加的话头部信息会报错，功能细节解释不清楚，待大佬补充

ORDER BY 按字段排序

报表结果

![[2-sqldashboard-ninja-advance-3791-15d65d0f.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
