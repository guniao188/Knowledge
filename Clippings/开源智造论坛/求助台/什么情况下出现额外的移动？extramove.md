---
title: "什么情况下出现额外的移动？extramove"
source: "http://www.thinkltd.cn/forum/1/extramove-306"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 什么情况下出现额外的移动？extramove

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/extramove-306>

很奇怪的，有装了限制负库存的功能，为啥仍然还是会产生额外的库存移动？产生这种额外移动的原因到底是什么？系统bug吗？

有开sn序列号，且之前有反馈偶然会产生extramove移动，导致负库存，后来装了负库存限制模块，仍然还是会出现这种情况，那到底导致extramove的逻辑是什么？可否协助调查一下？

额外发生了好几次了，目前接到的反馈不止一家客户出现，所以有必要了解下出现的原因，这样才知道 如何让用户避免这种错误。

## 补充/答案 1

extramove出现原因（详细作业中添加了一个初始作业上不存在的产品）   [/forum/1/question/bugextra-new-move-363](http://www.thinkltd.cn/forum/1/question/bugextra-new-move-363)

这里找到一个关于extra move的bug修复，Bug提出时间是2018年3月20日，修复时间是2018年3月27日。

下载Odoo最新代码替换一下，可能问题就没有了。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
