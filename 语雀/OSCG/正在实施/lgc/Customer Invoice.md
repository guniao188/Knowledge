---
title: "Customer Invoice"
client: lgc
type: 项目文档
phase: 实施期
yuque_url: "https://www.yuque.com/xinsuixiaoyao-degek/klxky6/ps85zd8t0g3wnl3h"
yuque_slug: "ps85zd8t0g3wnl3h"
tags: [Odoo, 实施期, 客户/lgc, 正在实施, 销售]
created_at: "2026-03-16T05:31:55.000Z"
updated_at: "2026-03-18T03:06:14.000Z"
published_at: "2026-03-18T03:05:46.000Z"
---
# Customer Invoice

#### 1.  Create order

##### a.  Create order, confirm order, and create invoice from sale order.

###### ⅰ.  step 1. Create order and confirm ![image](_附件/1773639424236-e00275c3-3916-49b9-96f8-e3-498465dfd32b5bad.png)

###### ⅱ.  step 2. Create Invoice from sale order and confirm invoice

![image](_附件/1773639538997-17b32bc7-d971-4bc8-86fc-ec-6048f2c77b2306ad.png)![image](_附件/1773639672131-9ed984ad-1368-46f6-a770-db-7ac19bd0352116e0.png)

![image](_附件/1773639790686-dc0b6d11-c676-460c-b425-42-c6769241b18c1ee7.png)

###### ⅲ.  step 3. Print Customer Invoice from order

![image](_附件/1773639583468-4c19cb22-390d-4117-9fb6-6a-fa5ad6d9251e5fa9.png)If created invoice fully, the customer invoice style is as follows:

![image](_附件/1773639907627-353d72fc-c106-4f67-8134-bc-840fe3844518c53f.png)

![image](_附件/1773639918897-25a22c50-7949-4903-9190-c2-000424e4d2c2bece.png)

And if not created, the customer invoice style is as follows:

![image](_附件/1773639737562-4c4ace8a-4116-47e6-a5cb-4f-56643424321fa098.png)

#### 2.  Modify order quantity

##### a.  2.1 Increase quantity or increase order line

###### ⅰ.  step1. click "Edit" button ![image](_附件/1773640095988-58dbfa01-ed73-4116-bcf5-22-975f6e00af47b44b.png)

###### ⅱ.  step 2. Modify order line

If you want to add more quantity, find the order line and modify the quantity.

![image](_附件/1773640117757-f667cf92-579b-4f7e-b8e3-ec-6e25a631ae97548f.png)

If you need to add line item,click "Add a product" and save.![image](_附件/1773646057138-b6ebef29-4bdb-4c8d-8488-51-e183a44f90d95466.png)

##### b.  2.2 reduce quantity

If you need to reduce the quantity, first locate the row and modify the quantity and click "save" buttom. If the delivery note hasn't been locked yet, simply add a quantity and save it.

But if the delivery note has been locked, you will see a prompt as shown in the image.![image](_附件/1773646700265-3e19a01c-e6eb-4cab-b319-b3-fd70e419f692854f.png)

When this pop-up appears, you need to modify the quantity in the delivery order to release inventory for other orders. The steps are as follows:

##### c.  Modify the quantity in the delivery order

###### ⅰ.  step 1.Turn to delivey order

![image](_附件/1773646803722-da43ec6a-69c9-479d-a0cc-cf-0d8dae9ab30c10f0.png)

###### ⅱ.  step 2.Click "Edit" Button and modify "Operations" page demand quantity. ![image](_附件/1773646900883-73c04530-45a4-4871-850e-60-cbf4ffbf497c9ad4.png)

#### 3.  Adjust invoiced amount

Create invoice and confirm to adjust invoiced amount,then print "customer invoice" from sale order

![image](_附件/1773648698396-a783206d-3cf0-4963-b7bc-ba-bd5a32aea45f13b4.png)

#### 4.  Register payment

Turn to invoices.

![image](_附件/1773763445588-1f3406ac-6fef-471a-8443-26-8518fbfbc63891d8.png)

##### a.  Only have one invoice

If you only have one invoice, clicking on it will automatically redirect you to that invoice; then you can click to “Register payment" and fill in payment information .![image](_附件/1773763710381-7600ad24-6fef-4291-81d0-bb-2beb53967de9795b.png)

##### b.  Multiple invoices

If there are multiple invoices, you will be redirected to a list view. If the customer has paid the amount for multiple invoices at the same time, simply select and click on them. Of course, you can also register them separately.

![image](_附件/1773763873206-67b25f0c-d6cc-44bf-8105-0a-d193a0189b6e6401.png)If the customer makes one payment, they need to select "group payment" so that two invoices correspond to one payment. Otherwise, they will correspond to two payments.

![image](_附件/1773763915405-841f2172-62b0-42a3-8701-63-430cd3f604bfcd32.png)


#### 5.  Refund

##### a.  Method 1：Add Credit Note：Recommended for use when applying for a full refund.

For the invoice order for which a refund is needed, click the "add credit note" button. This will create a refund invoice for the entire order, with the same amount, but the total amount will be negative due to the refund.

![image](_附件/1773801677647-4445a7f4-6b09-4e6d-9a38-31-11485d6e86729b24.png)![image](_附件/1773801960940-0780b99c-d612-4031-8012-db-e3c4bf560aa81032.png)If you want a full refund, simply click "confirm."

![image](_附件/1773802070958-4c49c221-3dff-4100-9d53-9e-b79831e32f3d5abf.png)

If a deposit or part of the product needs to be deducted, you can confirm after modifying the quantity or price in the credit invoice you created.


##### b.  Method 2: Modify the sales order quantity and then create an invoice. This method is recommended for refunds of a small number of products.

Change the quantity of the refunded products to 0 on the order page, then create an invoice. If you entered a reduction and an invoice has already been issued, it will automatically become a refund invoice.

![image](_附件/1773802217751-9d5aba34-2acb-47da-89fa-00-9716f0967aebe46a.png)The process for registering a refund is the same as registering a payment. Click "Register Payment" on the refund invoice and select the corresponding payment method.![image](_附件/1773802358436-34292ca4-cd34-4a88-b794-39-75bb69c0b60e22d8.png)
