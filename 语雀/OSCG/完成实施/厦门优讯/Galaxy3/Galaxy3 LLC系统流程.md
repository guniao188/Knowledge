---
title: "Galaxy3 LLC系统流程"
client: 厦门优讯
type: 项目文档
phase: 上线期
yuque_url: "https://www.yuque.com/xinsuixiaoyao-degek/klxky6/rciih3kndehndd58"
yuque_slug: "rciih3kndehndd58"
tags: [Odoo, 上线期, 完成实施, 客户/厦门优讯]
created_at: "2024-12-23T01:19:48.000Z"
updated_at: "2024-12-26T02:53:30.000Z"
published_at: "2024-12-26T02:53:30.000Z"
---
# Galaxy3 LLC系统流程

1、维护产品、供应商、客户信息

产品：采购、服务（选择结算方式）、订阅三种

2、维护项目产品，创建项目

3、创建销售订单:原功能需要通过选择项目产品来创建项目并关联

4、由销售订单中的可库存产品推出采购单

5、零星采购，采购订单选择项目；报销线下采购，费用报销选择分析分配

6、查看项目及费用情况


销售订单增加是否工勘通过。必填。指定工勘人员

模版：费用报销、产品、客户供应商

订阅续订通知：需要手动发送邮件或设置自动化动作

角色：销售、采购、财务、项目经理、工人


开发：

SO增加字段分类，并分类汇总total
