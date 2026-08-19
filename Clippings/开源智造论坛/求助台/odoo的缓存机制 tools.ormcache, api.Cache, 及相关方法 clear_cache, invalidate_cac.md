---
title: "odoo的缓存机制 tools.ormcache, api.Cache, 及相关方法 clear_cache, invalidate_cache, flush"
source: "http://www.thinkltd.cn/forum/1/odoo-tools-ormcache-api-cache-clear-cache-invalidate-cache-flush-720"
forum: "求助台"
author: "施叶寒"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# odoo的缓存机制 tools.ormcache, api.Cache, 及相关方法 clear_cache, invalidate_cache, flush

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:施叶寒 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo-tools-ormcache-api-cache-clear-cache-invalidate-cache-flush-720>

Odoo的缓存机制分为两类，

1. api.Cache() search,browse返回/界面onchange生成的ORM对象，在odoo框架内封装的数据库对象;

2. tools.ormcache 用于修饰具体方法，可以有效减少方法的调用频率。

1. api.Cache()  invalidate_cache

为了减少程序运行过程中与数据库之间的交互，odoo使用api.Cache()类实例来读取数据库里的数据，用于调用odoo模型付以的python方法，包括计算特殊字段(compute字段)的值。

举例说明：

现有字段sale.order.line(1)=>{'price_unit':1.0,'product_uom_qty':2.0}

```python
def _compute_total_amount(selfs):

    for self in selfs:

        self.total_amount = self.price_unit * self.product_uom_qty
```

total_amount = fields.Float(compute='_compute_total_amount')

## 补充/答案 1

print(self.total_amount)    => 2.0

self.write({'price_unit':self.price_unit + 1})

print(self.total_amount)    => 2.0

## 补充/答案 2

ORM对象用于减少数据读取的次数，因此只有实例的字段值为空时，才去读取一次。

1. ORM对象的所有数据库字段，会在初始化时同意从数据库加载；

2. ORM对象的特殊字段，如compute型字段，在程序用到的时候进行计算。

```python
    2.1 此时的compute方法执行过程中，用到的数据库字段的值，不再从数据库读取，而是读取Cache实例当时的字段的值(例如：初始化时加载的数据库的值，或是程序运行过程中write执行后的最新值)。

    2.2 Cache实例只有在自身的这个计算型字段为空(从没执行过compute方法)时，才执行compute方法。
```

从示例中可以看到，此时total_amount因为没有重新根据price_unit的最新值重新计算，而返回了异常数据。

对应方法：

1. compute方法 添加 @api.depends('price_unit','product_uom_qty')注解，修改price_unit后ORM对象将重新计算total_amount的值。

2. self.invalidate_cache()，这样可以清空对应记录的对应字段的值，这样ORM对象下次对字段取值的时候会再从数据库重新加载一遍。

2. api.Cache()  flush

所有ORM对象对自身字段的修改，如果需要存在数据库表中，最终会触发create, write方法，执行与数据库交互的sql语句。但是由于Odoo框架提供的机制，并不能认为create, write方法执行后，当前事务中的那条受影响记录就是可信的。

举例说明：odoo按以下顺序共执行了4个方法

1. ORM对象执行 create, write 方法

2. 数据库执行 insert, update 语句

3. ORM对象执行 inverse, 带有api.depends()注解的compute方法

4. ORM对象执行 带有api.constrains()注解的check方法

其中，第3、4步类似于 odoo提供的针对特定字段的自动动作，类似于面向业务的模型触发器，需要等到数据库的基础语句执行完成后由Odoo代为执行。

虽然执行3、4步的过程中，没有及时将运行中的数据变更同步至数据库表中，但由于ORM对象用到的所有数据来自于自身的最新数据，所以没有把问题暴露出来。

然后，出于一些特定原因，如：效率，如果此时直接在check方法中执行

self.env.cr.execute('select * from sale_order'),此时第3步inverse方法, compute方法的结果没有及时推送到数据库中，数据同步异常的问题就出来了。

对应方法：

在第3、4步执行sql语句之前，显示执行self.flush(),把当前存在ORM对象的最新待推送数据显式推送到数据库中。

3. tools.ormcache  clear_caches

虽然ORM对象能极大地减少与数据局的交互，但作为python对象，随着当前请求的开始进行初始化，随着当前请求的结束而销毁，无法实现跨请求的缓存。因此需要另一种机制来实现类似于redis的缓存机制。

举例说明：

ir.config_parameter的get_param方法。

```python
    @api.model

    @ormcache('self.env.uid', 'self.env.su', 'key')

    def _get_param(self, key):

        params = self.search_read([('key', '=', key)], fields=['value'], limit=1)

        return params[0]['value'] if params else None
```

系统参数的定位，有些类似于可以在界面配置的静态资源，因此在具体实现上，可以进行缓存。

对这段代码而言，

1. 如果属于系统重启后的第一次调用，将逐行执行代码，并在缓存中记录当前ormcache的参数及_get_param的最终返回值。

2. 其他情况下，对于当前请求下获取的这个具体的系统参数， 如果 用户ID、用户是否拥有超级权限、当前系统参数键名 与(当前请求或上一个请求)最近一次调用一致，那么Odoo将不再逐行执行该方法，直接返回已缓存的结果；如果不一致，那么  将逐行执行代码，并在缓存中替换为当前ormcache的参数及_get_param的最终返回值。

注：

1. ormcache中的参数，可以写若干个python表达式，但数据必须来源于该方法具体的某个参数。

2. 如果采用ormcache修饰具体的select方法，那在对应的insert,update,delete方法中需要显式地更新缓存。在源码中是这样实现的。

```python
    @api.model_create_multi

    def create(self, vals_list):

        self.clear_caches()

        return super(IrConfigParameter, self).create(vals_list)

    def write(self, vals):

        self.clear_caches()

        return super(IrConfigParameter, self).write(vals)

    def unlink(self):

        self.clear_caches()

        return super(IrConfigParameter, self).unlink()
```

3. 由于odoo系统会跨请求地缓存被修饰的方法的返回值，虽然不存在 持久化 的硬性需要(这点远胜redis)，但是如果缓存了一个ORM对象，就可能存在以下2种情况：

```python
    1. cr游标超时连接，执行具体的sql语句时报错

    2. cr游标一直被引用无法回收，导致数据库资源无意义的消耗

    3. 其他各种奇怪的情况
```

4. ormcache中的表达式，必须返回不可变对象，用于在前后调用时进行对比

5. 例如图片之类的真 静态资源还是需要通过IO流或者数据库进行读取，ormcache只缓存少量多次的数据

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
