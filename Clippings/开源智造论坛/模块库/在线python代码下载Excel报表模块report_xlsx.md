---
title: "在线python代码下载Excel报表模块report_xlsx"
source: "http://www.thinkltd.cn/forum/2/pythonexcelreport-xlsx-3615"
forum: "模块库"
author: "肖相扶"
published: 2024-11-07
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 在线python代码下载Excel报表模块report_xlsx

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-11-07
> <http://www.thinkltd.cn/forum/2/pythonexcelreport-xlsx-3615>

20221223升级到16.0版本：[https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/report_xlsx](https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/report_xlsx)

【20240803升级到17.0版本】OSCG_Git\17.0\extra-addons\report_xlsx

同时增加下述Excel数据报表功能：

1.  增加wizard弹窗，用户输入参数
2.  报表上的在线python代码接收用户输入的参数，抽取报表数据，写入Excel
3.  用户下载Excel报表
4.  以前版本的模块参考： [二开Excel/Docx word打印报表模块report_xlsx、report_docx](http://www.thinkltd.cn/forum/2/excel-docx-wordreport-xlsxreport-docx-2987)

【20241107吴键升级到18.0版本】[https://gitlab.com/oscg-china/extra-addons/-/tree/18.0/report_xlsx](https://gitlab.com/oscg-china/extra-addons/-/tree/18.0/report_xlsx)

【功能截图】

![[2-pythonexcelreport-xlsx-3615-1ce4951f.png]]

![[2-pythonexcelreport-xlsx-3615-4b97a5aa.png]]

截图示例在线代码示例：

    #Variant you can use
    # user_param: 用户在弹窗输入的参数
    #env: Odoo Environment on which the action is triggered
    #time, datetime, dateutil, pytz: useful Python libraries
    #logger:
    #UserError: Warning Exception to use with raise
    #'obj': record,
    #'wb': return of openpyxl.load_workbook(),
    #'ws': openpyxl.worksheet.worksheet.Worksheet,
    #'style': openpyxl.styles,
    #'add_img': add_img,
    #
    #Example:
    #ws['G9'] = obj.confirmation_date
    #ws["B1"].font=style.Font(name="宋体"，size=17,color="00CCFF")
    #ws.cell(2,1).fill = style.PatternFill("solid",fgColor="00FF02")
    #ws.cell(row,col).alignment = style.Alignment(horizontal='center', vertical='justify', wrap_text=True)
    #ws.merge_cells('A1:D4')
    #ws.unmerge_cells('A1:D4')
    #row = 17
    #idx = 1
    #for line in obj.order_line:
    #    ws.cell(row,1).value = idx
    #    add_img(ws, (row,2), line.product_id.image_medium, (100, 100))
    #    ws.cell(row,3).value = line.product_id.with_context(lang=obj.partner_id.lang).name
    #    ws.insert_rows(row,1)
    #
    #    row=row+1
    #    idx=idx+1

```python
    dt1 = datetime.now()
    tz = env.user.tz or 'UTC'
    utc_datetime = pytz.utc.localize(dt1, is_dst=False)
    try:
        context_tz = pytz.timezone(tz)
        localized_datetime = utc_datetime.astimezone(context_tz)
    except Exception:
        localized_datetime = utc_datetime

    ws.cell(1,1).value = '用户输入参数'
    ws.cell(1,2).value = user_param
    ws.cell(2,1).value = 'UTC Date time'
    ws.cell(2,2).value = "%s" % dt1
    ws.cell(3,1).value = 'Local Date time'
    ws.cell(3,2).value = "%s" % localized_datetime
```

## 补充/答案 1

【Odoo17代码示例】Odoo17版本注意事项：

1.  openpyxl建议安装3.1以上版本
2.  Excel中插入明细行的方法和以前不同了。模块中去除了insert_row方法，改成在代码中自己写明细行插入的方法，参考下面代码示例的 insert_row_format

    #在row的前面插入一行，并复制上一行的格式
```python
    def insert_row_format(wsheet, row):
        height = wsheet.row_dimensions[row].height
        wsheet.insert_rows(row+1,1)
        wsheet.row_dimensions[row+1].height = height
```

        #复制格式
```python
        for iCol in range(1, wsheet.max_column+1):
            wsheet.cell(row+1, iCol).font = copy(wsheet.cell(row, iCol).font)
            wsheet.cell(row+1, iCol).fill = copy(wsheet.cell(row, iCol).fill)
            wsheet.cell(row+1, iCol).border = copy(wsheet.cell(row, iCol).border)
            wsheet.cell(row+1, iCol).alignment = copy(wsheet.cell(row, iCol).alignment)
```

    #填充Excel模板数据
```python
    def fill_sheet():
        lang = obj.partner_id.lang
        ws['B6'] = obj.partner_id.name
        ws['B8'] = obj.partner_id.street or ''
        ws['B9'] = obj.partner_id.street2 or ''
        ws['B10'] = obj.partner_id.country_id.with_context(lang=lang).name or ''

        ws['N6'] = 'PI-%s' % obj.name
        ws['N7'] = obj.date_order or ''
        ws['N8'] = obj.commitment_date or ''
        ws['N9'] = obj.port_dest.name or ''
        ws['N10'] = obj.port_from.name or ''
        ws['N11'] = obj.payment_term_id.with_context(lang=lang).name or ''

        row = 16
        last_row = row + len(obj.order_line) - 1
        for line in obj.order_line:
            ws.cell(row,1).value = line.product_id.default_code or ''
            add_img(ws, (row,2), line.product_id.image_128, (90, 90))
            ws.cell(row,3).value = line.name
            ws.cell(row,4).value = line.price_unit
            ws.cell(row,5).value = line.product_uom_qty
            ws.cell(row,6).value = line.price_subtotal
            ws.cell(row,7).value = line.product_id.width or ''
            ws.cell(row,8).value = line.product_id.length or ''
            ws.cell(row,9).value = line.product_id.height or ''
            product_pack = line.product_id.packaging_ids and line.product_id.packaging_ids[0]
            if product_pack:
                ws.cell(row,10).value = product_pack.qty
                ws.cell(row,11).value = product_pack.width
                ws.cell(row,12).value = product_pack.length
                ws.cell(row,13).value = product_pack.height
                ws.cell(row,14).value = product_pack.volume
                ws.cell(row,15).value = line.product_uom_qty
                pack_qty = product_pack.qty != 0 and product_pack.qty or 1
                ws.cell(row,16).value = line.product_uom_qty/pack_qty
                ws.cell(row,17).value = line.product_uom_qty/pack_qty * product_pack.volume

            if row == last_row:
                break
            insert_row_format(ws, row)
            row=row+1

    fill_sheet()
```

## 补充/答案 2

16版本，安装  3.0.6的 openpyxl

以及Excel里不要留公式，如果需要公式的，直接python代码里取值然后给excel，因为插件里约束了他可以识别的公式，不在他识别范围内的就会报错

## 补充/答案 3

实际使用案例：华霆 V16 UDP平台服务器环境下：

report_xlsx模块

使用场景：因华霆的产品数据量非常大，到50w以上，而V16版本界面导出数据最多一次只能导出2W条记录，一旦客户的数据超出2万条数据，就不能导出需要的完整数据了，故采用了这个插件来解决导出列的问题

需要导出的列的模板提前在代码中指定好

搭配界面配置【设置/技术/报告】里的导出excel编写代码：

![[2-pythonexcelreport-xlsx-3615-c88b9fbd.png]]

![[2-pythonexcelreport-xlsx-3615-3dc8588b.png]]

![[2-pythonexcelreport-xlsx-3615-ffe8a103.png]]

代码：

#要导出的字段
# fields_to_export = ['id','product_brand_id', 'default_code', 'name','zt_jname', 'zt_bname', 'zt_lname','cj_categ_fname']
# fields_to_export = ['id','product_brand_id', 'default_code', 'name','barcode']
fields_to_export = ['id','default_code','name','box_num','sub_box_num']

prt_ids = env['product.product'].search(['&','|',('box_num','>',0),('sub_box_num','>',0),('uom_id','!=',28)], order='id', limit=85735)
exp_ids = prt_ids.export_data(fields_to_export)
row = 2
for p in exp_ids['datas']:
ws.cell(row,1).value = p[0]
ws.cell(row,2).value = p[1]
ws.cell(row,3).value = p[2]
ws.cell(row,4).value = p[3]
ws.cell(row,5).value = p[4]
row=row+1

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
