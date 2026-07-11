服务器进入数据库
sudo -u postgres psql

\l              -- 查看所有数据库
\c 数据库名      -- 切换数据库
\dt             -- 查看当前库所有表
\d 表名          -- 查看表结构
\du             -- 查看用户/角色
\dn             -- 查看 schema
\q              -- 退出 psql


CREATE DATABASE mydb;

DROP DATABASE mydb;

ALTER DATABASE old_name RENAME TO new_name;


执行sql:
 sudo -u postgres psql -d LGC_ERP_MASTER -f /mnt/sale_order_5_SINGLE_UPDATE.sql