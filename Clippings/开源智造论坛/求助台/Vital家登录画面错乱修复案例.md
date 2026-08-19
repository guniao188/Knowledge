---
title: "Vital家登录画面错乱修复案例"
source: "http://www.thinkltd.cn/forum/1/vital-884"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Vital家登录画面错乱修复案例

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/vital-884>

【问题现象】

1.  客户Vital Odoo13登录画面显示错乱，浏览器开发者模式查到 css 文件找不到（404错误）：09:15:58.826 GET https://erp.vitalmro.com/web/content/98045-571eeb2/3/web.assets_frontend.css  [HTTP/1.1 404 NOT FOUND 114ms]

2.  后台查附件文件 web.assets_frontend.css，以及数据库查该附件的存储路径（参考方法：[Odoo附件在file_store中的存储机制](http://www.thinkltd.cn/forum/1/question/odoofile-store-883)），发现硬盘上该文件大小为0，显然该css文件被破坏。

3.  从该服务器上另外一个数据库中，将附件文件web.assets_frontend.css，拷贝替换损坏的数据库的文件web.assets_frontend.css，命令示意如下：

![[1-vital-884-cb946db3.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
