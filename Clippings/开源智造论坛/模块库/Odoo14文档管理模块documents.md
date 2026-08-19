---
title: "Odoo14文档管理模块documents"
source: "http://www.thinkltd.cn/forum/2/odoo14documents-3386"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo14文档管理模块documents

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoo14documents-3386>

【功能概要】

1.  文档基本管理功能：上传文档、文档替换、文档分类、文档标签、文档所有者、删除文档

2.  文档权限：基于Odoo的记录规则设定文件读写权限

3.  文档版本记录：文档替换的操作历史，及历史版本下载、恢复

4.  文档分享：生成文档分享链接

5.  文档高级操作：可以自定义文档高级操作，例如基于供应商发来的电子发票自动创建供应商账单，基于文档名字自动划分文档分类、自动添加文档标签，等等。

【功能截图】

![[2-odoo14documents-3386-b1c49e86.png]]

![[2-odoo14documents-3386-4dae1471.png]]

![[2-odoo14documents-3386-f6e3c55f.png]]

![[2-odoo14documents-3386-327807d6.png]]

![[2-odoo14documents-3386-7b72f657.png]]

## 补充/答案 1

下述修改可以安装模块web_fix解决，安装此模块后，不需要修改下述代码。
模块位置：OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\web_fix

Odoo 15.0, 文档模块在社区版用，需要做如下修改：OSCGODOO15\source\odoo\addons\web\static\src\legacy\scss\secondary_variables.scss  文件的最后，添加下面这段代码：

//来自企业版的变量

@mixin o-details-modal($top: 0, $bottom: 0) {

```python
    position: fixed;

    z-index: $zindex-modal;

    right: 0;

    top: $top;

    bottom: $bottom;

    left: 0;

}
```

@mixin o-details-modal-header {

```python
    padding: 0.7rem 1.4rem;

    height: $o-navbar-height;

}
```

@mixin o-details-hide-caret {

```python
    // Hide the caret. For details see https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary

    list-style-type: none;

    &::-webkit-details-marker {

        display: none;

    }

}
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
