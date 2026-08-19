---
title: "Odoo12 -&gt; Odoo13版本升级技术解决方案"
source: "http://www.thinkltd.cn/forum/1/odoo12-odoo13-626"
forum: "求助台"
author: "杨浔波"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo12 -&gt; Odoo13版本升级技术解决方案

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:杨浔波 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo12-odoo13-626>

1. 先进入 选择分支13 将代码下载

2. 构建conf 文件 需要将db_name 参数表示12的数据库

3. 环境当中需要pip install git+git://github.com/OCA/openupgradelib.git

4. odoo-bin 启动命令除了加载-c 配置文件路径 另外增加 --update all --stop-after-init

5. 切换到正式的Odoo13环境，同理需要conf 文件 需要将db_name 参数表示12的数据库

6. 并且运行一次odoo-bin 启动命令除了加载-c 配置文件路径 另外增加 --update all --stop-after-init

7. 恢复正式环境的conf文件，正常启动访问选择升级好的12数据库

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
