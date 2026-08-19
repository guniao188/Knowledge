---
title: "待研课题：Form视图上扫码触发指定按钮"
source: "http://www.thinkltd.cn/forum/1/form-460"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 待研课题：Form视图上扫码触发指定按钮

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/form-460>

开发一个测试模块，模块功能如下：

1) SO的form视图上增加一个Text文本框，文本框下面增加一个“添加到明细行”的按钮

2) 扫描产品条码到文本框（一行一个条码），点击按钮“添加到明细行”，自动添加条码产品到SO的明细行，一个产品一行，数量默认为1

3) 扫描特定条码，触发功能“添加到明细行”，并清空文本框的条码，输入焦点落到文本框。如此，操作人员可以连续用条码枪操作，而不需要条码枪和鼠标切换操作。

参考代码：odoo\addons\barcodes\static\src\js\barcode_form_view.js  及  enterprise\stock_barcode\static\src\js\client_action\picking_client_action.js

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
