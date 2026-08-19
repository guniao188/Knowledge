---
title: "OCA后台作业管理queue_job"
source: "http://www.thinkltd.cn/forum/2/ocaqueue-job-2750"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA后台作业管理queue_job

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaqueue-job-2750>

V15版本 [https://github.com/OCA/queue/tree/15.0/queue_job](https://github.com/OCA/queue/tree/15.0)

模块链接：

13.0版本：

This addon adds an integrated Job Queue to Odoo.

It allows to postpone method calls executed asynchronously.

Jobs are executed in the background by a `Jobrunner`, in their own transaction.

Example:

```python
    from odoo import models, fields, api
    from odoo.addons.queue_job.job import job
    class MyModel(models.Model):
       _name = 'my.model'
       @api.multi
       @job
       def my_method(self, a, k=None):
           _logger.info('executed with a: %s and k: %s', a, k)
    class MyOtherModel(models.Model):
        _name = 'my.other.model'
        @api.multi
        def button_do_stuff(self):
            self.env['my.model'].with_delay().my_method('a', k=2)
```

In the snippet of code above, when we call `button_do_stuff`, a job capturing the method and arguments will be postponed. It will be executed as soon as the Jobrunner has a free bucket, which can be instantaneous if no other job is running.

Features:

- Views for jobs, jobs are stored in PostgreSQL
- Jobrunner: execute the jobs, highly efficient thanks to PostgreSQL's NOTIFY
- Channels: give a capacity for the root channel and its sub-channels and segregate jobs in them. Allow for instance to restrict heavy jobs to be executed one at a time while little ones are executed 4 at a times.
- Retries: Ability to retry jobs by raising a type of exception
- Retry Pattern: the 3 first tries, retry after 10 seconds, the 5 next tries, retry after 1 minutes, ...
- Job properties: priorities, estimated time of arrival (ETA), custom description, number of retries
- Related Actions: link an action on the job view, such as open the record concerned by the job

## [Installation](https://github.com/OCA/queue/tree/12.0/queue_job#id4)

Be sure to have the `requests` library.

##

## [Configuration](https://github.com/OCA/queue/tree/12.0/queue_job#id5)

- Using environment variables and command line:
  - Adjust environment variables (optional):
    - `ODOO_QUEUE_JOB_CHANNELS=root:4` or any other channels configuration. The default is `root:1`
    - if `xmlrpc_port` is not set: `ODOO_QUEUE_JOB_PORT=8069`
  - Start Odoo with `--load=web,queue_job` and `--workers` greater than 1. [[1]](https://github.com/OCA/queue/tree/12.0/queue_job#id2)
- Using the Odoo configuration file:

    [options]
```python
    (...)
    workers = 6
    server_wide_modules = web,queue_job
    (...)
```

    [queue_job]
    channels = root:2

- Confirm the runner is starting correctly by checking the odoo log file:

```python
    ...INFO...queue_job.jobrunner.runner: starting
    ...INFO...queue_job.jobrunner.runner: initializing database connections
    ...INFO...queue_job.jobrunner.runner: queue job runner ready for db
    ...INFO...queue_job.jobrunner.runner: database connections ready
```

- Create jobs (eg using `base_import_async`) and observe they start immediately and in parallel.
- Tip: to enable debug logging for the queue job, use `--log-handler=odoo.addons.queue_job:DEBUG`

|  |  |
|----|----|
| [[1]](https://github.com/OCA/queue/tree/12.0/queue_job#id1) | It works with the threaded Odoo server too, although this way of running Odoo is obviously not for production purposes. |

##

## [Usage](https://github.com/OCA/queue/tree/12.0/queue_job#id6)

To use this module, you need to:

1.  Go to `Job Queue` menu

###

### [Developers](https://github.com/OCA/queue/tree/12.0/queue_job#id7)

**Bypass jobs on running Odoo**

When you are developing (ie: connector modules) you might want to bypass the queue job and run your code immediately.

To do so you can set TEST_QUEUE_JOB_NO_DELAY=1 in your enviroment.

**Bypass jobs in tests**

When writing tests on job-related methods is always tricky to deal with delayed recordsets. To make your testing life easier you can set test_queue_job_no_delay=True in the context.

Tip: you can do this at test case level like this

```python
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(
            cls.env.context,
            test_queue_job_no_delay=True,  # no jobs thanks
        ))
```

Then all your tests execute the job methods synchronously without delaying any jobs.

## 补充/答案 1

上海华霆 备份不了数据库，手动备份提示
ValueError: &lt;class 'xmlrpc.client.ProtocolError'&gt;: "&lt;ProtocolError for localhost:8069/xmlrpc/db: 404 NOT FOUND&gt;
odoo-server.conf 配置
odoo13 缺省值  server_wide_modules = web,base
问题可参考以下链接
\https://github.com/Yenthe666/auto_backup/issues/122

## 补充/答案 2

#### 如过出现界面总是**断开和重新链接**的情况则可能是参数没有配置正确

一定要设置 longpolling_port 参数。

参考：

longpolling_port = 8072

workers = 2

server_wide_modules = web,base,queue_job

channels = root:2

## 补充/答案 3

![[2-ocaqueue-job-2750-87679fc8.png]]

UTF-8格式也转化过了，导入用的csv格式，点了【导入】按钮，会报这种错，有没有人遇到过？

Object of type 'lazy' is not JSON serializable

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
