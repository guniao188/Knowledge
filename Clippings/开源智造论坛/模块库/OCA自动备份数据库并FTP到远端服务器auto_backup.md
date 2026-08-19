---
title: "OCA自动备份数据库并FTP到远端服务器auto_backup"
source: "http://www.thinkltd.cn/forum/2/ocaftpauto-backup-2800"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA自动备份数据库并FTP到远端服务器auto_backup

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaftpauto-backup-2800>

模块链接：

这里有12.0版本

备份当前数据库，并sftp到指定的远端服务器。

## Database Auto-Backup

A tool for all your back-ups, internal and external!

###

### Installation

Before installing this module, you need to execute:

    pip3 install pysftp

###

### Configuration

Go to *Settings -> Database Structure -> Automated Backup* to create your configurations for each database that you needed to backups.

###

### Usage

Keep your Odoo data safe with this module. Take automated back-ups, remove them automatically and even write them to an external server through an encrypted tunnel. You can even specify how long local backups and external backups should be kept, automatically!

####

#### Connect with an FTP Server

#####

##### Keep your data safe, through an SSH tunnel!

Want to go even further and write your backups to an external server? You can with this module! Specify the credentials to the server, specify a path and everything will be backed up automatically. This is done through an SSH (encrypted) tunnel, thanks to pysftp, so your data is safe!

####

#### Test connection

#####

##### Checks your credentials in one click

Want to make sure if the connection details are correct and if Odoo can automatically write them to the remote server? Simply click on the ‘Test SFTP Connection’ button and you will get message telling you if everything is OK, or what is wrong!

####

#### E-mail on backup failure

#####

##### Stay informed of problems, automatically!

Do you want to know if the database backup succeeded or failed? Subscribe to the corresponding backup setting notification type.

####

#### Run backups when you want

From the backups configuration list, press *More > Execute backup(s)* to manually execute the selected processes.

## 补充/答案 1

###

### 上海华霆 备份不了数据库，手动备份提示

ValueError: : "

odoo-server.conf 配置

odoo13 缺省值  server_wide_modules = web,base

问题可参考以下链接

\https://github.com/Yenthe666/auto_backup/issues/122

## 补充/答案 2

1 下载模块auto_backup 12.0  \https://github.com/Yenthe666/auto_backup#12.0

2 安装依赖sudo pip3 install pysftp

3 安装模块和配置

![[2-ocaftpauto-backup-2800-6fba99ae.png]]

备份参数填写好后，到技术-> 安排的动作   设置备份规则后激活即可

![[2-ocaftpauto-backup-2800-203db043.png]]

 4 成功在本地和远程备份

![[2-ocaftpauto-backup-2800-7f80d68c.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
