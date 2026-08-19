---
title: "服务器：云服务器重启后发现无法登录SSH的问题"
source: "http://www.thinkltd.cn/forum/1/ssh-3631"
forum: "求助台"
author: "符赛红"
published: 2023-02-01
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 服务器：云服务器重启后发现无法登录SSH的问题

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2023-02-01
> <http://www.thinkltd.cn/forum/1/ssh-3631>

经与华为云沟通确认发现是服务器运维操作过程中导致的。

运维修改为ssh访问监听的端口号之后，云服务器没有重启过，所以仍会以默认的22登录。

导致云服务器重启后，ssh就登录不了。

另外，如果客户云服务器有买系统盘和数据盘的话，

数据盘运维只操作了手动挂载，但并没有执行自动挂载的处理，导致云服务器上一旦重启，就会发生数据盘丢失的问题，从而无法访问到任何数据库账套，数据丢失的情况。

请务必在新购服务器安装时，一定要手动挂载和自动挂载都需要操作一下。

参考华为云帮助文档

[https://support.huaweicloud.com/qs-ecs/zh-cn_topic_0085634797.html](https://support.huaweicloud.com/qs-ecs/zh-cn_topic_0085634797.html)

![[1-ssh-3631-d1b22477.png]]

数据盘ssh端口号监听变更，以及手动和自动挂载查看和操作处理视频录制说明：

链接：[https://pan.baidu.com/s/1FuZyb2P6c_HXj-WChkptTg?pwd=f4ft](https://pan.baidu.com/s/1FuZyb2P6c_HXj-WChkptTg?pwd=f4ft)
提取码：f4ft
--来自百度网盘超级会员V5的分享

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
