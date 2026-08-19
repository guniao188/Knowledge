---
title: "新人ERP入门培训之Python"
source: "http://www.thinkltd.cn/forum/3/erppython-3790"
forum: "方案库"
author: "肖相扶"
published: 2023-11-01
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# 新人ERP入门培训之Python

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:肖相扶 | 2023-11-01
> <http://www.thinkltd.cn/forum/3/erppython-3790>

1.  教程：[https://www.runoob.com/python3/python3-tutorial.html](https://www.runoob.com/python3/python3-tutorial.html)
2.  在线工具：
3.  实例学习：
4.  1.  运行并理解此处的python实例程序：[Python3 实例 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python3-examples.html)
    2.  逐行解释此实例的python代码：[Python 输出指定范围内的素数 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python3-prime-number-intervals.html)
    3.  编写python代码，实现如下功能：

给定数字N，打印形如下图的三角形。即第一行打印1个数字1，第二行打印2个数字2，第三行打印3个数字3，以此类推，第N行打印N个数字N。数字N小于1则取数字1，数字N大于9则取数字9。

![[3-erppython-3790-9e43ed31.png]]

## 补充/答案 1

str='123456789'
print(str[0])
print(str[1] * 2)
print(str[2] * 3)
print(str[3] * 4)
print(str[4] * 5)
print(str[5] * 6)
print(str[6] * 7)
print(str[7] * 8)
print(str[8] * 9)

![[3-erppython-3790-5b9cd12a.png]]

## 补充/答案 2

这是段华昌学了3天想出来的写法。但是题目要求的是N，不是固定的9。这个题目要求你学会函数定义def， if 语句用法，以及 for 语句用法。


## 评论

> [!quote] 肖相扶 · 2023-11-09
> 这是段华昌学了3天想出来的写法。但是题目要求的是N，不是固定的9。这个题目要求你学会函数定义def， if 语句用法，以及 for 语句用法。

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
