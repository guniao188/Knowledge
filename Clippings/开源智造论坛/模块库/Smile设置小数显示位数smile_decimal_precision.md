---
title: "Smile设置小数显示位数smile_decimal_precision"
source: "http://www.thinkltd.cn/forum/2/smilesmile-decimal-precision-3067"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile设置小数显示位数smile_decimal_precision

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smilesmile-decimal-precision-3067>

模块链接：

This module allows to distinguish computation digits and display digits in decimal precision. It is also possible to manage a number of decimal places to display on devices.

Features:

- The administrator edit the decimal precision by specifying the name of digits parameter.
- The administrator put the number of digits he want to compute.
- The administrator put the number of digits he want to display.
- By default the display digits equals the the digits calculated.
- The administrator can make the display digits superior than the the digits calculated.
- The administrator can make the display digits inferior than the the digits calculated.
-

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_decimal_precision#id1)

To edit a decimal precision :

1.  Choose a field that you want to edit its decimal accuracy (Ex. Product Price) :

2.  Go to `Settings > Technical > Database Structure`> Decimal accuracy menu.
3.  Select Decimal accuracy corresponding to field.

4.  Then edit the value of digits you want to compute, and the number of digits you want to display.

    In this example we put 3 digits to display and 5 to compute

5.  Now, go back to your interface to see the new decimal accuracy :

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
