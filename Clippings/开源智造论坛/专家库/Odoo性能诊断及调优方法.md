---
title: "Odoo性能诊断及调优方法"
source: "http://www.thinkltd.cn/forum/5/odoo-3872"
forum: "专家库"
author: "吴键"
published: 2024-02-28
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/专家库
---

# Odoo性能诊断及调优方法

> [!info] 来源
> 开源智造论坛 · 专家库 | 作者:吴键 | 2024-02-28
> <http://www.thinkltd.cn/forum/5/odoo-3872>

【问题列表】

1.  Odoo实际使用中，数据量大了，经常会出现某些操作特别慢。例如，客户西班牙斯达远东曾经出现过的性能问题：系统使用一段时间，入出库单据多了（超过100万条明细行），开启了自动生成入出库会计凭证的情况下，一个超过1000个明细行的入库单，验证入库时候，特别慢，甚至要半小时以上才能完成入库。
2.  Odoo17新出现的，入库时候自动生成序列号功能，如果一次性生成一万个序列号，实测下来，差不多要10分钟，如果一次性生成2万个序列号，基本无法生成（太慢）。Odoo入库出库的内部处理逻辑参考  [Odoo17入库出库中move line、quant的关系及性能优化](http://www.thinkltd.cn/forum/1/odoo17move-linequant-3886)
3.  Odoo16开始，提供了一些性能问题诊断和调优工具，参考 [Performance — Odoo 16.0 documentation](https://www.odoo.com/documentation/16.0/developer/reference/backend/performance.html) 。请研究调查此调优方法，做成中文版本的性能问题指南。
4.


## 附件

- [[附件/forum/5-odoo-3872-性能分析.rar|性能分析.rar]] (5.8 MB)

---

相关:[[Clippings/开源智造论坛/专家库/00-专家库索引.md|← 专家库索引]]
