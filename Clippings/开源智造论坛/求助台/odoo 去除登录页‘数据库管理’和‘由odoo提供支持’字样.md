---
title: "odoo 去除登录页‘数据库管理’和‘由odoo提供支持’字样"
source: "http://www.thinkltd.cn/forum/1/odoo-odoo-398"
forum: "求助台"
author: "符赛红"
published: 2023-05-04
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# odoo 去除登录页‘数据库管理’和‘由odoo提供支持’字样

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2023-05-04
> <http://www.thinkltd.cn/forum/1/odoo-odoo-398>

## 1、去除登录页面的数据库等连接，如下图：

## 方法一：

①、修改odoo.conf 文件里面的 list_db = True，将其修改‘False’即可：

``` prettyprint
list_db = False
注意：该方法仅隐藏数据库管理。
```

- 1

```python
  ``` prettyprint
  list_db = False
  ```
```

- 2

```python
  ``` prettyprint
  注意：该方法仅隐藏数据库管理。
  ```
```

②、去除‘由Odoo提供支持’:
A、激活开发者模式–>设置–>技术–>用户界面–>视图：

B、搜索框输入“login_layout”：

C、进入"Login Layout"注释如下代码：

D、点击保存，则登录界面去除‘数据库管理’和‘由odoo提供支持’字样：

## 方法二：

①、在自己开发的登录模块中进行处理：
注释：重写了‘addons–>web–>views–>webclient_templates.xml’的368~373行代码：

实现效果：

## 方法三：

方法三和方法一基本一样，一个从可视化进行操作，一个从后端代码中进行操作，建议使用方法一；
代码位置：‘addons–>web–>views–>webclient_templates.xml’的368~373行：

实现效果：

![[1-odoo-odoo-398-04485503.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
