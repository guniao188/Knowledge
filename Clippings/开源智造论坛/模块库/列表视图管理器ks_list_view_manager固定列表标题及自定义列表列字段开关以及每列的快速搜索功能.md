---
title: "列表视图管理器ks_list_view_manager固定列表标题及自定义列表列字段开关以及每列的快速搜索功能"
source: "http://www.thinkltd.cn/forum/2/ks-list-view-manager-3522"
forum: "模块库"
author: "钟卫卫"
published: 2024-01-22
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 列表视图管理器ks_list_view_manager固定列表标题及自定义列表列字段开关以及每列的快速搜索功能

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:钟卫卫 | 2024-01-22
> <http://www.thinkltd.cn/forum/2/ks-list-view-manager-3522>

该模块支持将列标题固定，以及列标题显示的字段能用户自定义，以及用户可以进行快速搜索。

客户购买插件，功能参考 https://apps.odoo.com/apps/modules/14.0/ks_list_view_manager/

V15版本，已购买，见链接，因SVN上传不了，这里可以下载。

https://apps.odoo.com/apps/modules/15.0/ks_list_view_manager/

![[2-ks-list-view-manager-3522-1e8b2840.png]]

![[2-ks-list-view-manager-3522-91ccb17d.png]]

另外还有一个模块与这个功能类似不过没有购买，功能稍微简单一些：

https://apps.odoo.com/apps/modules/15.0/odoo_advance_search/

https://apps.odoo.com/loempia/download/tmp/ks_list_view_manager/2022-06-05/33274/8e795ce82434a477969b7cdce569169e971d83f20e5c3ca231a899e293afdc62.zip?deps

V14版，模块存放地址：oscg_svn\14.0SRC\ks_list_view_manager

V13版，模块存放地址：oscg_svn\13.0SRC\ks_list_view_manager

## 补充/答案 1

这个插件，在原生的仪表板上也会出现搜索框，但是不生效，实际原生的仪表板也是不支持搜索的

告知客户忽略这个搜索即可

![[2-ks-list-view-manager-3522-6ce9df1b.png]]

## 补充/答案 2

有二个bug待修正：

bug描述：
1、在account move里，打开这个开关，

![[2-ks-list-view-manager-3522-bf8bab63.png]]

，能看到二个相同的列，

![[2-ks-list-view-manager-3522-0f717217.png]]

因为是在这个开关里的，视图上控制不到。

2、所有涉及弹窗的地方，下拉选项的值被沉底了，无法选择，
比如从价格表这里设置，明明产品有选项的，有好多产品资料了，但这里下拉选择是空白的，被沉底了，所以无法选择值，

![[2-ks-list-view-manager-3522-365d36c0.png]]

![[2-ks-list-view-manager-3522-88c0a13e.png]]

![[2-ks-list-view-manager-3522-0a5c2710.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
