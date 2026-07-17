---
title: "mrp_material_check"
source: "https://apps.odoo.com/apps/modules/19.0/mrp_material_check"
author:
  - "[[Randy Nguyen]]"
published:
created: 2026-07-16
description:
tags:
  - "clippings"
---
![](https://apps.odoocdn.com/web/image/loempia.module/322250/icon_image/84x84?unique=750c59d)

## MRP Material Check

by [Randy Nguyen](https://apps.odoo.com/apps/modules/browse?author=Randy%20Nguyen)

Odoo

| **Versions** | [17.0](https://apps.odoo.com/apps/modules/17.0/mrp_material_check) [18.0](https://apps.odoo.com/apps/modules/18.0/mrp_material_check) 19.0 |
| --- | --- |

You bought this module and need **support**? [Click here!](https://apps.odoo.com/apps/support/322250)

| **Versions** | [17.0](https://apps.odoo.com/apps/modules/17.0/mrp_material_check) [18.0](https://apps.odoo.com/apps/modules/18.0/mrp_material_check) 19.0 |
| --- | --- |

![MRP Material Check Icon](https://apps.odoocdn.com/apps/assets/19.0/mrp_material_check/icon.png?80c6415)

MRP Material Check

✓ Community ✓ Enterprise

Check Modes

2

🛡️

Odoo Version

19.0

⚡

License

LGPL-3

🔓

Dependency

mrp

📦[Contact / Support · nextstep.vina@gmail.com](mailto:nextstep.vina@gmail.com)Warn Mode Block Mode Free Forever

#### MRP Material Check

Stop negative stock from silently corrupting your books. A zero-config module that intercepts the **Produce** button on manufacturing orders and shows a clear popup listing **exactly which components are short** — with two modes: **Warn** (anyone can continue) and **Block** (only Managers can bypass).

😓 The Problem

- ✗ Odoo lets you click "Produce" even when components are completely out of stock — creating negative inventory instantly.
- ✗ Negative stock flows straight into accounting entries — your COGS and inventory valuations become unreliable.
- ✗ Operators don't know which component is short or by how much — they find out only after the damage is done.
- ✗ No role-based protection — any warehouse user can accidentally (or unknowingly) validate an order with zero stock.

🎯 The Solution

- ✓ Intercepts "Produce All" before any stock move — checks each component's quantity at the source location in real time.
- ✓ Popup table lists each short component: **Needed / In Stock / Shortage / Unit** — no guesswork.
- ✓ **Warn mode:** shows the popup, operator decides. **Block mode:** only Manufacturing Managers can press "Continue Anyway".
- ✓ Zero configuration — install, choose your mode in Manufacturing Settings, and go.

![MRP Material Check Demo](https://apps.odoocdn.com/apps/assets/19.0/mrp_material_check/banner.gif?80c6415)

#### Key Features

⚠️

Real-time component check — each shortage line shows Needed / In Stock / Shortage / Unit before production starts.

🛡️

Block mode — locks out regular operators; only Manufacturing Managers can override the shortage gate.

🔔

Warn mode — shows the popup with full detail but lets the operator decide to continue, preserving flexibility.

⚙️

One setting in Manufacturing › Configuration › Settings — switch between Warn and Block at any time.

📍

Location-aware — checks stock at the move's actual source location, not just global on-hand.

🔓

100% Free · LGPL-3 — only requires the standard `mrp` module. No paid tiers, no expiry.

#### Setup Guide

1) Place the **mrp\_material\_check** folder in your Odoo custom addons directory and restart the server.

2) Enable Developer Mode — go to **Settings → Activate Developer Mode**, then click **Apps → Update Apps List**.

3) Search for **"MRP Material Check"** in Apps and click **Install**.

4) Go to **Manufacturing → Configuration → Settings** and choose your preferred mode under **Insufficient Material Behaviour**.

![Manufacturing Settings — Insufficient Material Behaviour](https://apps.odoocdn.com/apps/assets/19.0/mrp_material_check/screenshots/01-settings-warn-mode.png?80c6415)

Manufacturing Settings — "Insufficient Material Behaviour" dropdown shows Warn and Block options

5) Open any confirmed Manufacturing Order with missing components and click **Produce All**.

![Confirmed Production Order with Not Available components](https://apps.odoocdn.com/apps/assets/19.0/mrp_material_check/screenshots/04-confirmed-production.png?80c6415)

Confirmed production order — "Component Status: Not Available" is already visible before clicking Produce All

6) The popup appears instantly, listing each short component with Needed / In Stock / Shortage. In **Warn mode** you can continue; in **Block mode** only Managers see "Continue Anyway".

![Shortage Popup — Warn Mode](https://apps.odoocdn.com/apps/assets/19.0/mrp_material_check/screenshots/05-warn-mode-shortage-popup.png?80c6415)

Warn mode popup — shows Demo Steel Rod: Needed 3.00 / In Stock 0.00 / Shortage 3.00 with "Continue Anyway" button

#### Frequently Asked Questions

In **Warn mode**, any user sees the shortage popup but can click "Continue Anyway" to proceed regardless. In **Block mode**, the "Continue Anyway" button is only visible to users who hold the **Manufacturing Manager** group. Regular operators see a lock message and must contact a manager.

The module checks `qty_available` at the move's specific **source location** (e.g. WH/Stock), not the global on-hand. Unit-of-measure conversion is applied automatically when the move's UoM differs from the product's base UoM.

No. The module only intercepts `button_mark_done()` on `mrp.production`. All other workflows (backorder creation, immediate transfer wizard, work orders, MPS) are untouched. Uninstalling removes the check cleanly with no data left behind.

Yes — the mode is stored as a system parameter. Go to **Manufacturing → Configuration → Settings → Insufficient Material Behaviour** and change the dropdown any time. The change takes effect immediately on the next production order.

Nothing extra happens. The module exits immediately and Odoo's standard production validation proceeds as normal — no popup, no delay.

#### Support

- [Email support: **nextstep.vina@gmail.com**](mailto:nextstep.vina@gmail.com)
- **Response time:** We aim to respond within 1–2 business days. Please include your Odoo version and a description of the issue.
- **License:** LGPL-3 — free to use, modify, and redistribute.

| **Availability** | Odoo Online  Odoo.sh  On Premise |
| --- | --- |
| **Odoo Apps Dependencies** | • Manufacturing (mrp)   • Inventory (stock)   • Discuss (mail) |
| **Lines of code** | 163 |
| **Technical Name** | `                         mrp_material_check` |
| **License** | LGPL-3 |