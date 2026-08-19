---
title: "Odoo13经常性的白屏打不开问题的解决思路"
source: "http://www.thinkltd.cn/forum/1/odoo13-607"
forum: "求助台"
author: "杨浔波"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo13经常性的白屏打不开问题的解决思路

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:杨浔波 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo13-607>

现发现Odoo13在服务器安装时经常出现切换或是新装模块后，屏幕变白。如何处理？

## 补充/答案 1

造成访问白屏的原因是丢失了字体样式和CSS加载不了本地，访问远程CSS服务器造成，因此从两个方面去解决：

1. 解决CSS本地加载，请在命令行中输入代码：

sudo npm install -g rtlcss

![[1-odoo13-607-b64929f3.png]]

2. 解决字体的问题，如之前帖子[《练习：平台：Odoo服务器加速的若干方法》](http://www.thinkltd.cn/forum/1/question/odoo-546)：此方法通过花钱一劳永逸，但有时候依然在和谐时期一样不能解决。来个粗暴的办法，改代码：

打开pycharm，启动Odoo13工程文件，使用pycharm的文件路径替换的办法，将源文件：fonts.googleapis.com 替换成：fonts.loli.net

![[1-odoo13-607-e6fef444.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
