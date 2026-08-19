---
title: "OWL开发技术培训大纲"
source: "http://www.thinkltd.cn/forum/5/owl-3828"
forum: "专家库"
author: "吴键"
published: 2024-02-28
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/专家库
---

# OWL开发技术培训大纲

> [!info] 来源
> 开源智造论坛 · 专家库 | 作者:吴键 | 2024-02-28
> <http://www.thinkltd.cn/forum/5/owl-3828>

【OWL开发文档及示例模块】

【OWL开发技术大纲】

1.  OWL沟通内容：
```python
    1.  1.前端(组件)基本构成单元：

        1.1传统 .html+.js+.css

                Html引入js,css

        1.2   OWL xml+js+css

        1.2.1        Js引入xml，Xml引入css
```

2.  OWL要点

```python
    2.1   .xml模版

    2.1.1 Xml使用Qweb作为模版引擎

    2.2  .js

           2.2.1导入引用文件(主要文件介绍)

           2.2.2 组件生命周期

           2.2.3 事件监听

           2.2.4 关于异步

           2.2.4 访问后端数据（初始化访问，用户行为访问）

                  2.2.4.1访问后端模型数据

                  2.2.4.2 访问后端控制器

           2.2.5模版数据的赋值方式

                  2.2.5.1初始化绑定

                  2.2.5.2 后期变更

           2.2.5嵌入服务器视图

           2.2.6 嵌入传统网页并实现交互

           2.2.6 打开服务器视图

           2.2.7 打开对话框

    2.3 组件注册

    2.4组件调用
```

【开发练习】

1.  销售订单明细行上，输入料号，每输入一个字符，系统立即自动搜索产品，下拉显示。当产品很多时候，如华霆，超过30万个SKU，此处搜索非常耗费服务器CPU，导致响应速度变慢。一个改善方法是，输入字符时候，延迟搜索，如延迟两秒，如此减少搜索次数。实现方法，在产品字段的options中，增加延迟搜索秒数的配置项，系统延迟设置的秒数再搜索。开发一个Odoo17的模块，实现此功能。---- 施叶寒
2.  手机拍照签收功能开发。司机订单送到后，手机扫码，显示订单客户、地址、产品明细，拍照上传，签收订单。实现方法，Odoo的扫码模块(stock_barcode)，增加“拍照签收”按钮，点击跳转到拍照签收画面， 此画面下部，显示三个按钮“扫码”、“拍照”、“签收”。点击扫码，系统调出Picking单，显示 客户、地址、产品明细。点击拍照，系统调出拍照画面，拍照自动上传到该Picking的附件上。点击签收，系统标记该Picking已签收（Picking上增加一个Boolean型签收标记字段）。---- 王澧鑫

【参考资料】

1.  Odoo官方OWL教程：[https://www.odoo.com/documentation/17.0/developer/reference/frontend/owl_components.html](https://www.odoo.com/documentation/17.0/developer/reference/frontend/owl_components.html)
2.  OWL示例模块： [Odoo16 js中弹窗应用开发示例](http://www.thinkltd.cn/forum/1/odoo16-js-3826)


## 附件

- [[附件/forum/5-owl-3828-owl培训资料.zip|owl培训资料.zip]] (283 KB)

---

相关:[[Clippings/开源智造论坛/专家库/00-专家库索引.md|← 专家库索引]]
