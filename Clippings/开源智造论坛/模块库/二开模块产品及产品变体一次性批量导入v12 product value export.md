---
title: "二开模块产品及产品变体一次性批量导入v12 product value export"
source: "http://www.thinkltd.cn/forum/2/v12-product-value-export-2653"
forum: "模块库"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开模块产品及产品变体一次性批量导入v12 product value export

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/v12-product-value-export-2653>

该模块存放于：F:\SVN\odoo_ecommerce\12.0SRC\v12 product value export

里面二个模块是有依赖，需要都安装。

此模块解决的问题是：

当一个产品模板有多个属性和属性值时，系统原有的功能，一旦启用变体，产品变体和产品模板，导入就变得非常复杂，而且属性和属性值的不同，会产生不同的SKU，而条码、内部编码、成本等信息又必须再到SKU变体中再去维护，用户操作上很不方便。

这个模块，为用户提供了方便，可以直接一次性在导入产品的同时，将变体相应的内部编码、条码等信息一并一次性的导入完成。

导入的模板分二个：导入模板存放在：

![[2-v12-product-value-export-2653-480619d8.png]]

一个是一次性的导入产品和产品变体及相应的属性属性值：import_product_var_add_excel

另一个为批量导入这些产品变体上关联的主供应商及供应商的价格：import_product_supplier_add_excel

具体请参考以下截图：

模板填写解说：

1、产品及产品变体导入时，会自动去查找是否已存在相应的属性和属性值，如果有，则不创建，如果没有，则自动创建；

2、产品的属性，需要设置默认值为：只有在报价单时生成；

3、产品分类在excel表中填写的值，必须与界面上的名字一样，填写最末级关联的分类名称即可，无须写完整路径，但要求用户在设置分类时，这个产品分类的name不要重复；

4、计量单位的填写，界面上如果用的中文状态，则excel中填写中文，如果界面是英文，请填写英文的在excel，否则会导入不成功；

5、属性和属性值的填写，分二列，一列只填写属性；另一列只填写相应的属性值，请务必与前面的属性的位置是对应的，多个值之间是用英文状态下的逗号隔开；

6、最后的id需要唯一，最好也是内部编码也唯一，用此作为关联，用于后面批量导供应商产品价格信息时，直接调用这列id，即能直接关联，就不需要再重新去匹配了；

7、安装完模块后，请记得在【设置/用户】中设置勾选下权限组，方可在【销售/产品】菜单下看到这个导入的菜单。

8、填写规范如附件所示；

9、录制的视频参考：

链接：https://pan.baidu.com/s/1gkFu233ZJVGzXIfhRuZBqQ
提取码：1663
复制这段内容后打开百度网盘手机App，操作更方便哦

![[2-v12-product-value-export-2653-38b0af49.png]]

![[2-v12-product-value-export-2653-38b0af49.png]]

![[2-v12-product-value-export-2653-950fe5c4.png]]

![[2-v12-product-value-export-2653-950fe5c4.png]]

![[2-v12-product-value-export-2653-5e207006.png]]

![[2-v12-product-value-export-2653-e8a9baf0.png]]

属性和属性值是一一对应的；

![[2-v12-product-value-export-2653-a99fc2e2.png]]

供应商价格导入：

![[2-v12-product-value-export-2653-08938e92.png]]

![[2-v12-product-value-export-2653-1e9e13a2.png]]

## 补充/答案 1

V11的版本也有，但是是有问题的，sh_import_product_var-11.0.1，这个模块这个版本，是网站购买的，原封不动的。很多BUG没有修复，实际使用时问题很多。比如：只支持英文界面的字段名，导入也缺少很多判断。

在这个版本上有修改过的，只有V12版本，几乎全部改了一遍，目前V12的版本有实际客户用上了。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
