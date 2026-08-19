---
title: "PostgreSQL 查看数据库、各表占用磁盘大小"
source: "http://www.thinkltd.cn/forum/1/postgresql-358"
forum: "求助台"
author: "沙正武"
published: 2023-05-04
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# PostgreSQL 查看数据库、各表占用磁盘大小

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:沙正武 | 2023-05-04
> <http://www.thinkltd.cn/forum/1/postgresql-358>

统计各数据库占用磁盘大小：

```python
SELECT d.datname AS Name,  pg_catalog.pg_get_userbyid(d.datdba) AS Owner,

    CASE WHEN pg_catalog.has_database_privilege(d.datname, 'CONNECT')

        THEN pg_catalog.pg_size_pretty(pg_catalog.pg_database_size(d.datname))

        ELSE 'No Access'

    END AS SIZE
```

FROM pg_catalog.pg_database d

```python
    ORDER BY

    CASE WHEN pg_catalog.has_database_privilege(d.datname, 'CONNECT')

        THEN pg_catalog.pg_database_size(d.datname)

        ELSE NULL

    END DESC -- nulls first

    LIMIT 20;
```

 以百赛的数据库为例

![[1-postgresql-358-9e48b33f.png]]

统计数据库中各表占用磁盘大小：

SELECT

```python
    table_schema || '.' || table_name AS table_full_name,

    pg_size_pretty(pg_total_relation_size('"' || table_schema || '"."' || table_name || '"')) AS size
```

FROM information_schema.tables

ORDER BY

    pg_total_relation_size('"' || table_schema || '"."' || table_name || '"') DESC;

![[1-postgresql-358-7f6c533c.png]]

查看表的记录行数

select relname, reltuples from pg_class join pg_namespace on (relnamespace = pg_namespace.oid)

where relkind = 'r' and pg_namespace.nspname = 'public'

  order by reltuples DESC;

![[1-postgresql-358-a65c4819.png]]

## 补充/答案 1

一些常用的PostgreSQL命令

查看版本信息

1.查看客户端版本

 psql --version

2.查看服务器版本

2.1查看版本信息

postgres=# show server_version;

2.2查看详细信息

postgres=# select version();

2.3 查看数字版本信息包括小版号

postgres=# show server_version_num;

或者

postgres=# select current_setting('server_version_num');

查看数据库文件路径的命令

show data_directory;  //需要superuser 用户

设置修改数据库的密码

sudo -u postgres psql

ALTER USER postgres WITH PASSWORD 'qazxsw';

查看pgsql进程，用于查看postgreSQL的端口，默认端口是5432

ps -ef | grep postgres

postgresql查看数据库、表、表空间（位置大小）、索引的方法    https://blog.csdn.net/silenceray/article/details/55198537

1.数据库

postgres=# \l    ----查看所有数据库

postgres=# select pg_database_size('test');    -----查看数据库的大小

postgres=# select pg_database.datname, pg_database_size(pg_database.datname) AS size from pg_database;   ----查看所有数据库的大小

postgres=# select pg_size_pretty(pg_database_size('test'));   ----以kb、mb、gb的形式显示数据库的大小

postgres=# \d         ---查看数据库的所有表

postgres=# \d a              -----查看表的信息（如果表中有索引会在下面显示索引的内容）

postgres=#  select pg_relation_size('a');    ----查看表的大小

postgres=# select pg_size_pretty(pg_relation_size('a'));    ------以kb、mb、gb的形式显示表的大小

postgres=# select pg_size_pretty(pg_total_relation_size('a'));   -----表的总大小，包括索引的大小

postgres=# \di                                           -------查看数据库的所有索引

postgres=#  select pg_size_pretty(pg_relation_size('a_index'));   -----查看索引大小

postgres=# \db             ------查看所有的表空间以及表空间对应的目录（pg_default、 pg_global为默认的表空间在data目录下）

postgres=# select pg_size_pretty(pg_tablespace_size('pg_default'));       ----查看表空间的大小

查看数据库服务器启动时间

SELECT pg_postmaster_start_time();

当前时间减去启动时间就是运行时间

postgres=# SELECT current_timestamp - pg_postmaster_start_time();

查看表的记录行数

select relname, reltuples from pg_class join pg_namespace on (relnamespace = pg_namespace.oid)

where relkind = 'r' and pg_namespace.nspname = 'public';

https://blog.csdn.net/t518vs20s/article/details/88395665   链接

1）查询当前所有连接的状态

select datname,pid,application_name,state from pg_stat_activity;

2）关闭当前state为 idle 空闲状态的连接

查看数据库剩余连接数：

select max_conn-now_conn as resi_conn from (select setting::int8 as max_conn,(select count(*) from pg_stat_activity) as now_conn from pg_settings where name = 'max_connections') t;

查看为超级用户保留的连接数:

show superuser_reserved_connections;

psql: FATAL:  53300: sorry, too many clients already

数据库连接已满，无法建立新的连接。

1、关闭空闲连接

select datname,pid,application_name,state from pg_stat_activity;

--查看目前所有的连接的进程id、应用名称、状态。

select pg_terminate_backend(pid) from pg_stat_activity;

--通过pid终止空闲连接

当前总共正在使用的连接数：

select count(1) from pg_stat_activity;

显示系统允许的最大连接数

show max_connections;

显示系统保留的用户数

show superuser_reserved_connections ;

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
