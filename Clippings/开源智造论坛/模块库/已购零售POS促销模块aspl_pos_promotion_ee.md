---
title: "已购零售POS促销模块aspl_pos_promotion_ee"
source: "http://www.thinkltd.cn/forum/2/posaspl-pos-promotion-ee-3252"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 已购零售POS促销模块aspl_pos_promotion_ee

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/posaspl-pos-promotion-ee-3252>

模块链接：

模块下载链接（如果链接过期请找购买人 King 重发下载链接）：

## 补充/答案 1

问题一  促销规则上如何增加适用门店 的条件？

1.  pos.promotion 模型上增加 many2many 到 pos.config 的字段

2.  代码文件 Odoo12\myaddons\aspl_pos_promotion_ee\static\src\js\promotion.js 中，促销规则加载的地方，添加适用门店的条件 ['x_poses','in',[self.config.id]]

![[2-posaspl-pos-promotion-ee-3252-3ab63fa2.png]]

![[2-posaspl-pos-promotion-ee-3252-a2e10e43.png]]

问题二  买X送Y的促销规则，如何实现多买多送？

实现方法：设置规则 买 3X 送 3Y ，买 2X 送 2Y，买 1X 送 1Y

![[2-posaspl-pos-promotion-ee-3252-a6a96e85.png]]

应用效果

![[2-posaspl-pos-promotion-ee-3252-ef10c496.png]]

## 补充/答案 2

买 X 送 Y：

![[2-posaspl-pos-promotion-ee-3252-4e9b9715.png]]

应用效果

![[2-posaspl-pos-promotion-ee-3252-25b3133e.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
