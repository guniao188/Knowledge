---
title: "产品图片、css文件、附件在file_store中的存储机制"
source: "http://www.thinkltd.cn/forum/1/cssfile-store-883"
forum: "求助台"
author: "肖相扶"
published: 2025-11-12
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 产品图片、css文件、附件在file_store中的存储机制

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2025-11-12
> <http://www.thinkltd.cn/forum/1/cssfile-store-883>

【原理说明】

1.  Odoo中的附件(ir.attachment)，实体文件存储在Odoo conf 文件的配置项目 data_dir 指定的文件夹下面的 file_store子文件夹中。 file_store文件夹下面，每个Odoo数据库对应一个子文件夹（以数据库名称命名）。

2.  附件模型(ir.attachment)中，字段 url 指定web访问路径，字段 store_fname 指定磁盘上的存储路径，checksum指定该附件数据的唯一标记。res_model, res_id, res_field指定该附件对应哪个模型的哪个id的哪个字段的值（Image或Bianary类型的字段，如产品的图片字段）。如下截图示例

3.  checksum的作用，上传附件文件（或产品图片文件），系统生成该文件的checksum，而后在 附件(ir.attachment) 中搜索该checksum，如果找到了，说明之前上传过该附件，直接取附件的store_fname作为新附件的store_fname，即两个附件对应同一个file_store的磁盘文件。

4.  下面第二个截图表示，模型product.template的id=96的产品的image_256字段对应的图片是file_store下的文件 77/77ad8a8797afa1aeeebbc69deb9ae5aafc1fefb7。如果该产品图片不显示，检查方法：先检查对应图片 附件(ir.attachment) 是否存在，其次检查file_store的文件是否被删除或者被破坏。附件是否被破坏的检查方法，下载附件，如果是图片文件，用图片软件看看是否可以正常打开。

5.  Odoo对css、js文件的处理，模块安装时候，系统自动编译模块中包含的css、js等文件，编译后的文件生成一条附件记录，附件的字段 url 为该css、js文件的web访问地址，store_fname为该附件的实际存储地址，file_size 为该文件大小。

6.  有时候Odoo界面显示异常(显示不全，缺乏格式信息等)，多数情况是某个css文件或js文件加载出错。打开浏览器开发者模式，查看哪个web_url的文件下载出错。根据web_url查看 附件(ir.attachment)记录的 store_fname ，检查一下是否磁盘文件被删除了或被损坏了。

7.  开启Odoo的开发者模式 “Activate the developer mode (with assets)”，系统会自动重新加载css、js文件（而不是取附件中的编译后文件）。因此该模式下css、js文件显示不全的问题可以自动解决。

![[1-cssfile-store-883-fd30a2b2.png]]

![[1-cssfile-store-883-4cd39f9e.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
