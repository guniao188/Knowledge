---
title: Baseline Custom Development Functional Summary
client: Baseline
type: 其他
module: POS
status: 已完成
phase: 上线期
created: 2026-05-12
updated: 2026-05-12
yuque_url: "https://www.yuque.com/xinsuixiaoyao-degek/klxky6/cggx8qe7pwyhbwy1"
tags: [Odoo, POS, 上线期, 客户/Baseline, 已完成, 采购]
---

# Baseline Custom Development Functional Summary

## 1. Baseline Core Business Extensions

The Baseline modules are the core customization layer. They adapt standard Odoo product, sales, purchase, inventory, and manufacturing documents to the customer's real business process. The main purpose is to capture richer product specifications, keep commercial information consistent across departments, and support operational requirements that standard Odoo does not cover out of the box.

### Baseline_expand

This is the main Baseline extension module. It adds a large set of business fields and supporting master data to products, sales orders, purchase orders, partners, product categories, and stock operations.

From a business perspective, this module allows the customer to manage products with detailed technical specifications instead of relying only on product name, internal reference, and category. It includes lighting/product-related attributes such as dimensions, material, voltage, lamp information, beam angle, CRI, casing color, warranty, IP information, and other product classification fields.

It also extends sales and purchase documents with customer-specific commercial and logistics information. Fields such as shipping number, shipping date, company group, margin information, and analytical distribution help sales, purchasing, warehouse, and finance teams work from the same record without maintaining side spreadsheets.
Related database tables:

- heat_sink
- company_group
- casing_color
- product_category
- stock_picking
- stock_move
- place_of_departure
- sale_order
- geographic_area
- product_ip_information
- titl
- cri
- luminaire_material
- sale_order_line
- purchase_order
- product_template
- business_type
- warranty
- iP
- lampholder
- cctk
- optic
- stock_rule
- lamp_brand
- res_partner
- brand
- beam_degres
- technology

### Baseline_expand2

This module adds advanced product search wizards for sales and purchase users.

In standard Odoo, product selection is usually based on name, internal reference, barcode, or category. For this customer, that is not enough because products are selected based on technical parameters. This module lets users search products by specification fields such as size, voltage, lamp type, material, beam degree, CCT, CRI, color, warranty, driver, ballast, and other attributes.

The practical value is that sales and purchasing users can find the correct product faster and with fewer mistakes. It is especially useful when many products have similar names but different technical configurations.
Related database tables:

- sale_order_line
- purchase_order_line
- product_selection_wizard
- product_template
- general_product_selection_wizard
- purchase_product_selection_wizard

### Baseline_expand3

This module adds additional document and product management extensions, including version-related behavior for sales and purchase orders and product logo management.

The version logic helps users track revisions of commercial documents. This is useful when quotations or purchase documents go through several rounds of changes and users need to distinguish the current version from previous ones. Product logo management supports more complete product master data and can be used in product-related display or reporting scenarios.
Related database tables:

- sale_order
- product_logo
- purchase_order
- product_template

### Baseline_expand_4

This module focuses more on operational execution after the commercial document is created. It extends behavior around manufacturing, stock movements, stock valuation, and shipping-related dates.

The business purpose is to keep delivery, inventory, manufacturing, and accounting information aligned. For example, when shipment dates or completion dates are important for reporting and valuation, this module helps ensure downstream records reflect the intended operational date rather than only the system processing date.
Related database tables:

- stock_move
- product_template
- mrp_production

### Baseline_expand_5

This module customizes purchase order confirmation.

Unlike the earlier Baseline modules, it does not mainly add new fields. Its value is in changing what happens when a purchase order is confirmed. This is typically where a customer wants extra validation, additional record updates, or custom downstream behavior before the purchase process can continue.
Related database tables:

- purchase_order

## 2. Sales, Purchasing, Procurement, and Order-Line Management

These modules improve how sales orders, purchase orders, procurement documents, and order lines are created, reviewed, linked, and communicated between departments.

