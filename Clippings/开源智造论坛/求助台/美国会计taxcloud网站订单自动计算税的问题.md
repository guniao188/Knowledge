---
title: "美国会计taxcloud网站订单自动计算税的问题"
source: "http://www.thinkltd.cn/forum/1/taxcloud-879"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 美国会计taxcloud网站订单自动计算税的问题

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/taxcloud-879>

如果客户实施部署美国会计，就会有不同州有不同税率的问题，就会用到系统会计里的taxcloud的功能。

对于不同州的客户订单，SO上体现不同的收货地址的税率，而且自动带上【税科目调整】的Taxcloud的值

主要涉及的配置要点：（前提条件用了美国的会计，即company所在的国家是美国

美国taxcloud的API接口及规范详见链接：****

1、会计/配置/设置菜单下，打开taxcloud功能，并配置好KEY，并刷新

![[1-taxcloud-879-561a11cd.png]]

2、在【税科目调整】记录中会生成一条云税的记录：

![[1-taxcloud-879-a4329f21.png]]

![[1-taxcloud-879-88847a31.png]]

这条记录不可以删除。

3、还需要将相应的销售产品上绑定好taxcloud的归属于产品tax类别：

![[1-taxcloud-879-eff14162.png]]

4、设置好之后，KEY这些完成后，后台一定记得重启一下odoo进程，以避免不生效的问题。

5、后台手动下订单：

![[1-taxcloud-879-2bff2468.png]]

![[1-taxcloud-879-dc1549ef.png]]

5、WEB网站shop里下订单，提交的订单也会依据客户的地址来自动判断带上税率

![[1-taxcloud-879-8898f375.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
