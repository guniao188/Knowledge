---
title: "Smile生成模块依赖关系图smile_module_graph"
source: "http://www.thinkltd.cn/forum/2/smilesmile-module-graph-3064"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile生成模块依赖关系图smile_module_graph

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smilesmile-module-graph-3064>

模块链接：

Generate Modules Graph from Odoo's user interface with upward, downward tree view or both.

You need to install Graphviz to print graph. More infos on [http://www.graphviz.org](http://www.graphviz.org).

You can install it with pip:

> - sudo apt install python3-pip
> - pip3 install pydot

Features:

- Print all modules graph.
- Print graph of selected modules only from tree view.
- Print graph of specific module.
- Select upward, downward or both in tree view to print selected module's graph.
-

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_module_graph#id1)

To print all modules graph:

1.  Go to `Applications > Print Modules Graph`.

2.  A popup view of Modules Graph will be displayed.

3.  Filter displayed modules in function of their state.

    >
    >
    >
    >
    >

4.  Click on the button `Print Graph` to print the image of module's generated graph.

    >
    >
    >
    >
    >

5.  Download the png file.

    >
    >
    >
    >
    >

To print graph of selected modules:

1.  Go to `Applications` tree view.

2.  Select modules then go to `Print > Modules Graph` to print the graph.

    >
    >
    >
    >
    >

3.  Select type of tree view (Up or Down or Up & Down), then Print the graph.

    >
    >
    >
    >
    >

4.  resultant graph:

    >
    >
    >
    >
    >

You can also print a graph of specific module:

1.  Go to a specific module, for example CRM.

2.  From the button `Print Graph` in module's form, print the graph.

    >
    >
    >
    >
    >
    >
    >
    >
    >
    >
    >


## 原帖外链配图

![[2-smilesmile-module-graph-3064-x4d9774e4.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_module_graph/static/description/modules_graph_form.png</small>

![[2-smilesmile-module-graph-3064-xf5359835.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_module_graph/static/description/print_graph.png</small>

![[2-smilesmile-module-graph-3064-x888dbbe5.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_module_graph/static/description/installed_modules_graph</small>

![[2-smilesmile-module-graph-3064-x97118d37.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_module_graph/static/description/selected_modules.png</small>

![[2-smilesmile-module-graph-3064-x5573b64d.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_module_graph/static/description/print_modules_graph.png</small>

![[2-smilesmile-module-graph-3064-x2adc64a1.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_module_graph/static/description/resultant_graph.png</small>

![[2-smilesmile-module-graph-3064-x601aecf6.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_module_graph/static/description/graph_of_module.png</small>

![[2-smilesmile-module-graph-3064-x8a11fc9c.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/12.0/smile_module_graph/static/description/crm_graph.png</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
