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

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
