---
title: "odoo的上下层级如何实现快速的导航树状结构归类"
source: "http://www.thinkltd.cn/forum/1/odoo-657"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# odoo的上下层级如何实现快速的导航树状结构归类

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo-657>

比如常用的产品分类，有多个层级的情况下，要如何让客户清楚的树状结构分得出上下层级，以树状形式展示？

答：在搜索视图里面，可以增加定义：

展示的效果如图所示：

![[1-odoo-657-f13cea4a.png]]

V13是叫控制面板视图，在V12是叫搜索视图，同一个类型的视图

效果：

![[1-odoo-657-b1b75679.png]]

能以层级展示，并能点三角形来展开，树状结构。

这个产品类别名字也是可以自定义的。

![[1-odoo-657-b19d753e.png]]

## 补充/答案 1

树状筛选 searchpanel 详细树形用法参考 [树形筛选searchpanel的详细用法](http://www.thinkltd.cn/forum/1/question/searchpanel-935)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
