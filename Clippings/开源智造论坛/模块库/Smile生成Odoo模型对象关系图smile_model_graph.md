---
title: "Smile生成Odoo模型对象关系图smile_model_graph"
source: "http://www.thinkltd.cn/forum/2/smileodoosmile-model-graph-3063"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile生成Odoo模型对象关系图smile_model_graph

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smileodoosmile-model-graph-3063>

模块链接：

Generate Models Graph from Odoo's user interface with depth and relation names between models.
You need to install Graphviz to print graph. More infos on [http://www.graphviz.org](http://www.graphviz.org). You can install it with pip:

- sudo apt install python3-pip
- pip3 install pydot
-

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_model_graph#id1)

After activating the Developer Mode, go to `Settings > Technical > Database Structure > Models`.

Select your model for which you want to download the graph. For example, `ir.model`. Then click on Print button and choose `Models Graph`.

Select the number of depth you want to display and finally click on `Print Graph`.

The result for the `ir.model` will be:

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
