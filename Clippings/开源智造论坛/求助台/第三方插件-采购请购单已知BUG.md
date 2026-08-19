---
title: "第三方插件-采购请购单已知BUG"
source: "http://www.thinkltd.cn/forum/1/bug-944"
forum: "求助台"
author: "葛忠彪"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 第三方插件-采购请购单已知BUG

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:葛忠彪 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/bug-944>

https://apps.odoo.com/apps/modules/15.0/purchase_request/

第三方插件采购请购单，比odoo自带的采购计划单好用一点

但是在多公司环境下，创建请购单会报错，原理如下

默认请购单编号为 New

并且写了代码，当编号为New时，清空New，去调取 自动序号

而在多公司情况下，自动序号只归属了其中一个公司，导致其他公司账套调不到序号，编号就为空了，就报错了

简单粗暴的做法是把序号上的公司置空

![[1-bug-944-17000138.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