### sale_and_purchase_link

This module improves traceability between sales orders and purchase orders.

For make-to-order or sales-driven purchasing flows, users need to know which purchase order was created for which sales demand. This module strengthens that link, helping sales, purchasing, and operations teams trace customer demand back to supplier procurement and vice versa.
Related database tables:

- sale_order
- purchase_order
- sale_order_line

### sale_remark_expand

This module carries sales order remarks and related information into downstream documents such as delivery orders, purchase orders, manufacturing orders, and stock movements.

In many companies, important customer requirements are entered on the sales order but are easily lost when the process moves to warehouse, purchasing, or production. This customization reduces that risk by passing information forward automatically, so downstream teams can see relevant instructions without manually copying notes.
Related database tables:

- purchase_order_line
- sale_order_line
- stock_move
- stock_rule
- mrp_production

### selecte_supplier_to_purchase

This module allows users to select a specific supplier when creating purchase orders from procurement flows.

When a product has multiple suppliers, standard automated purchasing may not always choose the vendor expected by the business user. This module gives the user more control, making procurement more accurate when vendor choice depends on price, lead time, customer requirement, or project arrangement.
Related database tables:

- sale_order_line
- stock_move
- stock_rule

### sale_stock_restrict

This module adds sales-side restrictions related to stock or project rules.

The purpose is to prevent users from confirming or processing sales in ways that do not match inventory or project-related controls. It helps sales users avoid invalid stock usage and gives operations better control over what can be sold or reserved.
Related database tables:

- sale_order_line
- sale_order
- res_config_settings
- project_project

### purchase_stock_quantity

This module adds stock quantity visibility or stock-related controls to purchasing.

The purpose is to help buyers make purchasing decisions with inventory information available. Instead of purchasing without knowing existing stock conditions, users can consider current or relevant stock quantities during the purchase process.
Related database tables:

- purchase_order_line
- purchase_order

### purchase_line_views

This module adds dedicated views for RFQ lines and purchase order lines.

Purchase users often need to analyze data at line level rather than document level. This module makes it easier to search, compare, and review purchase line information across multiple RFQs or purchase orders, especially for purchasing follow-up and supplier analysis.
Related database tables:

- purchase_order_line

### eg_sale_line_list_view

This module provides a list view for sales order lines.

It helps users review sales line data across orders without opening each sales order one by one. This is useful for checking ordered products, quantities, prices, margins, delivery status, or other line-level information.
Related database tables:

- sale_order_line

### bi_copy_sale_purchase_line

This module allows users to copy sales order lines and purchase order lines.

It reduces repeated manual input when documents contain similar products, quantities, pricing, or descriptions. This improves efficiency and reduces typing errors during order entry.
Related database tables:

- sale_order_line
- purchase_order_line
- sale_order
- purchase_order

### order_line_sequences

This module adds sequence numbers to sales order, purchase order, and delivery order lines.

Line numbers make documents easier to read and discuss. Customers, suppliers, warehouse staff, and internal users can refer to “line 10” or “line 20” instead of describing the product manually. This is especially useful for printed quotations, purchase orders, and delivery documents.
Related database tables:

- sale_order_line
- purchase_order_line
- stock_move
- stock_picking
- purchase_order
- sale_order

## 3. Advance Payments, Down Payments, Invoicing, and Payment Visibility

These modules support payment processes that happen before final invoicing, which is common in project-based, manufacturing, trading, or custom-order businesses.

### account_advance_payment

This module adds advance receipt and advance payment handling to accounting payment forms.

It introduces the concept of marking a payment as an advance payment or advance receipt and links it to corresponding accounting entries. This allows prepaid amounts to be recorded properly and later reconciled against customer invoices or vendor bills.

For finance users, the main benefit is cleaner accounting treatment of prepayments. For sales and purchasing users, it provides better visibility of deposits or prepaid vendor amounts.
Related database tables:

