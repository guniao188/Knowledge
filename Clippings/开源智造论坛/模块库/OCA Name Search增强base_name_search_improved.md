---
title: "OCA Name Search增强base_name_search_improved"
source: "http://www.thinkltd.cn/forum/2/oca-name-searchbase-name-search-improved-2803"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA Name Search增强base_name_search_improved

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-name-searchbase-name-search-improved-2803>

模块链接：

Odoo默认按name字段搜索记录，本模块增强此搜索功能：1. 可以定义name之外的附加搜索字段，系统先搜索name，搜索结果不足时候，再搜索附加字段；2. 按空格拆分字符进行搜索， "john brown" 可以匹配 "John M. Brown"。

Extends the name search feature to use additional, more relaxed matching methods, and to allow searching into configurable additional record fields.

The name search is the lookup feature to select a related record. For example, selecting a Customer on a new Sales order.

For example, typing "john brown" doesn't match "John M. Brown". The relaxed search also looks up for records containing all the words, so "John M. Brown" would be a match. It also tolerates words in a different order, so searching for "brown john" also works.

Additionally, an Administrator can configure other fields to also lookup into. For example, Customers could be additionally searched by City or Phone number.

How it works:

Regular name search is performed, and the additional search logic is only triggered if not enough results are found. This way, no overhead is added on searches that would normally yield results.

But if not enough results are found, then additional search methods are tried. The specific methods used are:

- Try regular search on each of the additional fields
- Try ordered word search on each of the search fields
- Try unordered word search on each of the search fields

All results found are presented in that order, hopefully presenting them in order of relevance.

## [Configuration](https://github.com/OCA/server-tools/tree/11.0/base_name_search_improved#id1)

The fuzzy search is automatically enabled on all Models. Note that this only affects typing in related fields. The regular `search()`, used in the top right search box, is not affected.

Additional search fields can be configured at Settings > Technical > Database > Models, using the "Name Search Fields" field.

##

## [Usage](https://github.com/OCA/server-tools/tree/11.0/base_name_search_improved#id2)

Just type into any related field, such as Customer on a Sale Order.

##

## [Known issues / Roadmap](https://github.com/OCA/server-tools/tree/11.0/base_name_search_improved#id3)

- Also use fuzzy search, such as the Levenshtein distance: [https://www.postgresql.org/docs/9.5/static/fuzzystrmatch.html](https://www.postgresql.org/docs/9.5/static/fuzzystrmatch.html)
- The list of additional fields to search could benefit from caching, for efficiency.
- This feature could also be implemented for regular `search` on the `name` field.


## 原帖外链配图

![[2-oca-name-searchbase-name-search-impr-xf4f81a43.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/server-tools/11.0/base_name_search_improved/images/image2.png</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
