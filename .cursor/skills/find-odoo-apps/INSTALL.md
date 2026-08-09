# 让 find-odoo-apps 在本机所有项目可用

## 为什么仓库里有了还用不了？

Cursor **只会**自动加载这些目录里的 skill：

- 项目内：`.cursor/skills/`（仅当前仓库）
- 本机全局：`~/.cursor/skills/`（所有项目）

把文件放在别的路径（例如以前的 `skills/`）**不会被发现**。

本仓库已把 skill 放在：

```text
.cursor/skills/find-odoo-apps/SKILL.md
```

因此：**打开本 Knowledge 仓库时**应可直接用。  
若要在**其他任意项目**也能用，必须再安装到本机全局目录一次。

## 一键安装到本机全局（推荐）

在仓库根目录执行：

```bash
bash .cursor/skills/find-odoo-apps/install-global.sh
```

手动等价命令：

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/find-odoo-apps
cp -R .cursor/skills/find-odoo-apps ~/.cursor/skills/find-odoo-apps
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.cursor\skills" | Out-Null
Remove-Item -Recurse -Force "$HOME\.cursor\skills\find-odoo-apps" -ErrorAction SilentlyContinue
Copy-Item -Recurse ".cursor\skills\find-odoo-apps" "$HOME\.cursor\skills\find-odoo-apps"
```

## 安装后必做

1. **完全退出并重启 Cursor**（只新开聊天有时不够）
2. 打开 **Customize → Skills**，确认有 `find-odoo-apps`
3. 在任意项目的 Agent 输入 `/find-odoo-apps`，或直接说「帮我查一下有没有 Odoo 请购单插件」

## 自检

```bash
test -f ~/.cursor/skills/find-odoo-apps/SKILL.md && echo "全局 skill 已安装" || echo "未安装到全局"
```

## Cloud Agent 说明

云端 Agent 读不到你电脑上的 `~/.cursor/skills/`。云端要靠仓库里的 `.cursor/skills/`（已提交）。本机全局安装只影响你自己电脑上的 Cursor。
