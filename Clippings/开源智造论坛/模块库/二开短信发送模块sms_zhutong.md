---
title: "二开短信发送模块sms_zhutong"
source: "http://www.thinkltd.cn/forum/2/sms-zhutong-3276"
forum: "模块库"
author: "肖相扶"
published: 2025-04-07
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开短信发送模块sms_zhutong

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2025-04-07
> <http://www.thinkltd.cn/forum/2/sms-zhutong-3276>

模块路径：

【20220730新增】OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\sms_zhutong

OSCG_SVN\odoo_ecommerce\13.0SRC\sms_zhutong

【模块设计】

1.  助通科技短信发送模块参考代码  [二开短信收发模块base_sms](http://www.thinkltd.cn/forum/2/base-sms-3034)

2.  Odoo 13提供了标准的短信发送API：单条发送 /iap/message_send，多条发送 /iap/sms/1/send 。接口参数等说明参考代码文件 odoo\addons\sms\models\sms_api.py

3.  本模块增加一个service_name为‘sms’ 的应用内购买记录（模型 iap.account），应用内购买记录参考代码文件 odoo\addons\iap\models\iap.py

4.  系统参数表中增加参数 'sms.endpoint'， 该参数指定短信发送服务器的url （实施时候，填写安装了本模块的odoo服务器url即可）

5.  系统参数表中，参数 sms_zhutong.username配置助通账号名，参数 sms_zhutong.password配置助通密码

6.  助通短信平台上的操作：1) 添加短信签名，如短信“【德马泰克科技】欢迎使用耀中耀华教育网络，您的验证码是：2743，15分钟内有效。请不要把验证码泄露给其他人，如非本人操作请忽略！”, 【德马泰克科技】 即为短信签名。发送短信时候，短信内容必须以短信签名开头。2) 注意让助通客服开通短信免审，否则短信提交后，可能要几十分钟后才能收到。

## 补充/答案 1

【模块用法】

1.  配置短信接口的URL、用户名、密码

2.  Parnter填写手机号码，点 SMS 发送短信

3.  查看正在发送或发送失败的短信列表（发送成功的短信系统会自动删除）

![[2-sms-zhutong-3276-1c9f1435.png]]

![[2-sms-zhutong-3276-be223ca5.png]]

![[2-sms-zhutong-3276-0f66243d.png]]

助通短信平台上的配置：短信接口用户名和密码

![[2-sms-zhutong-3276-08792903.png]]

提交短信签名并通过审核，否则不能发短信。

![[2-sms-zhutong-3276-7a75104e.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
