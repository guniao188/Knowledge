---
title: "OCA回款控制account_credit_control"
source: "http://www.thinkltd.cn/forum/2/ocaaccount-credit-control-2731"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA回款控制account_credit_control

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaaccount-credit-control-2731>

模块链接：

设定催款策略，检查到期应收账款，按设定策略自动催款。

Account Credit Control module is a part of Financial Tools used in business to ensure that once sales are made they are realised as cash. This module helps to identify outstanding debt beyond tolerance level and setup followup method.

###

### Configuration

Configure the policies and policy levels in `Accounting > Configuration > Credit Control > Credit Control Policies`. You can define as many policy levels as you need.

Configure a tolerance for the Credit control and a default policy applied on all partners in each company, under the Accounting tab.

You are able to specify a particular policy for one partner or one invoice.

###

### Usage

Menu entries are located in `Invoicing > Adviser > Credit Control`.

Create a new "run" in the `Credit Control Run` menu with the controlling date. Then, use the `Compute Credit Lines` button. All the credit control lines will be generated. You can find them in the `Credit Control Lines` menu.

On each generated line, you have many choices:
- Send a email
- Print a letter
- Change the state (so you can ignore or reopen lines)
- Mark a line as Manually Overridden. The line will get the ignored state when a second credit control run is done.
- Mark one line as Manual followup will also mark all the lines of the partner. The partner will be visible in "Do Manual Follow-ups".


## 原帖外链配图

![[2-ocaaccount-credit-control-2731-x194038c2.png]]
<small>原始地址: /web/image/1174/snipaste_20190127_174941.png?access_token=644f215d-672f-4e00-afe8-588729199722</small>

![[2-ocaaccount-credit-control-2731-x194038c2.png]]
<small>原始地址: /web/image/1176/snipaste_20190127_175158.png?access_token=f8582b3d-1376-41b3-9744-873c3fa0dde9</small>

![[2-ocaaccount-credit-control-2731-x194038c2.png]]
<small>原始地址: /web/image/1178/snipaste_20190127_175534.png?access_token=604b9389-36dc-484f-815e-d19f3c3e3651</small>

![[2-ocaaccount-credit-control-2731-x194038c2.png]]
<small>原始地址: /web/image/1180/snipaste_20190127_175640.png?access_token=a970a6f5-cd19-4d9e-b53e-18c716a9f37c</small>

![[2-ocaaccount-credit-control-2731-x194038c2.png]]
<small>原始地址: /web/image/1182/snipaste_20190127_175808.png?access_token=fc8ac90f-f6e2-4425-bdae-78f5ab7f8c08</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
