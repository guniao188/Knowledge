---
title: "如何在Form xml视图中根据字段进行横幅提醒标语设置以及如何配置状态颜色标签显示"
source: "http://www.thinkltd.cn/forum/1/form-xml-908"
forum: "求助台"
author: "杨浔波"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 如何在Form xml视图中根据字段进行横幅提醒标语设置以及如何配置状态颜色标签显示

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:杨浔波 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/form-xml-908>

这里以客户档案的是否是今天的生日为例：

在标签下放入以下代码：

        [x](#)

```python
            Today is Birthday!

        Wish
```

![[1-form-xml-908-dde2de67.png]]

## 补充/答案 1

高雅：
我想在单据上，把每个状态（确认，取消）都用这种方式展现，背景颜色可以不一样。
这个有什么快捷的写法吗

![[1-form-xml-908-91f24e4d.png]]

葛忠标答：

bg_color="bg-danger" 表示红色

![[1-form-xml-908-756ea2c4.png]]

 bg_color="bg-success" 这个表示绿色。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
