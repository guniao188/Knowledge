---
title: "OCA支持相似度搜索base_search_fuzzy"
source: "http://www.thinkltd.cn/forum/2/ocabase-search-fuzzy-2794"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA支持相似度搜索base_search_fuzzy

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocabase-search-fuzzy-2794>

模块链接：

本模块支持文本相似度搜索，以及创建Gin和Gist索引。

【文本相似度】

1.  三元模型是一组从一个字符串中获得的三个连续的字符。 我们可以通过计数两个字符串共享的三元模型的数量来测量它们的相似性。 这个简单的想法证明在测量许多自然语言词汇的相似性时是非常有效的。****

2.  `pg_trgm`从一个字符串提取三元模型时忽略非文字字符（非字母）。 当确定包含在字符串中的三元模型集合时，每个单词被认为有两个空格前缀和一个空格后缀。 例如，字符串"`cat`"中的三元模型的集合是 "` c`"，"` ca`"， "`cat`"和"`at `"。 字符串"`foo|bar`"中的三元模型的集合是 "` f`"，"` fo`"， "`foo`"，"`oo `"， "` b`"，"` ba`"， "`bar`"和"`ar `"。

3.  开启插件`pg_trgm以后，支持`相似度查找符 % ，例如 select id, name from res_partner where name % 'Jon Miller'

4.  `pg_trgm参考：`

5.  Gin及Gist索引参考：  及

This addon provides the ability to create GIN or GiST indexes of char and text fields and also to use the search operator % in search domains. Currently this module doesn't change the backend search or anything else. It provides only the possibility to perform the fuzzy search for external addons.

## [Installation](https://github.com/OCA/server-tools/tree/12.0/base_search_fuzzy#id1)

1.  The PostgreSQL extension `pg_trgm` should be available. In debian based distribution you have to install the postgresql-contrib module.
2.  Install the `pg_trgm` extension to your database or give your postgresql user the `SUPERUSER` right (this allows the odoo module to install the extension to the database).

##

## [Configuration](https://github.com/OCA/server-tools/tree/12.0/base_search_fuzzy#id2)

If the odoo module is installed:

1.  You can define `GIN` and `GiST` indexes for char and text via Settings -> Database Structure -> Trigram Index. The index name will automatically created for new entries.

##

## [Usage](https://github.com/OCA/server-tools/tree/12.0/base_search_fuzzy#id3)

1.  You can create an index for the name field of res.partner.

2.  In the search you can use:

    `self.env['res.partner'].search([('name', '%', 'Jon Miller)])`

3.  In this example the function will return positive result for John Miller or John Mill.

4.  You can tweak the number of strings to be returned by adjusting the set limit (default: 0.3). NB: Currently you have to set the limit by executing the following SQL statement:

    `self.env.cr.execute("SELECT set_limit(0.2);")`

5.  Another interesting feature is the use of `similarity(column, 'text')` function in the `order` parameter to order by similarity. This module just contains a basic implementation which doesn't perform validations and has to start with this function. For example you can define the function as followed:

    `similarity(%s.name, 'John Mil') DESC" % self.env['res.partner']._table`

For further questions read the Documentation of the [pg_trgm](https://www.postgresql.org/docs/current/static/pgtrgm.html) module.


## 原帖外链配图

![[2-ocabase-search-fuzzy-2794-x194038c2.png]]
<small>原始地址: /web/image/1263/snipaste_20190205_094430.png?access_token=d01ced48-0b1f-4fa4-a0eb-17c444f7e788</small>

![[2-ocabase-search-fuzzy-2794-x194038c2.png]]
<small>原始地址: /web/image/1265/snipaste_20190205_094825.png?access_token=086dd654-bdf2-45c3-9ce5-0ddc56c6eeb6</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
