---
title: "微信小程序或H5页面参考模块oejia_weshop-12.0"
source: "http://www.thinkltd.cn/forum/2/h5oejia-weshop-12-0-3361"
forum: "模块库"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 微信小程序或H5页面参考模块oejia_weshop-12.0

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/h5oejia-weshop-12-0-3361>

网址：https://github.com/JoneXiong/oejia_weshop/tree/12.0

下载下来初步看是用的odoo本身的对象：客户，产品，订单数据表

支持在线客服：

https://developers.weixin.qq.com/miniprogram/introduction/custom.html#%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D
这是微信小程序自带的客服介绍，免费的，也能实现基础的客服功能，支持多个客服账号

微信小程序功能模块：

没有测试过，不确定会有多少坑，也不确定是否与odoo后台能完整融合

## oejia_weshop

oejia_weshop（OE商城） 是一套包含强大电商ERP后台的小程序商城系统。

oejia_weshop 是 Odoo 对接微信小程序实现的商城应用。

如果您使用odoo的销售模块，而想要在微信小程序上实现自己的商城卖odoo里的商品，装上 oejia_weshop 模块即可。

如果您想要搭建一套进销存(ERP)系统并实现对接微信商城的管理，用 Odoo + oejia_weshop 模块，是个快捷方法。

##

## 特性

- 和 odoo 销售模块无缝集成，产品和订单统一管理
- 微信用户集成到 odoo 统一的客户（partner）管理
- 支持 Odoo 10.0、11.0、12.0

##

## 使用

1.  下载源码 (odoo10、11为master分支，odoo12为12.0分支）
2.  将整个oejia_weshop目录(名称不能变)放到你的 addons 目录下
3.  安装依赖的python库：xmltodict、pycrypto、itsdangerous；安装模块，可以看到产生了顶部“小程序”主菜单
4.  进入【设置】-【对接设置】页填写你的微信小程序相关对接信息
5.  小程序客户端: 见项目 [wechat-app-mall](https://github.com/JoneXiong/wechat-app-mall), 下载后修改接口api调用路径为您的odoo url即可，可参考[这里](https://github.com/JoneXiong/wechat-app-mall/blob/f2/README.md)修改

参考资料: [常见问题处理](http://oejia.net/blog/2018/12/21/oejia_weshop_qa.html)

##

## 试用

##

-

## 商务版示例截图：

## 

![[2-h5oejia-weshop-12-0-3361-30d7f629.png]]

## 测试订单

## 

![[2-h5oejia-weshop-12-0-3361-7d5a441f.png]]

## 

![[2-h5oejia-weshop-12-0-3361-22cd9c3c.png]]

## 文描支持后台直接编辑复制粘贴；

## 

![[2-h5oejia-weshop-12-0-3361-581f9b5b.png]]

## 微信登录使用的是新开发的数据表；

## 

![[2-h5oejia-weshop-12-0-3361-8ddfd8f1.png]]

## 

![[2-h5oejia-weshop-12-0-3361-507db61d.png]]

这里可以配置微信小程序手机端的shop横幅，电商类目，活动公告。

## 另外会做一些开发，加些优惠券之类的处理，以及相似产品的推荐销售。

-

## 这个模块独立于odoo的电商shop，是直接对接的odoo的sale.order订单。

## 客户的需求着重在于手机端下单和对接，故可以不使用pc端的shop来进行。

-

## 

![[2-h5oejia-weshop-12-0-3361-8e0571b4.png]]

![[2-h5oejia-weshop-12-0-3361-aceceb00.png]]

## 

![[2-h5oejia-weshop-12-0-3361-d37da7f3.png]]

-

## 商务版本功能支持：

主要特性

》支持odoo产品多规格变体

》下单的微信在线支付支持

》支持物流运费模板管理及运费计算规则配置

》支持快递物流跟踪信息的展示（对接快递鸟）

》打通Odoo的仓库管理，商品库存统一控制

》支持按客户类别显示不同商品

》支持商品对不同客户不同价格（odoo价格表机制）

》支持钱包功能，可以用钱包余额支付

》支持积分功能，积分明细查看

》支持小程序模板订阅消息推送，发货时自动触发消息推送

》支持小程序端三级分类导航

》支持生成商品海报图分享到朋友圈（可配合分销模块使用）

》支持扫条码/二维码加购物车下单

》售后退换货流程管理

》订单商品评价及管理支持

》允许多计量单位选择价格切换

》签到送积分功能

## 补充/答案 1

V13商务版本SVN路径：

D:\SVN\odoo_ecommerce\06.Customization\华霆电气\addons\V13addons\微信小程序

改后的模块见，有修改过产品图片显示的bug等

D:\SVN\odoo_ecommerce\06.Customization\华霆电气\addons\V13addons

另外源码开放的V12版本目录：

D:\SVN\odoo_ecommerce\12.0SRC\微信小程序

## 补充/答案 2

正泰的小程序模块路径是 /odoo/custom/xcx，其中包含小程序需要的3个模块 【oejia_weshop,  oejia_weshop_ent,  task_queue】

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
