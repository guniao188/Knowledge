---
title: "反向代理nginx或apache对于上传的文件大小限制说明"
source: "http://www.thinkltd.cn/forum/1/nginxapache-703"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 反向代理nginx或apache对于上传的文件大小限制说明

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/nginxapache-703>

如果有开反向代理，即域名访问或者是隐藏端口号，就会有文件大小的限制，默认是1m

如果想更改参数，则需要更改后台文件的配置参数

nginx修改参数：

client_max_body_size 100m;

apache修改参数：

![[1-nginxapache-703-531893f1.png]]

## 补充/答案 1

![[1-nginxapache-703-1e79b4fe.png]]

实际修改示例。

![[1-nginxapache-703-6be772c0.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
