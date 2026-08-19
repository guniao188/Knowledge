---
title: "todesk连接客户服务器传输文件  通过指令移动到对应文件夹路径（刘祥海老师技术指导）"
source: "http://www.thinkltd.cn/forum/1/todesk-3909"
forum: "求助台"
author: "葛忠彪"
published: 2024-04-30
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# todesk连接客户服务器传输文件  通过指令移动到对应文件夹路径（刘祥海老师技术指导）

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:葛忠彪 | 2024-04-30
> <http://www.thinkltd.cn/forum/1/todesk-3909>

客户本地化部署服务器，未开放SSH链接，本文档说明如何通过todesk传输文件，并更新至Odoo对应addons文件夹内

1.      通过todesk连接客户服务器后，点击控制按钮-文件传输

![[1-todesk-3909-3edbb651.jpg]]

![[1-todesk-3909-ee7b1410.jpg]]

2.      如果客户给的是Odoo账户，则直接传输到开发老师配置的Odoo addons目录下，并跳转至第X步重启服务器即可

如果客户给的是其他账户，一般先存放在Home/桌面上,直接在红框位置输入Home，并一步步进入桌面菜单

![[1-todesk-3909-13f638a2.jpg]]

3.      选中本地文件传输到服务器桌面上

![[1-todesk-3909-d5dfa24a.jpg]]

4.      在桌面空白处点击右键，在终端中打开

![[1-todesk-3909-b9c0aa60.jpg]]

5.      使用移动文件的指令，把桌面上指定的文件夹移动到指定路径

sudo 空格 mv 空格  文件夹名 空格  路径

其中 quality* 代表桌面上所有名字为quality开头的文件夹

sudo mv quality* /mnt/odoo/odoo17/custom/addons/

6.      通过 cd 空格 路径的方式进入对应addons文件夹，并使用ll指令检查已移动成功

cd /mnt/odoo/odoo17/custom/addons/

7.      刚移动过去的文件夹，权限都属于当前登录账户而非Odoo，通过下述指令，把addons里文件夹的权限都改成Odoo

sudo chown -R odoo:odoo ../addons

注意如果当前在 addons就是../  如果当前在addons上一级例如custom是 ./addons

8.      切换到Odoo账户，并重启Odoo服务（每家重启指令可能不同，请看对应服务器信息）

su odoo

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
