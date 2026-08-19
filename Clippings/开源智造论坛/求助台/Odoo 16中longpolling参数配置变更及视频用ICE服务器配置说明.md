---
title: "Odoo 16中longpolling参数配置变更及视频用ICE服务器配置说明"
source: "http://www.thinkltd.cn/forum/1/odoo-16longpollingice-3635"
forum: "求助台"
author: "肖相扶"
published: 2023-02-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo 16中longpolling参数配置变更及视频用ICE服务器配置说明

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-02-10
> <http://www.thinkltd.cn/forum/1/odoo-16longpollingice-3635>

Odoo16中，不再使用longpolling参数，改成了 websocket参数，对应的nginx中配置方法如下：

```python
         location /websocket {
           proxy_pass http://odoo16chat;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection $connection_upgrade;
           proxy_set_header X-Forwarded-Host $host;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
           proxy_set_header X-Real-IP $remote_addr;
         }
    此外，odoo conf文件中，如果使用nginx的话，proxy_mode要设置为True： proxy_mode = True

    关于Odoo的视频会议功能，Odoo视频功能基于webrtc技术实现（参考 https://www.kaifaxueyuan.com/frontend/webrtc.html）。
    webrtc中，需要配置ICE服务器，还要配置https。
    ICE服务器配置方法如下面截图（用于测试的免费ice服务器，生产用的话，需要另外购买或搭建ice服务器）：
    turn: openrelay.metered.ca:443?transport=tcp   openrelayproject    openrelayproject

![[1-odoo-16longpollingice-3635-804a1fa4.png]]

```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
