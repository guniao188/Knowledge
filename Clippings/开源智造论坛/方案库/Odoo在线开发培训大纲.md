---
title: "Odoo在线开发培训大纲"
source: "http://www.thinkltd.cn/forum/3/odoo-3762"
forum: "方案库"
author: "肖相扶"
published: 2023-11-30
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# Odoo在线开发培训大纲

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:肖相扶 | 2023-11-30
> <http://www.thinkltd.cn/forum/3/odoo-3762>

第一讲：Python代码开发

1.  概念：服务器动作、自动动作、计划任务
2.  python代码开发及测试
3.  1.  菜鸟学习python： [Python3 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python3-tutorial.html)
    2.  python代码在线测试： [Python3 在线工具 | 菜鸟工具 (runoob.com)](https://c.runoob.com/compile/9/)
4.  python日期及时间操作方法
5.  1.  参考： [Python日期时间操作指南 (baidu.com)](https://baijiahao.baidu.com/s?id=1769484471382177983&amp;wfr=spider&amp;for=pc)
    2.  练习：写一段代码，显示 今天的日期加200天后是星期几
6.  Odoo模型操作方法（增删改查），更多参考： [ORM API — Odoo 16.0 documentation](https://www.odoo.com/documentation/16.0/developer/reference/backend/orm.html)
7.  1.  查询：search(domain, offset=0, limit=None, order=None, count=False)   示例：product_ids = env['product.product'].search([('name', 'ilike', 'cbd')], offset=200, limit=100, order='default_code', count=False)
```python
    2.  创建：create(vals_list)  示例  env['res.partner'].create([{'name': '张三', 'company_type': 'person'}, {‘name’: '李四',  'company_type': 'person' }])
    3.  修改：write(vals)  示例 product_ids.write({'name': ‘测试产品’, 'default_code': 'P100'})
    4.  删除：unlink()    示例  product_ids.unlink()
    5.  汇总(group by)：read_group(domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True)   示例：读取会计科目余额 act_banances = env['accoun.move.line'].read_group([], ['account_id', 'balance'], ['account_id'])
    6.  id转对象：browse(id)  示例： p = env['res.partner'].browse(100)
    7.  外部id转对象：示例： obj = env.ref('account.action_account_config')
    8.  执行SQL语句：env.cr.execute("some_sql", params)，示例 env.cr.execute("""SELECT res_id, module, name FROM ir_model_data WHERE model = %s AND res_id in %s""", (self._name, tuple(self.ids)))
```

8.  one2many, many2many 字段值写法(明细行增加、删除、修改)
9.  1.  参考： [Odoo中one2many、many2many的操作](http://www.thinkltd.cn/forum/1/odooone2manymany2many-432)
10. 调试方法
11. 1.  示例：raise UserError("显示变量 a = %s, b = %s" % (a, b))
12. 执行其他动作/跳转到其他界面
13. 1.  示例：action = 需要执行的动作
    2.  参考：1. [服务器动作搜索关联产品并跳转到列表视图显示示例](http://www.thinkltd.cn/forum/1/339)   2. [跳转按钮的写法](http://www.thinkltd.cn/forum/1/964)  3.  [表单上关联的另一表单跳转过去后已是自动过滤后的列表](http://www.thinkltd.cn/forum/1/409)  4.  [产品变体表上面的小卡片按钮跳转功能及计算，待出库数量，待入库数量及跳转](http://www.thinkltd.cn/forum/1/872)
14. 其他开发变量
15. 1.  env:触发动作的 Odoo 环境
```python
        model:触发动作的 Odoo 模型记录；是一个无效的记录集
        record:触发动作的记录；可能无效
        records:在多个模式下触发动作的所有记录的记录集；可能无效
        time, datetime, dateutil, timezone: 有用的 Python 库
        log(message, level='info'):在 ir.logging 表中记录调试信息的日志记录功能
        UserError: 与 raise 一起使用的警告异常
        要返回动作，请配置:action = {...}
```

第二讲：视图及表单开发

1.  字段属性：
2.  1.  参考   [ORM API — Odoo 16.0 documentation](https://www.odoo.com/documentation/16.0/developer/reference/backend/orm.html)
3.  视图配置：
4.  1.  参考  [Views — Odoo 16.0 documentation](https://www.odoo.com/documentation/16.0/developer/reference/backend/views.html)
5.  动作配置：
6.  1.  参考   [Actions — Odoo 16.0 documentation](https://www.odoo.com/documentation/16.0/developer/reference/backend/actions.html)
7.  练习题：
8.  1.  在线开发一个请假单模型，模型字段包括 请假事由、请假日期、请假天数、请假人。
```python
    2.  创建请假单菜单
    3.  创建请假单的列表视图和Form视图
    4.  请假单上增加状态字段，以及“提交”、“审批”、“拒绝”、“取消”、“撤回”五个操作按钮。撤回按钮回到初始状态（草稿状态）。
    5.  创建网页版请假单：参考   [如何在网站页面上增加动态表单，并且取值于后台已存在的字段的写法](http://www.thinkltd.cn/forum/1/921)
```

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
