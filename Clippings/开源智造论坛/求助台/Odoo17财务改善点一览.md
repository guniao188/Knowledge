---
title: "Odoo17财务改善点一览"
source: "http://www.thinkltd.cn/forum/1/odoo17-3811"
forum: "求助台"
author: "肖相扶"
published: 2024-04-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17财务改善点一览

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-04-10
> <http://www.thinkltd.cn/forum/1/odoo17-3811>

返回  [Odoo17改善点列表](http://www.thinkltd.cn/forum/1/odoo17-3808)

1.  会计报表
    会计报表的配置更容易：拖动会计报表行上下移动或缩进缩出

![[1-odoo17-3811-35610be9.png]]

2.  发票Invoice上的折扣金额会计科目
    可以设定会计科目，用于核算发票Invoice上的折扣金额。发票上的折扣和SO销售订单上的折扣是独立的，没有关联关系。如果不设置折扣金额科目，则不产生折扣会计分录。

![[1-odoo17-3811-c07dd766.png]]

3.  固定资产改善
    增加了选择多个固定资产批量折旧的功能；固定资产导入时候，状态字段不可导入（导入后总是草稿状态）。
4.  自动解析时候只解析PDF附件
    接收邮件自动创建客户发票或供应商账单时候，优先自动解析PDF附件，获取发票资料。注：Odoo的邮件别名中，可以设定客户发票和供应商账单的邮箱，收到邮件后自动创建发票。
5.  自动核销功能改善
    自动核销的Wizard窗口重新设计了，更易于操作。
6.  Avalara地理位置和销项税
    通过 Avalara 地址接口校验Parnter的地址信息，校验后的地址信息可以用于销售税计算。 Avalara地址接口参考  [Address Validation | Avalara Developer](https://developer.avalara.com/avatax/address-validation/)
7.  AvaTax接口：使用销售发货的源仓库地址计算税额
    通过AvaTax接口计算销售发票税额时候，如果该销售发票关联了销售订单和销售发货单，用销售发货单的源仓库的地址计算税额。
8.  银行流水核销界面改善
    银行流水核销新界面更清晰。可以编辑、删除、打印银行对账单，在Journal Item视图上，还增加了审计记录。
9.  Bank statement PDF report layout
    The layout of the bank statement PDF report has been cleaned up.
10. 供应商账单AI功能更强了
    供应商账单自动识别时候，税和会计科目默认开启自动识别功能，产品自动识别功能可以在配置中设定是否启用。
11. 分支机构管理
    基于多公司结构，增加了分支机构管理功能。即公司下属的子公司的管理。目前尚无矩阵式管理的事业部功能。
12. 退票/红字发票功能简化
    Simplified the invoice action buttons. Debit notes was moved to the action menu.
13. Cross analytic
    Input on multiple analytic plans to do analytic cross-reporting.
14. 信用额度改善
    已确认但未开票的销售订单SO，纳入了Partner的应收账款计算范围，Partner信用额度超限报警时候，也按此新计算逻辑报警。
15. 财务报告中增加递延收益/费用报告
    The Deferred Expense/Revenue report allows auditing any amount. The audit can differ from the reported amount, as those are theoretical computations. Any difference means there is a manual entry to generate.
16. 递延管理
    递延管理完全脱离了资产模型的设置，直接在Invoice上产生递延凭证，不再需要预先设置递延模型。递延收益、递延费用详细用法参  [递延资产、待摊费用、递延收益等的处理方法](http://www.thinkltd.cn/forum/1/3818)
17. 发货日期
    Invoices（发票）上增加了发货日期字段，销售单上按钮“创建发票”时候，自动将发货日期带入发票的发货日期字段。
18. Down payment and POS
    The breakdown of taxes and accounts on down payment invoices remains consistent, irrespective of whether the invoice is initiated through the PoS or the Sales App.
19. Down payments tax breakdown
    On down payment invoices, the tax breakdown of the original sale order is now respected.
20. 新增提前付款折扣功能
    Improved display of due dates for early payment discounts and installments.
21. EDI格式
    客户列表视图上，增加EDI format字段，以及 Peppol 相关字段。需要安装模块 account_edi_ubl_cii，account_peppol 。peppol是欧洲的一个电子发票交换平台，参考资料 [https://peppol.com/blog/what-is-peppol/](https://peppol.com/blog/what-is-peppol/) 

![[1-odoo17-3811-d8bd95a3.png]]

22. 费用报销单上增加了日记账Journal字段
    费用报销单上增加了journal_id日记账字段；费用报销明细上传的附件，自动添加到费用报销的会计凭证。此附件也会自动导出到DateV（DateV是德国的一个税务、法务等服务软件平台，Odoo数据导出到DateV是德国本地化模块中的功能）。
23. Express VAT in local currency on invoices
    Tax computation appears in local currency on customer invoices made in foreign currency to comply with the 2010/45/EU directive.
24. Filter blank lines
    Added option to filter out lines at zero from fiscal reports.
25. Fleet: impact vehicle without a bill
    For Fleet and Accounting users, the bank reconciliation widget now allows you to specify the vehicle concerned on any manual operation.
26. 催款报告(Follow-up reports):缺乏客户联系信息的处理
    批量产生催款报告的时候，如果某个客户缺乏联系信息，单独标示出来，剩余客户继续处理，而不是中断后续处理。
27. Improve settings for tax calculation display on invoices
    Merged Line subtotals tax display and Rounding Method in Accounting settings.
28. 会计报告的PDF打印格式优化了
    会计报表打印出来的效果做了优化
29. Inter-company transactions - Attach a copy of the invoice PDF to the vendor bill
    A copy of the invoice is now added to the bill attachment of the counterpart company in the scope of inter-company transactions.
30. 发票日期字段可见
    发票日期（ invoice date ） 字段增加到了会计分录行、会计凭证，部分会计报表也有此字段显示。
31. Invoice layout overhaul
    The invoice layout is clearer. To satisfy the legal requirements of several countries, you can display the total amount in letters.
32. Invoice upload harmonization
    Harmonized invoice uploads in both Accounting and Documents. Draft credit notes can be changed to invoices. Factur-X documents detect the move type (invoice or credit note) from the Factur-X data.
33. Partner创建时候VAT号码匹配功能改善
    合作伙伴(Partner)创建时候，可以填写Partner名称，也可以填写Partner税号(VAT号码)，系统自动匹配，即填写名称，系统自动查找VAT号码，自动填写VAT号码。填写VAT号码系统自动查找名称，自动填写名称。新版改善了名称和VAT号码匹配功能。
34. Manual reconciliation
    The manual reconciliation widget was removed. Lines are silently reconciled unless a write-off entry is required, which launches a new reconciliation wizard.
35. 批量打印下载发票
    发票列表视图中的"send and print"功能，增加了批量下载功能。老版本功能只有邮件发送和邮递两种功能，新版本增加了下载功能。多选时候，下载文件为zip，单选时候为PDF文件。
36. 发票批量发送打印功能发票头上增加了banners提示
    发票在“批量发送打印”过程中，发票头上显示Banners提示用户。
37. 重新设计了冲销号
    重新设计了应收/应付和实收/实付的冲销号/部分冲销号，冲销号带有颜色，更一目了然。

![[1-odoo17-3811-7cced97c.png]]

38. 银行日记账上增加了Miscellaneous operations功能
    Dashboard上的银行日记账看板中，增加了  Miscellaneous operations功能。 该功能列示银行类科目，但没记录在银行日记账（bank_statement）上的会计分录。原则上，银行收付流水都应该通过银行日记账记录，而不应该直接记会计分录。 

![[1-odoo17-3811-456447ac.png]]

39. 改善了OCR发票识别功能易用性
    优化了文档上传功能：上传时候自动数字化，速度提高了五倍，改善了错误提示和警告提示语句。
40. OCR:退货凭证和红字发票
    OCR自动识别Invoice功能增强：可以自动识别Credit notes (退货凭证) and refund（红字发票），并自动创建对应单据。
41. 扫码支付保护
    只有打开了Send Money开关的银行账号，才能扫码支付。

![[1-odoo17-3811-778e9792.png]]

42. 支持PEPPOL平台（欧洲的电子发票交换平台）
    PEPPOL平台上注册后，可以通过PEPPOL轻松收发客户发票、供应商账单、红字发票。
43. 支持Ponto平台
    改善了平台Ponto的支持。
44. 提高了会计报表速度
    引进了新的预分组机制，大幅提升了大数据量情况下会计报表的加载速度。
45. Report sections
    Reports can now be grouped on the user interface and in the exports.
46. 重新设计了会计报表配置功能
    彻底重写了会计报表设计界面，大幅提高了易用性。
47. 发票的“发送打印”功能，支持多种发票数据格式
    发票的“发送打印”功能，不再仅仅是PDF格式，可以是各种XML数据格式。按什么格式发送发票，可以在客户上配置。

![[1-odoo17-3811-91f07324.png]]

48. SAF-T: remove blocking errors
    Warnings are displayed on the general ledger rather than when clicking the SAF-T export button.
49. SEPA Direct Debit (pain.008.001.08)
    Added support for the pain.008.001.08 format for SEPA Direct Debit.
50. SEPA non-latin characters
    SEPA characters mapping extended to cater to all European languages.
51. Tax taxonomy
    All localizations' taxes now use codes in their names to improve their display and usage in Odoo forms. Tax codes can be searched using shortcuts. The new Tax Description field contains longer descriptions of the taxes.
52. Taxes: modification restriction and logging
    Some fields on the Taxes model are now unmodifiable once the tax is used. Modifications done on some fields are tracked in the chatter.
53. UBL/CII: handle payment terms
    Improved UBL import with Cash Discounts and fixed taxes.
54. 用户门户：发票Invoices
    从用户门户下载发票Invoices时候，支持各种电子发票格式。
55. User-friendly bank synchronization
    Bank synchronization flows have been simplified. Buttons and alerts are displayed on the dashboard. Email notifications are sent to the account holder.
56. 供应商电子账单导入时候自动匹配PO单
    从Odoo支持的电子发票系统（如UBL 3.0发票）导入供应商账单时候，自动按价格、产品名称匹配采购订单PO明细行，匹配不上的，标示出来显示在供应商账单上。
57. VIES check
    The output of the VIES check is displayed on the partner and can be overridden when necessary. For eCommerce flows, the check can be restrictive, preventing the client from obtaining an invoice on which the reverse charge has been applied.

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
