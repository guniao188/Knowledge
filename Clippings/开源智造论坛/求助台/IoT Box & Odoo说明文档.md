---
title: "IoT Box &amp; Odoo说明文档"
source: "http://www.thinkltd.cn/forum/1/iot-box-odoo-3848"
forum: "求助台"
author: "张鹏飞"
published: 2024-09-06
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# IoT Box &amp; Odoo说明文档

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:张鹏飞 | 2024-09-06
> <http://www.thinkltd.cn/forum/1/iot-box-odoo-3848>

一、**所需硬件设备，事前工作**

硬件设备

1、PC

2、USB鼠标、键盘（最好是有线的避免烧录程序没有驱动）

3、IoT Box

4、HDMI显示器接口

5、网线

6、32G+内存卡

7、读卡器

8、充电线（与IOT Box匹配的，需要大多需要单独购买，IOT Box不会附赠）

事前工作：

1、IoT Box要求使用https域名，需要提前配置SSL证书

2、与官方沟通提前开启IoT Box订阅（免费）

3、要求域名仅供Odoo使用（如不要出现https给Odoo用，http另外使用）

二、**准备工作**

1、下载对应版本的镜像文件，地址：

https://www.odoo.com/documentation/17.0/applications/productivity/iot/config/flash_sdcard.html

2、下载、解压对应版本的镜像，地址：https://nightly.odoo.com/master/iotbox/

3、下载并安装烧录程序，地址：https://etcher.balena.io/#download-etcher

**三、配置步骤**

1、选择烧录文件

2、选择烧录的磁盘

3、选择磁盘后进行烧录

4、烧录完成后，将SD卡弹出，插入IOT Box，连接好相应设备

5、连接显示器后等待开机，右键打开浏览器

6、PC访问IoT Box的IP地址，要求PC与IoT Box处于同一局域网（需加端口号，默认8069）

7、odoo进入IoT Box，进入配置页面，点击【CONNECT】按钮，复制Tocken

需要注意：这里需要配置https的tocken，因此需要提前购买证书，配置https，对于配置了https后Tocken仍然显示http的原因是系统参数没有更新，手动更新一下就好了

8、在IoT Box的IP中粘贴Tocken，点击CONNECT

9、配置完成刷新odoo的IoT Box页面

参考文档：

​

## 补充/答案 1

截的图太多了，放出来上传不上去，具体看参考文档哈


## 评论

> [!quote] 张鹏飞 · 2023-12-29
> 截的图太多了，放出来上传不上去，具体看参考文档哈


## 附件

- [[附件/forum/1-iot-box-odoo-3848-IOT Box & Odoo说明文档.docx|IOT Box & Odoo说明文档.docx]] (6.8 MB)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
