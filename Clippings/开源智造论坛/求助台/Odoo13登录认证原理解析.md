---
title: "Odoo13登录认证原理解析"
source: "http://www.thinkltd.cn/forum/1/odoo13-609"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo13登录认证原理解析

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo13-609>

【业务背景】

1.  当用Vue或微信小程序开发前台，Odoo作为后台 时候，前台需要用自己的方式登录Odoo，并调用Odoo的方法获取数据。

2.  为了解决此问题，需要理解Odoo的登录认证机制。

【Odoo登录认证机制】

1.  GET方法获取Odoo指定数据库的登录页面/web?db=db_name，此时，Odoo会返回 csrf_token 变量。下次向Odoo提交请求时候，要求带上此 csrf_token，否则Odoo会报非法的csrf_token 。

2.  每次向Odoo发起http请求，Odoo都会返回新的 csrf_token， 下一次向Odoo发起请求时候，必须带上最新的（上一次的）csrf_token

3.  向 /web/login POST用户名、密码，登录Odoo，获取session，同时获得新的 csrf_token

4.  带上session，csrf_token 调用Odoo方法，获取数据。本例以 /web/binary/upload_attachment 为例，向Odoo指定的表单上传一个文件作为附件。

【示例代码】py 程序

# -*- coding: utf-8 -*-
```python
import xmlrpc.client
import requests
import re
```

url = "http://127.0.0.1:8089"
db = "O13_Test91"
username = 'admin'
password = "123"
odoo_session = requests.Session()
```python
odoo_csrf_token = ''
odoo_session_id = ''

def odoo_login():
    global odoo_csrf_token, odoo_session_id
```

    # 1) 获取Odoo登录页面(关键是获取 csrf_token)
```python
    url_db = "%s/web?db=%s" % (url,db)
    res = odoo_session.get(url_db)
    matchObj = re.match(r'.*csrf_token: "([^"]+)".*', res.text, re.S)
    if matchObj:
        odoo_csrf_token = matchObj.group(1)
        print("csrf_token1: %s" % odoo_csrf_token)
```

    #登录Odoo，获取session及新的 csrf_token
```python
    url_login = "%s/web/login" % url
    login_data={
                'csrf_token': odoo_csrf_token,
                'db': db,
                'login': username,
                'password': password,
            }
    res = odoo_session.post(url_login, login_data)
    cookie = res.headers["Set-Cookie"]
    matchObj = re.match(r'.*session_id=([^;]+);.*', cookie, re.S)
    if matchObj:
        odoo_session_id = matchObj.group(1)
        print("session_id: %s" % odoo_session_id)

    matchObj = re.match(r'.*csrf_token: "([^"]+)".*', res.text, re.S)
    if matchObj:
        odoo_csrf_token = "%s" % matchObj.group(1)
    print("csrf_token2: %s" % odoo_csrf_token)

def odoo_call():
```

    #调用Odoo方法：文件上传测试
```python
    upload_data={
                'callback': '',
                'model': 'stock.picking',
                'id': 10,
                'csrf_token': odoo_csrf_token,
            }
    url_upload = "%s/web/binary/upload_attachment" % url
    cookies = {'session_id': odoo_session_id}
    upload_files = {'ufile': open('F:/Odoo13/test/whou00001.png', 'rb')}
    res = odoo_session.post(url_upload, upload_data, files=upload_files, cookies=cookies)
    print(res.text)

if __name__ == "__main__":
    odoo_login()
    odoo_call()
```

## 补充/答案 1

【python通过网络接口登录odoo及调用json-rpc完整示例】

# -*- coding: utf-8 -*-

```python
import xmlrpc.client

import requests

import re

import json
```

url = "http://127.0.0.1:8469"

db = "O14_Ent01"

username = 'admin'

password = "123"

uid = None

cid = None

cids = []

odoo_session = requests.Session()

```python
odoo_csrf_token = ''

odoo_session_id = ''

def odoo_login():

    global odoo_csrf_token, odoo_session_id, uid, cid, cids

    url_db = "%s/web/login?db=%s" % (url, db)

    res = odoo_session.get(url_db)

    matchObj = re.match(r'.*csrf_token: "([^"]+)".*', res.text, re.S)

    if matchObj:

        odoo_csrf_token = matchObj.group(1)

        print("csrf_token1: %s" % odoo_csrf_token)

    cookie = res.headers["Set-Cookie"]

    matchObj = re.match(r'.*session_id=([^;]+);.*', cookie, re.S)

    if matchObj:

        odoo_session_id = matchObj.group(1)

        print("session_id: %s" % odoo_session_id)

    url_auth = "%s/web/session/authenticate" % url

    login_data = {

        'jsonrpc': '2.0',

        'id': 499807971,

        'csrf_token': odoo_csrf_token,

        'method': 'call',

        'params': {'db': db, 'login': username, 'password': password}

    }

    headers = {

        'Content-Type': 'application/json'

    }

    cookies = {

        'session_id': odoo_session_id

    }

    data_json = json.dumps(login_data)

    res = odoo_session.post(url=url_auth, data=bytes(data_json, 'utf-8'), headers=headers )  #, cookies=cookies

    res_json = json.loads(res.text)

    uid = res_json["result"]["uid"]

    cid = res_json["result"]["company_id"]

    cids = [x[0] for x in res_json["result"]["user_companies"]["allowed_companies"] ]

    print("Company ID = %s, User ID = %s" % (cid, uid))

def odoo_call():

    global odoo_csrf_token, uid, cid, cids

    url_call = "%s/web/dataset/call_kw/%s/%s" % (url, "res.partner", "search")

    call_data = {

        'jsonrpc': '2.0',

        'id': 496807891,

        'method': 'call',

        'params': {'model': 'res.partner', 'method': 'search', "args": [[]], "kwargs": {'context': {'lang': 'zh_CN', 'tz': 'Asia/Shanghai', 'uid': uid, 'allowed_company_ids': cids}}}

    }

    headers = {

        'Content-Type': 'application/json'

    }

    data_json = json.dumps(call_data)

    res = odoo_session.post(url=url_call, data=bytes(data_json, 'utf-8'), headers=headers )  #, cookies=cookies

    print(res.text)
```

    #res_json = json.loads(res.text)

```python
if __name__ == "__main__":

    odoo_login()

    odoo_call()
```

【VBA程序登录Odoo并调用json-rpc示例】

VBA request, json操作学习资料：[https://codingislove.com/http-requests-excel-vba/ ](https://codingislove.com/http-requests-excel-vba/)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
