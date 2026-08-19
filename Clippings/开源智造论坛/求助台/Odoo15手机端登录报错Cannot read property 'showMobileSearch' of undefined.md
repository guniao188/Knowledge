---
title: "Odoo15手机端登录报错Cannot read property &#39;showMobileSearch&#39; of undefined"
source: "http://www.thinkltd.cn/forum/1/odoo15cannot-read-property-showmobilesearch-of-undefined-937"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo15手机端登录报错Cannot read property &#39;showMobileSearch&#39; of undefined

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo15cannot-read-property-showmobilesearch-of-undefined-937>

【错误现象】

![[1-odoo15cannot-read-property-showmobilesearch-of-undefined-937-5b1c8c81.jpg]]

【修正方法】

文件 odoo15\custom\addons\web_mobile\static\src\js\core\dialog.js  注释下面代码行，重启Odoo，刷新页面报错消失。

![[1-odoo15cannot-read-property-showmobilesearch-of-undefined-937-10e4dbb6.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
