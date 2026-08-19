---
title: "SaaS库管理模块saas_master"
source: "http://www.thinkltd.cn/forum/2/saassaas-master-3536"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# SaaS库管理模块saas_master

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/saassaas-master-3536>

模块位置：OSCG_SVN\odoo_ecommerce\15.0SRC\SaaS工具\saas_master

【模块功能】

1.  增加SaaS库管理功能，包括维护模板库，创建SaaS库（复制模板库创建一个新的SaaS库），维护SaaS库

2.  模板库可以位于不同的硬件服务器，创建的SaaS库和模板库位于同一台服务器

3.

【配置方法】

1.  一台SaaS管理用的Odoo服务器，例如域名 saas.oscg.cn，该Odoo中预先配置好一个管理数据库（数据库名称saas）安装本模块

2.  一台模板数据库用的Odoo服务器，例如域名 template.oscg.cn，该Odoo中预先配置好一个模板数据库（数据库名称template）

3.  配置泛域名解析 *.oscg.cn 指向 模板服务器的IP

4.  模板服务器的Odoo配置文件中，配置 dbfilter=^%d  ，表示以域名匹配数据库，例如 erp01.oscg.cn 则匹配数据库 erp01 （Odoo服务器上必须存在名为 erp01的数据库，否则系统自动跳转到创建数据库的页面）

## 补充/答案 1

【功能截图】

![[2-saassaas-master-3536-faa28fed.png]]

![[2-saassaas-master-3536-5f5adca8.png]]

![[2-saassaas-master-3536-dca266ce.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
