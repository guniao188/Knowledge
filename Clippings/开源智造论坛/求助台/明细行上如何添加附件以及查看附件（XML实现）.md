---
title: "明细行上如何添加附件以及查看附件（XML实现）"
source: "http://www.thinkltd.cn/forum/1/xml-743"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 明细行上如何添加附件以及查看附件（XML实现）

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/xml-743>

【业务背景】

在销售明细行上添加附件文件。参考示例，系统的费用报销单的明细行上，可以点击按钮创建附件，上传附件，查看附件。在别的模型的明细行上，如果想要实现类似效果，如何做？

## 补充/答案 1

以销售明细行为例，实现方法如下：

1.  创建服务器动作，该服务器动作创建和上传附件。注意服务器动作的res_model 和 default_res_model 要设置为明细行的model

2.  销售明细行上XML上添加按钮，该按钮关联上述服务器动作(按钮的 name="服务器动作ID")。   其中 510 是服务器动作的id

res = env['ir.actions.act_window']._for_xml_id('base.action_attachment')

res['domain'] = [('res_model', '=', 'sale.order.line'), ('res_id', 'in', records.ids)]

res['context'] = {'default_res_model': 'sale.order.line', 'default_res_id': record.id}

action = res

![[1-xml-743-8bd66b6b.png]]

实现效果

![[1-xml-743-84e0bc3f.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
