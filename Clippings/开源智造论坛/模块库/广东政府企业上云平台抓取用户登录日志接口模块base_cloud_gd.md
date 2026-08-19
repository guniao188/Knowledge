---
title: "广东政府企业上云平台抓取用户登录日志接口模块base_cloud_gd"
source: "http://www.thinkltd.cn/forum/2/base-cloud-gd-3349"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 广东政府企业上云平台抓取用户登录日志接口模块base_cloud_gd

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/base-cloud-gd-3349>

模块链接：OSCG_SVN\odoo_ecommerce\13.0SRC\base_cloud_gd

【模块功能】

1.  广东政府企业上云补助平台，要求企业系统提供接口供平台抓取用户日志数据，以证明企业系统真实在用。接口规范参考模块目录下的文件“上云上平台接口规范v1.0”

2.  本模块提供日志数据抓取的接口链接：/gdcloud/user_log ，测试验证方法参考该模块下的测试程序： base_cloud_gd\controllers\test.py

3.  本模块安装需要依赖Python包：pycryptodomex， 安装命令（root用户）：  pip3 install pycryptodomex

4.  模块其他功能包括： a. 用户登录日志中增加登录用的IP; b. 系统参数表中增加参数：ir.config_parameter  记录广东上云平台分配给公司的平台ID; c. 增加菜单：设置 | 用户&公司 | 用户登录日志， 记录用户登录日志：用户名、时间、登录IP

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
