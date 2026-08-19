---
title: "多级BoM的MO合并领料的解决办法"
source: "http://www.thinkltd.cn/forum/1/bommo-755"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 多级BoM的MO合并领料的解决办法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/bommo-755>

【业务背景】

成品的MO单，多级BoM，MO确认时候，系统自动产生多个子MO。有些行业，如杭州迅得电子，生产实际中，有下面一些需求：

1) 生产排产时候，如果该成品MO及其子MO，原料齐套了，则安排生产；

2) 生产领料的时候，该MO及其子MO的原料一起领用；

3) 子MO完工产生的半成品，不入库房，直接在车间供下一道MO消耗掉；

 【解决方案】

1.  仓库开启两步制造，如此，系统会为MO生成仓库到车间的领料单Picking

2.   设置成品MO的补货组(procurement_group_id字段)。补货组字段MO上默认不显示，修改XML显示它。默认情况，MO创建时候，系统以MO单号作为补货组字段值，可以手工修改成方便跟单的补货组名称，如 “SO单号 - 产成品编码”

3.  安装模块mrp_procurement_fix (参考：[/forum/2/question/odoo14stock-procurement-fixmrp-procurement-fix-3394](http://www.thinkltd.cn/forum/2/question/odoo14stock-procurement-fixmrp-procurement-fix-3394))。该模块修复了一个Bug，即MO的补货组自动传导到子MO，以及生产领料的Picking单。因为补货组相同，MO产生的领料Stock Move，以及子MO产生的领料Stock Move，系统自动合并到同一个领料Picking

4.  车间半成品缺货时候，不要到仓库领料，半成品生产入库也不要入库到仓库。为此，需要配置一个“半成品制造”的生产作业类型，该作业类型的源库位和目标库位都是车间(Pre-production)，同时，系统的“制造”路线上增加一条规则：车间缺货时候直接制造，该制造的作业类型是“半成品制造”。注意该规则的优先级（单号规则 sequence字段）设小一点（默认是21，设置成20以下，例如19）。

5.  如果最上层MO的补货组设置为SO单号，则可以用SO单号跟踪所有MO/子MO/生产领料单

## 补充/答案 1

【方案截图】

半成品制造规则

![[1-bommo-755-8a062937.png]]

MO/子MO合并领料：

![[1-bommo-755-c07fed8f.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
