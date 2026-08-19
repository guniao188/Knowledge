---
title: "Odoo即时聊天im_系列模块介绍"
source: "http://www.thinkltd.cn/forum/2/odooim-3030"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo即时聊天im_系列模块介绍

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odooim-3030>

Odoo社区版自带的即时聊天/即时消息相关的模块有：

im_livechat
im_livechat_mail_bot
website_livechat
crm_livechat
website_helpdesk_livechat

## 补充/答案 1

【Odoo即时聊天群组】

【Odoo即时聊天窗口，及聊天机器人】

【Odoo即时聊天命令】聊天窗口支持的命令说明：

- @ 显示所有User，

- # 显示所有公开群组

- : 显示可用的聊天短句缩写

- / 显示聊天命令，常见聊天命令有：/help 显示帮助信息，/who 列示当前群组的所有User， /leave 退出当前群组。/lead 线索标题， crm_livechat模块提供，以当前聊天对象为客户，创建线索。/helpdesk ticke标题，website_helpdesk_livechat模块提供，创建工单Ticket。/helpdesk_search 关键词， 搜索工单。

【在线聊天/在线客服】

## 补充/答案 2

【即时聊天命令实现原理】

1.  模型 'mail.channel' 检查所有形如“_define_command_XXX”的方法，获取 XXX 作为命令，保存在命令列表中。聊天时候，/XXX 则查找命令列表，js直接调用 'mail.channel' 的execute_command，执行_execute_command_XXX 方法，执行命令。

2.  所以，继承模型 'mail.channel'，实现方法 “_define_command_XXX” 和 “_execute_command_XXX” ，即可增加新命令。

```python
class MailChannel(models.Model):
    _inherit = 'mail.channel'

    def _define_command_lead(self):
        return {'help': _('Create a new lead (/lead lead title)')}

    def _execute_command_lead(self, **kwargs):
        partner = self.env.user.partner_id
```


## 原帖外链配图

![[2-odooim-3030-x194038c2.png]]
<small>原始地址: /web/image/1569/snipaste_20190331_213422.png?access_token=f7b1c460-33eb-4de7-9315-a3d50eb3d5b2</small>

![[2-odooim-3030-x194038c2.png]]
<small>原始地址: /web/image/1571/snipaste_20190331_211640.png?access_token=68a0c7fb-e0e6-40e2-88da-62d8778bb5d4</small>

![[2-odooim-3030-x194038c2.png]]
<small>原始地址: /web/image/1573/snipaste_20190331_211058.png?access_token=12e8f62e-5fc7-4e7e-ba27-af4019546520</small>

![[2-odooim-3030-x194038c2.png]]
<small>原始地址: /web/image/1575/snipaste_20190331_213831.png?access_token=f585fef5-857e-4309-9398-373e87ee26ef</small>

![[2-odooim-3030-x194038c2.png]]
<small>原始地址: /web/image/1577/snipaste_20190331_214036.png?access_token=424a4fcd-67de-492b-a4d1-3a3cbe456429</small>

![[2-odooim-3030-x194038c2.png]]
<small>原始地址: /web/image/1583/snipaste_20190331_221407.png?access_token=973fcd05-6c0b-4521-bb63-dcdc26a56455</small>

![[2-odooim-3030-x194038c2.png]]
<small>原始地址: /web/image/1579/snipaste_20190331_215639.png?access_token=105f2315-21b4-414c-b685-bab827ef9a05</small>

![[2-odooim-3030-x194038c2.png]]
<small>原始地址: /web/image/1581/snipaste_20190331_215625.png?access_token=2937566e-dae0-4b4d-bdb8-975f22a192ba</small>

![[2-odooim-3030-x194038c2.png]]
<small>原始地址: /web/image/1585/snipaste_20190331_222106.png?access_token=b0b6a309-96e0-4da0-8e04-bbfd79299eab</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
