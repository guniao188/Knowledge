---
title: "打印pdf中日期字段不要显示时分秒的写法示例"
source: "http://www.thinkltd.cn/forum/1/pdf-922"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 打印pdf中日期字段不要显示时分秒的写法示例

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/pdf-922>

打印中日期只写日期，不要时分秒的写法：

                    Date Req:

把日期的格式在【设置/语言】那里打开中文，改一下日期格式，去掉年月日中文，改成2022-05-19这样格式

这样0:10才能用，代表前面10个字符。

![[1-pdf-922-5cdf69ce.png]]

另一种简便的处理方法：用t-options来处理，函数widget和xml的视图用法相同。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
