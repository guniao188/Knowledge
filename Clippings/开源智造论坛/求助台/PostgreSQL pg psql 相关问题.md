---
title: "PostgreSQL pg psql 相关问题"
source: "http://www.thinkltd.cn/forum/1/postgresql-pg-psql-653"
forum: "求助台"
author: "沙正武"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# PostgreSQL pg psql 相关问题

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:沙正武 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/postgresql-pg-psql-653>

****

**通过/web/database/manager备份出现以下错误**

**错误1：**Database backup error: Command `pg_dump` not found.

通过在odoo的配置文件中增加参数pg_path【数据库可执行文件路径】

   pg_path = /usr/lib/postgresql/10/bin/

**错误2：**Database backup error: Postgres subprocess ('/usr/bin/pg_dump', '--no-owner', '--file=/tmp/tmpihqdnjfj/dump.sql', 'odoo_watsonerp') error 1

原因1 是服务器上安装了多个版本的pg,而默认的pg_dump版本低于server的版本。更新pg_dump版本即可，通过以下命令

find / -name "pg_dump"

```python
  /usr/bin/pg_dump

  /usr/lib/postgresql/9.6/bin/pg_dump

  /usr/lib/postgresql/10/bin/pg_dump
```

rm /usr/bin/pg_dump

sudo ln -s  /usr/lib/postgresql/10/bin/pg_dump /usr/bin/pg_dump

如按照上面的操作还报同样的错，可以使用命令行手动备份出sql和filestore文件 然后还原。如果两边的数据库的所有者不一样，可以使用以下命令修改

A 服务器备份

pg_dump -p 5433 -h localhost --no-owner -F t -f /var/lib/postgresql/odoo_wats.tar2.gz  odoo_watsonerp

B 服务器恢复

CREATE DATABASE "odoo_watsonerp" WITH OWNER =openerp;

pg_restore  -Ft -d odoo_watsonerp -p 5433  /var/lib/postgresql/odoo_wats.tar.gz

alter database odoo_watsonerp owner to odoo;

![[1-postgresql-pg-psql-653-749452f6.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
