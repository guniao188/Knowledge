---
title: "V16官方存在的会计采购价格变更生成分录bug"
source: "http://www.thinkltd.cn/forum/1/v16bug-3884"
forum: "求助台"
author: "符赛红"
published: 2024-02-19
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# V16官方存在的会计采购价格变更生成分录bug

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2024-02-19
> <http://www.thinkltd.cn/forum/1/v16bug-3884>

业务发生背景说明：

PO已经入库完成之后，事后单价变更，当库存数量没有出库用掉的情冲下，BILL验证会自动生成差异金额的【库存计价】0数量的差异金额会计凭证分录，如果多次修改该BILL，会导致库存计价上的金额重复生成差异及分录，并且原入库的数量库存计价记录的【剩余金额】会重复累计，虽然会计账余额与库存计价余额相吻合，但实际上翻倍了。第一次改的价格出来能是正确的，但BILL如果重置再重新过账又会生成差异凭证，就不正确了。虽然BILL可以做红冲，也能正确，但第二次变更或第三次重置也会有些异常。

![[1-v16bug-3884-6b129fc9.png]]

解决办法：

方案一：

而让bill不能重置，而去生成红冲，重新生成BILL，一旦过账就不允许修改重置，但如果业务过程中存在经常价格变化的情况下，就比较麻烦，不能第二次修改调整。

方案二：

请会计特别注意：第一次变更可以不用设整，第二次重置修改，请调整重复生成的差异分录，取消掉，然后【库存计价】里修改【TOTAL VALUE】及原数是记录的【Remaining Value】

已经技术处理，可以会计【成本管理】权限组的用户可以看到这二个字段可以编辑人工修改为正确的

 改库存计价的form视图可编辑修改这二个字段

![[1-v16bug-3884-bf4b0238.png]]

![[1-v16bug-3884-6f67f2c2.png]]

![[1-v16bug-3884-78f0f641.png]]

## 补充/答案 1

原则上不能算BUG，因为账单重置为草稿按钮，官方是加了显示条件的，如果已经跑出计价是不显示这个按钮的，根据以下计算型方法的返回值决定是否显示重置草稿按钮

```python
    def _compute_show_reset_to_draft_button(self):
        super()._compute_show_reset_to_draft_button()
        for move in self:
            for line in move.line_ids:
```

                # if a line has correction layers hide the 'Reset to Darft' button
```python
                if line._get_stock_valuation_layers(move).stock_valuation_layer_ids.filtered('account_move_line_id'):
                    move.show_reset_to_draft_button = False
                    break
```

## 补充/答案 2

所以系统源码是想让用户不能修改和重置，就是方案一，要改就只能红冲来调整了。但实际业务中有些客户会要经常事后修改就很麻烦。


## 评论

> [!quote] 符赛红 · 2024-02-19
> 所以系统源码是想让用户不能修改和重置，就是方案一，要改就只能红冲来调整了。但实际业务中有些客户会要经常事后修改就很麻烦。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
