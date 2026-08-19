---
title: "Odoo13、14 登录报错Error: Undefined variable: $o-chatter-min-width解决方法/会计报表格式没有"
source: "http://www.thinkltd.cn/forum/1/odoo1314-error-undefined-variable-o-chatter-min-width-464"
forum: "求助台"
author: "肖相扶"
published: 2023-02-03
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo13、14 登录报错Error: Undefined variable: $o-chatter-min-width解决方法/会计报表格式没有

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-02-03
> <http://www.thinkltd.cn/forum/1/odoo1314-error-undefined-variable-o-chatter-min-width-464>

Odoo15企业版会计模块社区版安装比之前版本简单，参考 [Odoo15、Odoo16的会计模块account_accountant社区版安装说明](http://www.thinkltd.cn/forum/1/odoo15odoo16account-accountant-812)

企业版一些模块挪移到社区版使用时，有时登录画面会出现下面报错。

**odoo15 出现这个错误可以通过安装模块****web_fix解决，**
**模块位置：OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\web_fix**

odoo14 出现这个错误可以通过安装模块 fix_no_o_chatter_min_width 模块位置 odoo_ecommerce\14.0SRC\fix_no_o_chatter_min_width

解决方法是代码文件： Odoo13\addons\web\static\src\scss\primary_variables.scss 的最后，添加下述两行代码行即可（来自企业版的变量定义）：

【注意】最新Odoo 13.0版本（2020/04/01之后的版本？），下面两行不是追加到文件 primary_variables.scss，而是追加到文件odoo\addons\web\static\src\scss\secondary_variables.scss  的最后。**如果不追加，登录报错一闪而过，似乎不影响使用。但会计报表的格式没有了（报表Style出错的原因）**。

// Side chatter
$o-chatter-min-width: 530px !default;

【会计报表格式报错】

![[1-odoo1314-error-undefined-variable-o-chatter-min-width-464-1a967559.png]]

![[1-odoo1314-error-undefined-variable-o-chatter-min-width-464-228adb80.png]]

【企业版会计模块社区版中应用修改】

会计模块 account_accountant 依赖于模块 mail_enterprise，而模块mail_enterprise依赖于 web_mobile, 而web_mobile依赖于web_enterprise。经测试，mail_enterprise的__manifest__.py文件中，去掉对 web_mobile的依赖也可以安装使用。

**请一定注意！！！  移除mail_enterprise的__manifest__.py文件中的web_mobile依赖，并且不要复制web_mobile模块到addons中,否者创建数据库会报错！！！**

## 补充/答案 1

V15的目录：D:\workspace\odoo-15.0\addons\web\static\src\legacy\scss
肖总写过一个模块，针对文档及报表打印报错的，可以直接安装web_fix

## 补充/答案 2

后台更新后，需要重启系统，并且界面升级，否则创建客户资料时，会报js错误。

更改了\web\static\src\scss\primary_variables.scss 和\web\static\src\scss\secondary_variables.scss
仍会在网站那里报错字体样式丢失的问题。

会计的报表是没有问题的，但【网站】首页时会报错。叉掉又不影响。

![[1-odoo1314-error-undefined-variable-o-chatter-min-width-464-4da77be3.png]]

## 补充/答案 3

应该不要升级，重启 + 页面刷新即可。

另外 Odoo14 企业版的 文档管理模块 documents 要在社区版应用，需要做如下SCSS文件修改：

**odoo14 出现这个错误可以通过安装模块 fix_documents_css
模块位置 odoo_ecommerce\14.0SRC\\fix_documents_css**

文件OSCGO DOO14\source\enterprise\web_enterprise\static\src\scss\search_panel_mobile.scss 中的内容全部复制到下述文件的最后：OSCGODOO14\source\addons\web\static\src\scss\search_panel.scss

重启、刷新页面生效。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
