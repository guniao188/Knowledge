---
title: "采购需求计算模块mrp_mps_manual"
source: "http://www.thinkltd.cn/forum/2/mrp-mps-manual-3512"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 采购需求计算模块mrp_mps_manual

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/mrp-mps-manual-3512>

**【2021/12/16修改】此模块废弃，有新模块代替**：[物料需求计划模块purchase_mps](http://www.thinkltd.cn/forum/2/question/purchase-mps-3529)

【业务背景】

Odoo现有的MRP运算逻辑的优缺点分析：

Odoo现有的MRP功能逻辑是，先做生产单（MO），生产单确认时候，系统进行MRP计算，缺料部分产生补料单（采购、调拨或部件生产）。

实践中的做法是，a. 生产计划：根据预测需求、订单需求，决定要生产什么，生产多少，对应的在系统中创建MO；b. 确认MO，系统进行MRP运算，产生子MO（部件生产单）、采购建议；c. 采购部门按采购建议完成原料采购，仓库完成采购验收入库；d.生产部门（生产主管）根据MO的时间顺序（需求优先顺序），到料情况，把MO打印出来，派单到车间生产；e.  车间按MO单领料，完成生产，在MO纸质单据上填写完成数量（报工），纸质生产单交回生产主管；f. 生产主管将完工情况录入系统（系统报工）。

这种做法，容易给生产计划带来混乱：排生产计划时候，只是。

【模块功能】

【功能截图】

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
