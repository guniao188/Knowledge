---
title: "打印报表报错 ModuleNotFoundError: No module named &#39;_rl_renderPM&#39;"
source: "http://www.thinkltd.cn/forum/1/modulenotfounderror-no-module-named-rl-renderpm-4051"
forum: "求助台"
author: "周鸿飞"
published: 2025-06-27
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 打印报表报错 ModuleNotFoundError: No module named &#39;_rl_renderPM&#39;

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:周鸿飞 | 2025-06-27
> <http://www.thinkltd.cn/forum/1/modulenotfounderror-no-module-named-rl-renderpm-4051>

错误的详情：Odoo服务器错误

RPC_ERROR
Odoo Server Error

Occured on 60.190.211.154:8069 on 2025-06-25 03:29:12 GMT

Traceback (most recent call last):
File "/opt/odoo/odoo18/odoo18-venv/lib/python3.12/site-packages/reportlab/graphics/[renderPM.py",](https://renderpm.py) line 43, in _getPMBackend
import rlPyCairo as M
ModuleNotFoundError: No module named 'rlPyCairo'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File "/opt/odoo/odoo18/odoo18-venv/lib/python3.12/site-packages/reportlab/graphics/[renderPM.py",](https://renderpm.py) line 46, in _getPMBackend
import _rl_renderPM as M
ModuleNotFoundError: No module named '_rl_renderPM'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File "", line 1523, in template_1014
File "", line 1505, in template_1014_content
File "", line 1487, in template_1014_t_call_0
File "", line 260, in template_1014_t_call_1
File "/opt/odoo/odoo18/odoo-server/odoo/addons/base/models/[ir_qweb.py",](https://ir_qweb.py) line 2452, in _get_field

解决办法1：将Python版本3.12降级为3.11或者3.10 解决率100%

解决办法2:

```python
    sudo apt update
    sudo apt install -y libcairo2-dev libfreetype6-dev libjpeg-dev libpng-dev libtiff-dev libopenjp2-7-dev python3-dev pkg-config
    在安装python依赖
    pip install pycairo
    pip install  rlpycairo
    pip uninstall reportlab -y
    pip install --no-binary :all: reportlab
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
