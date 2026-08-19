---
title: "Odoo代码性能调优工具"
source: "http://www.thinkltd.cn/forum/3/odoo-36"
forum: "方案库"
author: "肖相扶"
published: 2023-08-07
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# Odoo代码性能调优工具

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:肖相扶 | 2023-08-07
> <http://www.thinkltd.cn/forum/3/odoo-36>

Python代码性能调试工具及参考链接：

1.  cProfile:

2.  pyFlame:

3.  smile_perf_analyzer: [/forum/2/question/smile-rpcsqlsmile-perf-analyzer-3068](http://www.thinkltd.cn/forum/2/question/smile-rpcsqlsmile-perf-analyzer-3068)

Odoo代码性能调优参考链接：

pyFlame是Uber开发的一个非常有效的分析Python代码运行瓶颈的工具。该工具从内存及CPU寄存器等底层采集数据，分析Python方法运行时间占比，并以图形化可视化方式展现方法间调用关系及运行时间占比关系。

Profile：Odoo 12.0自带一个Profile工具，该工具分析各个python方法的调用次数、调用时间、及数据库访问次数，分析结果以列表格式输出到Odoo log文件。

smile_perf_analyzer 模块将odoo的方法调用、SQL执行时间写入数据库的logs表。性能数据抓取不用修改代码，查阅起来更方便。

[ ](https://pyflame.readthedocs.io/en/latest/index.html)

## 补充/答案 1

Odoo Profile调优方法：

第一步，被调查方法的定义上增加 @profile，如下。

```python
from odoo.tools.profiler import profile

    @profile(minimum_time=10)
    @api.model
    def create_from_ui(self, orders):
```

@profile的用法及参数说明：

```python
    """
        Decorate an entry point method.
        If profile is used without params, log as shallow mode else, log
        all methods for all odoo models by applying the optional filters.

        :param whitelist: None or list of model names to display in the log
                        (Default: None)
        :type whitelist: list or None
        :param files: None or list of filenames to display in the log
                        (Default: None)
        :type files: list or None
        :param list blacklist: list model names to remove from the log
                        (Default: remove non odoo model from the log: [None])
        :param int minimum_time: minimum time (ms) to display a method
                        (Default: 0)
        :param int minimum_queries: minimum sql queries to display a method
                        (Default: 0)

        .. code-block:: python

          from odoo.tools.profiler import profile

          class SaleOrder(models.Model):
            ...

            @api.model
            @profile                    # log only this create method
            def create(self, vals):
            ...
            @api.multi
            @profile()                  # log all methods for all odoo models
            def unlink(self):
            ...
            @profile(whitelist=['sale.order', 'ir.model.data'])
            def action_quotation_send(self):
            ...
            @profile(files=['/home/openerp/odoo/odoo/addons/sale/models/sale.py'])
            def write(self):
            ...

        NB: The use of the profiler modifies the execution time
    """
```

第二步，分析Log文件中输出的profile分析数据，数据格式如下图所示。

点击图标下载示例文件（txt格式）。

## 补充/答案 2

【pyFlame调优方法】

第一步，安装pyflame工具：

sudo apt install autoconf automake autotools-dev g++ pkg-config python-dev python3-dev libtool make
git clone https://github.com/uber/pyflame.git
git clone https://github.com/brendangregg/FlameGraph.git
cd pyflame
./autogen.sh
./configure
make
sudo make install

第二步，执行pyFlame采样运行栈信息。这里分析Odoo POS模块的订单提交(方法 create_from_ui )性能为例。

pyflame --exclude-idle -s 90 -r 0.005 -p 22070 -o pos_create_from_ui.flame

-s 90 表示采集90秒，-r 表示每多少秒采集一次（本例5毫秒），-p表示采集哪个进程ID，-o表示采集数据输出到哪个文件。采集结束后，系统输出采集结果到该文件。

第三步，flamegraph.pl命令将采集的堆栈数据转化成可视化图形（SVG格式），便于分析性能瓶颈。

./FlameGraph/flamegraph.pl ./pos_create_from_ui.flame > ./pos_create_from_ui.svg

本例生成的示例SVG图形如下（点击图标用浏览器打开看效果）：


## 原帖外链配图

![[3-odoo-36-x194038c2.png]]
<small>原始地址: /web/image/1600/snipaste_20190421_172705.png?access_token=8e95e49f-036f-43e6-a86e-02b440f272be</small>

![[3-odoo-36-x194038c2.png]]
<small>原始地址: /web/image/1598/snipaste_20190421_170807.png?access_token=b91029d4-6834-4944-9d32-2baffb94b3c4</small>

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
