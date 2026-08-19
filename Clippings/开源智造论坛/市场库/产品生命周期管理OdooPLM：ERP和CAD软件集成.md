---
title: "产品生命周期管理OdooPLM：ERP和CAD软件集成"
source: "http://www.thinkltd.cn/forum/4/odooplm-erpcad-3972"
forum: "市场库"
author: "肖相扶"
published: 2024-08-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/市场库
---

# 产品生命周期管理OdooPLM：ERP和CAD软件集成

> [!info] 来源
> 开源智造论坛 · 市场库 | 作者:肖相扶 | 2024-08-16
> <http://www.thinkltd.cn/forum/4/odooplm-erpcad-3972>

Odoo是世界排名第一的免费开源ERP软件，Odoo的应用市场上有几万个功能插件，其中有个产品生命周期管理插件OdooPLM，可以实现CAD制图软件和ERP BoM的无缝集成。

OdooPLM包含两部分，一部分是CAD Client，一部分是OdooPLM。在本机上安装CAD Client，它会在CAD软件中增加Odoo集成的插件。该插件将CAD中的零件、图纸和Odoo ERP中的料号、BoM、图纸文档关联在一起。如下面截图所示，CAD中的设备图纸，点击OdooPLM插件中的Save图标，系统自动在Odoo ERP中创建/更新零件料号、BoM物料清单、图纸文档。

![[4-odooplm-erpcad-3972-170759e3.png]]

另一部分，OdooPLM模块，安装在Odoo ERP中。该模块增强了Odoo的料号、BoM和图纸管理功能。如下面截图，是CAD中一键保存到ERP中的零件料号看板。每个零件，名称、料号编码、样图、dwg图档，一键上传到了Odoo ERP中。

![[4-odooplm-erpcad-3972-4b31160a.png]]

OdooPLM还集成了Web 3D引擎 Three.js，CAD软件上传到Odoo ERP中的3D图档，如下面图示，可以在网页上可视化旋转预览。

![[4-odooplm-erpcad-3972-eb210c1a.png]]

OdooPLM支持市面上常见的CAD软件，包括 AutoCAD、SolidWorks、SolidEdge、ThinkDesign、Inventor、DraftSight等。

![[4-odooplm-erpcad-3972-6ebe12a2.png]]

Odoo ERP，以及Odoo上的PLM模块OdooPLM都是免费开源的。CAD端插件CAD Client，作者的收费是350欧一个用户。这样一个开源的PLM系统，各位觉得怎么样。

---

相关:[[Clippings/开源智造论坛/市场库/00-市场库索引.md|← 市场库索引]]
