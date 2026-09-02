---
title: Odoo 通用研发与运维
type: project
status: 长期
updated: 2026-08-27
tags: [Odoo, 研发, 运维]
---

# Odoo 通用研发与运维

## 高频工作流

1. 报错诊断：提取根因调用链，区分标准模块、自定义模块、配置、权限与数据问题。
2. 模块交付：Python、XML、manifest、ACL、外部 ID、版本兼容、升级与冒烟测试。
3. 安全部署：检查 → 备份 → 同步 addons → 升级测试库 → 冒烟 → 报告；失败时可恢复。
4. 数据修复：统计 → 预览 → 导出备份 → 确认 → 执行 → 报告 → 回滚。
5. 文档交付：先确认目录与业务流程，再生成、渲染、逐页检查。

## 建议优先自动化

- 模块修改后的自动检查与交付报告。
- 报价—订单—发货—开票—收款异常日报。
- 通用数据修复框架。
- 操作手册增量更新与多版本回归矩阵。
- 每周模块变更、部署状态、验收与风险总结。

## 版本矩阵

- Odoo 17：审批状态字段白名单、付款/请购等传统后端逻辑较多。
- Odoo 18：导入、单位、财务与列表视图增强任务较多。
- Odoo 19：OWL 前端、AI Copilot、排程与图形化审批等产品化需求较多。

## 可复用实现经验

