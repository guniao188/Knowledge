---
title: "Odoo的总线消息机制原理bus模块"
source: "http://www.thinkltd.cn/forum/1/odoobus-697"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo的总线消息机制原理bus模块

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoobus-697>

【模块功能及用法】

1.  当需要向Odoo客户端（浏览器）发送消息时候，调用模型"bus.bus"的方法 def sendone(self, channel, message) 。该方法实际是在数据表 bus_bus中创建一条包含该消息及频道的新记录，创建好以后，通知Odoo的消息进程。这里用到了Postgresql的 notify/listen机制，参考链接：

2.  Odoo的消息进程对应的代码参考文件odoo\addons\bus\models\bus.py， class ImDispatch 。该进程循环监听数据库是否有 总线通知（sendone 方法发出的消息），一方面处理Odoo客户端的消息请求（链接：/longpolling/poll）

3.  模型"bus.bus"自动删除创建时间超过100秒的消息。参考：[/forum/1/question/odoo-696](http://www.thinkltd.cn/forum/1/question/odoo-696)

4.  Odoo客户端不断轮询服务器端链接 /longpolling/poll 。每次轮询完，等待 10-30秒 的一个随机时间，再次轮询。轮询的js参考代码：odoo\addons\bus\static\src\js\longpolling_bus.js，方法 _poll ，代码行：   self._pollRetryTimeout = setTimeout(self._poll, self.ERROR_RETRY_DELAY + (Math.floor((Math.random()*20)+1)*1000));

5.  Odoo客户端轮询到消息后，触发notification事件，参考代码 odoo\addons\bus\static\src\js\longpolling_bus.js，方法 _onPoll， 代码 this.trigger("notification", notifs);

6.  Odoo其他模块，如果想处理某种消息，则js中定义自己的_onNotification 处理自己的消息，参考代码 this.call('bus_service', 'onNotification', this, this._onNotification);

7.

【消息通知用法示例】

企业版模块 delivery_iot，该模块中，Picking验证时候，如果获取到了快递公司的电子面单，则以总线通知形式将电子面单发给客户端，客户端获取电子面单后，自动调用 IoT Box的打印机打印电子面单。

后端Picking发送总线通知参考代码 odoo\delivery_iot\models\stock_picking.py

```python
    @api.returns('mail.message', lambda value: value.id)

    def message_post(self, **kwargs):

        message = super(StockPicking, self).message_post(**kwargs)

        if message.attachment_ids and 'Label' in message.attachment_ids.name and self.picking_type_id.iot_printer_id:

            self.env['bus.bus'].sendone(

                (self._cr.dbname, 'res.partner', self.env.user.partner_id.id),

                {

                    'type': 'iot_print_documents',

                    'documents': message.attachment_ids.mapped('datas'),

                    'iot_device_identifier': self.picking_type_id.iot_printer_id.identifier,

                    'iot_ip': self.picking_type_id.iot_printer_id.iot_ip,

                }

            )

        return message
```

客户端js获取消息的参考代码 odoo\delivery_iot\static\src\js\iot_widgets.js

this.call('bus_service', 'onNotification', this, this._onNotification);

```python
    _onNotification: function (notifs) {

        var self = this;

        _.each(notifs, function (notif) {

            var model = notif[0][1];

            var data = notif[1];

            if (model === 'res.partner' && data.type === 'iot_print_documents' && self.call('bus_service', 'isMasterTab')) {

                self._printDocuments(data.iot_device_identifier, data.iot_ip, data.documents);

            }

        });

    },
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
