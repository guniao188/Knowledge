---
title: "Odoo中Text类型报表的配置方法示例"
source: "http://www.thinkltd.cn/forum/1/odootext-3846"
forum: "求助台"
author: "肖相扶"
published: 2023-12-29
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo中Text类型报表的配置方法示例

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-12-29
> <http://www.thinkltd.cn/forum/1/odootext-3846>

【打印报表配置要点】

1.  报表的Template Name必须是对应的QWeb视图的外部ID
2.  Template Name以英文字符"."隔开的后半段名称，必须和QWEB视图的名称一致，如下截图示例。

![[1-odootext-3846-38c1e333.png]]

3.  配置服务器动作，从Odoo中抓取数据，调用配置好的Text报表，输出数据，如下截图示例。

![[1-odootext-3846-63f7df3e.png]]

【要点解析】

1.  服务器动作中，产品名称是postgresql的jsonb字段类型，该类型以json字典格式，存储着不同语种的产品名称，中文的Key是'zh_CN'。SQL语句中，jsonb字段的select方式  t.name->'zh_CN'，表示从该字段中，取key'zh_CN'对应的值。
2.  服务器动作中，通过报表的外部id，获取报表，而后通过方法  report_action，将报表数据传递给报表。报表的QWeb视图中，可以获取此处传递的数据，打印出来。
3.  Text类型的报表QWeb中，直接用t-esc指令导出数据即可

本例服务器动作参考代码：

xml_id = "__export__.ir_act_report_xml_794_b54a156b"
env.cr.execute("select p.id,p.default_code,t.name->'zh_CN' from product_product p left join product_template t on (p.product_tmpl_id=t.id)")
#data = env.cr.dictfetchall()
data = env.cr.fetchall()
data_prts={'data_prts':data}
#raise UserError("%s" % (data,) )
report_action = env.ref(xml_id).report_action(None, data=data_prts, config=False)
report_action.update({'close_on_report_download': True})
action = report_action

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
