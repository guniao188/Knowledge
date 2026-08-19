---
title: "练习：平台：Odoo服务器加速的若干方法"
source: "http://www.thinkltd.cn/forum/1/odoo-546"
forum: "求助台"
author: "肖相扶"
published: 2023-05-04
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 练习：平台：Odoo服务器加速的若干方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-05-04
> <http://www.thinkltd.cn/forum/1/odoo-546>

【问题背景】

客户Odoo服务器经常抱怨速度慢，慢的原因通常有下面一些：

1.  js、css、fonts 等静态资源下载速度慢，尤其Odoo字体用的Google字体（fonts.googleapis.com），有时候，国内封锁的缘故，Google字体下载极慢（几分钟以上）。此问题引起的速度慢诊断方法：开启浏览器的开发者模式，看各个链接的下载速度，如果某些静态资源下载偏慢，则是此问题。此问题解决方法：购买CDN加速服务。Odoo集成CDN的参考例子：

2.  并发用户数量多，Odoo进程数太少（或者服务器CPU数量太少）。以阿里云为例，实测经验表明，一个Odoo进程最佳支持3个用户同时访问，超过5个用户同时访问就明显感觉慢。此问题引起的速度慢的诊断方法：查服务器CPU使用率（htop命令），如果总是有一核CPU使用率超过100%，其他核不高，则多半是此问题。此问题解决方法：如果Odoo和数据库在同一台服务器，按 CPU数量 n + 1 配置Odoo进程数量（留一半CPU给数据库），如果Odoo和数据库分开服务器部署，则按 2n + 1 配置Odoo进程数量。

3.  数据库缓存配置低。如果服务器内存很大，但使用率却很低，考虑增加Odoo每进程的内存上限，并增加数据库缓存配置。Postgresql性能优化参考这里 [/forum/1/question/postgresql-452](http://www.thinkltd.cn/forum/1/question/postgresql-452)

4.  程序代码问题。如Odoo中不恰当地使用了计算型字段，会引发某些操作特别慢。常见慢操作包括 Sale Order确认、Picking确认等。此问题的诊断：如果某个操作总是很慢，而且单据越大则明显更慢，则多半是程序代码有问题（如果时快时慢则多半是网络或服务器配置问题）。此问题通常需要优化程序代码，没办法通过优化服务器配置解决。低性能代码的调查方法参考：[/forum/3/question/odoo-36](http://www.thinkltd.cn/forum/3/question/odoo-36) 。

问题1：请调查 菲尔 服务器，SO确认时快时慢的问题，优化Odoo进程数量、进程内存、Postgresql性能配置，看看速度是否有明显改善。

问题2：调查华生服务器，看看是否静态资源加载速度慢（CDN问题）引发访问速度慢，如果是，请参考上面CDN配置文章，帮助华生配置好CDN，并观察看访问速度是否明显改善。

## 补充/答案 1

Odoo 13以上版本按照如下方式操作：

1. 必须先安装部署nginx，并且用通配符解析，保障ip,域名都可以访问80端口反向代理8069

2. 通过IP访问，打开开发者模式方可见CDN设置界面

3. 按照上述符老师要求进行设置操作。即刷选里设置

^/[^/]+/static/

^/web/(css|js)/

^/web/image

^/web/content

^/website/image/

域名设置：//CDN加速域名/

CDN域名解析的资源如下：

[
](https://su.baidu.com/)4. 对于客户的解释如下：

一、CDN加速套餐一般以海外CDN加速服务为优，但考虑到海外的CDN加速经常遇到政策性问题被封，无法提供永久的长期保障。

二、国内CDN因为政策性问题和带宽技术等问题，也会有效果不理想的可能，尽可能让客户自行去和CDN服务商沟通。我们能提供的是91OST.COM的二级域名的海外CDN加速用于测试（测试不承诺服务质量，只是技术性验证）是否可以通过CDN改善访问速度，如改善，说明是CDN问题，只需要客户自行寻找CDN服务商即可。

## 补充/答案 2

问题一：尝试创建销售订单时确实出现加载时间长的现象，htop信息cpu和内存占用都不高，从符老师那边得知用户最近没有反馈说创建订单和发票卡顿的情况。

![[1-odoo-546-2d92b413.png]]

  继续跟进问题-----待空闲时间开启多进程后再次创建测试

     -- 1月15日开启多进程，创建速度还是很慢，速度并没有提升，

查看日志显示一直在缓存

![[1-odoo-546-0cd2bd39.png]]

参考网址 \https://www.odoo.com/forum/help-1/question/hardware-for-50k-website-visitors-128995#answer-129016

优化pg工具

![[1-odoo-546-6efbbf78.png]]

当配置了内存限制后

limit_memory_hard = 1677721600

limit_memory_soft = 1073741824

![[1-odoo-546-86064a46.png]]

一个动作不应该会如此耗费内存的，所以准备请小施帮助，查看是否是模块的问题。

问题二：华生的odoo服务已开启CDN加速，但访问 watsonerp.com 仍然很慢，原来是使用的是别名解析的，当通过watsonerp.com.w.kunlunsl.com 访问时速度就很快了。

![[1-odoo-546-f1a02f7c.png]]

## 补充/答案 3

CDN需要用户购买付费流量，开通后，需要在数据库账套的【网站】的【配置/设置】菜单页面，配置相应的域名及cdn筛选

类似于这样

^/[^/]+/static/
^/web/(css|js)/
^/web/image
^/web/content
^/website/image/

另外，需要后台配置nginx要反向解析,80 代理8069

在云服务器上的CDN配置参考：

![[1-odoo-546-984ab4fc.png]]

![[1-odoo-546-39979ee7.png]]

![[1-odoo-546-d040d8e2.png]]

以上是华为云的配置截图示例。

如果是阿里云的服务器，可以参考阿里的详细操作说明

https://yq.aliyun.com/articles/744160?spm=a2c4e.11155472.0.0.611d1a7dYbpxva

https://yq.aliyun.com/articles/745377?spm=a2c4e.11155472.0.0.611d1a7d3tm9X2

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
