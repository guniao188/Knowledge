---
title: "固定list列表视图中列的方法"
source: "http://www.thinkltd.cn/forum/1/list-3951"
forum: "求助台"
author: "高彩霞"
published: 2024-08-06
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 固定list列表视图中列的方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:高彩霞 | 2024-08-06
> <http://www.thinkltd.cn/forum/1/list-3951>

1、找到源码中的web模块，在/opt/odoo/odoo16/odoo-server/addons/web/static/src目录下新增一个文件夹fixedhead，将附件中步骤1的3个文件放在该目录下

![[1-list-3951-e3f6266d.png]]

2、在/opt/odoo/odoo16/odoo-server/addons/web目录下的[__manifest__.py](https://__manifest__.py)文件中的

```python
    "web.assets_backend_legacy_lazy":段代码的前面一个[]中将以下代码增加进去
                'web/static/src/fixedhead/js/main.js',
                'web/static/src/fixedhead/scss/main.scss',
                'web/static/src/fixedhead/xml/style.xml',
```

![[1-list-3951-72b07edc.png]]

3、在/opt/odoo/odoo16/odoo-server/addons/web/static/src/views/list目录下的list_renderer.xml视图中44行和45行中间增加以下代码

![[1-list-3951-9e6673a3.png]]

所有代码见附件

更改后的list列表中就会有一个小钉子，点击小钉子就是从当前这个字段前面的都固定，后面的列可以来回拖动，效果图如下：

![[1-list-3951-d3639c1e.png]]


## 附件

- [[附件/forum/1-list-3951-固定列.zip|固定列.zip]] (4 KB)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
