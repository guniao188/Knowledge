---
title: "Odoo15网站嵌入视频支持西瓜视频、哔哩哔哩视频的修改方法"
source: "http://www.thinkltd.cn/forum/1/odoo15-841"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo15网站嵌入视频支持西瓜视频、哔哩哔哩视频的修改方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo15-841>

Odoo网站嵌入视频默认支持的视频网站包括：'youtu.be', 'youtube.com', 'youtube-nocookie.com', 'instagram.com', 'vine.co', 'player.vimeo.com', 'vimeo.com', 'dailymotion.com', 'player.youku.com', 'youku.com'

如果需要支持西瓜视频 'ixigua.com'、哔哩哔哩视频 'player.bilibili.com', 'bilibili.com'，需要如下操作：

1.  代码文件 OSCGODOO15\source\addons\website\static\src\js\content\snippets.animation.js  代码行 var supportedDomains = ['youtu.be', 'youtube.com', 'youtube-nocookie.com', 'instagram.com', 'vine.co', 'player.vimeo.com', 'vimeo.com', 'dailymotion.com', 'player.youku.com', 'youku.com'];    增加西瓜和哔哩哔哩的支持，即改成 var supportedDomains = ['youtu.be', 'youtube.com', 'youtube-nocookie.com', 'instagram.com', 'vine.co', 'player.vimeo.com', 'vimeo.com', 'dailymotion.com', 'player.youku.com', 'youku.com'**, 'ixigua.com', 'player.bilibili.com', 'bilibili.com'**];

2.  代码文件 OSCGODOO15\source\addons\web_editor\static\src\js\wysiwyg\widgets\media.js  方法 _getVideoURLData 中 增加 else 的代码，如下图

else{

```python
        embedURL = url;

            type = 'directurl';

        }
```

![[1-odoo15-841-9fbd36fc.png]]

## 补充/答案 1

Odoo网站嵌入视频方法：

![[1-odoo15-841-fa0e9c0b.png]]

西瓜、哔哩哔哩视频URL获取方法：

![[1-odoo15-841-2e7e4826.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
