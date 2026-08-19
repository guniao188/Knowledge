---
title: "如何在Excel中插入条形码"
source: "http://www.thinkltd.cn/forum/1/excel-3636"
forum: "求助台"
author: "刘志鹏"
published: 2023-02-19
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 如何在Excel中插入条形码

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:刘志鹏 | 2023-02-19
> <http://www.thinkltd.cn/forum/1/excel-3636>

环境：Odoo16

使用的包：Openpyxl

在Odoo16源码中, ir.action.report模型有一个方法barcode

两个主要的参数，一个是条形码的类型，比如EABN8, EAN13, auto等等

还有一个是扫描条形码后打印的值

返回一个字节类型的条形码

![[1-excel-3636-5f1e35a7.png]]

[openpyxl](https://openpyxl.drawing.im)往Excel插入图片主要使用包openpyxl.drawing.image和add_image方法

image无法识别字节类型，需要先创建一个字节流，将条形码的字节写入字节流

然后再使用

下面上代码:

```python
    import openpyxl
    from io import BytesIO
    from openpyxl.utils import get_column_letter

    def add_barcode(ws, anchor, field_value, size):
        """
        ws是WorkSheet, anchor是图片在Excel中的位置,例如:(1,1) 就是A1
        field_value是扫描条形码后打印的值, size是条形码的长宽, 例如(800,300)
        """
        barcode = self.env['ir.actions.report'].barcode('auto', field_value)
        f = BytesIO()
        f.write(barcode)
        f.seek(0)
        image= openpyxl.drawing.image.Image(f)
        image.anchor = "%s%s" % (get_column_letter(anchor[1]), anchor[0])
        image.width, image.height = size
        ws.add_image(image)

    add_barcode(ws, (1,1), self.value, (800,300))
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
