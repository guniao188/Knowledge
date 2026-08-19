---
title: "Linux或macOS 如何通过代理git获取代码"
source: "http://www.thinkltd.cn/forum/1/linuxmacos-git-819"
forum: "求助台"
author: "杨浔波"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Linux或macOS 如何通过代理git获取代码

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:杨浔波 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/linuxmacos-git-819>

搜索了下，mac 版的 SourceTree 并没有设置代理的配置，因此要想走代理，可以直接从 Git 的配置下手，设置全局的代理。

### 2.1 移除当前 Git 全局配置代理

``` shell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

### 2.2 查看信息 Git 配置信息

``` shell
git config --global -l
```

### 2.3 重新为 Git 设置代理

``` shell
git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080'
```

### 2.4 再次查看 gitconfig 的配置

使用如下命令再次查看配置文件

``` shell
cat ~/.gitconfig
```

会发现多出了这两行

``` line-numbers
[http]
    proxy = socks5://127.0.0.1:1080
[https]
    proxy = socks5://127.0.0.1:1080
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