- account_move
- account_payment
- res_partner

### purchase_advance_payment

This module supports vendor advance payments from purchase orders.

It is used when suppliers require payment before shipment, production, or final billing. Users can create and track the advance payment from the purchase process, keeping the prepayment tied to the relevant purchase order.
Related database tables:

- purchase_advance_payment_inv
- purchase_order
- account_payment

### purchase_down_payment

This module supports purchase down payment bills or payment requests linked to purchase orders.

It formalizes the vendor down payment process. Instead of handling vendor prepayment only through manual journal entries, the user can initiate the down payment flow from the purchase order and keep the accounting document connected to the procurement record.
Related database tables:

- purchase_advance_payment_inv
- purchase_order_line
- purchase_order

### sale_advance_payment

This module supports customer advance receipts from sales documents.

It is used when customers pay deposits before delivery or before the final invoice. This helps sales and finance teams track which sales orders have received advance payments and how those amounts should be handled later.
Related database tables:

- sale_order
- account_payment

### payment_bank_charge

This module adds bank charge handling for advance payments and receipts.

In real payment processing, the amount paid by or received from the bank may differ from the business amount because of bank fees. This module helps separate the actual advance amount from the bank charge so accounting records are more accurate.
Related database tables:

- account_payment

### payment_status_in_sale

This module displays payment status and payment details directly on sales orders.

Sales users often need to know whether a customer has paid before arranging delivery or follow-up. Instead of opening invoices and payment records separately, this module brings payment visibility into the sales order, improving coordination between sales, finance, and operations.
Related database tables:

- sale_order
- purchase_order

### amout_to_words

This module converts monetary amounts into words.

This is useful for printed quotations, purchase orders, invoices, payment documents, or approval documents where the amount in words is required for clarity, compliance, or customer/vendor communication.
Related database tables:

- account_move
- sale_order
- purchase_order

### auto_create_bill_invoice

This module automates creation of bills or invoices from stock picking-related flows.

It reduces manual accounting work when the company expects invoices or bills to follow warehouse receipt or delivery confirmation. The benefit is fewer missed billing steps and faster document processing between warehouse and accounting.
Related database tables:

- account_move
- stock_picking

## 4. Approval Workflow and Tier Validation

The approval modules provide a reusable workflow framework and apply it to specific business documents. The goal is to make approvals configurable, traceable, and enforceable inside Odoo instead of relying on offline messages or manual confirmation.

### base_tier_validation

This is the core approval framework.

It provides common concepts such as requesting validation, assigning reviewers, approving, rejecting, restarting validation, and tracking review status. Other modules reuse this foundation to add approval control to expenses, leave requests, and other records.
Related database tables:

- comment_wizard
- tier_definition
- res_users
- res_config_settings
- tier_validation
- tier_review
- mail_message_subtype

### base_tier_validation_formula

This module adds formula-based approval conditions.

It allows approval rules to depend on document values or business conditions. For example, approval could vary by amount, department, user, company, or other document fields. This makes the approval process more flexible than a fixed one-size-fits-all workflow.
Related database tables:

- tier_definition
- tier_validation
- tier_review

### base_tier_validation_forward

This module allows approval tasks to be forwarded to another reviewer.

In real operations, the original approver may be unavailable or the responsibility may need to move to another person. Forwarding prevents approval bottlenecks and keeps the workflow moving.
Related database tables:

- comment_wizard
- tier_validation_forward_wizard
- tier_definition
- tier_validation
- tier_review
- mail_message_subtype

### base_tier_validation_notify

This module improves notification behavior around approvals.

It helps users know when a document requires review, when approval has been completed, or when action is needed. This reduces the chance that approval requests are missed.
Related database tables:

- mail_followers
- tier_validation
- tier_review
- tier_definition
- res_config_settings

### base_tier_validation_server_action

This module connects approval events with Odoo server actions.

