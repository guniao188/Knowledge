---
title: "OCA产品包装上添加单位字段packaging_uom"
source: "http://www.thinkltd.cn/forum/2/ocapackaging-uom-2848"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA产品包装上添加单位字段packaging_uom

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocapackaging-uom-2848>

模块链接：

This module was written to use unit of measure instead of quantity by package in the definition of packaging. The goal is to ease the use of packaging in sale and purchase.

## 补充/答案 1

这个模块我今天优化了一下。

加了一个这个字段：

![[2-ocapackaging-uom-2848-e4ed1796.png]]

![[2-ocapackaging-uom-2848-c3e015a6.png]]

## 补充/答案 2

这个模块我今天升级到了odoo12.发现几个问题：

1.在产品（template）菜单，新创建一个产品，然后添加一条包装信息，这个时候点击保存。包装信息就没有了。（查数据库没有创建成功的）

非得要保存一次产品成功了然后再添加才有效。（数据库才创建起来。）

我怀疑是不是变体，一对多的问题。

```python
    packaging_ids = fields.One2many(
        'product.packaging', string="Product Packages", compute="_compute_packaging_ids", inverse="_set_packaging_ids",
        help="Gives the different ways to package the same product.")
```

![[2-ocapackaging-uom-2848-bfc56693.png]]

我好像在另外一个客户的环境上（odoo12 社区版）测试没有这个问题。但是我在我本地环境和42上面的odoo12测试都有这个问题。这是个product模块，又不能整个覆盖。

2.这个模块添加了一个新的字段uom_categ_domain_id，它的default的方法里面的  product_id = self.env.context.get("default_product_id") 死活返回一个false，这个又是怎么回事。我看到截图都可以的。。。我odoo12环境测试不行，因为华生都是同一个category，所以我全部注释掉，return 1.

```python
    uom_categ_domain_id = fields.Many2one(
        default=_default_uom_categ_domain_id,
        comodel_name='uom.category'

    @api.model
    def _default_uom_categ_domain_id(self):
        product_id = self.env.context.get("default_product_id")
        if not product_id:
            return self.env['uom.category']
        uom = self.env['product.product'].browse(product_id).uom_id
        return uom.category_id.id

![[2-ocapackaging-uom-2848-cb6a0cfe.png]]

```


## 原帖外链配图

![[2-ocapackaging-uom-2848-x194038c2.png]]
<small>原始地址: /web/image/1342/snipaste_20190214_135718.png?access_token=701ebd43-fee0-4152-a7ca-adde9ca35495</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
