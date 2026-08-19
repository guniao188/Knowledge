---
title: "Smile数据库代码升级管理smile_upgrade"
source: "http://www.thinkltd.cn/forum/2/smilesmile-upgrade-3060"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile数据库代码升级管理smile_upgrade

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smilesmile-upgrade-3060>

模块链接：

This module helps you upgrade database automatically after code update and server restarting.

### [Usage](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_upgrade#id2)

####

#### [Configuration](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_upgrade#id3)

#####

##### [Upgrade tree view](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_upgrade#id4)

Upgrades directory must be structured like this:

    project
    ├── upgrades
    |   ├── 1.1
    |   |   ├── __upgrade__.py
    |   |   ├── *.sql
    |   |   ├── *.py  # only for post-load
    |   |   ├── *.csv  # only for post-load
    |   |   ├── *.xml  # only for post-load
    |   ├── 1.2
    |   |   ├── __upgrade__.py
    |   |   ├── *.sql
    |   ├── upgrade.conf

You can find an example of upgrade in [demo directory](https://github.com/Smile-SA/odoo_addons/blob/12.0/smile_upgrade/smile_upgrade/demo) of this module.

#####

##### [Configure the version](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_upgrade#id5)

Fill the file *__upgrade__.py* with following options:

- version

- databases: let empty if valid for all databases

- translations_to_reload: language codes list to reload in post-load

- description

- modules_to_install_at_creation: modules list to install at database creation

- modules_to_upgrade: modules list to update or to install

- pre-load: list of .sql files

- post-load: list with .sql, .py, .csv and .xml files
  - .../filename (depending on option upgrades_path) or
  - module_name/.../filename

Each Python file in post-load must have a function post_load_hook(env)

#####

##### [Configure the version to load](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_upgrade#id6)

The upgrade version to load is set in file *upgrade.conf*, at the root of the *upgrades* directory, with this content (replace the version by your version number):

    [options]
    version=1.2

####

#### [Execute an upgrade](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_upgrade#id7)

#####

##### [Odoo configuration](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_upgrade#id8)

Update your Odoo configuration file with the following options:

- upgrades_path (required): path to the upgrades directory
- stop_after_upgrades (default: False): stop server after upgrades if True

#####

##### [Execute upgrade](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_upgrade#id9)

To execute an upgrade, you need to launch server with the following command:

    odoo.py -c  -d  --load=web,smile_upgrade

####

#### [Additional features](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_upgrade#id10)

#####

##### [Specify error management](https://github.com/Smile-SA/odoo_addons/tree/12.0/smile_upgrade#id11)

In post-load, you can replace filename string by tuple to specify error management.

Available options are:

- raise (default value): if an error is raised, stop upgrade execution by raising the error
- rollback_and_continue: if an error is raised, rollback to the savepoint set before the file execution and continue with the other files of the list
- not_rollback_and_continue: if an error is raised, no rollback is done and continue with the other files of the list

Example:

```python
    'post-load': [
        ('post-load/fix_product_pricelist.py', 'rollback_and_continue'),
    ],
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
