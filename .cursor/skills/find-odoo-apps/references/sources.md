# 检索来源与费用字段说明

仅在执行 `find-odoo-apps` 技能、需要核对入口或价格含义时读取。

## 主入口

| 来源 | URL | 用途 |
| --- | --- | --- |
| Odoo Apps Store | https://apps.odoo.com/apps/modules | 官方应用市场，含免费与付费第三方模块 |
| 按版本浏览 | https://apps.odoo.com/apps/modules/19.0 （把版本换成目标版） | 过滤兼容版本 |
| Apps 模块直达 | https://apps.odoo.com/apps/modules/<version>/<technical_name> | 核对价格、许可、依赖 |
| OCA Apps 目录 | https://apps.odoo-community.org/modules | OCA 模块浏览 |
| OCA 模块直达 | https://apps.odoo-community.org/modules/<technical_name> | 版本、许可、仓库链接 |
| OCA 分类 | https://apps.odoo-community.org/categories | 按业务域浏览 |
| OCA GitHub | https://github.com/OCA | 主发现渠道：源码、分支、README、manifest |
| Odoo Apps FAQ（许可/定价键） | https://apps.odoo.com/apps/faq | 理解 `price` / `currency` / `license` |

### 抓取失败时的备用路径

1. WebSearch：`site:apps.odoo.com <keywords>` / `site:apps.odoo-community.org <technical_name>`
2. GitHub API：`/orgs/OCA/repos`、`/repos/OCA/<repo>/contents?ref=<version>`、`/repos/OCA/<repo>/branches`
3. Apps 页超时很常见：不要因此跳过付费核对；用搜索摘要里的价格线索 + 详情页重试

## GitHub 检索示例

```text
org:OCA approval
org:OCA subcontract
org:OCA "stock" "barcode"
org:OCA path:__manifest__.py "purchase_request"
```

进入具体仓库后检查：

- 是否存在目标版本分支（`16.0`、`17.0`、`18.0`、`19.0`…）
- 模块目录下 `__manifest__.py`：`name`、`summary`、`depends`、`license`、`version`、`price`（OCA 通常无 price）
- README 的功能边界与配置说明

常见 OCA 仓库主题（按需进入，非穷尽）：

- `sale-workflow`、`purchase-workflow`、`account-invoicing`、`account-financial-tools`
- `stock-logistics-workflow`、`stock-logistics-warehouse`、`manufacture`、`product-attribute`
- `server-auth`、`server-ux`、`web`、`project`、`crm`、`hr`、`bank-payment`、`l10n-china`（若存在/相关本地化仓）

## Apps 详情页应抓取的字段

- 标题（显示名）
- Technical Name
- 作者 / 维护者
- Versions / Availability（支持版本列表）
- Price（Free 或金额）
- License
- Odoo Apps Dependencies / Community Apps Dependencies
- Lines of code（可选，辅助判断体量）
- Website / GitHub 链接
- 简介与截图描述是否覆盖需求点

## 费用怎么写才算「列清楚」

### Apps 商店标价

- `Free` → 写「免费」
- `$ 99.00` / `€ 49.99` → 原样写金额与币种
- 说明：「Odoo Apps 页面标价；购买与下载通常按数据库授权，以结算页为准」
- 不要自行换算人民币，除非用户要求

### 许可与商业含义（简写）

| License | 通常含义 |
| --- | --- |
| AGPL-3 / LGPL-3 / GPL-3 | 开源；模块价常为免费（仍可能有实施成本） |
| OPL-1 | Odoo 专有许可，常见于 Apps 付费模块 |
| Other proprietary | 专有；以厂商条款为准 |
| OEEL-1 | 与 Enterprise 相关许可；注意 EE 依赖 |

### 隐性成本（费用汇总里按需列出）

1. **Odoo Enterprise 订阅**：模块依赖 Discuss 以外的 EE 应用时必须点明
2. **多数据库 / 多公司**：Apps 是否需重复购买——不确定就写「未在页面确认」
3. **版本升级费**：商店标价通常针对当前模块版本；跨大版本是否另购写「需向发布商确认」
4. **实施与二开**：免费/付费模块都可能需要配置或对齐业务的二次开发
5. **厂商站外售卖**：若详情指向独立报价/订阅，单列「厂商订阅/服务费（非 Apps 标价）」

### OCA

- 模块代码：通常免费下载使用（遵守 AGPL/LGPL 义务）
- 费用汇总写：模块许可免费；实施、托管、合规（AGPL 衍生作品义务）另计
- 不要把 OCA 写成「官方原厂支持」

## 匹配度判定（内部标准）

- **高**：核心流程与需求一致，目标版本有发布，依赖可接受
- **中**：覆盖主要场景但缺 1–2 个关键点，或版本/许可有摩擦
- **低**：同领域但流程假设不同；仅作备选
- **不推荐**：停更、仅旧版、明显不相关、依赖无法满足

## 检索失败时

- 应用市场页面超时或结构变化导致读不到价格 → 给链接并写「未能读取当前标价」
- OCA `/shop?search=` 类泛搜索不可靠 → 改用 GitHub `org:OCA` + `/modules/<technical_name>` 直达
- GitHub 限流 → 改用 OCA Apps 直达页或缩小搜索范围后重试
- 中文需求在 Apps 英文结果差 → 先译成英文功能词再搜，并补充中国本地化/企微等中文关键词
