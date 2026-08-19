---
title: "Debian12操作系统PDF打印插件安装不好问题解决一例"
source: "http://www.thinkltd.cn/forum/1/debian12pdf-4062"
forum: "求助台"
author: "肖相扶"
published: 2025-08-05
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Debian12操作系统PDF打印插件安装不好问题解决一例

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2025-08-05
> <http://www.thinkltd.cn/forum/1/debian12pdf-4062>

杭州东豹阀门的Odoo服务器，客户误选择了Debian12操作系统，Odoo安装过程中，出现了PDF插件安装不对，PDF报表打印不了的问题，怎么解决呢？

## 补充/答案 1

Debian12操作系统wkhtmltopdf版本对应：

【1】检查是否残留版本：which wkhtmltopdf ；dpkg -l | grep wkhtmltopdf

【2】安装依赖：apt install -y fontconfig libfreetype6 libjpeg62-turbo libpng16-16 libx11-6 libxcb1 libxext6 libxrender1 xfonts-75dpi xfonts-base

【3】插件下载：wget [https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_amd64.deb](https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_amd64.deb)

【4】若缺少依赖：sudo apt -f install

【5】安装插件：dpkg -i [wkhtmltox_0.12.6.1-3.bookworm_amd64.deb](https://wkhtmltox_0.12.6.1-3.bookworm_amd64.deb)

【6】拷贝软链接：ln -s /usr/local/bin/wkhtmltopdf /usr/bin；ln -s /usr/local/bin/wkhtmltoimage /usr/bin

【7】测试安装结果并重启：wkhtmltopdf --version

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
