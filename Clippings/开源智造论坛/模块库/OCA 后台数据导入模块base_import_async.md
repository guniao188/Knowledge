---
title: "OCA 后台数据导入模块base_import_async"
source: "http://www.thinkltd.cn/forum/2/oca-base-import-async-3101"
forum: "模块库"
author: "Administrator"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA 后台数据导入模块base_import_async

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:Administrator | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-base-import-async-3101>

V15版本：[https://github.com/OCA/queue/tree/15.0/queue_job](https://github.com/OCA/queue/tree/15.0)

OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\base_import_async

模块链接：

13.0版本：

测试发现，上述12.0, 13.0 链接的模块不可安装/安装后不可使用，修改后可以使用的模块放到了SVN，如下：

SVN模块12.0： OSCG_SVN\odoo_ecommerce\12.0SRC\base_import_async

SVN模块13.0： OSCG_SVN\odoo_ecommerce\13.0SRC\base_import_async

- 该模块将一个大的csv数据导入文件拆分为多个小文件，每个文件100条数据，而后在后台分多job逐个文件导入。

- 经测试，product.template文件导入，i5 4核16G windows机器，使用本模块，每分钟大约导入300条数据。

- 数据导入时候，有时候会报一个js错，但好像不影响数据导入。

- 注意，本模块的使用依赖于 模块 queue_job，queue_job 需要开启Odoo多进程，odoo conf 文件需要按下述方法配置（参考 [/forum/2/question/ocaqueue-job-2750](http://www.thinkltd.cn/forum/2/question/ocaqueue-job-2750)）：
  [options]
```python
  (...)
  workers = 2
  server_wide_modules = web,queue_job

  (...)
```

  [queue_job]
  channels = root:2

## 补充/答案 1

测试用数据导入文件：

注意：该文件为product.template对象，共2万8千5百多条产品数据。该文件数据导入前，先创建产品分类“All / Internal” 。

数据导入：

拆分出的csv文件：

后台数据导入job：


## 原帖外链配图

![[2-oca-base-import-async-3101-x194038c2.png]]
<small>原始地址: /web/image/1841/snipaste_20190714_222207.png?access_token=9f294797-6ab3-4014-8b40-3dbddb5c7b3e</small>

![[2-oca-base-import-async-3101-x194038c2.png]]
<small>原始地址: /web/image/1843/snipaste_20190714_222431.png?access_token=41d249ae-a452-45c9-945c-81b544d0f11c</small>

![[2-oca-base-import-async-3101-x194038c2.png]]
<small>原始地址: /web/image/1845/snipaste_20190714_222545.png?access_token=d0b7dd0c-978b-4c3d-8da2-fa195a20186b</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
