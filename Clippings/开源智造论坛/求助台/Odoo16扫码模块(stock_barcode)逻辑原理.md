---
title: "Odoo16扫码模块(stock_barcode)逻辑原理"
source: "http://www.thinkltd.cn/forum/1/odoo16-stock-barcode-3821"
forum: "求助台"
author: "肖相扶"
published: 2023-12-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo16扫码模块(stock_barcode)逻辑原理

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-12-10
> <http://www.thinkltd.cn/forum/1/odoo16-stock-barcode-3821>

1.  进入扫码界面时候，系统加载Cach数据到浏览器缓存。Cach加载步骤如下：
2.  1.  文件 stock_barcode\static\src\components\main.js，方法 setup()，调用后端方法 /stock_barcode/get_barcode_data，获取Cach数据。
```python
    2.  Cach数据结构参见文件stock_barcode\static\src\lazy_barcode_cache.js 。其缓存数据有两个：dbIdCache和dbBarcodeCache 。
    3.  dbIdCache的key值，先是模型名，其次是记录id，其value是该记录的各字段值。每个模型包含哪些字段，则取决于模型方法 _get_fields_stock_barcode 所返回的字段。
    4.  dbBarcodeCache的key值，先是模型名，其次是barcode，value是该记录的各字段值。
    5.   后端方法/stock_barcode/get_barcode_data 的实现中，调用各模型的方法 _get_stock_barcode_data，获取该模型的Cach数据。代码参见文件stock_barcode\controllers\stock_barcode.py
    6.  以stock.picking的 _get_stock_barcode_data实现为例，说明如下。
    7.  1.  返回字典类型数据，分records, config等几部分，其中 records 又是一个字典，Key是模型名，返回stock.picking关联的各个模型的字段值。
        2.  每个模型返回哪些字段值，从模型方法_get_fields_stock_barcode()获取
        3.  config 的数据，来自stock.picking.type模型的方法 _get_barcode_config()
```

3.  扫描条码时候，系统解析条码，再处理条码。入口方法参见文件 stock_barcode\static\src\components\main.js的方法 _onBarcodeScanned
4.  解析条码步骤如下：
5.  1.  从Cach中查找条码，如果找到了，获取条码数据，返回条码数据，以及匹配成功标记。解析条码方法参见文件stock_barcode\static\src\models\barcode_model.js 的方法 _parseBarcode
    2.  解析条码的第一步，从条码中拆解出条码的各个组成部分，如条码类型，产品条码，重量单价等信息。方法参见文件 addons\barcodes\static\src\js\barcode_parser.js的方法 parse_barcode，此方法根据模型barcode.nomenclature 的设置，提取条码格式数据。

![[1-odoo16-stock-barcode-3821-452d290f.png]]

    3.  解析条码的第二步，从Cach中获取条码对象(产品、库位、包裹、批次等)。参见文件stock_barcode\static\src\lazy_barcode_cache.js中方法getRecordByBarcode
6.  处理条码步骤如下：待查

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
