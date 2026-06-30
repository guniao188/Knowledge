---
title: Galaxy 问题反馈
client: 厦门优迅-Galaxy3
type: 问题跟踪
module: HR
status: 已完成
phase: 上线期
created: 2025-02-14
updated: 2025-02-14
yuque_url: "https://www.yuque.com/xinsuixiaoyao-degek/klxky6/movynvleqpexr44u"
tags: [HR, Odoo, 上线期, 客户/厦门优迅-Galaxy3, 已完成, 报表, 采购, 销售, 问题跟踪]
---

# Galaxy 问题反馈

1、采购的控制策略已修改，默认值已修改![image](_附件/1739503779961-7fca79f1-1788-4207-ae95-f5-9c20b163fb8b703d.png)

2、销售订单预览、打印pdf已处理。

![image](_附件/1739505789478-6f71f7cd-2d31-4539-b80e-61-f060625ef3994946.png)![image](_附件/1739505298643-2e8d03e3-5605-4d48-9104-72-e08427119bc17472.png)3、销售订单的开票策略是按交付数量开票，价格是产品或客户价格表设置的价格，此处无问题。

4、员工上面设置每个人的每小时工资。![image](_附件/1739505868943-ca4e1fe4-d789-4354-b705-25-f8931ee6b40b0683.png)

5、采购情况需要去采购订单上看，不反馈到项目上![image](_附件/1739506018432-5d9d5dba-0bc8-4c28-a114-89-8a95e492ed468143.png)

6、Bill 问题，bill会去校验有没有开，不会出现开出多金额的情况![image](_附件/1739506075914-617d90d9-38ce-4ab6-8d32-87-6be4b5f7b01fcbb7.png)

7、日报会议上已确认通过消息记录在任务右侧

![image](_附件/1739506157474-59632968-fd46-46d6-ae4c-07-62f30552881cd418.png)

8、项目

```
<t t-set="user" t-value="object" data-oe-t-inline="true"></t>
<t t-set="working_hour" t-value="user.working_hour_by_userId(user.id)" data-oe-t-inline="true"></t>

<t t-set="_today" t-value="datetime.date.today()" data-oe-t-inline="true"></t>
<t t-set="today_work" t-value="object.env['account.analytic.line'].search([
('employee_id.user_id','=',object.id),('date','=',_today),
])" data-oe-t-inline="true"></t>

<div>
    亲爱的 【<t t-out="object.name" data-oe-t-inline="true"></t>】，
</div>
<div>
    截止到【<t t-out="timezone(env.user.tz).localize(datetime.datetime.now().astimezone('UTC')).strftime('%Y-%m-%d %H:%M:%S')" data-oe-t-inline="true"></t>】 ，
    你的Timesheet填写了【<t t-out="sum(today_work.mapped('unit_amount'))" data-oe-t-inline="true"></t>】小时，
    还有【<t t-out="working_hour" data-oe-t-inline="true"></t>】小时未完成。
    </div>
<div>
    请在下班前完成今天的Timesheet填写！
</div>

<div>
    谢谢！
</div>
```

文档和gant分享需要有内部账户或做开发到外部网站。

9、销售订单确认自动创建项目：通过项目产品（原生功能 ，需要设置好项目产品的类型）

通过销售订单确认自动创建采购订单，已在产品类别上配置好补货策略，可以选择产品类别为All或每个产品维护好她的路线为MTO+采购。选择两个方法中的一个即可。建议选第一种。
