---
title: "服务器动作增加用户参数输入弹窗base_server_action_with_params"
source: "http://www.thinkltd.cn/forum/2/base-server-action-with-params-3758"
forum: "模块库"
author: "肖相扶"
published: 2024-06-18
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 服务器动作增加用户参数输入弹窗base_server_action_with_params

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-06-18
> <http://www.thinkltd.cn/forum/2/base-server-action-with-params-3758>

模块链接：OSCG_Git\extra-addons\base_server_action_with_params

2024年4月23日升级到了Odoo 17.0：

     OSCG_Git\17.0\extra-addons\\ base_server_action_with_params

【模块功能】

1.  Odoo的服务器动作，执行时候，用户没法录入参数。例如，有时候，希望输入一个日期或者月份，服务器动作中取得用户输入的日期，做一些对应处理。
2.  本模块在服务器动作上增加字段(with_param)，如果勾选该字段，执行服务器动作时候，先弹窗，用户录入参数（一个任意的字符串），点击按钮“执行服务器动作”，系统运行服务器动作中的python代码。python代码可以直接使用用户录入的参数（user_param），解析该参数（字符串），进行相应处理。
3.  20230908改善：兼容Odoo15。之前版本在Odoo15中，勾选带参数后服务器动作上不能使用变量 records 和 record。改善后Odoo15上可以正常使用。
4.  20240618改善，弹窗的Wizard参数录入从Char类型改成了Text类型。如此，可以从Excel文件拷贝参数列表（如料号、条码、序列号等）到Wizard参数框。

【功能截图】

![[2-base-server-action-with-params-3758-b7955442.png]]

![[2-base-server-action-with-params-3758-d9af8865.png]]

## 补充/答案 1

部署后，需要把模型“服务器动作”的访问权限加上内部用户

不然像补货池这种调用服务器动作的菜单就打不开了

![[2-base-server-action-with-params-3758-3135012c.png]]

也可以直接改代码，增加下面一行，并且下面的内容整体往右移4个空格

![[2-base-server-action-with-params-3758-a749330d.png]]

如果对于弹窗数据要校验的话，可以用python中的try语法

例如下文中就在判断输入的内容是不是浮点型，如果不是就报错

try:
a = float(user_param)
```python
except:
raise UserError('请输入数字')
for i in records:
```

i.write({'production_durations':i.product_uom_qty * float(user_param),'production_durations2':i.product_uom_qty * float(user_param)})

当然如果不需要校验数据，只是去系统里找有没有符合条件的数据，则不需要用到try，例如刷会计分录的分析账户

a = env['[account.analytic.account'].search([('code','=',user_param)])](https://account.analytic.account&#39;%5D.search(%5B(&#39;code&#39;,&#39;=&#39;,user_param)%5D))
```python
if not a:
raise UserError('请输入正确的分析账户')
for i in records:
```

i.write({'analytic_account_id'[:a.id})](https://:a.id%7D))

附件是测试报告


## 附件

- [[附件/forum/2-base-server-action-with-params-3758-批量刷数据功能优化.docx|批量刷数据功能优化.docx]] (688 KB)

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
