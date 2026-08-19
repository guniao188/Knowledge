---
title: "应聘简历自动补填功能hr_recruitment_applicant_txt"
source: "http://www.thinkltd.cn/forum/2/hr-recruitment-applicant-txt-3579"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 应聘简历自动补填功能hr_recruitment_applicant_txt

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/hr-recruitment-applicant-txt-3579>

模块位置：OSCG_SVN\odoo_ecommerce\15.0SRC\HR\hr_recruitment_applicant_txt

【业务背景】

1.  从Boss直聘等招聘网站收到的简历，发送到HR邮箱，Odoo自动收取HR邮箱的邮件，并自动创建简历表单。

2.  此处希望有一个功能，自动提取简历附件中的邮箱、手机、姓名等信息，自动补填到Odoo的简历表单上。如此，节省人工拷贝粘贴的时间。

【模块功能】

1.  简历上增加字段applicant_txt，以及方法 def extract_applicant_txt()，服务器动作上调用该方法，该方法从PDF格式的简历上提取简历文字信息，写入字段applicant_txt。BOSS直聘网站过来的简历是PDF附件，本方法自动提取文字信息。51job过来的简历是HTML格式，且简历中无邮箱、手机信息，因而本方法不提取51job的简历；

2.  增加服务器动作，该服务器动作从提取的简历文本信息中，自动提取手机号码、邮箱、姓名、期望薪资等信息，填写到简历表单

3.  注意事项，有些PDF简历实际是图片，提取不了文字，此类简历，还是需要手工拷贝粘贴填写简历

【功能截图】

![[2-hr-recruitment-applicant-txt-3579-a0778c23.jpg]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