It allows custom automation to be executed when a document enters or completes approval. This gives the customer a way to trigger additional business logic without hard-coding every scenario into the approval framework.
Related database tables:

- tier_definition
- tier_review

### hr_expense_tier_validation

This module applies the approval framework to employee expense sheets.

It ensures expense claims are reviewed according to the customer's approval policy before they proceed to accounting or reimbursement.
Related database tables:

- hr_expense
- tier_definition
- hr_expense_sheet
- tier_validation

### hr_time_off_tier_validation   and   time_off_tier_validation

These modules apply approval workflow logic to time-off requests.

They ensure leave applications follow the required approval hierarchy. The modules are useful where time-off approval depends on manager review, HR control, or custom company rules.

## 5. HR, Leave, Overtime, and Payroll

These modules localize and extend Odoo HR to better match the customer's leave, overtime, salary, and payroll practices.

### hr_expand

This module extends leave allocation behavior.

It supports monthly allocation splitting and automatic carry-forward. This is useful when annual leave or other entitlements need to be distributed month by month and unused balances need to be carried forward according to company policy.
Related database tables:

- hr_leave
- hr_leave_allocation

### count_alldays

This module adjusts leave day-counting behavior.

Some companies count leave by calendar days, while others count working days or follow special work-entry rules. This module helps align Odoo's leave duration calculation with the customer's HR policy.
Related database tables:

- hr_leave
- hr_work_entry
- hr_leave_type

### holidays_remaining_leave

This module improves the display of remaining leave balances.

Employees and HR users can see leave availability more conveniently, reducing the need to navigate through multiple HR screens just to confirm remaining entitlement.
Related database tables:

- hr_leave

### hr_holidays_legal_ot

This module manages statutory holidays, shift adjustments, overtime requests, and overtime compensatory leave.

It supports HR processes where public holidays, adjusted working days, overtime, and compensatory leave must be recorded and controlled. This is especially relevant for local compliance and internal attendance management.
Related database tables:

- hr_leaves_legal
- mail_thread
- resource_calendar_leaves
- resource_calendar_attendance
- hr_leaves_legal_line
- hr_ot_request
- mail_thread_main_attachment
- mail_activity_mixin
- analytic_mixin
- hr_work_entry_type
- ir_sequence
- hr_leave_type

### hr_payroll_cn

This module provides China payroll-related support.

It is intended to adapt payroll processing to local payroll requirements, structures, or calculation needs.
Related database tables:

- hr_rule_parameter_value
- hr_contract
- hr_payslip_line
- hr_payslip_worked_days
- hr_payslip
- hr_rule_parameter
- hr_payslip_input_type
- hr_salary_rule_category
- hr_payroll_structure
- hr_salary_rule

### hr_salary_ext

This module supports monthly variable salary imports.

Payroll teams can import or maintain variable salary items such as allowances, bonuses, deductions, reimbursements, or other one-off monthly adjustments. This reduces manual entry during payroll preparation and improves payroll data consistency.
Related database tables:

- hr_payslip
- hr_employee
- hr_salary_extension
- mail_thread

## 6. Inventory, Warehouse, and Stock Governance

These modules improve stock accuracy and control over warehouse adjustment operations.

### inventory_stock_adjustments

This module provides a controlled inventory adjustment process.

Inventory adjustments can directly affect stock value and financial results, so they should not be completely unrestricted. This module adds approval control, adjustment wizards, reporting, and related security rules, helping warehouse and finance teams manage stock corrections in a more governed way.
Related database tables:

- inventory_selection
- inventory_selection_line
- stock_adjustment_report_export
- stock_inventory_line
- stock_quant
- stock_move
- stock_inventory
- ir_module_category
- res_groups
- product_product

### stock_no_negative

This module prevents stock from becoming negative.

It protects inventory accuracy by blocking operations that would consume more stock than available. This is important for warehouse discipline, cost calculation, and reliable inventory reporting.
Related database tables:

- stock_location
- stock_quant
- product_category
- product_template

