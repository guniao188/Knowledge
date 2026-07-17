---
title: "mrp_material_check"
source: "https://apps.odoo.com/apps/modules/19.0/mrp_material_check"
author:
  - "[[Randy Nguyen]]"
published:
created: 2026-07-16
description:
tags:
  - "clippings"
---
![](https://apps.odoocdn.com/web/image/loempia.module/322250/icon_image/84x84?unique=750c59d)

## MRP 物料检查(MRP Material Check)

作者:[Randy Nguyen](https://apps.odoo.com/apps/modules/browse?author=Randy%20Nguyen)

Odoo

| **版本** | [17.0](https://apps.odoo.com/apps/modules/17.0/mrp_material_check) [18.0](https://apps.odoo.com/apps/modules/18.0/mrp_material_check) 19.0 |
| --- | --- |

您购买了此模块并需要**支持**?[点击这里!](https://apps.odoo.com/apps/support/322250)

| **版本** | [17.0](https://apps.odoo.com/apps/modules/17.0/mrp_material_check) [18.0](https://apps.odoo.com/apps/modules/18.0/mrp_material_check) 19.0 |
| --- | --- |

![MRP Material Check Icon](https://apps.odoocdn.com/apps/assets/19.0/mrp_material_check/icon.png?80c6415)

MRP 物料检查

✓ 社区版 ✓ 企业版

检查模式

2

🛡️

Odoo 版本

19.0

⚡

许可证

LGPL-3

🔓

依赖

mrp

📦[联系 / 支持 · nextstep.vina@gmail.com](mailto:nextstep.vina@gmail.com)警告模式 阻止模式 永久免费

#### MRP 物料检查

阻止负库存悄无声息地破坏您的账目。这是一个零配置模块,它会拦截制造单上的**生产**按钮,并弹出清晰的窗口,列出**具体哪些组件短缺** —— 提供两种模式:**警告模式**(任何人都可继续)和**阻止模式**(仅经理可绕过)。

😓 面临的问题

- ✗ 即使组件完全缺货,Odoo 也允许您点击"生产"—— 瞬间产生负库存。
- ✗ 负库存直接流入会计分录 —— 您的销货成本(COGS)和库存估值将变得不可靠。
- ✗ 操作员不知道哪个组件短缺或短缺多少 —— 只有在造成损失后才会发现。
- ✗ 没有基于角色的保护 —— 任何仓库用户都可能不小心(或无意中)在零库存下验证订单。

🎯 解决方案

- ✓ 在任何库存移动之前拦截"全部生产" —— 实时检查每个组件在源位置的数量。
- ✓ 弹出表格列出每个短缺组件:**需要数量 / 库存数量 / 短缺数量 / 单位** —— 一目了然。
- ✓ **警告模式:** 显示弹窗,由操作员决定。**阻止模式:** 只有制造经理才能按下"仍然继续"。
- ✓ 零配置 —— 安装、在制造设置中选择模式,即可使用。

![MRP Material Check Demo](https://apps.odoocdn.com/apps/assets/19.0/mrp_material_check/banner.gif?80c6415)

#### 主要功能

⚠️

实时组件检查 —— 在生产开始前,每条短缺行显示 需要数量 / 库存数量 / 短缺数量 / 单位。

🛡️

阻止模式 —— 锁定普通操作员;只有制造经理可以覆盖短缺关卡。

🔔

警告模式 —— 显示带完整详情的弹窗,但允许操作员决定是否继续,保留灵活性。

⚙️

在 制造 › 配置 › 设置 中设置一项 —— 随时在警告和阻止之间切换。

📍

位置感知 —— 检查移动的实际源位置库存,而不仅仅是全局在手数量。

🔓

100% 免费 · LGPL-3 —— 仅需要标准的 `mrp` 模块。没有付费层级,没有到期时间。

#### 安装指南

1)将 **mrp\_material\_check** 文件夹放入您的 Odoo 自定义插件(addons)目录并重启服务器。

2)启用开发者模式 —— 前往 **设置 → 激活开发者模式**,然后点击 **应用 → 更新应用列表**。

3)在应用中搜索 **"MRP Material Check"** 并点击 **安装**。

4)前往 **制造 → 配置 → 设置**,在 **物料不足行为(Insufficient Material Behaviour)** 下选择您喜欢的模式。

![Manufacturing Settings — Insufficient Material Behaviour](https://apps.odoocdn.com/apps/assets/19.0/mrp_material_check/screenshots/01-settings-warn-mode.png?80c6415)

制造设置 —— "物料不足行为"下拉菜单显示 警告 和 阻止 选项

5)打开任何组件缺失且已确认的制造单,然后点击 **全部生产**。

![Confirmed Production Order with Not Available components](https://apps.odoocdn.com/apps/assets/19.0/mrp_material_check/screenshots/04-confirmed-production.png?80c6415)

已确认的生产订单 —— 在点击"全部生产"之前,"组件状态: 不可用"已经可见

6)弹窗立即出现,列出每个短缺组件的 需要数量 / 库存数量 / 短缺数量。在**警告模式**下您可以继续;在**阻止模式**下,只有经理会看到"仍然继续"。

![Shortage Popup — Warn Mode](https://apps.odoocdn.com/apps/assets/19.0/mrp_material_check/screenshots/05-warn-mode-shortage-popup.png?80c6415)

警告模式弹窗 —— 显示 Demo Steel Rod: 需要 3.00 / 库存 0.00 / 短缺 3.00,并带有"仍然继续"按钮

#### 常见问题

在**警告模式**下,任何用户都会看到短缺弹窗,但可以点击"仍然继续"以照常执行。在**阻止模式**下,"仍然继续"按钮仅对拥有 **制造经理(Manufacturing Manager)** 用户组的用户可见。普通操作员会看到锁定信息,并必须联系经理。

模块在移动的特定**源位置**(例如 WH/Stock)检查 `qty_available`,而不是全局在手数量。当移动的计量单位(UoM)与产品的基本 UoM 不同时,会自动应用计量单位换算。

不会。该模块只拦截 `mrp.production` 上的 `button_mark_done()`。所有其他工作流程(欠单创建、立即调拨向导、工单、MPS)均不受影响。卸载时会干净地移除检查,不留任何数据。

可以 —— 模式作为系统参数存储。前往 **制造 → 配置 → 设置 → 物料不足行为**,随时更改下拉选项。更改将在下一张生产订单上立即生效。

不会有额外操作。模块立即退出,Odoo 的标准生产验证照常进行 —— 无弹窗,无延迟。

#### 支持

- [邮件支持: **nextstep.vina@gmail.com**](mailto:nextstep.vina@gmail.com)
- **响应时间:** 我们力求在 1-2 个工作日内回复。请附上您的 Odoo 版本和问题描述。
- **许可证:** LGPL-3 —— 可自由使用、修改和再分发。

| **可用性** | Odoo Online  Odoo.sh  本地部署 |
| --- | --- |
| **Odoo 应用依赖** | • 制造(mrp)   • 库存(stock)   • 讨论(mail) |
| **代码行数** | 163 |
| **技术名称** | `                         mrp_material_check` |
| **许可证** | LGPL-3 |
