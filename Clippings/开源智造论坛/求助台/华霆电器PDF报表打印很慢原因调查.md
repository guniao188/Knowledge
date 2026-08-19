---
title: "华霆电器PDF报表打印很慢原因调查"
source: "http://www.thinkltd.cn/forum/1/pdf-617"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 华霆电器PDF报表打印很慢原因调查

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/pdf-617>

华霆电器Odoo 13服务器，HTML报表打印很快，PDF报表很慢。经调查，原因在于HTML转PDF的命令wkhtmltopdf 执行过程中，会从Odoo服务器获取 .css 文件。获取 .css 文件的链接类似    ，该url从浏览器访问是正常的，但从Odoo服务器上 wget 访问却超时。

经进一步调查，是对方换了路由器，新路由器防火墙原因，wget之类命令行无法获取css文件，导致pdf打印很慢超时。

服务器上手工执行 wkhtmltopdf 命令，同样很慢，而后报超时错误。wkhtmltopdf命令参数参考：

Odoo html转pdf命令行参考（代码文件 Odoo13\source\odoo\addons\base\models\ir_actions_report.py 的方法 def _run_wkhtmltopdf）：

/usr/local/bin/wkhtmltopdf  --disable-local-file-access  --cookie session_id  36637713f87a6a33f50eed0d9e33b850aedfd70f   --page-size A4  --margin-top 20.0  --dpi 90  --header-spacing  20 --margin-left  7.0  --margin-bottom  28.0  --margin-right  7.0  --orientation  Portrait  --header-html /odoo/pdf_test/report.header.tmp.4yglv1ws.html  --footer-html  /odoo/pdf_test/report.footer.tmp.ikysmy8b.html  /odoo/pdf_test/report.body.tmp.0.cfaxmada.html  /odoo/pdf_test/report.tmp.2.pdf

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
