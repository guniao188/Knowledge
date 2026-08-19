---
title: "OCA支持Odoo服务监控nsca_client"
source: "http://www.thinkltd.cn/forum/2/ocaodoonsca-client-2796"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA支持Odoo服务监控nsca_client

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaodoonsca-client-2796>

模块链接：

## NSCA Client

This is a technical module to send passive alerts to your favorite NSCA daemon (Nagios, Shinken...). This module is based on the Odoo cron system and requires a NSCA client installed on the system to satisfy the `/usr/sbin/send_nsca` command.

###

### Installation

To use this module, you need to install a NSCA client.

On Debian/Ubuntu:

    $ sudo apt-get install nsca-client

###

### Configuration

To configure this module, you need to:

- Configure your server and a passive service in your monitoring tool (e.g service `Odoo Mail Queue` on host `MY-SERVER`).
- Declare your NSCA server in the menu Configuration / Technical / NSCA Client / Servers

- Create NSCA checks in the menu Configuration / Technical / NSCA Client / Checks

- Code the methods which will be called by the NSCA checks.

Such methods must return a tuple `(RC, MESSAGE, PERFORMANCE_DATA)` where `RC` is an integer, `MESSAGE` a unicode string AND `PERFOMANCE_DATA` is a dictionary. `RC` values and the corresponding status are:

- 0: OK
- 1: WARNING
- 2: CRITICAL
- 3: UNKNOWN

`PERFORMANCE_DATA` is not mandatory, so it could be possible to send `(RC, MESSAGE)`. Each element of `PERFORMANCE_DATA` will be a dictionary that could contain:

- value: value of the data (required)
- max: Max value on the chart
- min: Minimum value on the chart
- warn: Warning value on the chart
- crit: Critical value on the chart
- uom: Unit of Measure on the chart (s - Seconds, % - Percentage, B - Bytes, c - Continuous)

The key of the dictionary will be used as the performance_data label.

E.g:

```python
    class MailMail(models.Model):
        _inherit = 'mail.mail'
        @api.model
        def nsca_check_mails(self):
            mails = self.search([('state', '=', 'exception')])
            if mails:
                return (1, u"%s mails not sent" % len(mails), {
                  'exceptions': {'value': len(mails)}})
            return (0, u"OK", {'exceptions': {'value': len(mails)}})
```

On the example, the performance data will use the label `exceptions` and the value will be the number of exception of mails.


## 原帖外链配图

![[2-ocaodoonsca-client-2796-x194038c2.png]]
<small>原始地址: /web/image/1267/server.png?access_token=2298077f-cc49-49f9-bb3c-82cf63b75603</small>

![[2-ocaodoonsca-client-2796-x194038c2.png]]
<small>原始地址: /web/image/1269/check.png?access_token=18e04207-cff7-4571-a5fd-05138bc07e6f</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
