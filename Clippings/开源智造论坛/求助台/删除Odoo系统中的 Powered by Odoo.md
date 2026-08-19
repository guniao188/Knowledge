---
title: "删除Odoo系统中的 Powered by Odoo"
source: "http://www.thinkltd.cn/forum/1/odoo-powered-by-odoo-243"
forum: "求助台"
author: "杨浔波"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 删除Odoo系统中的 Powered by Odoo

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:杨浔波 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo-powered-by-odoo-243>

> > 1.  database管理页面的LOGO替换：

> > 替换：/web/static/src/img/logo2.png

> >

> > 2. icon替换修改

> > 替换：web/static/src/img/favicon.ico

> >

> > 3. title标签属性修改：

> > （1）修改/web/view/database_manager.html

> > （2）修改survey/views/survey_templates.xml

> > （3）修改mass_mailing/views/unsubscribe_templates.xml

> >

> > 4. 修改未启用website时登录页当中的Powered By Odoo

> > 查找如下web/views/webclient_templates.xml代码并注释或修改：

> > 371行附近：

> >        [Powered by Odoo](https://www.odoo.com?utm_source=db\&amp;utm_medium=auth)

> >

> > 5. 修改系统设置界面当中的Odoo有关信息

> > （1）Odoo三大商城链接：

> > 查找：web_settings_dashboard/static/src/xml/dashboard.xml代码

> > 39行 ：

> > 整个DIV注释

> > （2）Odoo产品信息

> > 查找：/enterprise/web_enterprise/static/src/xml/base.xml代码

> > 220行：修改odoo相关字样

> > 查找：web_settings_dashboard/static/src/xml/dashboard.xml 代码

> > 113行：修改Odoo相关字样

> > 118行：区域块注释或修改

> > 93行：  去掉或修改之后的区域代码块或修改

> >

> > 6.修改Website的Create a free website with Odoo

> > 查找：/website/views/website_templates.xml 294行

> >  修改或注释相关Odoo代码

> >

> > 7. 修改登录后用户名下的Odoo.com账户sso链接和支持相关链接

> > 查找：web/static/src/xml/base.xml 1551行

> > [My Odoo.com account](#) 修改或注释相关代码

> >

> > 8. 修改Odoo登录后后台全局title属性

> > 查找：web/static/src/js/chrome/abstract_web_client.js 103行

> > this.set('title_part', {"zopenerp": "Odoo"}); 修改成自定义信息。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
