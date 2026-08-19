---
title: "OCA电话销售计划crm_phonecall_planner、partner_phonecall_schedule、crm_phonecall_summary_predefined"
source: "http://www.thinkltd.cn/forum/2/ocacrm-phonecall-plannerpartner-phonecall-schedulecrm-phonecall-summary-predefined-2810"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA电话销售计划crm_phonecall_planner、partner_phonecall_schedule、crm_phonecall_summary_predefined

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocacrm-phonecall-plannerpartner-phonecall-schedulecrm-phonecall-summary-predefined-2810>

模块链接：

To use this module, you need to specify your partners' preferred phone call schedule:

1.  Go to any partner's form > *Phone Calls*.
2.  Set the preferred phone calling schedule for the partner.
3.  Repeat above steps for all of your partners.

##

## [Usage](https://github.com/OCA/crm/tree/11.0/crm_phonecall_planner#id2)

Now, to actually generate the phone call planning:

1.  Go to *Sales > Phone Calls > Planner*.
2.  Fill the fields under *Call details*. Those fields will be saved literally in the generated phone calls.
3.  Fill the fields under *Criteria*. Those fields are used to filter the partners and the preexisting calls. The UTM fields will also be saved literally in the generated phone calls.
4.  Fill the fields under *Times*. See note below.
5.  Fill the fields under *Repetition*. See note below.
6.  Press *Generate planning*.
7.  Wait a little bit (this is usually a long process).
8.  You will get to the list of planned phone calls. Start calling!

###

### [Note about *Times* section](https://github.com/OCA/crm/tree/11.0/crm_phonecall_planner#id3)

The *Start* and *End* times behave in a special way:

- Their *date* part is used to know the start and end dates for the planning.
- Their *time* part is used to know the time at which we will plan calls *each day under the date range*.

The *Call duration* field indicates the time spacing you want to leave between one call and the next one.

So, for instance, if you select start on *2017-09-01 09:00:00*, end on *2017-09-03 10:00:00* and duration of *1:00*, it will try to generate these phone calls:

- 2017-09-01 09:00:00
- 2017-09-01 10:00:00
- 2017-09-02 09:00:00
- 2017-09-02 10:00:00
- 2017-09-03 09:00:00
- 2017-09-03 10:00:00

###

### [Note about *Repetition* section](https://github.com/OCA/crm/tree/11.0/crm_phonecall_planner#id4)

If you choose not to repeat calls, the planner will try to schedule one single phone call for each **criteria combination** (*Partner + Campaign + Source + Medium*) under the specified conditions in the *Times* section (see note above).

If you choose instead to repeat calls after some amount of days (*Days gap*), the planner will:

1.  Try to find a partner that matches the **criteria combination** and has never been called; then schedule a call for him.
2.  If all matching partners have already been called, then search for matching partners that have not been called in the specified *Days gap*; then schedule a call for the one with least total scheduled calls.
3.  If there is still no match, then schedule nothing and continue.
4.

If you know the best moment to call your partners, use this addon to keep track of it and be able to filter partners that you can comfortably call now.

To use the phonecall schedules, you need to:

1.  Go to any partner form.
2.  Go to the *Phone calls* tab.
3.  Select any of the available schedules.
4.  A readonly checkbox will tell you if it is a good time to call him/her.
5.  A readonly aggregated schedule is visible too.

To filter partners available to call right now:

1.  Go to the partners view.
2.  Use the built-in filter *Available for phone calls now*

## 补充/答案 1

模块：

To configure the possible summary options:

1.  Activate the developer mode
2.  Go to *CRM > Configuration > Leads & Opportunities > Phone Calls > Summaries*.
3.  Add or modify types there.

##

## [Usage](https://github.com/OCA/crm/tree/11.0/crm_phonecall_summary_predefined#id2)

1.  Go to *CRM > Phone Calls > Logged Calls*.
2.  There you can use the new *Summary* field
3.


## 原帖外链配图

![[2-ocacrm-phonecall-plannerpartner-phon-x194038c2.png]]
<small>原始地址: /web/image/1283/snipaste_20190206_112425.png?access_token=21374a6e-58d8-4b8a-8481-8a03dfbe2e8c</small>

![[2-ocacrm-phonecall-plannerpartner-phon-x194038c2.png]]
<small>原始地址: /web/image/1285/snipaste_20190206_112917.png?access_token=cc0c1acf-9fea-45a2-b74c-072c2bb125f4</small>

![[2-ocacrm-phonecall-plannerpartner-phon-x194038c2.png]]
<small>原始地址: /web/image/1287/snipaste_20190206_111633.png?access_token=310aea17-71b8-45fa-8bf3-a5067aa27357</small>

![[2-ocacrm-phonecall-plannerpartner-phon-x194038c2.png]]
<small>原始地址: /web/image/1289/snipaste_20190206_113817.png?access_token=6861531a-84e8-4810-a7d6-5d7161b8c787</small>

![[2-ocacrm-phonecall-plannerpartner-phon-x194038c2.png]]
<small>原始地址: /web/image/1291/snipaste_20190206_113734.png?access_token=74eebe92-0c9a-4dbc-b36a-92a34f385a15</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
