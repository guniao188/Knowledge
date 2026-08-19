---
title: "客户使用本地服务器，打印报表时会转很久才能正常下载pdf文件"
source: "http://www.thinkltd.cn/forum/1/pdf-851"
forum: "求助台"
author: "葛忠彪"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 客户使用本地服务器，打印报表时会转很久才能正常下载pdf文件

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:葛忠彪 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/pdf-851>

排除掉数据量，报表代码，环境等原因，有可能是端口隐射的问题

因为客户的服务器是通过端口映射发布到公网上的，有可能我们工程师配置了直接的外网访问地址，导致打印PDF的时候无法加载到CSS样式，所以出现超时，所以在系统参数那里增加了report.url指向服务器本身就可以了

![[1-pdf-851-ee1e86e9.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
