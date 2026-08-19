---
title: "OCA密码安全策略设置password_security"
source: "http://www.thinkltd.cn/forum/2/ocapassword-security-3038"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA密码安全策略设置password_security

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocapassword-security-3038>

模块链接：

This module allows admin to set company-level password security requirements and enforces them on the user.

It contains features such as

- Password expiration days
- Password length requirement
- Password minimum number of lowercase letters
- Password minimum number of uppercase letters
- Password minimum number of numbers
- Password minimum number of special characters

###

### Configuration

# Navigate to company you would like to set requirements on # Click the `Password Policy` page # Set the policies to your liking.

Password complexity requirements will be enforced upon next password change for any user in that company.

####

#### Settings & Defaults

These are defined at the company level:

| Name | Default | Description |
|----|----|----|
| password_expiration | 60 | Days until passwords expire |
| password_length | 12 | Minimum number of characters in password |
| password_lower | 0 | Minimum number of lowercase letter in password |
| password_upper | 0 | Minimum number of uppercase letters in password |
| password_numeric | 0 | Minimum number of number in password |
| password_special | 0 | Minimum number of unique special character in password |
| password_history | 30 | Disallow reuse of this many previous passwords |
| password_minimum | 24 | Amount of hours that must pass until another reset |

###

### Usage

Configure using above instructions for each company that should have password security mandates.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
