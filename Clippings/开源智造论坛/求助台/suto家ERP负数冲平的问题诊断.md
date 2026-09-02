---
title: "suto家ERP负数冲平的问题诊断"
source: "http://www.thinkltd.cn/forum/1/sutoerp-291"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# suto家ERP负数冲平的问题诊断

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/sutoerp-291>

suto家ERP之前有很多负数出库的Stock Move，但运行调度器却不能冲平，什么原因？

经调查，存在下面一些问题：

1) 运行调度器，Odoo负数冲平时候，系统只会找符合下面三个条件的Stock Move： a. FIFO成本核算的产品, b.剩余数量为负数的， c. 源库位或目标库位至少有一个的company_id 为False  。找到这些Stock Move，再用之后的入库Stock move冲平。suto家的虚拟库位“Production-asia” 之前设置了company_id，导致该类负数Stock Move不被冲平。

2)   符合上述条件的，待冲平Stock move中，存在成本价格（stock Move的value字段）为零的情况，系统自动生产会计凭证时候，会报异常，导致冲平中断，不能完成。

3) 如果会计期间已经关闭，则系统冲平之前的stock move，自动产生会计凭证会报错，导致冲平中断，不能继续。

## 补充/答案 1

有个问题，生产位置上因为需要配置会计科目，所以需要与company_id进行绑定，这里置空的话，多公司的情况下是会有问题吧？如果公司为空，那是否意味着多公司的Move为负的可以互冲？

这个值在产品上有设置默认依当前抬头切换自动默认到指定公司抬头的位置的。

另外，锁账日期去掉后，是不是意味着这个冲账的过程，会改动之前的账目吗，还是跑在当前月份账目？

存在为0价值的可库存商品，为0的是可以设置成手动计价的，可以出入库，本身就不需要产生会计凭证。代码已经在客户环境上已经更新了么？

另外，内部调拔单价问题，因只对新创建的数据生效，那么历史数据有什么办法可以很快速的激活重新计算出这个库存的价值呢？

## 补充/答案 2

文件 addons/stock_account/models/stock.py， 方法 def _prepare_account_move_line(self, qty, cost, credit_account_id, debit_account_id):


## 原帖外链配图

![[1-sutoerp-291-x194038c2.png]]
<small>原始地址: /web/image/1642/TIM%E6%88%AA%E5%9B%BE20190522193815.png?access_token=ec12a588-0f85-401b-9b6d-1e3d9704cc3f</small>

![[1-sutoerp-291-x194038c2.png]]
<small>原始地址: /web/image/1644/TIM%E6%88%AA%E5%9B%BE20190522193936.png?access_token=fe433aa5-e4dc-4f86-a027-91aeff823ab9</small>

![[1-sutoerp-291-x194038c2.png]]
<small>原始地址: /web/image/1646/TIM%E6%88%AA%E5%9B%BE20190522194238.png?access_token=566f2e0e-89e1-4680-be8d-5e1eddd83039</small>

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
