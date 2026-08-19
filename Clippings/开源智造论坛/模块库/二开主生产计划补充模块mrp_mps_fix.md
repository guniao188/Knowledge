---
title: "二开主生产计划补充模块mrp_mps_fix"
source: "http://www.thinkltd.cn/forum/2/mrp-mps-fix-3137"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开主生产计划补充模块mrp_mps_fix

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/mrp-mps-fix-3137>

模块链接：OSCG_SVN\odoo_ecommerce\12.0SRC\mrp_mps_fix

【生产计划相关知识参考】

1.  主生产计划详细概念：

2.  生产作业计划：

3.  生产批量：

4.  期量标准：

5.  劳动定额：

模块功能：

1.  改善主生产计划画面产品显示顺序：产品上增加预测显示顺序的字段Forecast Seq；

2.  增加sale.forecast、sale.forecast.indirect、mrp.mps.report三个模型视图及菜单；

3.  增加预测分组功能：产品上增加预测分组字段forecast_group，预测画面的搜索框增加按预测分组搜索产品

4.  产品上增加是否产生补货单的控制字段：no_procure，默认点击小绿点“启动补货”时候，不产生补货单。系统原有功能，会将该期间（如整月）的生产数量产生一个大的补货单（生产单），日期为该期间第一天。如此的补货单，实际生产中还需要手工拆单、设置计划生产日期。还不如不产生补货单，时候人工根据预测计划手工创建补货单。

Odoo自带的主生产计划模块功能参考这里：[/forum/2/question/odoomrp-mps-3088](http://www.thinkltd.cn/forum/2/question/odoomrp-mps-3088)

![[2-mrp-mps-fix-3137-cdcd7594.png]]

![[2-mrp-mps-fix-3137-24469172.png]]

![[2-mrp-mps-fix-3137-221dcc38.png]]

## 补充/答案 1

多次运行MPS的方法：

当某产品在某期间已经运行过MPS（点击过“启动补货”的小绿点），则该期间该产品的补货数量变成不可修改了。

如果希望修改该期间，重新运行MPS，操作方法是：1) 找到运行MPS系统自动产生的单据，取消它们；2)该产品该期间的所有需求预测(sale.forecast)的state字段设置成“预测”。如此，该产品该期间的补货数量又可以修改了，修改后，点击绿色小圆点，系统又重新运行一遍MPS，产生新的补货单据。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
