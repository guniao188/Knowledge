---
title: "16版本浅层次去Odoo化方法"
source: "http://www.thinkltd.cn/forum/1/16odoo-3745"
forum: "求助台"
author: "葛忠彪"
published: 2024-07-05
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 16版本浅层次去Odoo化方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:葛忠彪 | 2024-07-05
> <http://www.thinkltd.cn/forum/1/16odoo-3745>

以往其他帖子

[http://www\\\.thinkltd\\\.cn/forum/1/odoo\\\-odoo\\\-398](http://www%5C%5C%5C%5C.thinkltd%5C%5C%5C%5C.cn/forum/1/odoo%5C%5C%5C%5C-odoo%5C%5C%5C%5C-398)

[http://www.thinkltd.cn/forum/1/odootileodoo-823](http://www%5C%5C%5C%5C.thinkltd%5C%5C%5C%5C.cn/forum/1/odootileodoo%5C%5C%5C%5C-823)

## 补充/答案 1

/addons/web/static/src/public/database_manager.qweb.html

第4行附近的title

/web/static/src/webclient/webclient.js

第36行附近的title

/web/views/webclient_templates.xml

第14行附近的title

上述内容是修改登录之前，网页页签左上角显示的Odoo字样

web/static/img/favicon.ico

把客户提供的图标文件的文件名改成favicon并替换，这一步是修改登录之前，网页页签左上角显示的图标

登录后网页页签左上角的图标是在公司form表单上添加图片

如果开启了网站的，是在设置模块里添加图片

上述完成后需要升级一下web模块(可以结合后续改动一起升级)

/web/static/src/webclient/user_menu_items.js

120行-125行附近documentation、support、profile、odoo_account行注释

删除用户菜单下，含odoo连接的菜单，例如odoo账户

/opt/odoo/odoo16/odoo-server/addons/web/static/src/public/database_manager.qweb.html

  并把图片上传至 第28行附近img后面的路径

改的是登录前选择数据库界面的大图片

/addons/web/static/src/public/database_manager.qweb.html

103行左右的small修改odoo和连接

以上是修改数据库管理界面中，创建数据库和还原数据库界面上的odoo字样和跳转连接

设置模块的视图里

隐藏整个“关于”区域，包括google商城连接、社区版等字样

找到 about附近的内容 把整个div设置invisible=1

修改一下归档的用户 odoobot的名字，然后清理一下系统消息

Odoo字段的Error弹窗，处理起来有利有弊（只能LOG看报错内容了），根据客户需求再确认

以及类似费用报销tree界面的谷歌连接，根据客户是否有这个模块单独处理视图或者调查去除方法

## 补充/答案 2

增加3处修改

pos点点击配置-编辑pos点、安装多语言后、设置模块新增pos门店 这3个弹窗的左上角odoo去除方法

这3个地方有一个共性，Odoo没有提前预置好一个窗口动作，而是通过def临时返回，此时因为没有申明动作名称，所以左上角显示Odoo，刻意增加个name参数就好了


## 附件

- [[附件/forum/1-16odoo-3745-odoo16浅层次去odoo化说明.docx|odoo16浅层次去odoo化说明.docx]] (1.5 MB)
- [[附件/forum/1-16odoo-3745-11号会议提到的去Odoo方法.doc|11号会议提到的去Odoo方法.doc]] (503 KB)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
