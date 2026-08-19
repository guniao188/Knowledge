---
title: "Smile导入导出设置权限smile_web_impex"
source: "http://www.thinkltd.cn/forum/2/smilesmile-web-impex-3057"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile导入导出设置权限smile_web_impex

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smilesmile-web-impex-3057>

模块链接：

This module adds access rules for import/export features.

For each user, you can indicate if it can import/export data.

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_web_impex#id1)

**Access rights configuration**

**Import/Export**

## 补充/答案 1

华霆电器实际应用中，发现有个js报错，该报错似乎不影响使用，但时不时跳出来，干扰用户操作。

![[2-smilesmile-web-impex-3057-5887906f.png]]

经查，该报错原因及修复方法如下：

【错误原因】

该模块代码文件 smile_web_impex\static\src\js\web_impex.js 的代码行 self.$buttons.find(

未先判断 self.$buttons  是否不为 undefined，如果为 undefined， 则调用 find方法就会报上述错误。

【修复方法】

上述代码文件中，self.$buttons.find(   代码行的前面增加判断语句 if (self.$buttons != undefined)  ，如下图（该文件中共有六处需要修改）。修改后，重启，刷新页面即可。

![[2-smilesmile-web-impex-3057-c509d25f.png]]

## 补充/答案 2

`import`, `export_xlsx 这二个函数可以控制界面的导入和导出，但只是左上角的按钮，V13，中间的动作导出仍需要用上面的模块来实现。`

![[2-smilesmile-web-impex-3057-f8bd0b5b.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
