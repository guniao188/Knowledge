---
title: "Odoo16消息通知实现原理"
source: "http://www.thinkltd.cn/forum/1/odoo16-3823"
forum: "求助台"
author: "肖相扶"
published: 2023-12-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo16消息通知实现原理

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-12-10
> <http://www.thinkltd.cn/forum/1/odoo16-3823>

消息通知实现效果：

![[1-odoo16-3823-cc1d9b5d.png]]

消息通知使用方法：

```python
    import { useService } from "@web/core/utils/hooks";
    ...

    const notification = useService('notification');
    notification.add('a message', {type: 'danger', sticky: true, onClose: () => {alert("Notification closed"); }, });
```

1.  添加提示消息(add)时候，支持的options参数有 type, sticky, onClose 三个。
2.  type有info, success, warning, danger 四种，消息弹窗的显示颜色不同。danger边框是红色，warning边框是黄色，info边框是绿色。
3.  sticky为true表示消息弹窗不自动关闭，需要鼠标点击关闭。false则消息弹窗默认显示4秒后自动关闭。
4.  onClose是一个函数，消息关闭时候系统自动调用该函数。

上述示例代码的显示效果如下：

![[1-odoo16-3823-6a0ce539.png]]

消息通知内部原理：

消息服务的实现代码文件参考 addons\web\static\src\core\notifications\notification_service.js

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
