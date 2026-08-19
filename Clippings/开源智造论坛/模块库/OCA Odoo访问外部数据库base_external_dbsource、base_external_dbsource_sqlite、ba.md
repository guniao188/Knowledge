---
title: "OCA Odoo访问外部数据库base_external_dbsource、base_external_dbsource_sqlite、base_external_dbsource_mysql"
source: "http://www.thinkltd.cn/forum/2/oca-odoobase-external-dbsourcebase-external-dbsource-sqlitebase-external-dbsource-mysql-2756"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA Odoo访问外部数据库base_external_dbsource、base_external_dbsource_sqlite、base_external_dbsource_mysql

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-odoobase-external-dbsourcebase-external-dbsource-sqlitebase-external-dbsource-mysql-2756>

1.  通用外部数据库：

2.  SQLite数据库：

3.  MySQL数据库：

13.0模块：

This module allows you to define connections to foreign databases using ODBC, Firebird, Oracle Client or SQLAlchemy.

## [Configuration](https://github.com/OCA/server-backend/tree/11.0/base_external_dbsource#id2)

To configure this module, you need to:

1.  Database sources can be configured in Settings > Technical > Database Structure > Data sources.

##

## [Usage](https://github.com/OCA/server-backend/tree/11.0/base_external_dbsource#id3)

- Go to Settings > Technical > Database Structure > Database Sources
- Click on Create to enter the following information:
- Data source name
- Password
- Connector: Choose the database to which you want to connect
- Connection string: Specify how to connect to database

## 补充/答案 1

Sample connection strings:
    - Microsoft SQL Server:
      mssql+pymssql://username:%s@server:port/dbname?charset=utf8
    - MySQL: mysql://user:%s@server:port/dbname
    - ODBC: DRIVER={FreeTDS};SERVER=server.address;Database=mydb;UID=sa
    - ORACLE: username/%s@//server.address:port/instance
    - PostgreSQL:
        dbname='template1' user='dbuser' host='localhost' port='5432' password=%s
    - SQLite: sqlite:///test.db
    - Elasticsearch: https://user:%s@localhost:9200


## 原帖外链配图

![[2-oca-odoobase-external-dbsourcebase-e-x194038c2.png]]
<small>原始地址: /web/image/1239/snipaste_20190129_231851.png?access_token=b16978bc-bc3c-4f2b-b7c1-91cdde5d8f82</small>

![[2-oca-odoobase-external-dbsourcebase-e-x194038c2.png]]
<small>原始地址: /web/image/1241/snipaste_20190129_233310.png?access_token=7e5b2ef6-ebec-4209-bfd1-c9ece0de4b9b</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
