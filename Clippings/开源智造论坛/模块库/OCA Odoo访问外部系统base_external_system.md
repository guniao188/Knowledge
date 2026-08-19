---
title: "OCA Odoo访问外部系统base_external_system"
source: "http://www.thinkltd.cn/forum/2/oca-odoobase-external-system-2758"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA Odoo访问外部系统base_external_system

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-odoobase-external-system-2758>

模块链接：

12.0版本：

例如，调用短信接口发短信，调用淘宝店铺抓单，等场景，都可以用此模块封装外部系统（更好地管理外部系统IP、端口、用户名、密码等）。

This module provides an interface/adapter mechanism for the definition of remote systems.

Note that this module stores everything in plain text. In the interest of security, it is recommended you use another module (such as keychain or red_october to encrypt things like the password and private key). This is not done here in order to not force a specific security method.

###

### Implementation

The credentials for systems are stored in the `external.system` model, and are to be configured by the user. This model is the unified interface for the underlying adapters.

####

#### Using the Interface

Given an `external.system` singleton called `external_system`, you would do the following to get the underlying system client:

    with external_system.client() as client:
        client.do_something()

The client will be destroyed once the context has completed. Destruction takes place in the adapter's `external_destroy_client` method.

The only unified aspect of this interface is the client connection itself. Other more opinionated interface/adapter mechanisms can be implemented in other modules, such as the file system interface in [OCA/server-tools/external_file_location](https://github.com/OCA/server-tools/tree/9.0/external_file_location).

####

#### Creating an Adapter

Modules looking to add an external system adapter should inherit the `external.system.adapter` model and override the following methods:

- `external_get_client`: Returns a usable client for the system
- `external_destroy_client`: Destroy the connection, if applicable. Does not need to be defined if the connection destroys itself.

###

### Configuration

Configure external systems in Settings => Technical => External Systems

## 补充/答案 1

下图是一个ssh远程登录别的系统，执行命令的配置信息及 adapter 实现代码:  点击“Test Connection”按钮，执行 ssh登录远程服务器，执行  echo hello!  命令，并将执行结果输出到 fingerprint 字段 。

```python
import paramiko
from odoo import api, models

class ExternalSystemSSH(models.Model):
    """
    """

    _name = 'external.system.ssh'
    _inherit = 'external.system.adapter'
    _description = 'External System SSH'

    @api.multi
    def external_get_client(self):
        """
        """
        super(ExternalSystemSSH, self).external_get_client()
        host = self.system_id.host
        port = self.system_id.port
        username = self.system_id.username
        password = self.system_id.password
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host,port,username,password,timeout=10)

        return ssh

    @api.multi
    def external_destroy_client(self, client):
        """
        """
        super(ExternalSystemSSH, self).external_destroy_client(client)
        client.close()

    @api.multi
    def external_test_connection(self):
        """
        """
        client = self.external_get_client()
        cmd = ['echo hello!']
        for m in cmd:
            stdin, stdout, stderr = client.exec_command(m)
```

            #stdin.write("Y")   #简单交互，输入 ‘Y’
            out = stdout.readlines()
            #屏幕输出
```python
            if not self.fingerprint:
                self.fingerprint = "%s" % out
            else:
                self.fingerprint += "%s" % out

        self.external_destroy_client(client)
```


## 原帖外链配图

![[2-oca-odoobase-external-system-2758-x194038c2.png]]
<small>原始地址: /web/image/1243/snipaste_20190130_151720.png?access_token=ea82b6d5-0844-4a1c-964a-6cdcc0137ce4</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
