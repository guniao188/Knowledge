---
title: "工商银行网银流水Excel导入Odoo银行日记账"
source: "http://www.thinkltd.cn/forum/1/excelodoo-4036"
forum: "求助台"
author: "肖相扶"
published: 2025-01-25
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 工商银行网银流水Excel导入Odoo银行日记账

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2025-01-25
> <http://www.thinkltd.cn/forum/1/excelodoo-4036>

【详细操作截图】

1.  工商银行网银流水（Excel）文件格式

![[1-excelodoo-4036-0c8d4374.png]]

2.  Odoo导入操作界面

![[1-excelodoo-4036-85d8f2ad.png]]

 

![[1-excelodoo-4036-58cd19d7.png]]

3.  导入后的会计凭证（待核销）

![[1-excelodoo-4036-32ed8acf.png]]

4.  银行流水核销操作界面

![[1-excelodoo-4036-04e8353c.png]]

## 补充/答案 1

对方单位和系统中的partner_id往往对不上（差几个字），是否考虑用一个char字符先存起来，然后用服务器动作去匹配，有其他方案吗

## 补充/答案 2

差几个字的原因是什么呢？我理解银行的打款名是工商注册名，很准确。是不是Odoo系统中维护的Partner名称不准确？如果是，应该修正Odoo的Partner名。偶尔的名称不一致，核销时候人工勾选决定。


## 评论

> [!quote] 肖相扶 · 2025-01-25
> 差几个字的原因是什么呢？我理解银行的打款名是工商注册名，很准确。是不是Odoo系统中维护的Partner名称不准确？如果是，应该修正Odoo的Partner名。偶尔的名称不一致，核销时候人工勾选决定。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
