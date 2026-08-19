---
title: "Odoo消息和附件发送到企业微信/钉钉mail_wechat、mail_ding"
source: "http://www.thinkltd.cn/forum/2/odoo-mail-wechatmail-ding-3513"
forum: "模块库"
author: "肖相扶"
published: 2024-05-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo消息和附件发送到企业微信/钉钉mail_wechat、mail_ding

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-05-15
> <http://www.thinkltd.cn/forum/2/odoo-mail-wechatmail-ding-3513>

模块链接：OSCG_SVN\odoo_ecommerce\14.0SRC\企业微信验证登录Odoo\mail_wechat

OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\\mail_wechat

OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\mail_ding

【20240514吴键升级到Odoo17.0】OSCG_Git\17.0\extra-addons\mail_wechat

【2022年12月1日改善】即使设置成“企业微信”处理消息，如果是从外部发往Odoo的邮件，不以企业微信消息形式通知关注者，而是用邮件通知关注者（从Odoo系统发出的消息，以企业微信消息形式通知）。关注者也可以直接用邮件客户端回复客户。和客户间来往的邮件都会自动进入Odoo。

【模块功能】

1.  Odoo用户偏好，消息处理方式中，增加一种新方式“企业微信”。Partner表单上增加“企业微信UserID”字段

2.  如果用户偏好的消息处理方式是“企业微信”，且User对应的Partner上填写了“企业微信UserID”，Odoo的消息将发送到该User的企业微信中，包括消息中包含的附件也会以文件形式发到企业微信

3.  Odoo对接企业微信，接口信息参考这里：[Odoo14企业微信登录验证auth_oauth_wechat](http://www.thinkltd.cn/forum/2/question/odoo14auth-oauth-wechat-3496) 。系统自动查找企业微信登的录验证方式，从该验证方式中获取企业微信对接需要的参数（corpid, agentid, corpsecret）

4.  Odoo对接钉钉/钉钉授权登录，接口密钥等设置参考[钉钉扫码登录auth_oauth_ding](http://www.thinkltd.cn/forum/2/question/auth-oauth-ding-3575)

5.  注意：讨论中直接发的聊天信息不会发送到企业微信

6.  已知问题，消息中添加  中文名  附件文件，如果发送不到企业微信，则是Python的文件上传模块的一个Bug，参照这里 [解决Python3 requests库 post方法 上传附件，name和filename中文乱码问题_JiangDong的博客-CSDN博客_python requests 上传附件](https://blog.csdn.net/u013250071/article/details/82493892) ，修改Python包 urllib3 。修改方法如下截图

![[2-odoo-mail-wechatmail-ding-3513-8e2931ab.png]]

【功能截图】

![[2-odoo-mail-wechatmail-ding-3513-87211d89.png]]

![[2-odoo-mail-wechatmail-ding-3513-d8896305.png]]

![[2-odoo-mail-wechatmail-ding-3513-0c0c8515.png]]

钉钉消息截图

![[2-odoo-mail-wechatmail-ding-3513-d24991ee.jpg]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
