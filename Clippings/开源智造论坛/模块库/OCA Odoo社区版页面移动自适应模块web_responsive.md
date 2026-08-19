---
title: "OCA Odoo社区版页面移动自适应模块web_responsive"
source: "http://www.thinkltd.cn/forum/2/oca-odooweb-responsive-3322"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA Odoo社区版页面移动自适应模块web_responsive

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-odooweb-responsive-3322>

模块链接：https://github.com/OCA/web/tree/13.0/web_responsive

该模块在社区版基础上，增加移动自适应功能。

This module adds responsiveness to web backend.

Features for all devices:

- New navigation with an app drawer

- Quick menu search from the app drawer

Features for mobile:

- App-specific submenus are shown on full screen when toggling them from the "hamburger" menu

- View type picker dropdown displays confortably

- Top app bar is always visible, but the control panel is hidden when scrolling down, to save some vaulable vertical space

- Form status bar action and status buttons are collapsed in dropdowns. Other control panel buttons use icons to save space.

- Breadcrumbs navigation is collapsed with a "back arrow" button.

Features for computers:

- Keyboard shortcuts for easier navigation, **using ``Alt + Shift + [key]``** combination instead of just `Alt + [key]`. See  to understand why.

- Autofocus on search menu box when opening the drawer

- Set chatter on the side of the screen, optional per user

- Full width form sheets

- Sticky chatter topbar

- AppMenu waits for action finished to show the view

- Sticky header & footer in list view

- Sticky statusbar in form view

- Followers and send button is displayed on mobile. Avatar is hidden.

- When the chatter is configured on the side part, the document viewer fills that part for side-by-side reading instead of full screen. You can still put it on full width preview clicking on the new maximize button.

**Table of contents**

- [Usage](https://github.com/OCA/web/tree/13.0/web_responsive#usage)
- [Known issues / Roadmap](https://github.com/OCA/web/tree/13.0/web_responsive#known-issues-roadmap)
- [Bug Tracker](https://github.com/OCA/web/tree/13.0/web_responsive#bug-tracker)
- [Credits](https://github.com/OCA/web/tree/13.0/web_responsive#credits)
  - [Authors](https://github.com/OCA/web/tree/13.0/web_responsive#authors)
  - [Contributors](https://github.com/OCA/web/tree/13.0/web_responsive#contributors)
  - [Maintainers](https://github.com/OCA/web/tree/13.0/web_responsive#maintainers)

##

## [Usage](https://github.com/OCA/web/tree/13.0/web_responsive#id1)

The following keyboard shortcuts are implemented:

- Navigate app search results - Arrow keys
- Choose app result - `Enter`
- `Esc` to close app drawer

##

## [Known issues / Roadmap](https://github.com/OCA/web/tree/13.0/web_responsive#id2)

- To view the full experience in a device, the page must be loaded with the device screen size. This means that, if you change the size of your browser, you should reload the web client to get the full experience for that new size. This is Odoo's own limitation.
- App navigation with keyboard.
- Make it more beautiful. Maybe OCA-branded?
- Handle long titles on forms in a better way

## 补充/答案 1

或者最新版的这个模块，backend_theme_v13现在也已可以正常支持移动端了，显示界面是OK的。theme依赖于模块ow_web_responsive
在OCA里面可以找到https://github.com/OCA/web

![[2-oca-odooweb-responsive-3322-d23c9e6a.png]]

![[2-oca-odooweb-responsive-3322-9562c022.png]]

如果需要修改主题壁纸包，或主题标题栏颜色，需要修改以下几个文件

替换这个目录下的这个图片，即壁纸

F:\SVN\odoo_ecommerce\06.Customization\Vital Vince\addons\新版皮肤包\backend_theme_v13\static\src\img

如果要更改主题框颜色，需要修改：

F:\SVN\odoo_ecommerce\06.Customization\Vital Vince\addons\新版皮肤包\backend_theme_v13\static\src\scss  目录下style.scss文件

第22行左右

// Odoo EE colors
//$brand-primary: #810541;
//$brand-secondary: #810541;
//------------------------
$brand-primary: #810541;
$brand-secondary: #810541;
//------------------------

的颜色代码

以及第280行的颜色代码的透明度百分比，由原来的35%有改成了85%,这个是在创建或编辑时字段选择时，为了方便能看清字，所以颜色有调整，因为前面有将蓝色调，调成了紫红色调，故透明度也调整了。

.o_required_modifier {
    &.o_input, .o_input {
        background-color: lighten($brand-primary, 85%) ! important;

还可以将背景壁纸简单ps一下，添加客户的logo名字。

![[2-oca-odooweb-responsive-3322-cd723924.png]]


## 原帖外链配图

![[2-oca-odooweb-responsive-3322-x91d96815.gif]]
<small>原始地址: https://user-images.githubusercontent.com/973709/48417193-09a1e080-e74a-11e8-8a0c-e73eb689b2fb.gif</small>

![[2-oca-odooweb-responsive-3322-x32adebd9.gif]]
<small>原始地址: https://user-images.githubusercontent.com/973709/48417213-17576600-e74a-11e8-846a-57691e82636b.gif</small>

![[2-oca-odooweb-responsive-3322-xbb9e9186.gif]]
<small>原始地址: https://user-images.githubusercontent.com/973709/48417297-51286c80-e74a-11e8-9a47-22c810b18c43.gif</small>

![[2-oca-odooweb-responsive-3322-x0d97904a.gif]]
<small>原始地址: https://user-images.githubusercontent.com/973709/50964496-5cd4ad00-14c7-11e9-9261-fd223a329d02.gif</small>

![[2-oca-odooweb-responsive-3322-x49515a10.gif]]
<small>原始地址: https://user-images.githubusercontent.com/973709/50965446-e08f9900-14c9-11e9-92d6-dda472cb6557.gif</small>

![[2-oca-odooweb-responsive-3322-x661d85b5.gif]]
<small>原始地址: https://user-images.githubusercontent.com/973709/50965168-1d0ec500-14c9-11e9-82a0-dfee82ed0861.gif</small>

![[2-oca-odooweb-responsive-3322-x331654db.png]]
<small>原始地址: https://user-images.githubusercontent.com/973709/48417578-ff341680-e74a-11e8-8881-017709e912bc.png</small>

![[2-oca-odooweb-responsive-3322-xa0880ca5.gif]]
<small>原始地址: https://user-images.githubusercontent.com/973709/48417270-41108d00-e74a-11e8-9172-cba825d027ed.gif</small>

![[2-oca-odooweb-responsive-3322-xdaf358c2.png]]
<small>原始地址: https://user-images.githubusercontent.com/973709/48417428-ac5a5f00-e74a-11e8-8839-5bc538c54c1d.png</small>

![[2-oca-odooweb-responsive-3322-x84905e7e.gif]]
<small>原始地址: https://raw.githubusercontent.com/OCA/web/13.0/web_responsive/static/img/listview.gif</small>

![[2-oca-odooweb-responsive-3322-x0d459063.gif]]
<small>原始地址: https://raw.githubusercontent.com/OCA/web/13.0/web_responsive/static/img/formview.gif</small>

![[2-oca-odooweb-responsive-3322-x14ed2f1a.gif]]
<small>原始地址: https://raw.githubusercontent.com/OCA/web/13.0/web_responsive/static/img/document_viewer.gif</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
