---
title: "二开短信收发模块base_sms"
source: "http://www.thinkltd.cn/forum/2/base-sms-3034"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开短信收发模块base_sms

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/base-sms-3034>

模块链接：OSCG_SVN\odoo_ecommerce\12.0SRC\base_sms

该模块使用助通科技的短信网关收发短信。助通科技网关接口参考该模块目录下的文件 sms_interface.doc

1.      勾选Partner，群发短信；

2.      短信发送接口，短信先放入短信队列表base.sms；

3.      增加计划任务，从短信队列表base.sms提取发送类的draft短信，发送出去；同时收取短信，插入到短信队列表base.sms，状态为Draft

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
