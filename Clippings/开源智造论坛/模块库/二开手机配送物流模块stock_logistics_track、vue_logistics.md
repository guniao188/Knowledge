---
title: "二开手机配送物流模块stock_logistics_track、vue_logistics"
source: "http://www.thinkltd.cn/forum/2/stock-logistics-trackvue-logistics-3328"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开手机配送物流模块stock_logistics_track、vue_logistics

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/stock-logistics-trackvue-logistics-3328>

模块链接：OSCG_SVN\odoo_ecommerce\13.0SRC\手机物流\stock_logistics_track

基于VUE框架的H5手机端：OSCG_SVN\odoo_ecommerce\13.0SRC\手机物流\vue_logistics

【业务背景】

1.  建材经销商（上海卡夫，涂料代理商），接到订单后，典型的仓库发货配送流程是：仓管员打印发货单、拣货员拣货、另一个拣货员复核、调度人员安排配送车辆（通常是一车配送多个订单）、司机及跟车员装车（通常是第二天）、逐单配送（实时收集配送车辆位置）、客户签收（一般都是配送到工程现场，现场没有人，要求司机卸货后 拍照签收）、回单（交给仓管员确认关单）。

2.  上述流程，希望 拣货完成、拣货复核、派车完成、装车完成、实时收集车辆位置、拍照签收，这些操作环节都可以管理起来，谁操作的，什么时候操作的，系统都留下记录。这些操作，需要在手机端完成。例如，拣货完成，拣货员手机扫描拣货单（打单环节打印出来的纸质单据），手机调出拣货单，拣货员点击 “拣货完成” 按钮。

3.  其他一些类似操作场景：家具等大件发货（仓库需要打单、拣货、复核、打包等操作），食材配送到餐饮店（从打单到司机拍照签收等操作）

【模块功能】

1.  Stock Picking单上增加操作记录，操作类型有：打单、拣货、复核、打包、派车、装车、签收、回单

2.  波次单（stock.picking.batch）上增加司机、配送日期等字段，增加运输路径记录（收集车辆GPS轨迹）

3.  增加拣货员、调度员、司机三个权限组，拣货员可以操作 拣货、复核，调度员可以操作 派车，司机可以操作 装车、签收。复核时候检查，复核员和拣货员不可以是同一人。

4.  手机端操作有两个操作界面，一个以发货单(stock.picking)为中心的操作，包括 拣货、复核、签收三个操作。一个以 装车单（stock.picking.batch）为中心的操作，包括 派车、装车两个操作。

5.  发货单操作：用户进入操作界面，扫描发货单号（二维码），系统调出发货单，显示操作记录；用户点击“拣货完成”、“拣货复核”按钮，系统记录操作人及操作时间；用户点击“拍照”，系统自动上传照片作为该单据的附件。用户点击“签收”按钮时候，系统会自动提示要求先拍照。

6.  装车单操作：用户进入操作界面，扫描装车单号（二维码，基于stock.picking.batch的打印单据），系统调出装车单，显示发货单明细；用户点击“扫码派单”，扫描拣货单号，系统自动添加到当前装车单；司机点击“装车”，系统开始定时获取位置GPS，上传到装车单上。

7.  手机端操作，每次操作，系统在界面上以红色字体提示操作状态（成功 or 失败）

8.  装车后，手机端每隔6分钟上传一次GPS位置。每次上传后，红色状态显示上传时间。如果时间长时间不变（超过6分钟），可以判断系统背后的GPS上传停止了，点击“刷新GPS”可以重启位置上传。

9.  Website的我的订单界面，增加一个链接 “订单物流”，点击跳转到 订单物流 网页，该网页上半部分显示配送地图（用高德地图API），下半部分显示 物流操作轴。配送地图上显示：发货仓位置（取订单对应的发货单的发货库位的 parnter_id 地址），GPS轨迹（取发货单对应装车单的运输轨迹），目标地址（发货单的partner_id的地址）。参考：Odoo标准模块 base_geolocalize 在Partner上增加了GPS位置字段。

10. 发货单自动打印：独立Python程序 auto_print.py  自动获取“就绪”状态的拣货单，自动打印，打印完毕后标记对应Stock Picking 为已打印(auto_printed 字段)。实施时候，auto_print.py 部署到仓库的电脑上，通过Windows的计划任务定期调用，自动打印拣货单。注意部署的时候，需要修改程序中的 IP，用户名，密码等参数信息，或者也可以在远程数据库中配置相关参数。

![[2-stock-logistics-trackvue-logistics-3328-7921a103.png]]

## 补充/答案 1

1.  华为Mate10手机，微信浏览器GPS获取 测试结果：

```python
    1.  GPS位置信息获取非常正确

    2.  微信前台显示网页时候，GPS获取正常。微信打开着网页退居后台（前台在看视频或者上网），GPS获取正常。

    3.  熄屏状态，不管微信网页在前台显示还是在后台显示，都获取不到GPS。亮屏后，立即开始正常获取GPS。背后原因应该是，微信浏览器在熄屏情况下，js的setInterval 停止工作。

    4.
```

2.  华为Mate10手机，Google浏览器GPS获取测试结果：

3.  1.  GPS位置获取的好像是上一次缓存的位置，不太正确

    2.  Chrome浏览器在后台运行（前台在看微信等其他软件），获取不到GPS。熄屏情况下也获取不到GPS。

手机UC浏览器测试结果：

## 补充/答案 2

【功能截图】

![[2-stock-logistics-trackvue-logistics-3328-7f2dd916.png]]

![[2-stock-logistics-trackvue-logistics-3328-4b9ea248.png]]

手机端操作界面

![[2-stock-logistics-trackvue-logistics-3328-de5020a4.png]]

![[2-stock-logistics-trackvue-logistics-3328-eb5e5e44.png]]

![[2-stock-logistics-trackvue-logistics-3328-53243cb5.png]]

扫码/拍照界面

![[2-stock-logistics-trackvue-logistics-3328-085b17e6.png]]

装车后，手机端每隔6分钟上传一次GPS位置。根据红色状态提示的时间，可以判断系统背后的GPS上传是否停止了，如果停止了，点击“刷新GPS”可以重启位置上传。

查订单物流GPS轨迹

![[2-stock-logistics-trackvue-logistics-3328-65b1a504.png]]

## 补充/答案 3

重复扫同一个码，会有乱码。建议修改一下，重复扫描时，给提示一个二维码已扫的提示

![[2-stock-logistics-trackvue-logistics-3328-65afb410.png]]

![[2-stock-logistics-trackvue-logistics-3328-1c52a7ce.png]]

![[2-stock-logistics-trackvue-logistics-3328-1c52a7ce.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
