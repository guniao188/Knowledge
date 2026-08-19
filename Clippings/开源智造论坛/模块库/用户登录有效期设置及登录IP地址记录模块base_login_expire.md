---
title: "用户登录有效期设置及登录IP地址记录模块base_login_expire"
source: "http://www.thinkltd.cn/forum/2/ipbase-login-expire-3633"
forum: "模块库"
author: "肖相扶"
published: 2023-03-07
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 用户登录有效期设置及登录IP地址记录模块base_login_expire

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2023-03-07
> <http://www.thinkltd.cn/forum/2/ipbase-login-expire-3633>

模块位置：OSCG_Git\extra-addons\base_login_expire

【模块功能】

1.  用户表单上增加“登录有效期”字段expires，用户登录时间超过“登录有效期”，系统报Session Timeout错误，强制要求重新登录系统。登录有效期默认为12小时，登录有效期设置为0，则不作登录有效期检查。
2.  增加用户登录日志菜单，该菜单显示用户登录日志(res.users.log)，用户登录日志上增加 ip 字段，记录用户登录的IP地址。
3.  Odoo15, 16版本测试通过。

【功能截图】

![[2-ipbase-login-expire-3633-0ee3c9bd.png]]

![[2-ipbase-login-expire-3633-5c6b4538.png]]

## 补充/答案 1

这个可以做到是按用户是否有过操作来监测多长时间没有动作了，才退出吗？


## 评论

> [!quote] 符赛红 · 2023-04-28
> 这个可以做到是按用户是否有过操作来监测多长时间没有动作了，才退出吗？

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
