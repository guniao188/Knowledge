---
title: "如何默认安装OSCG会计科目表？"
source: "http://www.thinkltd.cn/forum/1/oscg-385"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 如何默认安装OSCG会计科目表？

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/oscg-385>

会计模块account 的文件 addons\account\\_init__.py  方法 _auto_install_l10n 中，会根据国家代码默认安装会计科目表。

修改国家代码 CN 对应的会计科目表即可默认安装科目表 l10n_cn_oscg ，如下图：

![[1-oscg-385-9745ccc8.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
