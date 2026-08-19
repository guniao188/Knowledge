---
title: "较早的V14版本（之后官方已自行修复），原生委外模块BUG"
source: "http://www.thinkltd.cn/forum/1/v14-bug-3877"
forum: "求助台"
author: "葛忠彪"
published: 2024-02-05
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 较早的V14版本（之后官方已自行修复），原生委外模块BUG

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:葛忠彪 | 2024-02-05
> <http://www.thinkltd.cn/forum/1/v14-bug-3877>

系统重现问题

1.销售下单，确认后跑出发货单和制造单

2.MO部分完工，跑出MO欠单

3.此时去验证发货单，要么提示待产数量必须为正数，要么直接把另一个MO欠单给关单了

调查结果如下

源码 mrp_subcontracting模块

picking 的py里对picking的完成方法_action_done写了继承，其中有一段

```python
    for picking in self:
    productions_to_done = picking._get_subcontracted_productions()._subcontracting_filter_to_done(
    而    def _get_subcontracted_productions(self):
            return self.move_lines.move_orig_ids.production_id
```

返回了这个picking下所有sotck.move的上游移动的制造订单（不管是不是委外）

    _subcontracting_filter_to_done 返回了这些MO里状态不是完成的MO

最后走下面方法把未完成的MO给标记为完成

    productions_to_done.with_context(subcontract_move_id=True, mo_ids_to_backorder=production_ids_backorder).button_mark_done()

## 补充/答案 1

官方自己已经在后续的版本（包括14版本）修复了，图1是三朴的14版本（比有BUG的探微的版本晚一点），图2是16版本

从代码解读，委外入库单验证时，的确是要把背后所有的委外MO给关闭掉，但是应该要判断一下此单（或者说stock.move）是否是委外

对于14版本一直没更新过源码的客户，对下面方法写继承过滤掉不是委外的就可以了，也可以拉一版较新的14源码覆盖

![[1-v14-bug-3877-9a167165.png]]

![[1-v14-bug-3877-95dc0950.png]]

这件事情告诉我们，即使是相同的大版本，也建议客户定期更新源码

一般我们更新源码报2小时（docker安装另评估）

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
