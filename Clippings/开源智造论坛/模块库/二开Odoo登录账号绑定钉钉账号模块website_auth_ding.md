---
title: "二开Odoo登录账号绑定钉钉账号模块website_auth_ding"
source: "http://www.thinkltd.cn/forum/2/odoowebsite-auth-ding-3282"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开Odoo登录账号绑定钉钉账号模块website_auth_ding

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoowebsite-auth-ding-3282>

【模块设计】
```python
    用户的“我的账号”页面上，增加一个website网页链接 “绑定钉钉登录”（如果已经绑定，则不显示）；
    “绑定钉钉”页面显示绑定钉钉的二维码，扫码绑定钉钉账号。
    用户以Odoo账号密码登录时候，登录成功后检查是已绑定钉钉，如果未绑定，则自动跳转到页面 “绑定钉钉账号” 。
```

## 补充/答案 1

【模块用法】

1. 用户登录后，在网站首页，进入我的账号；

‘2. 通过手机扫码绑定钉钉账号。

![[2-odoowebsite-auth-ding-3282-3886cc2d.png]]

![[2-odoowebsite-auth-ding-3282-6d377ec3.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
