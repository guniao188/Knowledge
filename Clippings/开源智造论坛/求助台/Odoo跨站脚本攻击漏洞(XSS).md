---
title: "Odoo跨站脚本攻击漏洞(XSS)"
source: "http://www.thinkltd.cn/forum/1/odoo-xss-3898"
forum: "求助台"
author: "肖相扶"
published: 2024-03-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo跨站脚本攻击漏洞(XSS)

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-03-15
> <http://www.thinkltd.cn/forum/1/odoo-xss-3898>

【问题背景】

1.  客户数皆智能的Odoo系统（Odoo15）被静安区网信办检测出“跨站脚本攻击漏洞(XSS)”。跨站脚本，即Cross Site Script (通常简写为XSS)是指攻击者利用网站程序对用户输入过滤不足，输入可以显示在页面上对其他用户造成影响的HTML代码，从而盗取用户资料、利用用户身份进行某种动作或者对访问者进行病毒侵害的一种攻击方式。
2.  测试方法，Odoo域名后面跟上链接(/web/set_profiling?profile=0&collectors=)  

![[1-odoo-xss-3898-98c1738a.png]]

  页面会自动跳转到百度网页
3.  经测试只有Odoo15有此问题，Odoo14、16、17都无此漏洞。
4.  修复建议：1. 输入验证和过滤：对用户输入的所有数据进行严格的验证和过滤，包括表单输入、URL参数、Cookie等。确保输入的数据不包含恶意脚本或特殊字符。
    2. 输出编码：对输出到浏览器的数据进行HTML编码，防止恶意脚本在浏览器中执行。可以使用现成的HTML编码库或函数进行编码。
    3. 限制脚本执行：在服务器端设置适当的Content-Security-Policy（CSP）头部，限制页面中脚本的执行，防止攻击者注入恶意脚本。

![[1-odoo-xss-3898-4025db32.png]]

【问题修复方法】

文件 OSCGODOO15\source\addons\web\controllers\profiling.py  方法def profile中，原代码行return json.dumps(state)替换成下面截图红框的代码。

![[1-odoo-xss-3898-b1df00b7.png]]

使用此方法进行处理返回值即可。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