## 7. Product Images and Product Data Maintenance

These modules improve visual identification of products and reduce manual product-image maintenance.

### product_image_list_view

This module displays product images in product list views.

It is useful when users work with products that have similar names or codes but different appearances. Visual identification reduces selection mistakes.
Related database tables:

- product_product
- product_template

### sale_product_image

This module displays product images on sales and purchase order lines.

It helps users verify that the correct item has been selected and improves readability of commercial or internal documents.
Related database tables:

- sale_order
- purchase_order_line
- sale_order_line
- res_config_settings
- mrp_bom
- purchase_order

### widget_preview_image

This module allows users to preview image fields directly from the interface.

It reduces the need to open full records just to check an image.
Related database tables:

- No dedicated business model/table was found. This module mainly changes web assets, JavaScript behavior, styles, or generic UI behavior.

### product_image_suggestion

This module assists with product image assignment.

Its purpose is to improve product master-data quality by helping users identify or maintain suitable product images.
Related database tables:

- product_image_suggestion
- product_template

### product_import   and   zehntech_product_image_import_from_url

These modules support importing product images from external URLs.

They are useful when suppliers or websites provide product image links. Instead of downloading and uploading images manually, users can bring images into Odoo more efficiently.

## 8. Project Management Extensions

These modules support project data enrichment and standardized project creation.

### project_fields

This module adds customer-specific fields to projects.

It allows project teams to track information that is important to the customer's process but not available in standard Odoo project records.
Related database tables:

- project_project

### project_tasks_from_templates

This module allows projects and tasks to be created from templates.

It is useful for repeatable project types. Instead of creating the same task structure manually every time, users can start from a predefined template, improving consistency and saving setup time.
Related database tables:

- project_stage
- project_sub_task
- project_task_template
- project_task_type
- project_project

## 9. Integrations and Connectors

These modules support external system integration, especially e-commerce integration with WooCommerce.

### ks_base_connector

This is the shared connector foundation.

It provides common structures for products, images, sale orders, workflows, and synchronization configuration. Other connector modules can reuse this foundation instead of rebuilding the same integration logic.
Related database tables:

- sale_order
- res_config_settings
- product_pricelist
- stock_quant
- account_move
- ks_sale_workflow_configuration
- ks_common_product_images
- product_attribute_value
- res_partner
- product_category
- product_product
- product_attribute
- product_template
- ks_message_wizard
- account_journal
- uom_uom

### ks_woocommerce

This module integrates Odoo with WooCommerce.

It supports synchronization of e-commerce products, orders, customers, stock, and delivery-related data. The business purpose is to reduce duplicate data entry between the online store and Odoo, while keeping sales and inventory information aligned.
Related database tables:

- ks_woo_auto_customer_syncing_configuration
- ks_woo_logger
- res_partner
- ks_woo_connector_instance
- ks_message_wizard
- ks_webhooks_configuration
- ks_woo_email_report
- email_entry
- product_pricelist
- account_tax
- account_move
- account_move_line
- ks_woo_product_variant
- product_product
- ks_woo_partner
- sale_order
- sale_order_line
- stock_quant
- product_attribute
- ks_woo_product_attribute
- ks_woo_product_tag
- product_attribute_value
- ks_woo_pro_attr_value
- ks_woo_coupons
- ks_woo_product_category
- product_category
- ks_woo_product_images
- ks_global_record_mapping

## 10. Reporting, Query, and Excel Output

These modules provide reporting and data extraction capabilities beyond standard Odoo screens.

### report_xlsx

This module provides an Excel report framework.

It supports XLSX templates and parameterized report exports. This is useful when users need formatted Excel outputs for management reports, operational reports, reconciliation, or customer-specific report layouts.
Related database tables:

- base_action_param_export_wizard
- ir_actions_report

### query_deluxe

This module allows authorized users to run PostgreSQL queries from Odoo and export or print the results.

