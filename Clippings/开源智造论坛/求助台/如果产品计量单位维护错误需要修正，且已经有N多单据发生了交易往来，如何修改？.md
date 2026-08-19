---
title: "如果产品计量单位维护错误需要修正，且已经有N多单据发生了交易往来，如何修改？"
source: "http://www.thinkltd.cn/forum/1/n-517"
forum: "求助台"
author: "符赛红"
published: 2023-05-06
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 如果产品计量单位维护错误需要修正，且已经有N多单据发生了交易往来，如何修改？

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2023-05-06
> <http://www.thinkltd.cn/forum/1/n-517>

产品计量单位一旦维护错了， 且有了关联的单据，是不可以直接修改的。这种情况会有，但不会常有，故采用强制修正的方式调整数据。

![[1-n-517-07d3c60f.png]]

**操作修改案例：**

安咖，门板由错误的‘米’，改成‘平方米’

操作步骤分享：

更改门板计量单位，由原来的m改成平方m

因原来的m还有其他产品关联着，不能直接更改名称，故数据库中作修改。

第一步，改产品模板，改后，相关联的产品变体也会自动变更；

select count(*) from product_template where uom_po_id=8 and name like '%门板%';
69个产品模板，先查找看已界面的记录数是否吻合。

update product_template set uom_po_id=26 where uom_po_id=8 and name like '%门板%';
update product_template set uom_id=26 where uom_id=8 and name like '%门板%';

第二步，批量更新stock move的计量单位  (涵盖菲尔、安咖抬头在内，用的合并报表抬头进行，即上级会包含底下全部数据）
通过界面服务器动作修改
有953条记录批量被更改，条件：产品名称中含有“门板”，计量单位分组中仅原来是m的数据记录；
for r in records:
        r.write({'product_uom': r.product_id.product_tmpl_id.uom_id.id})

第三步，批量更新stock move line的计量单位
通过界面服务器动作修改
有953条记录批量被更改，条件：产品名称中含有“门板”，计量单位分组中仅原来是m的数据记录；

第四步，批量更新销售订单明细的计量单位
通过界面服务器动作修改
有49条记录批量被更改，条件：产品名称中含有“门板”，计量单位分组中仅原来是m的数据记录；

第五步，批量更新采购订单明细的计量单位
通过界面服务器动作修改
有963条记录批量被更改，条件：产品名称中含有“门板”，计量单位分组中仅原来是m的数据记录；

第六步，检查bom明细行，是否有这样的产品单位需要调整
经检查没有发现有要改的

第七步，检查制造生产订单，是否有需要改的
经确认无

第八步，会计项目明细，通过界面服务器动作修改
1050条记录，条件：产品名称中含有“门板”，计量单位分组中仅原来是m的数据记录；

第九步，检查【存货】下面的菜单，成本历史，成本核算上的产品
无m门板记录要改

第十步，检查会计发票明细行
有953条记录调整了单位
for r in records:
        r.write({'uom_id': r.product_id.product_tmpl_id.uom_id.id})

## 补充/答案 1

刷stock.move.line 的时候，直接从仓库模块的库存移动进入会报错

可以在产品中的产品移动中进入，这个界面不会报错

服务器任务代码为

```python
for r in records:

  r.write({'product_uom_id': r.product_id.product_tmpl_id.uom_id.id})
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
