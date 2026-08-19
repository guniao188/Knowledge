---
title: "Odoo企业微信登录验证auth_oauth_wechat"
source: "http://www.thinkltd.cn/forum/2/odooauth-oauth-wechat-3496"
forum: "模块库"
author: "肖相扶"
published: 2024-05-07
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo企业微信登录验证auth_oauth_wechat

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-05-07
> <http://www.thinkltd.cn/forum/2/odooauth-oauth-wechat-3496>

模块链接：OSCG_SVN\odoo_ecommerce\14.0SRC\企业微信验证登录Odoo\auth_oauth_wechat

【20240507刘祥海升级到Odoo17.0】17版本模块链接： https://gitlab.com/oscg-china/extra-addons/-/tree/17.0/auth_oauth_wechat [](https://gitlab.com/oscg-china/extra-addons/-/tree/17.0/auth_oauth_wechat?ref_type=heads)

OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\auth_oauth_wechat

【20240507吴键增强企业微信直接登录功能 】Odoo15.0中测试通过：

1.  点击企业微信中的Odoo应用APP，自动直接登录Odoo主页；
2.  在企业微信中点击Odoo服务器链接（如 [http://www.thinkltd.cn/web](http://www.thinkltd.cn/web) 注意要有 /web），自动直接登录Odoo；
3.  企业微信中点击来自Odoo的消息(如审批通知)，直接跳转到消息关联的单据Form画面。

配置方法及使用方法，参考该模块文件夹下面的文档 ”微信登录配置方法.docx“

【模块功能】

1.       Odoo登录页面上添加企业微信账号OAuth扫码登录的配置参数

2.       其他参数都默认填写好了，需要填写的是 客户ID

**3.       客户ID的格式是：corpid agentid corpsecret   三者间以一个英文空格隔开**

4.       作业域中，系统自动保存企业微信API调用的 access_token，不要手工修改

5.       其中身份验证网址，如果希望，扫码的企业微信用户ID没有绑定到Odoo的User，则自动在Odoo中创建一个User，则网址配置时候加上 “?create_user” 。例如：

6.       系统自动创建Odoo用户时候，该用户取值如下：

login：优先取企业微信在的手机号码，没有手机号码则取微信中的邮箱，也没有则取微信的用户账号ID

name : 优先取企业微信中的名称，没有则取微信用户账号ID

mobile: 从微信中取值

email: 从微信中取值

phone: 从微信中取值

权限组：取自Odoo自带的模板用户“Default User Template” （该用户处于归档状态） ，修改该用户的权限设置，即可设置默认权限组

7.       如果要归档一个自动从企业微信账号ID创建的Odoo的User，注意归档后还要修改其login，清除“OAuth用户ID(oauth_uid)”，否则该企业微信账号ID再次扫描时候，系统再次自动创建Odoo用户时候，会报数据库唯一性校验错误（OAuth服务商，OAuth用户ID必须唯一）。

【功能截图】

![[2-odooauth-oauth-wechat-3496-3556ddca.png]]

![[2-odooauth-oauth-wechat-3496-465b70e3.png]]

![[2-odooauth-oauth-wechat-3496-74c04e14.png]]

## 补充/答案 1

补充：

**corpid agentid corpsecret 三个参数**
**corpid：**

![[2-odooauth-oauth-wechat-3496-907bedb5.png]]

****

** agentid：**

![[2-odooauth-oauth-wechat-3496-5eb9f7e7.png]]

![[2-odooauth-oauth-wechat-3496-227a645c.png]]

**corpsecret：**
**

![[2-odooauth-oauth-wechat-3496-227a645c.png]]

**

![[2-odooauth-oauth-wechat-3496-c45aa6e6.png]]

作用域不需要填写，用户扫码登陆或者企业微信直接登陆后，会自动填写

企业要维护企业微信授权登陆的可信域配置

![[2-odooauth-oauth-wechat-3496-fb9dcdee.png]]

![[2-odooauth-oauth-wechat-3496-34f909d4.png]]

配置企业微信直接登录的网页登录可信域

![[2-odooauth-oauth-wechat-3496-4eb0103b.png]]

![[2-odooauth-oauth-wechat-3496-e5217df5.png]]

用户需接受信息的话需要在用户关联的联系人上的

![[2-odooauth-oauth-wechat-3496-b33358c8.png]]

模型需要增加一下访问权限，否则用户不能发送消息，会提示权限问题

![[2-odooauth-oauth-wechat-3496-04feef9b.png]]


## 附件

- [[附件/forum/2-odooauth-oauth-wechat-3496-odoo17企业微信登录.docx|odoo17企业微信登录.docx]] (823 KB)

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
