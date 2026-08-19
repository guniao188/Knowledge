---
title: "Odoo钉钉集成模块odooDingTalk"
source: "http://www.thinkltd.cn/forum/2/odooodoodingtalk-3439"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo钉钉集成模块odooDingTalk

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odooodoodingtalk-3439>

模块链接：

【模块配置】

钉钉数据同步用的配置：

![[2-odooodoodingtalk-3439-0b3bd3bb.png]]

扫描登录用的APPId及Secret：

![[2-odooodoodingtalk-3439-9e83fd7b.png]]

钉钉回调函数设置。此设置的目的在于，当钉钉中进行某些操作（发生某种事项）时候，需要通知Odoo。钉钉通知Odoo的方式是，调用Odoo服务器端的一个特定URL（回调URL）。例如，钉钉审批通过后，调用回调URL通知Odoo，Odoo执行指定的模型方法。注意：进行此项配置时候，Odoo服务器上只可以有一个数据库，否则回调URL不知道对应到哪个数据库。

![[2-odooodoodingtalk-3439-c7ad0ab2.png]]

![[2-odooodoodingtalk-3439-16aa17ce.png]]

【模块功能】

1.  从钉钉同步部门、员工信息到Odoo，可以自动创建Odoo用户

2.  钉钉扫码授权登录Odoo，或钉钉免密登录Odoo

3.  Odoo表单推送到钉钉审批：1) 钉钉中做好审批表单、审批流程，Odoo中配置Odoo表单到钉钉表单的字段对应关系；2) Odoo表单推送到钉钉，Odoo表单上有钉钉审批状态字段；3) 钉钉审批通过后，钉钉通知Odoo表单（钉钉审批状态字段改变），Odoo继续后续流程。

4.  从钉钉抓取考勤记录到Odoo

5.  Odoo发送钉钉消息

![[2-odooodoodingtalk-3439-339841af.png]]

## 补充/答案 1

新建模型如果需要通过钉钉审批，必需维护两个信息：

1、模块必需继承消息      _inherit = ['mail.thread', 'mail.activity.mixin']

![[2-odooodoodingtalk-3439-f2269a6f.png]]

![[2-odooodoodingtalk-3439-c0bb603f.png]]

需增company_id   因为审批记录回调的时候不能准确定位单据，所以需要增加公司字段！

![[2-odooodoodingtalk-3439-71fea583.png]]

## 补充/答案 2

dingtalk_mc

dingtalk_message

dingtalk_user_ext

目前有在用钉钉的客户：沃开V14，科明、崇山生物V15

## 补充/答案 3

【钉钉审批功能配置】

Odoo中表单上增加按钮“提交至钉钉审批”，钉钉审批后，Odoo表单中“钉钉审批状态”自动改变。也可以设置钉钉审批后Odoo表单执行指定方法（如自动完成Odoo表单状态变化）。

![[2-odooodoodingtalk-3439-3eb3fad9.png]]

![[2-odooodoodingtalk-3439-57b03518.png]]

![[2-odooodoodingtalk-3439-a8b46b25.png]]

## 补充/答案 4

安装钉钉前需安装额外的三方库(requirements.txt)文件中。

具体安装见百度云盘视频：基础操作视频--> 钉钉安装前额外三方库

## 补充/答案 5

钉钉包安装requirement依赖指令：pip3 install -r /opt/odoo14/oscg-addons/dingtalk_mc/requirements.txt

## 补充/答案 6

Odoo“费用报表”模型到钉钉“报销”审批表单的配置：

![[2-odooodoodingtalk-3439-a1948400.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
