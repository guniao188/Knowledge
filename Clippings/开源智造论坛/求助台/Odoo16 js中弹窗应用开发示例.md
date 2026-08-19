---
title: "Odoo16 js中弹窗应用开发示例"
source: "http://www.thinkltd.cn/forum/1/odoo16-js-3826"
forum: "求助台"
author: "肖相扶"
published: 2023-12-14
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo16 js中弹窗应用开发示例

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-12-14
> <http://www.thinkltd.cn/forum/1/odoo16-js-3826>

【代码参考】

1.  弹窗代码：addons\web\static\src\core\confirmation_dialog\confirmation_dialog.js中的 ConfirmationDialog
2.  调用弹窗示例代码：addons\sale\static\src\js\product_discount_field.js 中 ProductDiscountField 的 onChange 方法

【实现效果】

1.  销售设置中，勾选 折扣

![[1-odoo16-js-3826-6dfe1415.png]]

2.  销售订单上，添加不少于三个明细行，而后修改第一行的折扣字段，系统自动弹窗询问是否将折扣应用到所有明细行。

![[1-odoo16-js-3826-c4422073.png]]

3.  点击保存按钮，保存成功后弹窗消息提示开发示例
4.  1.  开发代码示例，参考Odoo16代码仓库：OSCG_Git\extra-addons\sale_discount_select\static\src\js\save_ok.js
    2.  运行效果截图

![[1-odoo16-js-3826-2705254f.png]]

5.  折扣弹窗中增加明细行，勾选明细行后应用折扣的开发示例
6.  1.  开发代码参考  Odoo16代码仓库：OSCG_Git\extra-addons\sale_discount_select\static\src\js\sale_discount_select.js、select_dialog.js、select_dialog.xml
    2.  运行效果截图

![[1-odoo16-js-3826-dfe386ad.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
