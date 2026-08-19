---
title: "CSV数据文件批量自动导入模块 base_import_replace_extid"
source: "http://www.thinkltd.cn/forum/2/csv-base-import-replace-extid-3348"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# CSV数据文件批量自动导入模块 base_import_replace_extid

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/csv-base-import-replace-extid-3348>

模块链接：OSCG_SVN\odoo_ecommerce\13.0SRC\base_import_replace_extid

【模块功能】

1.  当字段添加、视图修改、动作菜单添加等，都通过csv文件导入方式实现时候，有几个问题：其一是，csv文件较多，每次导入都要点开不同菜单，分别导入，操作较为繁琐；其二是，搜索视图、动作、菜单等的 XML 数据里面，经常需要以外部ID形式引用别的数据，但系统标准的csv导入功能不支持此种形式的外部ID引用

2.  安装本模块后，运行模块文件夹下面脚本程序 csv_data/auto_import.py ，将自动导入该脚本所在目录下的 csv 数据文件。注意，运行该脚本程序之前，1) 请将程序中的服务器IP、用户名、密码等修改为自己服务器的参数；2) 需要导入的csv文件添加到脚本程序的csv_list

3.  csv数据文件制作时候，外部ID引用的地方，以大括号{{ id }}标记。自定义的id注意带上 __import__. ，例如：{{__import__.action_pm_batch_mrc}}

4.  数据导入时候，系统自动将大括号{{ id }}标记的外部id查找替换成数据库id

5.  csv_data/auto_import.py脚本默认csv文件为 gb2312 格式编码

6.  **注意事项**：**csv文件要求是 gb2312 格式编码，且不可以有多余的列（不导入的列）**

7.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