- QWeb 左右签字区需随任一方长名称共同下移时，使用同一表格行共享行高；分别排版或给名称固定高度会导致错位或溢出。
- Odoo 17 预测页出现 `false 已预留`，通常表示相关库存移动缺少可显示的来源/调拨名称；释放前需预览来源和制造关联，优先调用标准取消预留逻辑，禁止直接改 `stock_quant.reserved_quantity`。
- Odoo 18 列表中的 Char 邮箱字段可直接使用 `widget="email"` 生成 `mailto:` 链接，无需 JavaScript；行内编辑时恢复输入框是标准行为。
- 外部接口同步不能因本地已有单据就跳过详情刷新；并行返回的发货与签收集合应按业务键合并。接口暂时缺少明细时保留旧记录，避免把“响应不完整”误判为“业务数据已删除”。
- Odoo 18 补货弹窗的 `Time Horizon` 优先读取页面上下文 `global_visibility_days`，其次读取系统参数 `stock.visibility_days`，标准缺省为 0；它与单条补货规则的 `Visibility Days` 是不同参数。
- Odoo 19 发票/销售明细的章节备注组件会主动禁止列排序，以保护 `sequence` 与打印结构；默认显示的 `product_template_id` 又是非存储计算字段。强制本地排序不会永久改写业务顺序。
- Odoo 18 多发票“分组付款”只创建一笔付款并交给核销引擎，默认不是按比例分摊；分配受到期日、币种和金额排序影响。标准界面没有逐张发票自定义分配金额的配置。
- Odoo 17 制造订单确认会直接或间接更新 `state`、`consumption`、`product_qty`、`product_uom_id` 及制造移动/工单等关联字段；审批中写保护需按模型分别配置白名单，不能只放行制造订单主表。
- Odoo 服务器动作中抛出 `UserError` 会回滚整个事务，包括之前执行的 SQL；需要反馈结果时用日志与通知。混用 ORM 和原生 SQL 时应在 SQL 前 `flush`，SQL 后仅清缓存而不要把旧 ORM 值再次刷新回数据库。
- 单位关联 ID 替换必须同时核对产品销售/采购单位、BOM 主表与 BOM 明细，并验证单位类别和换算比例；强制替换比例不同的单位会改变数量含义。
- Odoo 前端可编辑性可能同时受表单模式与字段 `readonly` 修饰控制；只切换到 edit 模式不等于字段已可写，后端仍需同步强制权限规则。
- Owl 动态权限组件要遵守生命周期顺序，先让原生钩子初始化 `values` 再做布尔转换。代码已注册字段但数据库缺列时应升级所属模块，不要手工 `ALTER TABLE`。
- Odoo 18 采购行 `qty_received` 对库存商品主要累计已完成、关联采购行且满足计入口径的 `stock.move.quantity`，并按采购单位换算；标准判断关注来源位置 `location_id.usage` 是否为 `supplier`/`transit`，不会等目标位置真正进入 `Stock`。三步入库若要求最后一步才算已收，需要定制目标位置判断，并确认末段移动是否仍保留 `purchase_line_id` 或沿 `move_dest_ids` 追踪。
- `Missing template: "web.GraphView"` 表示 GraphController 的 JS 已加载但对应 Owl/QWeb XML 模板未进入资源集合，优先检查浏览器/反向代理缓存、资源包重建、多 worker 代码一致性、`addons_path` 和自定义 assets 的 `remove/replace`，不是 Forecast 数据计算错误。
- Odoo 18 Float 两位小数应同时核对字段 `digits=(16, 2)` 和视图 `options={'digits': [16, 2]}`；`monetary` 默认受币种精度控制，需 `field_digits=True` 才采用字段精度，`type="number"` 可能在编辑态显示原始值。
- 导入唯一性校验应显式跳过空值；多个空 `service_number` 在 Odoo 中都是 `False`，若自定义重复检查未过滤，会被误报为重复编号。
- 直接把销售/采购订单状态及已交付、已收、已开票统计刷满但不生成库存或会计单据，只适用于经确认的历史修复。采购标准确认会触发 `_create_picking()`，不能直接调用；统计字段是计算字段，后续重算可能覆盖，必须在测试库验证并保留一致性说明。
- 会计资产负债表检查使用“资产合计 = 负债合计 + 所有者权益合计”；若差额恰好等于当期净利润，优先检查本年利润是否纳入权益以及 `sum/-sum` 符号。2026-08-10 样表差额为 164,411.04，推测漏入本年利润，待会计口径确认。
- Odoo 休假方法 `_cancel_invalid_leaves()` 不是由 `@api.model` 自动触发，而是标准计划任务 `Time Off: Cancel invalid leaves` 默认每天调用；它检查未来 31 天内、处于待审批/已批准且使用累计分配的请假，预计余额超限时强制取消。实际运行时点以数据库中的 `ir.cron.nextcall` 为准。
- Odoo 18 服务产品常见两种开票策略：`ordered_prepaid` 按订购数量开票；`delivered_manual` 按手工交付数量开票。工时和里程碑策略是否出现取决于相关模块与配置。
- Odoo 18 同一价格表的规则按“产品变体 > 产品 > 类别 > 全部产品”匹配，同级优先最小数量更大者，再按类别/记录 ID 排序；取第一条命中规则而不是最低价。无规则时回退 `list_price`，公式以销售价格为基准时才由 `list_price` 继续计算。
- 计划任务没有当前选中记录，`record/records` 可能为 `None`；批量重算应主动搜索目标记录。按公司重算成本时必须显式设置公司上下文并阻止自定义跨公司同步，报价单成本/毛利只重算最近三个月 `draft/sent` 状态，正式执行前仍需测试库核验。
- Odoo 19 欠单流程不会调用 `stock.move._key_assign_picking()`；该键只影响初次分配 picking。要按合并前来源拆分欠单，应先调用 `super()._create_backorder()`，再对返回欠单按已记录的原 picking 后处理拆分，避免复制原生欠单逻辑。
- Odoo 18 的 Analytic 报表列按分析账户/计划展开，不保证横向列天然互斥；分析列合计大于基础 Total 时，优先排查重复或残留 `account.analytic.line`、跨计划重复统计，而不是先怀疑 Excel 求和。若分录被重置草稿后重新过账，还应同时检查重复 COGS Journal Items。
- Analytic Items 正常应由标准过账流程创建、由标准重置草稿流程清理；额外设置“状态变为 Posted 时手工创建”的自动化容易重复。服务器动作绑定 `account.move.line` 时应使用 `line.move_id.state` 判断状态，并调用原生 `_create_analytic_lines()`，不要按 `account.move` 访问 `record.state` 或 `invoice_line_ids`。

