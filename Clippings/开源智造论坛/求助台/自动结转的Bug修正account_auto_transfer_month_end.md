---
title: "自动结转的Bug修正account_auto_transfer_month_end"
source: "http://www.thinkltd.cn/forum/1/bugaccount-auto-transfer-month-end-904"
forum: "求助台"
author: "肖相扶"
published: 2023-03-20
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 自动结转的Bug修正account_auto_transfer_month_end

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-03-20
> <http://www.thinkltd.cn/forum/1/bugaccount-auto-transfer-month-end-904>

2022年11月03日，经验证，此Bug在Odoo 16.0中已有修正，但修正不彻底。

【Odoo16Bug现象】

1.  如果连续生成多个月的结转凭证，日期是正确的。
2.  如果生成多个结转凭证后，过账第一个凭证，删除剩余的凭证，再结转生成剩余的凭证，则新生成的结转凭证的起始日期，系统取的最近一笔已过账结转凭证的日期，该日期是上月月末，而不是本月月初。
3.  修正方法：文件OSCGODOO16\source\enterprise\account_auto_transfer\models\transfer_model.py 方法 def _determine_start_date(self)，最后一行代码 return move_ids[0].date if move_ids else self.date_start 改成  return move_ids[0].date + relativedelta(days=1) if move_ids else self.date_start

【问题】

1.  Odoo15.0企业版模块 account_auto_transfer，可以设置科目余额定期自动结转功能，系统自动产生科目结转的会计凭证。

2.  不过，该模块有一个Bug。起始日期设置为1月1日，频率为1个月。系统实际计算逻辑是，1月1日加一个月，等于2月1日，1月份的自动结转凭证日期为2月1日。系统计算二月份的结转凭证时候，再加一个月，等于3月1日，二月份的结转凭证在3月1日，而不是期望的最后一天（3月31日）。

3.  模块account_auto_transfer_month_end（位置 OSCG_SVN\odoo_ecommerce\15.0SRC\存货核算\account_auto_transfer_month_end）修正上述问题，自动结转设置时候，可以勾选月末，则系统总是取月末那天作为自动结转凭证的日期。

4.  注意事项：定期自动结转的起始日期必须是某月1日，如果是其他日期，例如某月10日，则系统结转该月10日到次月9日的凭证。

【功能截图】

![[1-bugaccount-auto-transfer-month-end-904-d3276d79.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
