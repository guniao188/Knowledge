---
title: "mit恢复数据库脚本"
client: mit
type: 项目文档
phase: 实施期
yuque_url: "https://www.yuque.com/xinsuixiaoyao-degek/klxky6/orhvq9uyvu15cyvi"
yuque_slug: "orhvq9uyvu15cyvi"
tags: [Odoo, 实施期, 客户/mit, 技术, 正在实施]
created_at: "2026-06-10T02:50:49.000Z"
updated_at: "2026-06-26T07:07:25.000Z"
published_at: "2026-06-18T14:28:44.000Z"
---
# mit恢复数据库脚本

```
unzip odoo_18_mit_3.zip -d /mnt/odoo/odoo18/custom/addons/dump.sql.zip

createdb -U odoo -O odoo 客户数据库名

sudo -u postgres createdb -O odoo odoo18_mit_1
sudo -u postgres dropdb mit

sudo -u postgres psql -d mit_master -f /mnt/odoo/odoo18/custom/addons/dump.sql
sudo -u postgres psql -d odoo18_618_1 -f /mnt/odoo/odoo18/custom/addons/618_1dump.sql
sudo -u postgres psql -d mit_master01 -f /mnt/odoo/odoo18/custom/addons/new_dump.sql
sudo -u postgres psql -d odoo18_mit -f /mnt/odoo/odoo18/custom/addons/614mit_cn_recreate_full.sql
psql -U odoo -d 客户数据库名 -f /tmp/restore/odoo_18_mit_3/dump.sql

psql -U odoo -d odoo18_mit_2 -f mit_cn_community_full.sql
./odoo-bin -c odoo.conf -d <db_name> -u web,website --stop-after-init

rsync -a --info=progress2 \
  /mnt/odoo/odoo18/data/db_filestore/mit_master01/ \
  /mnt/odoo/odoo18/data/db_filestore/filestore/mit_master01/


  sudo -u postgres psql -d mit_5 -c "DELETE FROM ir_attachment WHERE url LIKE '/web/assets/%';"
sudo -u postgres psql -d mit_5 -c \
  "UPDATE ir_config_parameter SET value = 'http://14.103.73.17:8069' WHERE key = 'web.base.url';"
sudo -u odoo /opt/odoo/odoo18/odoo-server/odoo-bin \
  -c /mnt/odoo/odoo18/custom/odoo.conf \
  -d mit_5 \
  -u web,sale,account,purchase,stock,mrp,studio_customization \
  --stop-after-init
```
