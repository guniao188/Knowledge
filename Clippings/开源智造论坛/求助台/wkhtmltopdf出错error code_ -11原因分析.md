---
title: "wkhtmltopdf出错error code: -11原因分析"
source: "http://www.thinkltd.cn/forum/1/wkhtmltopdferror-code-11-326"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# wkhtmltopdf出错error code: -11原因分析

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/wkhtmltopdferror-code-11-326>

参考：

原因似乎是最后一页为空白内容，或者某Row存在跨页现象，解决办法是增加或减少一行（避免空白页或跨页行），就不报错了。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
