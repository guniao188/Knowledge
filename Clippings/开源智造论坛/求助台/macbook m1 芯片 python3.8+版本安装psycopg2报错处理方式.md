---
title: "macbook m1 芯片 python3.8+版本安装psycopg2报错处理方式"
source: "http://www.thinkltd.cn/forum/1/macbook-m1-python3-8-psycopg2-843"
forum: "求助台"
author: "杨浔波"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# macbook m1 芯片 python3.8+版本安装psycopg2报错处理方式

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:杨浔波 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/macbook-m1-python3-8-psycopg2-843>

1. 首先终端模式启用Rosetta
2. 进入pycharm生成的虚拟环境后敲入下列命令：

``` lang-py
env LDFLAGS="-L/opt/homebrew/opt/openssl@1.1/lib -L/opt/homebrew/opt/readline/lib" pip3 --no-cache install psycopg2
```

``` lang-py

```

## 补充/答案 1

如果依然不能解决可以尝试安装：

``` lang-py
brew install openssl
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
