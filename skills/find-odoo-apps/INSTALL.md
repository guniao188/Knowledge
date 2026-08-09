# 安装为全局 Skill（所有项目可用）

Cursor 只在以下位置自动发现 skill：

| 位置 | 作用域 |
| --- | --- |
| `~/.cursor/skills/` | **用户级（全局）**，本机所有项目可用 |
| `<项目>/.cursor/skills/` | 仅当前项目 |

本目录是分发包，不会因为放在仓库里就全局生效。请安装到用户目录。

## macOS / Linux

在仓库根目录执行：

```bash
mkdir -p ~/.cursor/skills
rm -rf ~/.cursor/skills/find-odoo-apps
cp -R skills/find-odoo-apps ~/.cursor/skills/find-odoo-apps
```

或使用绝对路径复制（不依赖当前目录）：

```bash
cp -R /path/to/Knowledge/skills/find-odoo-apps ~/.cursor/skills/find-odoo-apps
```

## Windows（PowerShell）

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.cursor\skills" | Out-Null
Remove-Item -Recurse -Force "$HOME\.cursor\skills\find-odoo-apps" -ErrorAction SilentlyContinue
Copy-Item -Recurse "skills\find-odoo-apps" "$HOME\.cursor\skills\find-odoo-apps"
```

## 验证

1. 重启 Cursor，或新开一个 Agent 对话
2. 打开 **Customize → Skills**，应能看到 `find-odoo-apps`
3. 在任意项目里输入 `/find-odoo-apps`，或直接描述 Odoo 插件需求

## 更新

仓库里的 `skills/find-odoo-apps` 更新后，重新执行上面的复制命令覆盖 `~/.cursor/skills/find-odoo-apps` 即可。
