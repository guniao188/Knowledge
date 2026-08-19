---
title: "Odoo的nginx如何配置阿里云免费SSL证书"
source: "http://www.thinkltd.cn/forum/1/odoonginxssl-597"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo的nginx如何配置阿里云免费SSL证书

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoonginxssl-597>

第一步，购买阿里云免费SSL证书。购买链接：

![[1-odoonginxssl-597-364146da.png]]

![[1-odoonginxssl-597-1907aee7.png]]

第二步，设置nginx 使得可以访问 SSL 认证文件 fileauth.txt

odoo nginx配置文件中，加入如下内容

![[1-odoonginxssl-597-028783d7.png]]

下载的认证文件 fileauth.txt ，放到服务器的下述目录 ：/var/www/html/.well-known/pki-validation/fileauth.txt

如此，SSL认证服务器可以通过URL  /.well-known/pki-validation/fileauth.txt  访问到认证文件

第三步，nginx 上安装 SSL证书

SSL证书购买后，从阿里云操作台下载 .key 及 .pem 两个证书文件。nginx 配置文件所在文件夹 创建 cert 目录，并上传两个证书文件到该文件夹。如下：

root@ecs-s6-large-2-linux-20191024165225:/odoo# ls /etc/nginx/cert/
fileauth.txt  test.s1.oscg.cn.key  test.s1.oscg.cn.pem

nginx的Odoo配置文件，增加SSL证书域名的配置，本例 配置文件是 /etc/nginx/sites-available/odoo-nginx.conf ，证书域名是 test.s1.oscg.cn ，对应的配置参考如下：

```python
    server {
        listen      80;
        server_name  test.s1.oscg.cn;
        rewrite ^(.*) https://$host$1 permanent;
    }

    server {
        listen       443 ;
        server_name  test.s1.oscg.cn;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        ssl on;
        ssl_certificate cert/test.s1.oscg.cn.pem;
        ssl_certificate_key cert/test.s1.oscg.cn.key;
        ssl_session_timeout 5m;
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers on;

        location /longpolling {
            proxy_pass http://127.0.0.1:8072;
        }
        location / {
            proxy_redirect off;
            proxy_pass http://127.0.0.1:8069;
            proxy_connect_timeout  300s;
        }
```

      # log
       access_log /var/log/nginx/odoo.access.log;
       error_log /var/log/nginx/odoo.error.log;
       # common gzip
```python
       gzip_types text/css text/scss text/plain text/xml application/xml application/json application/javascript;
       gzip on;
    }
```

nginx SSL证书安装方法参考  及

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
