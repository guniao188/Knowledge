---
title: 中绿 Odoo 18
type: project
status: 历史方案与代码已回填，部署待确认
updated: 2026-08-17
tags: [Odoo18, 中绿, 寄售, 条码, 多语言]
---

# 中绿 Odoo 18

## 客户寄售方案

- 业务方向是我方把货寄放客户处：商品送达客户时仍属本公司资产，因此每个客户使用独立内部库位，发货至寄售仓只做内部调拨。
- 客户实际销售/领用后，才从客户寄售库位向客户位置交货并按已交付数量开票；未售退回仍走内部调拨。
- 销售订单标准只能选仓库，不能直接指定源库位。低频业务可在取消预留后手工改交货源位置；高频业务使用“每客户一条销售订单行路线”，由 Pull 规则指定客户寄售库位。
- 不应修改全局交货操作类型的默认源位置，否则普通销售订单也会错误扣减寄售库存。

## 条码界面多语言

- `/Users/yaodaidi/git/zhonglv/stock_barcode` 已将主菜单硬编码混合文案改为 Odoo 原生语言切换。
- 修改 `static/src/main_menu/main_menu.js`、`main_menu.xml`、`main_menu.scss`、`i18n/zh_CN.po` 及 `i18n/stock_barcode.pot`；语言选择保存到当前用户并刷新整套条码界面。
- XML、PO/POT 和差异检查通过；升级模块、重建前端资源以及正式环境验证尚未确认。

## 交付物

- `/Users/yaodaidi/Documents/New project/Odoo18_客户寄售路线完整实施方案.docx`，已完成逐页渲染检查。

## 来源

- `梳理 Odoo 18 寄售流程`，thread `019f830f-3150-7232-98a5-3d543bed6fb6`。
- `添加多语言切换支持`，thread `019f831c-13e3-76a0-b864-11b438655a13`。
