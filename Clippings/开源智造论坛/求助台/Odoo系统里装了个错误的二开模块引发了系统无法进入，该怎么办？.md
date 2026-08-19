---
title: "Odoo系统里装了个错误的二开模块引发了系统无法进入，该怎么办？"
source: "http://www.thinkltd.cn/forum/1/odoo-4072"
forum: "求助台"
author: "杨浔波"
published: 2025-09-26
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo系统里装了个错误的二开模块引发了系统无法进入，该怎么办？

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:杨浔波 | 2025-09-26
> <http://www.thinkltd.cn/forum/1/odoo-4072>

如：我个人不小心安装了ddmrp的解决方案，引发了系统Odoo无法正常使用打开，是不是只能通过备份库进行恢复，该库的之前做的测试和数据成果都废掉了？

解决方案：无需删库跑路，仅需通过Odoo的Shell模式即可解决该问题。以ddmrp这个第三方模块为例。

1. 首先进入odoo-bin Shell模式：

    python3 odoo-bin shell -c odoo.conf -d odoo18_demo

2. 进行模块卸载的Python Shell脚本编写：

    # 获取模块模型并搜索目标模块
    module = env['ir.module.module'].search([('name', '=', 'ddmrp')])
    # 检查后执行卸载
```python
    if module:
        module.button_immediate_uninstall()
        print(f"模块 ddmrp 已标记为卸载")
    else:
        print("未找到指定模块")

![[1-odoo-4072-7ab6ef16.png]]

    PS：可以从SHELL中看到模块数据在清理中
```

![[1-odoo-4072-d109de98.png]]

可以看到Odoo系统的ddmrp模块最终被清理卸载干净！

![[1-odoo-4072-0fa09fe5.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