## 代码仓库

- 本地：`/Users/yaodaidi/odoo18`、`/Users/yaodaidi/odoo19`。
- 历史任务已建立私有远程仓库 `guniao188/odoo18`（`odoo18` 分支）与 `guniao188/odoo19`（`odoo19` 分支）并设置 upstream；远程和当前权限仍需在下一次推送前核验。
- 仅提交源码，排除数据库、转储、虚拟环境、运行数据、本地配置和 IDE 文件。Odoo 19 曾检测到约 9,000 项嵌套 Enterprise 差异，应按模块提交。
- 安全风险：历史任务中曾在聊天里出现 GitHub Token；本知识库未保存其内容，吊销状态待确认。后续使用系统/GitHub CLI credential helper，不在聊天或仓库中传递 Token。

## 文档资产

- 已交付：`/Users/yaodaidi/Documents/New project/Odoo19财务凭证与科目应用说明_完善版.docx`，18 页，保留 15 张截图并完成逐页检查。
- 已交付：`/Users/yaodaidi/Documents/New project/purchase_report_purchaseorder_document_copy_2.xml`，采购 QWeb 签字区强制清除表格边框并保留签字横线，已通过 XML 校验；部署后需重新生成 PDF 验证 WPS 显示。
- 待完成：`/Users/yaodaidi/Documents/New project/Odoo18_补货规则说明文档.docx`，9 页内容已生成，但任务在最终跨应用编号和版式复核时中断，不能标记为正式交付。

## 可复用模块资产

- `web_binary_pdf_preview`：Odoo 18 Binary 字段按需弹窗预览，支持 PDF、常见图片及 Excel；Excel 在浏览器本地解析，支持多工作表，默认最多 500 行 × 100 列，不执行宏或上传第三方。
- 源码：`/Users/yaodaidi/Documents/New project/web_binary_pdf_preview`；安装包：`/Users/yaodaidi/Documents/New project/web_binary_pdf_preview.zip`；版本 `18.0.1.3.0`。
- 已完成 JavaScript、XML、manifest、翻译、ZIP 结构及实际 XLSX 解析验证；未发现 Odoo 数据库安装验证证据，部署状态保持待确认。
- `purchase_order_chinese_name`：Odoo 18 采购订单自动关联供应商 `chinese_name`，支持表单/列表显示、搜索和分组；源码 `/Users/yaodaidi/Documents/New project/purchase_order_chinese_name`，安装包 `/Users/yaodaidi/Documents/New project/purchase_order_chinese_name-18.0.1.0.0.zip`。静态、XML、ZIP 校验通过，数据库安装及依赖模块名待确认。
- `stock_backorder_split_by_source`：Odoo 19 在服务器动作通过 ORM 合并 `stock.move.picking_id` 时记录原 picking，创建欠单后按来源自动拆分；源码 `/Users/yaodaidi/Documents/New project/stock_backorder_split_by_source`，安装包 `/Users/yaodaidi/Documents/New project/stock_backorder_split_by_source-19.0.1.0.0.zip`。模块必须在合并前安装，SQL 合并和既有历史合并无法恢复来源；静态/ZIP 校验通过，数据库安装测试未确认。

## Codex 本地运行风险

- 2026-07-18 曾确认 `/Users/yaodaidi/.codex/logs_2.sqlite` 持续 TRACE 写入，并创建备份 `/Users/yaodaidi/.codex/logs_2.sqlite.pre-trace-block-20260718-004616.bak`。
- 当时为满足 `MAX(id)` 与 WAL 均停止增长，安装了无条件 `BEFORE INSERT` trigger，导致 TRACE、INFO、DEBUG 等所有新日志都被拦截；当时 WAL 已截断为 0。
- 当前 trigger 是否仍存在尚未重新核验。若需要 Codex 本地日志排错，应先只读检查 trigger 和日志增长状态，再决定是否恢复写入。
