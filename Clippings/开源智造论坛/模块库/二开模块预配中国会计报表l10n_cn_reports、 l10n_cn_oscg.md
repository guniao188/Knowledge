---
title: "二开模块预配中国会计报表l10n_cn_reports、 l10n_cn_oscg"
source: "http://www.thinkltd.cn/forum/2/l10n-cn-reports-l10n-cn-oscg-2486"
forum: "模块库"
author: "肖相扶"
published: 2024-10-23
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开模块预配中国会计报表l10n_cn_reports、 l10n_cn_oscg

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-10-23
> <http://www.thinkltd.cn/forum/2/l10n-cn-reports-l10n-cn-oscg-2486>

1.  【20241011】此二模块升级到了Odoo18.0，下载链接：OSCG_Git\18.0\extra-addons\l10n_cn_oscg、OSCG_Git\18.0\extra-addons\l10n_cn_reports

2.  【20231206】此二模块升级到了Odoo 17.0，下载链接：[https://gitlab.com/oscg-china/extra-addons/-/tree/17.0](https://gitlab%5C.com/oscg%5C-china/extra%5C-addons/%5C-/tree/17%5C.0)

3.  【20240116】Bug修正：

4.  1.  现金流量表报错的问题修正
    2.  会计科目表选择的下拉框中，不出现开源智造科目表的问题修正

5.  Odoo16的会计科目及报表模块说明，参考：[Odoo16的三大会计报表改善l10n_cn_reports](http://www.thinkltd.cn/forum/2/question/odoo16l10n%5C-cn%5C-reports%5C-3586)

6.  模块存放位置
    15\\0版本：OSCG_SVN\odoo_ecommerce\15\\0SRC\存货核算\\\\ \\\\ \**15\\0新增了功能**：自动在会计科目上添加现金流量表标签

7.  15\\0版本，现金流量表诊断SQL：[Odoo15中现金流量表诊断SQL](http://www.thinkltd.cn/forum/1/question/odoo15sql%5C-918)

8.  Odoo系统，现金流量表的编制原理参见这里\[Odoo13现金流量表原理解析](http://www.thinkltd.cn/forum/1/question/odoo13%5C-435)

9.  14.0版本有新加一个新版本（依据申能标准的会计科目清单，code统一位数及会计报表按新科目代码调配，并自动有绑定好现金流量表的标签，以及科目有在模块在进行了群组分配）SVN\odoo_ecommerce\14.0SRC\存货核算\科目代码格式标准化（***如果要用新版本，请大家多收点工时，费了不少力气来把数据归整统一）
```python
    14.0版本位置：OSCG_SVN\odoo_ecommerce\14.0SRC\存货核算\l10n_cn_reports

    12.0版本位置：OSCG_SVN\odoo_ecommerce\12.0SRC\l10n_cn_reports
```

10. 本模块依赖中国会计科目模块 l10n_cn_oscg

11.  新增会计凭证打印功能；

12.  新增中国资格式的产负债表、利润表、现金流量表

13.  （需要启用分析会计功能）增加现金流量表标签(字段 analytic_tag_ids )，会计分录录入时候，分录标签上，手工标记现金流量相关标记，如此，系统会自动归集现金流量表。

14.  本模块依赖模块 account_reports， 社区版应用时候，可以拷贝account_reports 到社区版再安装。

## 补充/答案 1

模块 l10n_cn_oscg 新增下述默认设置功能：

    # 2. 修改中文时间显示格式为%Y/%m/%d %H:%M:%S
    # 3. Partner国家默认为中国，语言默认为中文
    # 4. Price小数位数默认设置为4位，数量小数位数默认设置为2位
    # 5. 人民币汇率默认设置为1.0 ，美元默认为6.9，欧元为 7.8. 汇率转换小数默认设置为4位

2020/3/9 l10n_cn_reports改写了现金流量表的实现方法：

1.  原来的现金流量表通过配置而成，系统取数逻辑是：1) 含有现金、银行类科目的分录明细上，手工标记现金流量标签，如

2.   “销售产成品、商品、提供劳务收到的现金”；2) 报表取数时候，自动获取相应标签的分录金额到现金流量表。

3.  存在的问题是，例如收到客户货款100元，其中应交税费 10元，在现金流量表上，100元应该拆成90元 和 10元，分别进入不同项目：90元进入“销售产成品、商品、提供劳务收到的现金”，10元进入“支付的税费”

4.  新的现金流量表基于Odoo13现金流量表的逻辑，参考现金科目对方分录（应收、应付），查找对应的核销分录的对方科目，根据该科目上设置的现金流量标签，归集其金额。取数逻辑参考：[/forum/1/question/odoo13-435](http://www.thinkltd.cn/forum/1/question/odoo13-435)

5.  具体实现技术是，继承Odoo13的现金流量表实现方法。代码文件 enterprise\account_reports\models\account_cash_flow_report.py  覆盖继承方法 def _get_lines( )  ，按中国会计的现金流量表取数实现。

【操作截图】

![[2-l10n-cn-reports-l10n-cn-oscg-2486-2e493a80.png]]

会计科目上标记“现金流量标签”

![[2-l10n-cn-reports-l10n-cn-oscg-2486-fa86d2bd.png]]

## 补充/答案 2

这个模块依赖企业版的account_reports模块，account_reports模块安装需要“会计”模块（account_accountant）升级到企业版。最新的13代码会计模块好像做了修改，不再依赖于任何模块，导致无法升级到企业版。所以我们的三大报表现在无法安装，包括企业版会计模块的那些功能，现在都没办法给客户安装。

![[2-l10n-cn-reports-l10n-cn-oscg-2486-776d82b8.png]]

## 补充/答案 3

依赖关系（下面几个模块一并挪移到社区版），另外参考这里添加变量 [/forum/1/question/odoo13error-undefined-variable-o-chatter-min-width-464](http://www.thinkltd.cn/forum/1/question/odoo13error-undefined-variable-o-chatter-min-width-464)

1.  account_reports

2.  account_accountant

3.  mail_enterprise

4.  web_mobile

## 补充/答案 4

V15的版本下载下来还是没有现金流量表的标签。

科目的代码方式统一有调整过的版本存放目录：

D:\svn\SVN\odoo_ecommerce\06.Customization\谱源\v15addons\oscgaddons\l10n_cn_oscg

另外一个问题，这个模块中自带的会计赁证的打印，**默认无法批量勾选在列表上打印多个**，解决方案是界面上调配增加参数设置：

![[2-l10n-cn-reports-l10n-cn-oscg-2486-64d8e8c3.png]]

![[2-l10n-cn-reports-l10n-cn-oscg-2486-1c16806c.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
