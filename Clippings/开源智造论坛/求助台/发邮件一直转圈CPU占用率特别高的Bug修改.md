---
title: "发邮件一直转圈CPU占用率特别高的Bug修改"
source: "http://www.thinkltd.cn/forum/1/cpubug-821"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 发邮件一直转圈CPU占用率特别高的Bug修改

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/cpubug-821>

【问题现象】

1.  有些邮件发送是正常的，有些邮件发送一直转圈，发送不出去。查CPU占有率还特别高（接近100%）

2.  将公司名称改成全英文字母则发送邮件又正常

【问题原因】

1.  经调查，原因在于python自带的email 模块有Bug，邮件的 reply-to含有中文且较长时候，如这样的reply-to: reply_to = '"星融元数据技术（苏州）有限公司 供应商发票审批-AF-SZ20210002" ' 。email模块的文件python\Lib\email\\header_value_parser.py 的方法 def _fold_as_ew(to_encode, lines, maxlen, last_ew, ew_combine_allowed, charset):  会陷入死循环，因而出现上述Bug现象

2.  经调查，pyhon 3.7及以下版本都有上述问题，用python 3.8的emai模块替换低版本的email模块，则Bug解决，发邮件正常。或者解压附件的email模块替换上述Bug模块也可以。

3.  陕西光电子，星融元 都出现过上述Bug

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
