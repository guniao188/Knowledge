---
title: "二开模块base_wechat_crop企业微信登录"
source: "http://www.thinkltd.cn/forum/2/base-wechat-crop-3148"
forum: "模块库"
author: "施叶寒"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开模块base_wechat_crop企业微信登录

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:施叶寒 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/base-wechat-crop-3148>

1. 模块存放位置： SVN\odoo_ecommerce\12.0SRC\base_wechat_crop

2. 使用场景： 客户通过企业微信扫码登录odoo

3. odoo当前的不足：用户无法通过企业微信扫码登录odoo

4. 使用方法：

### 一、企业微信配置：

开启Qauth服务商：

![[2-base-wechat-crop-3148-5d7f7de0.png]]

![[2-base-wechat-crop-3148-1d234522.png]]

查看企业微信ID：登录企业微信——>我的企业（最底部）

![[2-base-wechat-crop-3148-50c447f4.png]]

查看agentID和secret：应用管理——>某个具体应用：

![[2-base-wechat-crop-3148-c264fa42.png]]

corp_secret获取：管理工具——>通讯录同步（必须是管理员登录才能看到）：

![[2-base-wechat-crop-3148-7ab924f0.png]]

![[2-base-wechat-crop-3148-2fa15d53.png]]

### 二、同步服务商：

同步服务商：

![[2-base-wechat-crop-3148-b8589453.png]]

同步成功之后，会看到服务商出现：weixin

![[2-base-wechat-crop-3148-12900696.png]]

![[2-base-wechat-crop-3148-12900696.png]]

三.一键同步用户

一键同步用户（只有同步服务商之后才会出现意见同步用户按钮）：

![[2-base-wechat-crop-3148-69f94b0b.png]]

一键同步用后，会看到微信用户关联到系统用户

![[2-base-wechat-crop-3148-63e4da59.png]]

![[2-base-wechat-crop-3148-6c6f485e.png]]

### 四、微信登录：

现在可以使用微信登录啦！

![[2-base-wechat-crop-3148-12a599ad.png]]

## 补充/答案 1

企业微信对接第三方模块参考

https://gitee.com/rainbowstudio/wxwork/tree/14.0/

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
