---
title: "数据库命令还原后希望标识为neutralized测试库标识，如何操作"
source: "http://www.thinkltd.cn/forum/1/neutralized-3913"
forum: "求助台"
author: "符赛红"
published: 2024-04-07
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 数据库命令还原后希望标识为neutralized测试库标识，如何操作

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2024-04-07
> <http://www.thinkltd.cn/forum/1/neutralized-3913>

用命令还原的测试库环境账套，不会自动标记测试库，即上面这个红色醒目标识，为用户方便快速识别是在测试账套中：

![[1-neutralized-3913-8eb860e2.png]]

界面上还原测试库时勾选上：即可出现这个醒目标识。

![[1-neutralized-3913-ee1c3a6d.png]]

后台命令还原出来的数据库也想要有这个标识的操作方法如下：

![[1-neutralized-3913-a46171de.png]]

第一步：在系统参数里增加这个参数：database.is_neutralized设置为True，系统参数里找不到的话，请界面上创建一条这个系统参数

![[1-neutralized-3913-2616d1dc.png]]

第二步，在外部ID里面找到这张视图，关联进入，将这张视图存档的状态，改成生效状态：

键=web.neutralize_banner的视图由存档状态变成启用状态

![[1-neutralized-3913-3efb62a4.png]]

![[1-neutralized-3913-cf8252fc.png]]

刷新页面就能生效了。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
