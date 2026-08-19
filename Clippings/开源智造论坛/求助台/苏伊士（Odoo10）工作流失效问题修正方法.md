---
title: "苏伊士（Odoo10）工作流失效问题修正方法"
source: "http://www.thinkltd.cn/forum/1/odoo10-3897"
forum: "求助台"
author: "肖相扶"
published: 2024-03-11
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 苏伊士（Odoo10）工作流失效问题修正方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-03-11
> <http://www.thinkltd.cn/forum/1/odoo10-3897>

【工作流机制】

1.  工作流相关数据库表 wkf, wkf_activity, wkf_instance, wkf_workitem。
2.  1.  wkf: 工作流表
```python
    2.  wkf_activity: 工作流节点表
    3.  wkf_instance：工作流实例表
    4.  wkf_workitem：工作流实例当前执行节点表，一个工作流实例只有一个当前执行节点
```

3.  单据（如sale.contract）上点击按钮，系统触发 odoo\workflow\service.py 方法 def validate 。该方法查找 state='active' 工作流实例
4.  执行 odoo\workflow\instance.py 的方法 def validate 。该方法查找 instance对应的当前执行节点workitem
5.  执行节点执行activity上定义的函数，参见odoo\workflow\workitem.py 的方法 def _execute的代码行 returned_action = self.wkf_expr_execute(activity)
6.  单据工作流失效，常见原因是，该单据的工作流实例的state不是 'active' ，因而导致系统找不到有效工作流实例。对应的，该工作流实例的当前执行节点也不存在。
7.  纠正办法是，查找到该单据的工作流实例，将其状态修改成 'active' ，同时在 wkf_workitem中增加一个当前执行节点记录（如第一个节点），同时修改单据状态（和当前执行节点对应的状态）。

【诊断代码】

1.  查找单据对应的工作流id：select id from wkf where osv='sale. contract' and on_create=True
2.  查找工作流的节点：select id, name from wkf_activity where wkf_id=2
3.  查找单据对应的工作流实例：sql = "select * from wkf_instance where wkf_id=2 and res_type='sale.contract' and res_id=7672" #异常单
4.  查找单据对应的工作流实例的当前执行节点：select wi.id, wi.act_id, wi.state, wa.name from wkf_workitem wi left join wkf_activity wa on (wi.act_id = wa.id) where inst_id=1264744
5.  odoo xml rpc诊断参考代码如下：

```python
    import xmlrpc.client

    url = 'http://v10-release.scipsita.com'
    db = 'stable_new'
    username = 'admin'
    password = 'Q#foca2VSh'

    common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
```

    #print(common.version() )
```python
    uid = common.authenticate(db, username, password, {})
    api = xmlrpc.client.ServerProxy('%s/xmlrpc/2/object' % url)

    sql = "select id from wkf where osv='sale. contract' and on_create=True"
```

    #sql="select id, name from wkf_activity where wkf_id=2"
    #sql = "select * from wkf_instance where wkf_id=2 and res_type='sale.contract' and res_id=7672" #异常单
    #[{'res_type': 'sale.contract', 'uid': 188, 'wkf_id': 2, 'state': 'complete', 'res_id': 7672, 'id': 1264744}]
    #sql="select wi.id, wi.act_id, wi.state, wa.name from wkf_workitem wi left join wkf_activity wa on (wi.act_id = wa.id) where inst_id=1264744"
    #[]

    #纠正SQL
    #sql1="update wkf_instance set state='active' where id=1264744"
    #sql="select nextval('wkf_workitem_id_seq')"
    #sql2="insert into wkf_workitem (id,act_id,inst_id,state) values (%s,%s,%s,'active')" % (4187523, 11, 1264744)
    #sql3="update sale_contract set state='draft' where id=7672"
    res_sess = api.execute_kw(db, uid, password, 'sync.wac.wms.record', 'sql_execute', [sql])

【纠正代码】服务器动作中执行

1.  工作流实例的状态更新为active：sql1="update wkf_instance set state='active' where id=1264744"
2.  插入工作流实例当前执行节点：#sql="select nextval('wkf_workitem_id_seq')"，#sql2="insert into wkf_workitem (id,act_id,inst_id,state) values (%s,%s,%s,'active')" % (4187523, 11, 1264744)
3.  更新单据状态到当前执行节点对应的状态：#sql3="update sale_contract set state='draft' where id=7672"

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
