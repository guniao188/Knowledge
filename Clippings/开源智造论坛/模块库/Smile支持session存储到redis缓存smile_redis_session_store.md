---
title: "Smile支持session存储到redis缓存smile_redis_session_store"
source: "http://www.thinkltd.cn/forum/2/smilesessionredissmile-redis-session-store-3055"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile支持session存储到redis缓存smile_redis_session_store

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smilesessionredissmile-redis-session-store-3055>

模块链接：

## Redis Session Store

This module allows you to use a Redis database to manage sessions, instead of classic filesystem storage.

Redis is an open source, in-memory data structure store, used as a database, cache and message broker.

It is useful for load balancing because session's directory may not be shared.

##

## Requirements

You need to install and to start a Redis server to use this module. Documentation is available on [Redis website](http://redis.io/topics/quickstart).

You need to install package redis:

    pip3 install redis

##

## Usage

To use Redis, install this module and please add enable_redis = True option in configuration file.

###

### Available options

- redis_host (default: localhost): Redis host
- redis_port (default: 6379): Redis port
- redis_dbindex (default: 1): Redis database index
- redis_pass (default: None): Redis password

## 补充/答案 1

相对好的版本是以下链接：

https://apps.odoo.com/apps/modules/12.0/session_redis/

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
