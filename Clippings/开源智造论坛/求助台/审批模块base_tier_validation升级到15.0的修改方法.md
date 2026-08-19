---
title: "审批模块base_tier_validation升级到15.0的修改方法"
source: "http://www.thinkltd.cn/forum/1/base-tier-validation15-0-836"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 审批模块base_tier_validation升级到15.0的修改方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/base-tier-validation15-0-836>

文件 base_tier_validation\\_manifest__.py 做下述修改即可：

```python
    'assets': {

        'web.assets_backend': [

            'base_tier_validation/static/src/js/systray.js',

            'base_tier_validation/static/src/js/tier_review_widget.js',

            'base_tier_validation/static/src/scss/systray.scss',

            'base_tier_validation/static/src/scss/review.scss',

        ],

        'web.assets_qweb': [

            'base_tier_validation/static/src/xml/*',

        ],

     },
```

![[1-base-tier-validation15-0-836-fcc4664c.png]]

## 补充/答案 1

此外，Odoo 15，文件 base_tier_validation\models\tier_validation.py 需要做下述修改

1.  方法 message_post 的参数 subtype改成了 subtype_id, 传值也由以前版本的外部id改成了数据库id 。对应的该模块message_post调用的地方（共4处），需要如下修改：

2.  模型 bus.bus 的方法 sendmany 名称改成了  _sendmany ，参数 notifications也由两元素改成了三元素

3.

4.  

![[1-base-tier-validation15-0-836-3bde8f0e.png]]

5.

6.  返回外部ID改成返回数据库ID：

![[1-base-tier-validation15-0-836-7184fa94.png]]

调用处subtype改成subtype_id

![[1-base-tier-validation15-0-836-46e05cae.png]]

## 补充/答案 2

需要在界面上再增配置访问控制列表权限：

数据表comment.wizard

![[1-base-tier-validation15-0-836-63d67bbe.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
