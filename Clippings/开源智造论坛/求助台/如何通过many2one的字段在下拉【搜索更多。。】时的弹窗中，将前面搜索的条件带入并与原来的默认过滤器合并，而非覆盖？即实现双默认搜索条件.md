---
title: "如何通过many2one的字段在下拉【搜索更多。。】时的弹窗中，将前面搜索的条件带入并与原来的默认过滤器合并，而非覆盖？即实现双默认搜索条件"
source: "http://www.thinkltd.cn/forum/1/many2one-920"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 如何通过many2one的字段在下拉【搜索更多。。】时的弹窗中，将前面搜索的条件带入并与原来的默认过滤器合并，而非覆盖？即实现双默认搜索条件

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/many2one-920>

**需求背景：以下示例为V13版本，其他版本可能存在视图名字不同的情况。**

如何通过many2one的字段在录入搜索字符后，没有找到想要到内容或出现的内容选项仍太多，就需要跳转到【搜索更多。。】里，进入产品搜索的弹窗界面，这时如果前面有设置过用户的产品默认过滤器（有库存的列表），这时前面在订单上录入搜索的字符就会要在这个弹窗里重新录入一遍，才可以满足有库存的情况下的同时搜索，即双过滤条件；

如果用户没有设置产品默认的过滤器，则系统自带的功能里，会将前面录入过搜索的字符带入弹窗中，但实际业务中，用户需要在二个条件同时兼顾的情况下，尤其是产品数据特别多（几十万）的客户，搜索就特别费劲和需要时间，故这个过滤器就非常有必要。

将前面搜索的条件带入并与原来的默认过滤器合并，而非覆盖？即实现双默认搜索条件。

老肖做法参考：

代码：

产品变体表product.product的search视图上的搜索条件增加：

', 0)]"/>

![[1-many2one-920-4f262b11.png]]

另外产品变体菜单的动作上增加上下文引用该搜索过滤器：

|  |
|----|
| {"search_default_filter_to_sell":1,"search_default_qty_available_ok":1} |
|  |

![[1-many2one-920-bb5b3ae8.png]]

然后so订单上form视图里，产品字段上下文默认筛选器里指定：

继承视图：sale.order.form.context.supplierinfo

代码：

```python
                {'partner_id': parent.partner_id, 'quantity': product_uom_qty,
                'pricelist': parent.pricelist_id, 'uom': product_uom, 'company_id': parent.company_id,
                'supplierinfo_type': 'customer', 'display_name_only':True, 'display_default_code':False}

                {'partner_id': parent.partner_id, 'quantity': product_uom_qty,
                'pricelist': parent.pricelist_id, 'uom': product_uom, 'company_id': parent.company_id,
                'default_lst_price': price_unit, 'supplierinfo_type': 'customer', 'display_name_only':True,
                'display_default_code':False, 'search_default_qty_available_ok':1}
```

![[1-many2one-920-e61f1fdf.png]]

实现的效果展示：

![[1-many2one-920-da478af5.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
