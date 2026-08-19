---
title: "Odoo论坛中复制链接默认打开新窗口等问题改善"
source: "http://www.thinkltd.cn/forum/1/odoo-3598"
forum: "求助台"
author: "肖相扶"
published: 2022-12-17
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo论坛中复制链接默认打开新窗口等问题改善

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-17
> <http://www.thinkltd.cn/forum/1/odoo-3598>

Odoo论坛复制链接时候有几个问题：

1.  复制的链接，点击链接总是在原窗口打开，希望链接默认在打开新窗口
2.  复制过来的链接，显示的颜色等style如何改变

【修改方法】以Odoo 15为例

1.  论坛帖子的显示风格修改：论坛显示风格的CSS文件是 odoo15\odoo\addons\website_forum\static\src\scss\website_forum.scss 。在其中的 .o_wforum_readable 中增加css即可改变论坛的显示样式。如下面截图修改论坛中链接的显示颜色。

![[1-odoo-3598-3e8d0f8b.png]]

2.  论坛编辑时候，复制粘贴 URL 链接时候，有两种情况，一种是粘贴 HTML文本，一种是粘贴 URL地址。前者的情况，Odoo直接粘贴该 HTML文本，后者情况，Odoo创建一个标签。对应的处理代码参见文件 odoo\odoo15\odoo\addons\web_editor\static\lib\odoo-editor\src\OdooEditor.js 中的 _onPaste(ev) 方法。
3.  粘贴 HTML文本的情况，需要在该HTML文本的A标签中添加属性 target="_blank" 。参考下面截图代码。
4.  粘贴URL地址的情况，在系统链接默认属性（ defaultLinkAttributes ）中增加属性“ target = '_blank' ” 。参考下面截图代码。

![[1-odoo-3598-94fcae0a.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
