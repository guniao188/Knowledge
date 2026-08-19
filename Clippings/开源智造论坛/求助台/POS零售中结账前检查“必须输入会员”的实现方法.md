---
title: "POS零售中结账前检查“必须输入会员”的实现方法"
source: "http://www.thinkltd.cn/forum/1/pos-478"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# POS零售中结账前检查“必须输入会员”的实现方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/pos-478>

【业务背景】

1.  塞班零售客户有一个要求：每个零售订单必须设置客户是哪个国家的。

2.  建议方案是，每个国家设置一个Partner，如中国客户、日本客户，零售单上选择该 国家Partner。

3.  但有个问题，系统的partner不是必输字段，如何强制要求输入Parntner呢？

【问题解决】

1.  经调查，POS订单结完账，提交服务器前有一个检查订单合法性的js方法 order_is_valid，该方法中增加检查代码即可。

2.  代码文件：Odoo12\source\addons\point_of_sale\static\src\js\screens.js ，方法 order_is_valid， 增加下述代码即可实现上述检查。

```python
        if(!order.get_client()){
            this.gui.show_popup('error',{
                'title': _t('No Client Country'),
                'body':  _t('Plese set client country to your order before it can be validated'),
            });
            return false;
        }
```

![[1-pos-478-439e4161.png]]

## 补充/答案 1

实现效果截图

![[1-pos-478-4db466c9.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
