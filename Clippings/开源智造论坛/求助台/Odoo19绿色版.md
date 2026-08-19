---
title: "Odoo19绿色版"
source: "http://www.thinkltd.cn/forum/1/odoo19-4074"
forum: "求助台"
author: "肖相扶"
published: 2025-10-24
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo19绿色版

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2025-10-24
> <http://www.thinkltd.cn/forum/1/odoo19-4074>

【说明】

1.  下载链接：[https://drive.weixin.qq.com/s?k=AJMA_QfeAAcKiEl6su](https://drive.weixin.qq.com/s?k=AJMA_QfeAAcKiEl6su) ，下载zip包，解压即可
2.  source文件夹下为odoo源码，版本更新时候，从github下载源码，分别覆盖odoo、addons、enterprise三个文件夹即可
3.  bin文件夹有odoo的conf文件，及log文件
4.  runtime文件夹为python及postgresql的运行文件。第一次启动时候，会自动创建Postgresql数据簇文件夹 runtime\data
5.  myaddons文件夹下面放二开的，或者第三方下载的addons
6.  start.bat，双击启动PostgreSQL数据库，及Odoo系统； stop.bat，双击停止Odoo系统，及PostgreSQL数据库。
7.  绿色包自带数据库版本为PG 16.0，数据库超级密码参见文件 bin\odoo.conf 中标注的超级密码，为 w6gy-dru3-xr7z

【Bug注意】第一次运行 start.bat 启动是正常的，但第二次启动报错，不能启动。修正方法如下：start-pg.bat文件，if not exist %data_dir% set initdb="T" 代码行的前面，增加一行代码 set initdb=""  如下截图 

![[1-odoo19-4074-2c69b73b.png]]

【启停方式】

1.  启动：文件夹解压后，双击 start.bat 。系统第一次启动时候，自动初始化数据库文件夹data，初始化过程中会提示输入数据库管理员 postgres 的密码，可以任意输入，如 odoo，按提示输入两遍。
2.  系统默认的数据库端口为 5432，Odoo端口为 8069
3.  停止： 双击 stop.bat ，系统自动停止Odoo，再停止PostgreSQL数据库。
4.  操作截图 

![[1-odoo19-4074-55727ce1.png]]

 

![[1-odoo19-4074-5c85755d.png]]

![[1-odoo19-4074-cb3d45e1.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
