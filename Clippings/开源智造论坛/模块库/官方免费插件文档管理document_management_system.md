---
title: "官方免费插件文档管理document_management_system"
source: "http://www.thinkltd.cn/forum/2/document-management-system-3350"
forum: "模块库"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 官方免费插件文档管理document_management_system

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/document-management-system-3350>

当客户用社区版，但又想要文档管理时，可以用这个链接下载使用，因移植的企业版的文档模块，有可能无法直接在社区版上使用，会报js的一些前端错误

https://apps.odoo.com/apps/modules/13.0/document_management_system/

或者这个模块文档预览功能可以结合使用

https://apps.odoo.com/apps/modules/13.0/ks_binary_file_preview/

https://apps.odoo.com/apps/modules/13.0/document_page_work_instruction/

但均未做测试，需要测试后再给客户。

[
](https://apps.odoo.com/apps/modules/12.0/muk_web_preview_opendocument/)

## 补充/答案 1

如果移植的企业版的文档模块出现一闪而逝的CSS报错，可以用以下方法解决。[\\forum/1/question/odoo13error-undefined-variable-o-chatter-min-width-464]

把以下代码追加到odoo-server\addons\web\static\src\scss\secondary_variables.scss

![[2-document-management-system-3350-42f17fba.png]]

```python
    @mixin o-details-modal($top: 0, $bottom: 0) {
        position: fixed;
        z-index: $zindex-modal;
        right: 0;
        top: $top;
        bottom: $bottom;
        left: 0;
    }

    @mixin o-details-modal-header {
        padding: 0.7rem 1.4rem;
        height: $o-navbar-height;
    }
    @mixin o-details-hide-caret {
        // Hide the caret. For details see https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary
        list-style-type: none;
        &::-webkit-details-marker {
            display: none;
        }
    }
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
