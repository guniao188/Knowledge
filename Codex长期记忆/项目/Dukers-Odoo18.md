---
title: Dukers Odoo 18
type: project
status: 损益表 Analytic 差异根因已定位，修复执行待确认
updated: 2026-08-27
tags: [Odoo18, 客户/Dukers, 销售, 发票, 退货, 财务]
---

# Dukers Odoo 18

## 业务问题

Will-Call、COD 和信用卡费原本作为数量固定为 1 的服务产品，首次部分开票时会一次性全额进入发票，且退货时缺少对应调整。

## 实现

- 新模块：`/Users/yaodaidi/odoo18/psus-dukersusa/dukers_sale_invoice_adjustment`
- 保持原 `dukers_sale` 的销售界面和勾选框不变，只接管发票/退款调整逻辑。
- 发票折扣按销售订单已经确定的折扣金额比例分摊：

  `本次调整 = 订单已有调整金额 × 本次开票商品金额 ÷ 订单商品总金额`

- 因此订单折扣 -70、交付并开票一半时，本次折扣为 -35；保留订单中手工调整后的折扣总额。
- 支持分批开票、部分退货、Credit Note、草稿发票修改后重算及升级时重算旧草稿。
- 模块版本 `18.0.1.1.0`，4 个业务测试全部通过。

## 待办

- 部署后升级模块并验证实际税组、运费/服务费是否应进入折扣基数。
- 未发现正式环境部署证据，状态保持“待部署确认”。

## 2026-08 损益表 Analytic 差异

- 2026 年 6 月损益表的 Excel 横向汇总公式无误；差额集中在收入与销售成本两个底层科目，其余 Revenue、Gross Profit、Net Profit 等差额均为上层汇总传导。
- 根因已定位到发票重置草稿后重新过账：旧 Analytic Items 未清除，又生成新记录，造成 Analytic 口径重复；同时发现同一发票存在两套相同 COGS Journal Items，基础损益表也可能重复计入销售成本。
- 当前 `analytic_distribution` 合计为 100%，因此不是当前分配比例超额；应核对已生成的 `account.analytic.line` 与日记账明细之间的一致性。
- 已生成日记账明细服务器动作 `/Users/yaodaidi/Documents/New project/server_action_repair_analytic_items.py`：仅处理已过账记录，保留最早的完全重复 Analytic Item，删除后续副本；缺失且存在分析分配时调用 Odoo 18 原生 `_create_analytic_lines()` 补建。
- 风险边界：服务器动作不删除重复 COGS Journal Items；COGS 需通过会计安全流程单独核查。未找到修复已在测试库或正式库执行的证据。
- 建议停用“过账时手工创建 Analytic Items”的自动化规则，依赖 Odoo 标准过账/重置草稿流程；手工修复动作只用于异常数据。该建议尚待实际配置确认。

## 当前待办

- 在测试库先预览并执行 Analytic Item 修复，再复核 2026 年 6 月损益表两种口径。
- 确认重复 COGS 的正确会计处理方案后再修改，避免直接删除已过账明细破坏总账平衡。
- 核查生产环境是否安装并运行了会自动补写分析分配的自定义逻辑，以及是否仍存在直接写 `state = draft` 绕过标准清理的操作。

- 来源：`设计部分发货折扣方案`，thread `019f8830-1bdb-7d01-b54e-07152c9016dc`。
- 来源：`分析利润表总和差异原因`，thread `01a017c4-bca6-75d1-bd05-5ab234dcc5ca`；`检查损益表Analytic汇总差异`，thread `01a0187e-b8fa-7d00-8347-eec3abce67be`；`Fix account.move analytic lines`，thread `019f5fc6-be7a-7411-9f38-afc6aa9bbc72`。
