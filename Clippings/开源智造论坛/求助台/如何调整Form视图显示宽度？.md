---
title: "如何调整Form视图显示宽度？"
source: "http://www.thinkltd.cn/forum/1/form-455"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 如何调整Form视图显示宽度？

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/form-455>

下述方法在Odoo 13测试有效，Odoo 12未测试过。

**odoo14 可以在SVN查找模块并安装即可：**

模块名：odoo_form_width_css

模块路径：\14.0SRC\odoo_form_width_css

或者使用以下方法（不建议）

方法一：

文件 Odoo13\source\odoo\addons\web\static\src\scss\form_view_extra.scss  第一行有下述代码，$sheet-max-width: 1280px;  即为Form视图Sheet的宽度，系统默认值是1140px，修改后刷新页面（刷新不行，则重启Odoo再刷新），即可看到效果 。
.o_form_view {
```python
    $sheet-max-width: 1280px;
    $sheet-min-width: 650px;
    $sheet-padding: 16px;
```

方法二：

另外一种方法是，参照下图，修改 max-width: $sheet-max-width; 成  max-width: none;  增加 width: auto;  如此，则Form视图的Sheet 改为全屏显示。

修改方法图示：

![[1-form-455-48de2817.png]]

调整Form视图宽度后效果图：

![[1-form-455-8374d9f5.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
