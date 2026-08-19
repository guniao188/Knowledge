---
title: "Smile视图页面数据显示自动刷新smile_web_auto_refresh"
source: "http://www.thinkltd.cn/forum/2/smilesmile-web-auto-refresh-3054"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile视图页面数据显示自动刷新smile_web_auto_refresh

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smilesmile-web-auto-refresh-3054>

模块链接：

This module is a fork of web_auto_refresh developped by Fisher Yu on Odoo v10. This fork works with all non-edited views, not only with kanban and list views.

## [Configuration](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_web_auto_refresh#id1)

To configure this module, you need to:

1.  Go to `Setting > Technical > Actions > Window Actions`, find the desired action, activate the auto search Check box
2.  Add one automated action for the target model, in the linked automated action add the following python code:

     model.env['bus.bus'].sendone('auto_refresh', model._name).
    This automated action can be applied (when to run) to creation, update or delete per your requirement.

3.  It is also possible to force the opening of a page by indicating #action.

    > For example: an automatic return to the home page is done by executing the code:

    model.env ['bus.bus'].sendone ('auto_refresh', '#home')

##

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_web_auto_refresh#id2)

(We will take stock.picking as a example model)

1.  Activate the auto search from `Settings > Technical > Actions > Window Actions` menu :

    >
    >
    >
    >
    >

2.  Add the automated action for the target model from `Settings > Technical > automation > Automated Actions` menu :

    >
    >
    >
    >
    >

3.  Go to any view of the selected model, in display mode.

4.  In another session (login via another browser and other computer), create, change or delete records of the model, then save.

5.  The original view in display mode will be auto refreshed.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
