---
title: "带参数执行服务器动作/上传Excel文件服务器动作进行处理base_server_action_params"
source: "http://www.thinkltd.cn/forum/2/excelbase-server-action-params-3583"
forum: "模块库"
author: "肖相扶"
published: 2024-12-01
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 带参数执行服务器动作/上传Excel文件服务器动作进行处理base_server_action_params

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-12-01
> <http://www.thinkltd.cn/forum/2/excelbase-server-action-params-3583>

【 20230918升级到16.0版本 】作了改善：1) Demo数据改成了米切尔的真实BoM数据，Demo服务器动作改成了真实Excel BoM导入的代码。2) 新增变量 excel_book，用于操作原始Excel文件，以及对应示例：导入复杂格式的Excel建材销售订单。

16.0版模块链接：OSCG_Git\extra-addons\base_server_action_para

2024年4月23日升级到了Odoo 17.0：OSCG_Git\17.0\extra-addons\base_server_action_params

2024/10/30日吴键升级到了Odoo18.0：[https://gitlab.com/oscg-china/extra-addons/-/tree/18.0/base_server_action_params](https://gitlab.com/oscg-china/extra-addons/-/tree/18.0/base_server_action_params)

模块链接：OSCG_SVN\odoo_ecommerce\15.0SRC\基础框架\base_server_action_params

【模块功能】

1.  Odoo的服务器动作不能让用户输入参数。本模块提供了一个Wizard弹窗，在弹窗上，用户可以输入参数（文本框），或者上传Excel文件，选择要执行的服务器动作。在服务器动作中，可以接收用户参数（user_param），以及Excel数据（excel_data）。

2.  服务器动作中，处理完数据后，可以跳转到希望的画面（action）。

【功能截图】

![[2-excelbase-server-action-params-3583-f1c3f674.png]]

示例服务器动作

![[2-excelbase-server-action-params-3583-d0df24d4.png]]

## 补充/答案 1

24年12月1日：

最新版本的xlrd不支持.xlsx文件

解决方案：

指定xlrd版本1.2.0安装

pip3 install xlrd==1.2.0 -i [https://mirrors.aliyun.com/pypi/simple/](https://mirrors.aliyun.com/pypi/simple/)

如果已经安装，先卸载

pip3 uninstall xlrd

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
