---
title: "OCA审批工作流base_tier_validation、purchase_tier_validation、sale_tier_validation"
source: "http://www.thinkltd.cn/forum/2/ocabase-tier-validationpurchase-tier-validationsale-tier-validation-2588"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA审批工作流base_tier_validation、purchase_tier_validation、sale_tier_validation

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocabase-tier-validationpurchase-tier-validationsale-tier-validation-2588>

#### **此贴废弃，参考更新贴**：

###### [OA审批流程推荐方案base_tier_validation](http://www.thinkltd.cn/forum/2/question/oabase-tier-validation-3498)

######

销售订单审批模块链接：OSCG_SVN\odoo_ecommerce\12.0SRC\sale_tier_validation

经测试，12.0版本，将py文件中所有的 @api.multi 删除（可以批量替换成空），即可正常安装使用。

模块链接：

[](https://github.com/OCA/server-ux/tree/11.0/base_tier_validation)

[](https://github.com/OCA/purchase-workflow/tree/11.0/purchase_tier_validation)

## Base Tier Validation

This module does not provide a functionality by itself but an abstract model to implement a validation process based on tiers on other models (e.g. purchase orders, sales orders...).

**Note:** To be able to use this module in a new model you will need some development.

See [purchase_tier_validation](https://github.com/OCA/purchase-workflow/tree/11.0/purchase_tier_validation) as an example of implementation.

### Configuration

To configure this module, you need to:

1.  Go to *Settings > Technical > Tier Validations > Tier Definition*.
2.  Create as many tiers as you want for any model having tier validation functionality.

## 补充/答案 1

https://github.com/OCA/sale-workflow/tree/14.0

## Available addons

| addon | version | summary |
|----|----|----|
| [sale_commercial_partner](https://github.com/OCA/sale-workflow/blob/14.0/sale_commercial_partner) | 14.0.1.0.1 | Add stored related field 'Commercial Entity' on sale orders |
| [sale_discount_display_amount](https://github.com/OCA/sale-workflow/blob/14.0/sale_discount_display_amount) | 14.0.1.0.1 | This addon intends to display the amount of the discount computed on sale_order_line and sale_order level |
| [sale_last_price_info](https://github.com/OCA/sale-workflow/blob/14.0/sale_last_price_info) | 14.0.1.0.1 | Product Last Price Info - Sale |
| [sale_order_archive](https://github.com/OCA/sale-workflow/blob/14.0/sale_order_archive) | 14.0.1.0.0 | Archive Sale Orders |
| [sale_order_line_date](https://github.com/OCA/sale-workflow/blob/14.0/sale_order_line_date) | 14.0.1.0.1 | Adds a commitment date to each sale order line. |
| [sale_order_line_note](https://github.com/OCA/sale-workflow/blob/14.0/sale_order_line_note) | 14.0.1.0.0 | Note on sale order line |
| [sale_order_lot_generator](https://github.com/OCA/sale-workflow/blob/14.0/sale_order_lot_generator) | 14.0.1.0.1 | Sale Order Lot Generator |
| [sale_order_lot_selection](https://github.com/OCA/sale-workflow/blob/14.0/sale_order_lot_selection) | 14.0.1.0.0 | Sale Order Lot Selection |
| [sale_partner_incoterm](https://github.com/OCA/sale-workflow/blob/14.0/sale_partner_incoterm) | 14.0.1.0.0 | Set the customer preferred incoterm on each sales order |
| [sale_product_category_menu](https://github.com/OCA/sale-workflow/blob/14.0/sale_product_category_menu) | 14.0.1.0.1 | Shows 'Product Categories' menu item in Sales |
| [sale_product_multi_add](https://github.com/OCA/sale-workflow/blob/14.0/sale_product_multi_add) | 14.0.1.0.1 | Sale Product Multi Add |
| [sale_product_set](https://github.com/OCA/sale-workflow/blob/14.0/sale_product_set) | 14.0.1.1.1 | Sale product set |
| [sale_quotation_number](https://github.com/OCA/sale-workflow/blob/14.0/sale_quotation_number) | 14.0.1.0.2 | Different sequence for sale quotations |
| [sale_tier_validation](https://github.com/OCA/sale-workflow/blob/14.0/sale_tier_validation) | 14.0.1.0.0 | Extends the functionality of Sale Orders to support a tier validation process. |
| [sale_validity](https://github.com/OCA/sale-workflow/blob/14.0/sale_validity) | 14.0.1.0.1 | Set a default validity delay on quotations |

## 补充/答案 2

sale_tier_validation 使用说明：

svn地址：/odoo_ecommerce/12.0SRC/sale_tier_validation

使用前，

1) 需要将base_tier_validation/models/tier_validation.py/write方法的前半段（119-138）方法注释。

这个方法原意是禁止审批时修改，然而继承portal.mixin的模块（比如sale.order）会时不时修改一些与实际业务无关的系统字段（比如access_token）。所以需要将静止功能转移至相应模块来实现。
2）需要将base_tier_validation/models/tier_validation.py/evaluate_tier方法中，return self.search([('id', '=', self.id)] + domain)

修改为return self.sudo().search([('id', '=', self.id)] + domain)

base_tier_validation_enhance使用说明

svn地址：/odoo_ecommerce/12.0SRC/base_tier_validation_enhance

在原有模块支持并行审批的基础上，额外支持串行审批。

具体实现方法是，业务模型始终仅允许 所有待审批的review，中sequence最小的review（如有多个）进行审批。

定义具体规则时，如下设置：

名称 | 序号

一级审批，1；

二级审批A， 2；

二级审批B， 2；

三级审批，3。

另外需要注意 权限组之间的继承关系。如果存在权限继承，那么将会允许 高层领导 对 底层审批 进行处理。

## 补充/答案 3

新增鼎实际使用反馈，该模块审批日期显示有Bug，和中国时间差了 8小时。

![[2-ocabase-tier-validationpurchase-tier-validationsale-tier-validation-2588-7336af35.png]]

【Bug原因】

base_tier_validation模块中，js代码直接用 t-esc="review.reviewed_date" 显示审批时间，显示的是数据库中存放的UTC时间。应该在显示之前将 UTC 时间转换成Local时间。

【修正方法】

代码文件 base_tier_validation\static\src\js\tier_review_widget.js 中，line 37行  self.reviews = data; 之后，增加下述UTC转Local时间的代码：

```python
                self.reviews.forEach(function(review){
                  var dt = review.reviewed_date;
                  if(dt != false){
                    var d = new Date();
                    var offset = - d.getTimezoneOffset();
                    var utc_dt = new Date(dt.replace(/-/g,'/')).getTime();
                    var local_dt = new Date(utc_dt + offset * 60000);
                    var mm = local_dt.getMonth() + 1;
                    mm = "00".substr((""+mm).length,2) + mm;
                    var dd = local_dt.getDate();
                    dd = "00".substr((""+dd).length,2) + dd;
                    var hh = local_dt.getHours();
                    hh = "00".substr((""+hh).length,2) + hh;
                    var M = local_dt.getMinutes();
                    M = "00".substr((""+M).length,2) + M;
                    var ss = local_dt.getSeconds();
                    ss = "00".substr((""+ss).length,2) + ss;
                    var displayedValue = (local_dt.getFullYear()) + "-" + mm + "-" + dd + " " + hh + ":" + M + ":" + ss;
                    review.reviewed_date = displayedValue;
                  }
```

![[2-ocabase-tier-validationpurchase-tier-validationsale-tier-validation-2588-f0adde8b.png]]

## 补充/答案 4

什么时候能有完整的V13版本出来？要能测试通过的，且能真正使用的版本。

## 补充/答案 5

如果实际需求出现，经理下单+希望跳过员工审批的需求，可以修改 审批定义的domain条件来实现。低级审批的domain，只定义('create_uid.groups_id.name','=','员工审批')来进行控制。

由于技术限制，domain中只允许进行字符串比对。

## 补充/答案 6

本模块已完成本地化工作代码svn地址是：
http://dev.oscg.cn/svn/odoo_ecommerce/12.0SRC/base_tier_validation/

http://dev.oscg.cn/svn/odoo_ecommerce/12.0SRC/purchase_tier_validation/

本地化效果：


## 原帖外链配图

![[2-ocabase-tier-validationpurchase-tier-x194038c2.png]]
<small>原始地址: /web/image/877/snipaste_20190120_013236.png?access_token=42c49149-f1bb-4061-b080-1fc0000f57e8</small>

![[2-ocabase-tier-validationpurchase-tier-x194038c2.png]]
<small>原始地址: /web/image/875/snipaste_20190120_012214.png?access_token=e09b921a-cdee-4cb1-a3d0-f03ba2ab5a68</small>

![[2-ocabase-tier-validationpurchase-tier-x194038c2.png]]
<small>原始地址: /web/image/892/snipaste_20190120_114918.png?access_token=1f449d1a-8efc-4b0b-be4e-55c41f9a7b1f</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
