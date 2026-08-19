---
title: "第三方多Odoo数据库间数据自动同步管理base_synchro"
source: "http://www.thinkltd.cn/forum/2/odoobase-synchro-2815"
forum: "模块库"
author: "杨浔波"
published: 2024-03-21
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 第三方多Odoo数据库间数据自动同步管理base_synchro

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:杨浔波 | 2024-03-21
> <http://www.thinkltd.cn/forum/2/odoobase-synchro-2815>

【20221222升级到16.0版本】[https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/base_synchro](https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/base_synchro) 重构了所有代码，增加了在线代码调用远端服务器数据同步功能。新增功能截图：

![[2-odoobase-synchro-2815-03d32835.png]]

![[2-odoobase-synchro-2815-ce99e97a.png]]

模块链接：[https://github.com/JayVora-SerpentCS/SerpentCS_Contributions/tree/12.0/base_synchro](https://github.com/JayVora-SerpentCS/SerpentCS_Contributions/tree/12.0/base_synchro)

13.0版本：

14.0版本：[SerpentCS_Contributions/base_synchro at 14.0 · JayVora-SerpentCS/SerpentCS_Contributions · GitHub](https://github.com/JayVora-SerpentCS/SerpentCS_Contributions/tree/14.0/base_synchro)

【20220420增加】15.0性能改善版：OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\base_synchro

原来的版本性能极差，产品数据同步，10秒一条数据，改善后的版本1秒同步5条产品。

【20221116功能增加】增加方法 get_rpc_proxy() 获取远端数据库的rpc调用代理，而后可以使用 proxy.get('model') 方法获取远端的模型，调用模型的各种方法。服务器动作中的示例代码：

![[2-odoobase-synchro-2815-a0f45ee2.png]]

【模块功能】

1.  Servers to be synchronized 配置Odoo服务器信息，IP、Odoo端口、数据库、用户名、密码等，用于数据同步时候，发起Odoo RPC调用

2.  Synchronized objects 配置要同步的模型，模型字段，同步方式（下载 or 上传），数据过滤条件Domain。

3.  To Synchronize IDs 待同步的数据ID 。同步时候，系统把待同步（新增或更新）的数据的ID存放于此表。之后每次同步时候，先检查此表有无待同步的ID，如果有，则先同步此表的ID。没有待同步的ID，系统再按Latest Synchronization 时间筛选新修改的数据ID，存放于此表，后续逐个同步。

4.  Synchronized instances 第一次同步过来的数据，系统自动记录该数据的本地 ID，及 远程 ID。后续同步时候，系统查找此表，如果找到了，则更新，没找到则新增。

5.  同步时候，系统检查每个要同步的模型，筛选上次同步时间（Latest Synchronization，每次同步完系统自动记录同步时间）后，新增(create_date)或新修改(write_date)的数据。将此部分数据ID抓取下来，存放到 To Synchronize IDs中，存放时候，每条记录存放1000个id（默认值为1000，可以在 Todo Size 中设置）。

6.  many2one的字段，系统自动到Synchronized objects中查找关联的 ID，因此many2one关联的模型数据必须先同步。Synchronized objects 中的Sequence配置同步先后顺序，Sequence小的先同步。

7.  计划任务自动同步的配置方法：env['base.synchro'].schedule_sync(server_id, user_id)    server_id 是Servers to be synchronized 配置的Odoo服务器，user_id 是同步报告发给哪个User 。

```python
    【功能截图】

![[2-odoobase-synchro-2815-d4583023.png]]

![[2-odoobase-synchro-2815-caeda0a9.png]]

![[2-odoobase-synchro-2815-b8e501ec.png]]

    代码：
    server_id = env['base.synchro.server'].browse(1)
    user_id = env['res.users'].browse(2)
    env['base.synchro'].schedule_sync(server_id, user_id)
```

## 补充/答案 1

刘祥海老师技术指导

如果客户是域名访问且绑了证书（HTTPS）登录，以及做了 nginx跳转

例如乾坤的登录域名是[https://erp.ztqk.com.cn/](https://erp.ztqk.com.cn/)  此时就要如下图改造（我改的代码比较丑陋，主要看思路和效果）

![[2-odoobase-synchro-2815-69a29c42.png]]

![[2-odoobase-synchro-2815-5ad79b6a.png]]

## 补充/答案 2

【产品属性同步】带有属性、属性值、变体的产品同步配置要点：

1.  各模型同步顺序：

2.  1.  product.attribute
```python
    2.  product.attribute.value
    3.  product.template.attribute.line
    4.  product.product
```

3.  产品(product.product)同步时候，变体值需要同步的字段（两个）：

4.  1.  product_template_attribute_value_ids
    2.  product_template_variant_value_ids
    3.

## 补充/答案 3

如果多台服务器，需要改写增补代码：

示列如下：

``` MsoNormal
user_id = env['res.users'].browse(2)
server1 = env['base.synchro.server'].browse(1)
env['base.synchro'].schedule_sync(server_id1, user_id)
```

#第二台服务器

``` MsoNormal
server2 = env['base.synchro.server'].browse(2)
env['base.synchro'].schedule_sync(server_id2, user_id)
```

整个复杂的上传和下载的测试，有在华霆UDP平台使用示例，并有编写测试报告和详细操作说明。

请参考：

D:\svn\SVN\odoo_ecommerce\06.Customization\华霆电气\实施及配置\华霆合作工时及开发下的文件

【华霆武汉平台与DS分区服务器相互同步数据的功能的测试报告.docx】

**这个功能还能广泛用于客户系统版本ODOO的升级，需要带原来数据的情况，只要数据表相同。就比较容易同步进来基础数据。**

**业务数据如果已完成的话，没有测试哦，只测试到了基础数据。**

## 补充/答案 4

【功能截图】

1.  定义需要同步的模型，数据Domain，不同步的字段

2.  Wizard发起同步，系统自动将数据同步（上传、下载）到目标数据库。实际动作是在目标数据库中Create或write记录

![[2-odoobase-synchro-2815-3673ab73.png]]

![[2-odoobase-synchro-2815-c725b07a.png]]

发起同步：

![[2-odoobase-synchro-2815-709ca0c1.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
