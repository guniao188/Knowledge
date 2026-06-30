---
title: RMA更新invoice中lot操作流程及测试报告
client: Dukers
type: 测试
module: 财务
status: 已完成
phase: 上线期
created: 2024-08-14
updated: 2024-08-14
yuque_url: "https://www.yuque.com/xinsuixiaoyao-degek/klxky6/zqezmpdi3g1iia31"
tags: [Odoo, 上线期, 客户/Dukers, 已完成, 测试, 财务, 采购, 销售]
---

# RMA更新invoice中lot操作流程及测试报告

操作流程：先确认退货单，再确认重发货单。

![image](_附件/1723623223126-105e4d27-0827-4e93-bfff-15-3016b06cc6a15151.png)

情况一、重发货前未创建invoice，invoice中直接使用最新的发货单上的lot

![image](_附件/1723623367090-eb11ad26-6a25-4122-a589-04-8dcfccef87cb6d49.png)![image](_附件/1723623435783-fbc98e49-8e79-4632-8870-6a-fb945ff95c9073ed.png)![image](_附件/1723623456900-3488e308-6ebe-4000-9b4c-40-ea610d7d87f5b98c.png)![image](_附件/1723623486279-62c684b3-3619-4434-9ab3-1f-63def837fffa3a7d.png)![image](_附件/1723623552070-a69ebb59-d4ce-41a9-946f-74-83ad2b5ee936be23.png)![image](_附件/1723624278125-895a6d22-ff0f-4381-ac27-9a-fe14310ca415573a.png)

情况二、重发货前创建了invoice，invoice中对应的lot需要进行变更，根据重发货上的lot进行显示

![image](_附件/1723624517810-ed4300f7-1711-47e2-9178-bc-11564e1d8d4cb507.png)![image](_附件/1723624530272-1901b1c9-e6e9-4d81-a0f2-4d-4e71b09aa599b316.png)![image](_附件/1723624580757-80941796-eac0-4513-86b0-75-f7661bc2d50f54e2.png)![image](_附件/1723624610409-8dcde1b7-8171-4958-b04e-d2-7d024cd7c48b4664.png)![image](_附件/1723624681331-86e264bb-a54c-4e4a-88b5-6b-3f19faa8ae2d74d1.png)

情况三、有退货退款的情况，需要创建红冲发票的流程用odoo原生的return发货单及创建退款单的红冲发票。![image](_附件/1723622827249-077a0f68-2db4-40cd-92d1-9c-36089257ff0db2ed.png)![image](_附件/1723625228331-fb4ee23e-b81d-42de-9381-a5-d899ff5180d77f1f.png)
