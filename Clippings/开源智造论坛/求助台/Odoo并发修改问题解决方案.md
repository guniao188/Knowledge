---
title: "Odoo并发修改问题解决方案"
source: "http://www.thinkltd.cn/forum/1/odoo-270"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo并发修改问题解决方案

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo-270>

【问题】张三、李四都打开同一个SO，李四修改SO，保存。之后张三也修改SO，保存。结果张三的修改会覆盖李四的修改。

【分析】

1.  参考链接：

2.  Odoo中保存的时候，只会保存修改过的字段。如果李四和张三修改的是同一个字段，则张三的修改会覆盖李四的修改。如果不是同一个字段，则不会覆盖；

3.  如果该字段定义了属性 track_visibility='onchange' ，则李四、张三的修改都会记录在Message区域，即使发生了覆盖事件，事后也是可以还原的；

4.  Odoo有_check_concurrency()机制，可以使用该机制严禁覆盖。

## 补充/答案 1

_check_concurrency()机制原理，Write、Unlink时候，系统检查 context 里面是否有 __last_update， 如果有，__last_update里面是一个字典，Key值为 “模型名称,ID”，值为 一个时间戳。系统检查待修改记录的最后更新时间，如果该时间比__last_update的时间戳新，说明别人已经更新过该记录，系统报错。

_check_concurrency()机制利用方法：read的时候读取记录的__last_update， 存起来，Write的时候，将存起来的__last_update写入Context，示例如下：

```python
class SaleOrder(models.Model):
    _inherit = "sale.order"

    __last_update2 = {}

    @api.multi
    def read(self, fields=None, load='_classic_read'):
        if '__last_update' not in fields:
            fields.append('__last_update')
        res = super(SaleOrder, self).read(fields=fields, load=load)
        for r in res:
            if r['__last_update'] and r.get('id',None):
                self.__last_update2['%s,%s,%s' % (self._name, r['id'],self.env.user.id)] = r['__last_update']

        return res

    @api.multi
    def write(self, vals):
        k = '%s,%s,%s' % (self._name, self.id,self.env.user.id)
        k2 = '%s,%s' % (self._name, self.id)
        last = self.__last_update2.get(k,None)
        if last:
            ctx = {k: v for k, v in self._context.items() }
            ctx['__last_update']={k2:last}
            self = self.with_context(ctx)

        res = super(SaleOrder, self).write(vals)
        return res
```


## 原帖外链配图

![[1-odoo-270-x194038c2.png]]
<small>原始地址: /web/image/1543/snipaste_20190329_155915.png?access_token=a8aa23cd-e414-4a0e-a8d8-2060c1b07faa</small>

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
