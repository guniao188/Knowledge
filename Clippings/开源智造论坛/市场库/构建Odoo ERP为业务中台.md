---
title: "构建Odoo ERP为业务中台"
source: "http://www.thinkltd.cn/forum/4/odoo-erp-3907"
forum: "市场库"
author: "肖相扶"
published: 2024-03-28
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/市场库
---

# 构建Odoo ERP为业务中台

> [!info] 来源
> 开源智造论坛 · 市场库 | 作者:肖相扶 | 2024-03-28
> <http://www.thinkltd.cn/forum/4/odoo-erp-3907>

如何基于世界排名第一的免费开源Odoo ERP系统构建业务中台？Odoo作为ERP软件，拥有几万个功能插件，功能应用非常丰富。其实Odoo还是一个非常优秀的企业应用快速开发平台。Odoo作为开发平台，自带标准的xml-rpc和json-rpc接口。企业其他系统可以通过Odoo的API KEY对授权了的数据对象做增删改查等任意操作，可以调用Odoo数据对象的所有其他业务方法。因为这个功能特性，Odoo非常容易作为业务中台使用。在Odoo中快速实现业务对象和业务控制 ，前端业务界面通过API KEY调用业务方法。

作为技术爱好者的福利，我把python语言通过Odoo API KEY调用Odoo的代码示例截图放在下面。这段程序代码十多行，实现的功能是，先通过Odoo API KEY取得Odoo认证（authenticate），而后调用客商表（res.partner，客户和供应商，Odoo中统一叫业务伙伴）的查询方法（search），查得所有客商的名称（name字段）列表。其他开发语言，如Java、PHP、GO、Javascript等任意开发语言都可以调用Odoo的API接口。Odoo API以JSON格式返回结果数据。

![[4-odoo-erp-3907-582c28e6.png]]

---

相关:[[Clippings/开源智造论坛/市场库/00-市场库索引.md|← 市场库索引]]
