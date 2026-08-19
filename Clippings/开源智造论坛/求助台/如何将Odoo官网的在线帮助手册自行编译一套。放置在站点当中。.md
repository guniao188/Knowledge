---
title: "如何将Odoo官网的在线帮助手册自行编译一套。放置在站点当中。"
source: "http://www.thinkltd.cn/forum/1/odoo-682"
forum: "求助台"
author: "杨浔波"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 如何将Odoo官网的在线帮助手册自行编译一套。放置在站点当中。

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:杨浔波 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo-682>

1. 要解决如Odoo官网一样的在线实施手册，比如站点：https://www.odoo.com/documentation/user/13.0/index.html

2. 通过官方已经在github上开放的文档进行内容编辑（汉化或再创作），地址：https://github.com/odoo/documentation-user

3. 发布到自己的官网体系内，并开放共享给到其他客户

4. 借此机会捞取官方的网站的头代码和底部代码

## 补充/答案 1

已经成功在Windows和Mac上都将问题解决（由于时间的原因，先更新MacOS的操作方案）

**MacOS/Ubuntu 类uinx的操作系统：**

1.前提条件使用的电脑能正常运行Odoo13的环境（目的确保：LESS编译没有问题、GCC（macOS是xcode）是正常）

2. 在操作系统的自带Python3环境里安装如下三个包：Sphinx、Werkzeug、Requst （MacOS建议用Pycharm来装，少麻烦，否则会自动装到Python2当中）

3. 下载官方的Github用户手册文件，开发手册在源代码的doc当中。

4. 用终端进入文件根目录，输入make html，如下图：

![[1-odoo-682-53b19c46.png]]

5. 编译完成后在子目录_bulid\html当中，点击index.html则可以打开在线帮助文档。

![[1-odoo-682-6003a5c5.png]]

![[1-odoo-682-c2e5cdb9.png]]

**其他补充：**
关于文档的格式是RST格式，这个类似于MD的文档格式，里面涉及一些特殊语法，后面我会专门的贴出相关的语法快速的标签，或者我们只需要基于官方的文件汉化或修改即可。之后在编译，编译过程中涉及的一些警告报错，无需理会，只要有进度就行，如无进度一般原则上是系统变量没有找到sphinx-build导致的，只需要将改目录设置到系统执行变量中即可。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