It is mainly a technical and administrative tool for diagnostics, ad hoc reporting, data checking, and troubleshooting. Because it can access database information directly, it should be used with proper access control.
Related database tables:

- pdforientation
- querydeluxe
- mail_thread
- mail_activity_mixin
- res_groups
- ir_actions_report

## 11. Web Interface and Usability Improvements

These modules improve daily user experience in Odoo. They do not necessarily change business logic, but they make forms, lists, popups, and relational fields easier and safer to use.

### cr_sticky_views

This module keeps list headers, list footers, form headers, or status bars visible while scrolling.

It is helpful for long lists or complex forms because users can keep context while reviewing many rows or fields.
Related database tables:

- No dedicated business model/table was found. This module mainly changes web assets, JavaScript behavior, styles, or generic UI behavior.

### d100_form_extend   and   full_screen_form_view

These modules improve form viewing space.

They allow users to hide or expand parts of the form layout, especially the chatter area, so data-heavy records can be edited more comfortably.

### dragable_and_resizable_wizard

This module makes popup wizards draggable and resizable.

It improves usability when a wizard contains many fields or when users need to compare popup content with the underlying record.
Related database tables:

- No dedicated business model/table was found. This module mainly changes web assets, JavaScript behavior, styles, or generic UI behavior.

### web_listview_width

This module allows users to adjust list-view column widths.

It is useful when tables contain long product names, references, descriptions, or technical fields.
Related database tables:

- No dedicated business model/table was found. This module mainly changes web assets, JavaScript behavior, styles, or generic UI behavior.

### web_m2x_options   and   rel_create_group_ma

These modules control quick-create behavior on many-to-one and many-to-many fields.

They help improve master-data governance by preventing users from creating incomplete related records directly from dropdown fields.

### auto_save_restrict

This module prevents unwanted automatic saving of incomplete records.

It helps avoid accidental draft data and gives users more control over when records should actually be saved.
Related database tables:

- No dedicated business model/table was found. This module mainly changes web assets, JavaScript behavior, styles, or generic UI behavior.

## Overall Business Value

The custom development is mainly designed to make Odoo fit a more detailed and controlled operating process.

The strongest customization area is product and order management. The customer appears to require rich product specifications, advanced product search, and strong transfer of information from sales into purchasing, warehouse, manufacturing, and accounting. This indicates a business where product configuration, technical accuracy, and cross-department handover are important.

The second major area is financial process support for advance payments and down payments. The system has been extended so that prepayments can be created, tracked, reconciled, and reviewed from sales, purchase, and accounting processes rather than being handled outside the system.

The third area is governance: approvals, inventory restrictions, negative-stock prevention, and controlled inventory adjustments. These modules reduce operational risk and help enforce company rules inside Odoo.

The fourth area is localization and internal management, especially HR leave, overtime, salary imports, and China payroll-related requirements.

Finally, the system includes several usability, reporting, image, and connector modules. These make the system easier to use in daily operations and reduce manual work in reporting, product image maintenance, and e-commerce synchronization.

Overall, these modules work together to turn standard Odoo into a more industry-specific operating platform for the customer, covering sales, purchasing, inventory, manufacturing, finance, HR, reporting, and integration needs.

## Appendix: Complete Database Table Reference

The table names below are the database tables involved in each module. Some wizard tables are transient and may only be used temporarily, but they are included because they are part of the module implementation.

### Baseline_expand

- heat_sink
- company_group
- casing_color
- product_category
- stock_picking
- stock_move
- place_of_departure
- sale_order
- geographic_area
- product_ip_information
- titl
- cri
- luminaire_material
- sale_order_line
- purchase_order
- product_template
- business_type
- warranty
- iP
- lampholder
- cctk
- optic
- stock_rule
- lamp_brand
- res_partner
- brand
- beam_degres
- technology
- shipping_type
- purchase_order_line

### Baseline_expand2

