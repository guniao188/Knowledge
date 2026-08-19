---
title: "无法正常启动Odoo15的服务，报resource.setrlimit(rlimit, (config[&#39;limit_memory_hard&#39;], hard)) 错误，如何处理。"
source: "http://www.thinkltd.cn/forum/1/odoo15-resource-setrlimit-rlimit-config-limit-memory-hard-hard-820"
forum: "求助台"
author: "杨浔波"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 无法正常启动Odoo15的服务，报resource.setrlimit(rlimit, (config[&#39;limit_memory_hard&#39;], hard)) 错误，如何处理。

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:杨浔波 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo15-resource-setrlimit-rlimit-config-limit-memory-hard-hard-820>

在新的macos12.0.1版本中，因为Python内存调用机制版本出了问题，所以和Odoo Server.py文件中的内存调用代码有冲突

```python
    def set_limit_memory_hard():
        if os.name == 'posix' and config['limit_memory_hard']:
            rlimit = resource.RLIMIT_RSS if platform.system() == 'Darwin' else resource.RLIMIT_AS
            soft, hard = resource.getrlimit(rlimit)
            resource.setrlimit(rlimit, (config['limit_memory_hard'], hard))
```

可通过修改源代码解决该问题。但建议不要去修改，怕影响内存优化的问题。问题复现报错如下：

Traceback (most recent call last): File "/Users/odoo/Documents/odoo15/odoo-bin", line 8, in  odoo.cli.main() File "/Users/odoo/Documents/odoo15/odoo/cli/command.py", line 61, in main o.run(args) File "/Users/odoo/Documents/odoo15/odoo/cli/server.py", line 176, in run main(args) File "/Users/odoo/Documents/odoo15/odoo/cli/server.py", line 170, in main rc = odoo.service.server.start(preload=preload, stop=stop) File "/Users/odoo/Documents/odoo15/odoo/service/server.py", line 1342, in start rc = server.run(preload, stop) File "/Users/odoo/Documents/odoo15/odoo/service/server.py", line 547, in run self.start(stop=stop) File "/Users/odoo/Documents/odoo15/odoo/service/server.py", line 487, in start set_limit_memory_hard() File "/Users/odoo/Documents/odoo15/odoo/service/server.py", line 83, in set_limit_memory_hard resource.setrlimit(rlimit, (config['limit_memory_hard'], hard)) ValueError: current limit exceeds maximum limit

上述问题，不排除未来Linux内核改进后尤其是兼容Python3.8之前版本是否会存在类似问题。

解决方案：在odoo-bin启动参数后增加配置参数 --limit-memory-hard 0

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
