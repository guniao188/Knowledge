---
title: "纯前端微信小程序和odoo后端合作方案调查 示例是18版本"
source: "http://www.thinkltd.cn/forum/1/odoo-18-4103"
forum: "求助台"
author: "葛忠彪"
published: 2026-03-30
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 纯前端微信小程序和odoo后端合作方案调查 示例是18版本

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:葛忠彪 | 2026-03-30
> <http://www.thinkltd.cn/forum/1/odoo-18-4103>

一、登录认证

由于纯前端无法直接获取用户手机号，因此需要前端向微信请求code，传给后端，后端再用此code向微信请求获取用户openid，借由此openid判断当前用户在后端程序是是哪个用户

结合odoo的登录机制，把session传给前端，后续前端把session传进rpc接口里，系统即知道是哪位用户在实际操作，附件是代码示例

/

二、调取OdooRPC接口

要重写一个新方法，如下示例

注：另起模块老是报错，直接放进源码addons/web/controllers/[dataset](https://dataset.py).py是可以运行的

```python
        @http.route(['/wx/web/dataset/call_kw', '/wx/web/dataset/call_kw/'], type='json', auth="user", readonly=_call_kw_readonly)
        def wx_call_kw(self, model, method, args, kwargs, path=None):
            Model = request.env[model]

            get_public_method(Model, method)        return call_kw(request.env[model], method, args, kwargs)
```

前端传参如下示例

header: {
```python
                                                'content-type': 'application/json',
                                                'Cookie': 'session_id=' + wx.getStorageSync('session_key'),  // todo
                                                'X-Content-Type-Options': "nosniff"
                                        },
```


## 附件

- [[附件/forum/1-odoo-18-4103-controllers.py|controllers.py]] (8 KB)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
