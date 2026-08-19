---
title: "Odoo页面默认时间及数据库时间差8小时原因调查"
source: "http://www.thinkltd.cn/forum/1/odoo8-692"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo页面默认时间及数据库时间差8小时原因调查

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo8-692>

杭州诺瓦服务器是客户自己购买的物理服务器，客户安装的操作系统。运行Odoo发现，如下图，Odoo的默认时间比实际时间多了8小时，订单保存后，查数据库时间，正常情况，数据库时间应该是UTC时间，但诺瓦的数据库时间是中国时间（比UTC多了8小时）。

![[1-odoo8-692-67fbe5d3.png]]

进一步调查发现，下述python代码，在正常服务器上，设置UTC环境变量后（os.environ['TZ'] = 'UTC'），获取的是UTC时间，但同样的代码在诺瓦服务器上允许，获取的时间却是中国时间。由此可见，应该是python或操作系统的UTC时区设置有问题。

```python
import os

from datetime import datetime
```

print(datetime.now())

os.environ['TZ'] = 'UTC'

print(datetime.now())

## 补充/答案 1

调查发现，是服务器上的UTC时区文件设置错误。时区文件查看命令： ls -l /usr/share/zoneinfo/

关于Linux的时区解说，参考这里

![[1-odoo8-692-2d693c6b.png]]

查看UTC时区文件： view /usr/share/zoneinfo/UTC，如下图，最后是 CST-8 结尾，这表示中国时间（东八区），对比正常服务器，应该是 UTC0 结尾。

![[1-odoo8-692-fd304358.png]]

从正常服务器上，拷贝正确的UCT（UTC 软链接到 UCT 文件），替换诺瓦服务器的UCT时区文件，重启Odoo，时间恢复正常。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
