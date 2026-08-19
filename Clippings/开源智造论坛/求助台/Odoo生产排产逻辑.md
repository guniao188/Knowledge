---
title: "Odoo生产排产逻辑"
source: "http://www.thinkltd.cn/forum/1/odoo-569"
forum: "求助台"
author: "肖相扶"
published: 2025-04-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo生产排产逻辑

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2025-04-15
> <http://www.thinkltd.cn/forum/1/odoo-569>

1.  以下各条详细解释Odoo内部逻辑，在深入逻辑细节之前，建议先参考大的排产逻辑  [Odoo订单排产详解](http://www.thinkltd.cn/forum/4/odoo-3952)

2.  点击制造订单（MO）上的“计划”按钮，系统根据MO上的工艺路线，自动创建工序单（Work Order），并设置工序单的计划时间。

3.  此排产过程中，系统实际做了两件事情，其一是，选择在哪个工作中心上加工，其二是，什么时间开始加工，什么时候结束加工。算法代码参看：Odoo13\source\odoo\addons\mrp\models\mrp_production.py  方法 def _plan_workorders

4.  系统排产算法中，参考设置包括：1) MO的工单开始时间 date_start_wo字段，2) 工作中心Work Center上的可选工作中心alternative_workcenter_ids字段，3) 工作中心Work Center上的工作时间字段 resource_calendar_id，4) 资源日历resource.calendar的时段表resource.calendar.leaves，时段表记录资源的不可用时段（time_type=='leave'），或负荷时段（（time_type== 'other'）），5) 工艺路线的工步的时长(time_cycle字段)，6) 工作中心的生产前时间(time_start)、生产后时间(time_stop)、容量(capacity字段)、时间效率(time_efficiency字段)

5.  工序单（Work Order）生产时长计算方法：工序单生产数量除以工作中心容量，得到生产周期数。生产周期数量 * 工步时长，加上生产前时间(time_start)、生产后时间(time_stop)，得到工序单总的生产时长。time_cycle = workorder.operation_id.time_cycle
                    cycle_number = float_round(workorder.qty_producing / workcenter.capacity, precision_digits=0, rounding_method='UP')
                    duration_expected = workcenter.time_start + workcenter.time_stop + cycle_number * time_cycle * 100.0 / workcenter.time_efficiency

6.  工序单开始时间、结束时间计算方法：制造订单MO的date_start_wo字段为基础时间（没值的话，则取当前时间），再根据工作中心的工作时间字段 resource_calendar_id计算计划的开始时间。加上工序单时长，同样参考工作中心的工作时间字段 resource_calendar_id计算计划的结束时间。resource_calendar_id上有工作时段(什么时候上班、什么时候下班)，也有工作中心的不可用时段、负荷时段。

7.  系统比较默认工作中心，及其可选工作中心，选取计划结束时间最早的工作中心作为本工序单的工作中心（相应的计划开始时间、计划结束时间，作为本工序单计划时间）。也即，优先选取效率最高、负荷最少的工作中心。

8.  工序单排产后，系统创建一个工作时段resource.calendar.leaves 记录（Work Order的leave_id字段），记录哪个资源（工作中心）、哪个日历（resource.calendar）、什么时候开始、什么时候结束。安排新的工序单时候，系统会参考资源的resource.calendar.leaves。

9.  当修改工序单Work Order的计划开始时间、结束时间，系统同步修改工作时段resource.calendar.leaves的开始、结束时间。

10. 本排产逻辑也适用于Odoo17，如下截图所示。

![[1-odoo-569-8c54b82e.png]]

11. MO上有字段is_plan标记单子是否已经排产。可以取消排产，再次排产（点击“安排”）。再次排产时候，系统会找设备的空闲时间档，如果存在某个空挡期，该空档期大于订单需要的加工时长，系统将订单安排到该空挡期。如果不存在大于订单时长的空档期，系统将订单日期往后排。因此，系统排产时候，不能利用琐碎的空档期。

12. 可以多个订单一起排产，如此，优先级高的订单先排产。

![[1-odoo-569-71ef4832.png]]

13. 产品/产品BoM上的制造提前期对排产的影响。系统根据客户的交期，减去主产品的制造提前期，得到主产品的MO的计划开始日期。此日期再减去子产品的制造提前期，得到子产品MO的计划开始日期。实际排产时候（点击安排按钮），系统从MO的计划开始日期之后（如果MO的计划开始日期早于当前，则从当前时间之后），查找设备的空闲期，调整计划开始日期。如果设备很忙，调整后的子MO的计划开始日期有可能晚于对应的上级MO的计划开始日期。如果出现这种情况，则上级MO的计划开始日期即使到了，因为物料不齐套（子部件还没生产好），实际是无法安排生产的。只能取消安排，等子部件好了，再安排生产。

14. 一个好的排产做法是，只对物料齐套的MO做“安排”。产品的制造提前期，应该设置得冗余一点，确保大多数情况下，产品/子产品都可以在制造提前期内完成。

15. 对于大的MO单（不能在制造提前期内完成生产），最好拆成小MO单进行排产。拆分原则是，确保每一个子部件的MO，都可以在它的制造提前期内完成生产。

![[1-odoo-569-d4251d01.png]]


## 附件

- [[附件/forum/1-odoo-569-Odoo排产图解.pptx|Odoo排产图解.pptx]] (1.3 MB)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
