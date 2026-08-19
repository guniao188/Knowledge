---
title: "忘记odoo管理员密码"
source: "http://www.thinkltd.cn/forum/1/odoo-561"
forum: "求助台"
author: "沙正武"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 忘记odoo管理员密码

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:沙正武 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo-561>

###### 链接：https://www.jianshu.com/p/afe7667bbf5d

#### 在Odoo7以前，密码都是明文显示。

- 直接使用数据库查询`res_users`这种表即可
  `select login,password from res_users; `

#### 在后面的版本,密码通过SHA-512 哈希加密。然后存储在password_crypt这个字段里

- 换个思路，直接使用python来生成SHA-512的哈希值。直接update 用户表中的password_crypt在字段
  `pip install passlib

``` python
from passlib.context import CryptContext
a = CryptContext(['pbkdf2_sha512']).encrypt('MY_PASSWORD')
```

然后用a的值来update

``` sql
UPDATE res_users SET password_crypt='your new password hash' WHERE id=1;
```

## 补充/答案 1

还可以更简单，找一个已知密码的用户，数据库查一下该用户的password_crypt 字段值，update到admin用户的
password_crypt字段上，则admin的密码就是那个已知密码。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
