---
title: "auth_ldap 实施方法"
source: "http://www.thinkltd.cn/forum/1/auth-ldap-621"
forum: "求助台"
author: "施叶寒"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# auth_ldap 实施方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:施叶寒 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/auth-ldap-621>

ldap模块参考 [/forum/2/question/odooadauth-ldap-3353](http://www.thinkltd.cn/forum/2/question/odooadauth-ldap-3353)

LDAP文件系统采用DC、OU、CN这三个关键字形成树状结构。其中，DC代表作用域，OU代表组织单元，CN代表文件标识。

    用户登录时，系统首先以配置的授权用户向服务器请求访问他的兄弟记录。如果通过认证，就去访问服务器中的LDAP base，即若干个‘OU=,OU=,DC=,DC=,’定义数据所在的目录，然后根据 界面登录的login当作CN，password当作对应的密码去做相应匹配。

LDAP Server address： 指定服务器的host地址，localhost

LDAP Server port： 指定服务器的端口，默认389

Use TLS： False

LDAP base： 服务器的目录，由甲方提供。格式如下：OU=Users,OU=CHN,DC=blasia,DC=bausch,DC=com

LDAP filter： 以用户名登录：sAMAccountName=%s；以邮箱登录：mail=%s

Sequence： 10

Create User： True

Template User： 创建新用户的模板用户

LDAP binddn： 以指定的用户发起请求。格式如下：CN=,OU=,OU=,DC=,DC=,

LDAP password: 指定用户的密码。

## 补充/答案 1

#### Windows 平台下安装**python_ldap ** 依赖需要**手动安装**，自动安装报编译错误

python_ldap 包的下载地址 https://www.lfd.uci.edu/~gohlke/pythonlibs/

我的电脑是64位的，python版本是3.7 那么就下载 【python_ldap-3.3.1-cp37-cp37m-win_amd64.whl】

如果电脑是64位的，python版本是3.6那就就下载   【python_ldap-3.3.1-cp36-cp36m-win_amd64.whl】

一定要一致，不然报平台不支持。

下载完成后 用cmd进入到包的下载目录中 然后执行pip install python_ldap-3.3.1-cp37-cp37m-win_amd64.whl 即可。
或者 python -m pip install python_ldap-3.3.1-cp37-cp37m-win_amd64.whl

LDAP 筛选   使用uid： uid=%s

配置参考

odoo官方：https://www.odoo.com/documentation/user/13.0/general/auth/ldap.html

错误解决：https://github.com/odoo/odoo/issues/34537

知乎对AD和LDAP的讲解：https://zhuanlan.zhihu.com/p/45553448

## 补充/答案 2

![[1-auth-ldap-621-e677cf2f.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
