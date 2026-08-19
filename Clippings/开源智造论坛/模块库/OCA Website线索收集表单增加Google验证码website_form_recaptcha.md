---
title: "OCA Website线索收集表单增加Google验证码website_form_recaptcha"
source: "http://www.thinkltd.cn/forum/2/oca-websitegooglewebsite-form-recaptcha-3039"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA Website线索收集表单增加Google验证码website_form_recaptcha

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-websitegooglewebsite-form-recaptcha-3039>

模块链接：

Adds a ReCaptcha field widget for website forms (extends the website_form module).

**Translations**

This module will try to use the language of your website. If it can't find it for any reason, it will default to google API and use the language of the browser or your location.

## [Configuration](https://github.com/OCA/website/tree/11.0/website_form_recaptcha#id4)

First of all you must obtain a ReCaptcha key from [Google](http://www.google.com/recaptcha/admin)

**Global setup**

- Add site key to recaptcha.key.site system parameter
- Add secret key to recaptcha.key.secret system parameter

**Single website setup**

- Go to website settings
- Set site key and secret key

##

## [Usage](https://github.com/OCA/website/tree/11.0/website_form_recaptcha#id5)

To use this module, you need to:

- Already have a form-enabled model (refer to website_form docs)
- Set website_form_recaptcha to True on that model (similar to enabling forms)
- Add an element with the o_website_form_recaptcha class anywhere in the form

Look at website_crm_recaptcha module for example implementation.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
