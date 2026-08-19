---
title: "Odoo Environment 开发时的安全方便的调用测试验证方式"
source: "http://www.thinkltd.cn/forum/1/odoo-environment-914"
forum: "求助台"
author: "杨浔波"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo Environment 开发时的安全方便的调用测试验证方式

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:杨浔波 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo-environment-914>

建议在调用Environment（self.env）方式是无需代码里用调试语句验证，只需启动odoo的shell模式即可。方式如下

Macos用iTerm，Windows用cmd 敲入以下命令：

python odoo-bin shell -d DatabaseName

![[1-odoo-environment-914-8610389c.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