- sale_order_line
- purchase_order_line
- product_selection_wizard
- product_template
- general_product_selection_wizard
- purchase_product_selection_wizard

### Baseline_expand3

- sale_order
- product_logo
- purchase_order
- product_template

### Baseline_expand_4

- stock_move
- product_template
- mrp_production

### Baseline_expand_5

- purchase_order

### account_advance_payment

- account_move
- account_payment
- res_partner

### amout_to_words

- account_move
- sale_order
- purchase_order

### auto_create_bill_invoice

- account_move
- stock_picking

### auto_save_restrict

- No dedicated business model/table was found. The module mainly changes web assets, JavaScript behavior, styles, configuration, or generic UI behavior.

### base_tier_validation

- comment_wizard
- tier_definition
- res_users
- res_config_settings
- tier_validation
- tier_review
- mail_message_subtype

### base_tier_validation_formula

- tier_definition
- tier_validation
- tier_review

### base_tier_validation_forward

- comment_wizard
- tier_validation_forward_wizard
- tier_definition
- tier_validation
- tier_review
- mail_message_subtype

### base_tier_validation_notify

- mail_followers
- tier_validation
- tier_definition

### base_tier_validation_server_action

- tier_definition
- tier_review

### bi_copy_sale_purchase_line

- sale_order_line
- purchase_order_line

### count_alldays

- hr_leave
- hr_work_entry
- hr_leave_type

### cr_sticky_views

- No dedicated business model/table was found. The module mainly changes web assets, JavaScript behavior, styles, configuration, or generic UI behavior.

### d100_form_extend

- No dedicated business model/table was found. The module mainly changes web assets, JavaScript behavior, styles, configuration, or generic UI behavior.

### dragable_and_resizable_wizard

- No dedicated business model/table was found. The module mainly changes web assets, JavaScript behavior, styles, configuration, or generic UI behavior.

### eg_sale_line_list_view

- sale_order_line

### full_screen_form_view

- No dedicated business model/table was found. The module mainly changes web assets, JavaScript behavior, styles, configuration, or generic UI behavior.

### holidays_remaining_leave

- hr_leave

### hr_expand

- hr_leave
- hr_leave_allocation

### hr_expense_tier_validation

- hr_expense
- tier_definition
- hr_expense_sheet
- tier_validation

### hr_holidays_legal_ot

- hr_leaves_legal
- mail_thread
- resource_calendar_leaves
- resource_calendar_attendance
- hr_leaves_legal_line
- hr_ot_request
- mail_thread_main_attachment
- mail_activity_mixin
- analytic_mixin
- hr_work_entry_type
- ir_sequence
- hr_leave_type

### hr_payroll_cn

- hr_rule_parameter_value
- hr_contract
- hr_payslip_line
- hr_payslip_worked_days
- hr_payslip
- hr_rule_parameter
- hr_payslip_input_type
- hr_salary_rule_category
- hr_payroll_structure
- hr_salary_rule

### hr_salary_ext

- hr_payslip
- hr_employee
- hr_salary_extension
- mail_thread

### hr_time_off_tier_validation

- No dedicated business model/table was found. The module mainly changes web assets, JavaScript behavior, styles, configuration, or generic UI behavior.

### inventory_stock_adjustments

- inventory_selection
- inventory_selection_line
- stock_adjustment_report_export
- stock_inventory_line
- stock_quant
- stock_move
- stock_inventory
- ir_module_category
- res_groups

### ks_base_connector

- sale_order
- res_config_settings
- product_pricelist
- stock_quant
- account_move
- ks_sale_workflow_configuration
- ks_common_product_images
- product_attribute_value
- res_partner
- product_category
- product_product
- product_attribute
- product_template
- ks_message_wizard
- account_journal
- uom_uom

### ks_woocommerce

- ks_woo_auto_customer_syncing_configuration
- ks_woo_logger
- res_partner
- ks_woo_connector_instance
- ks_message_wizard
- ks_webhooks_configuration
- ks_woo_email_report
- email_entry
- product_pricelist
- account_tax
- account_move
- account_move_line
- ks_woo_product_variant
- product_product
- ks_woo_partner
- sale_order
- sale_order_line
- stock_quant
- product_attribute
- ks_woo_product_attribute
- ks_woo_product_tag
- product_attribute_value
- ks_woo_pro_attr_value
- ks_woo_coupons
- ks_woo_product_category
- product_category
- ks_woo_product_images
- ks_global_record_mapping
- ks_woo_webhook_logger
- ks_woo_reverse_workflow_configuration
- ks_sale_workflow_configuration
- ks_woo_product_template
- product_template
- product_pricelist_item
- product_combo
- product_combo_item
- product_tag
- ks_woo_meta_mapping
- delivery_carrier
- ks_woo_delivery_carrier
- ks_woo_payment_gateway
- ks_woo_sale_report
- ks_woo_auto_sale_workflow_configuration
- ks_woo_order_status
- ks_woo_auto_product_syncing_configuration
- ks_woo_dashboard
- ks_woo_instance_selection
- map_res_partner_wizard
- map_product_category_wizard
- map_product_attribute_wizard
- map_product_wizard
- map_wizard_line
- ks_woo_reset_credentials
- ks_sales_print_report_wizard
- ks_woo_queue_jobs
- ks_woo_prepare_to_export
- ks_woo_update_product_configuration
- ks_woo_product_configuration
- ks_woo_instance_operations
- ir_module_category
- res_groups
- res_users
- ir_sequence
- stock_picking
- ks_woocommerce_instances
- ir_actions_report

### order_line_sequences

- sale_order_line
- purchase_order_line
- stock_move
- stock_picking

### payment_bank_charge

- account_payment

### payment_status_in_sale

- sale_order
- purchase_order

### product_image_list_view

- No dedicated business model/table was found. The module mainly changes web assets, JavaScript behavior, styles, configuration, or generic UI behavior.

### product_image_suggestion

- product_image_suggestion
- product_template

### product_import

- product_import
- product_template
- product_product

### project_fields

- project_project

### project_tasks_from_templates

- project_stage
- project_sub_task
- project_task_template
- project_task_type
- project_project

### purchase_advance_payment

- purchase_advance_payment_inv
- purchase_order
- account_payment

### purchase_down_payment

- purchase_advance_payment_inv
- purchase_order_line
- purchase_order

### purchase_line_views

- purchase_order_line

### purchase_stock_quantity

- purchase_order_line
- purchase_order

### query_deluxe

- pdforientation
- querydeluxe
- mail_thread
- mail_activity_mixin
- res_groups
- ir_actions_report

### rel_create_group_ma

- res_users
- res_groups

### report_xlsx

- base_action_param_export_wizard
- ir_actions_report

### sale_advance_payment

- sale_order
- account_payment

### sale_and_purchase_link

- sale_order
- purchase_order

### sale_product_image

- sale_order
- purchase_order_line
- sale_order_line
- res_config_settings
- mrp_bom

### sale_remark_expand

- purchase_order_line
- sale_order_line
- stock_move
- stock_rule
- mrp_production

### sale_stock_restrict

- sale_order_line
- sale_order
- res_config_settings
- project_project

### selecte_supplier_to_purchase

- sale_order_line
- stock_move
- stock_rule

### stock_no_negative

- stock_location
- stock_quant
- product_category
- product_template

### time_off_tier_validation

- tier_definition
- hr_leave
- tier_validation

### web_listview_width

- No dedicated business model/table was found. The module mainly changes web assets, JavaScript behavior, styles, configuration, or generic UI behavior.

### web_m2x_options

- ir_http
- ir_config_parameter

### widget_preview_image

- No dedicated business model/table was found. The module mainly changes web assets, JavaScript behavior, styles, configuration, or generic UI behavior.

### zehntech_product_image_import_from_url

- product_template
- product_import
