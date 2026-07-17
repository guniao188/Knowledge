---
title: "planning_drag_generic_19"
source: "https://apps.odoo.com/apps/modules/19.0/planning_drag_generic_19"
author:
  - "[[Armonia]]"
published:
created: 2026-07-15
description:
tags:
  - "clippings"
---
![](https://apps.odoocdn.com/web/image/loempia.module/309969/icon_image/84x84?unique=791676d)

## Manufacturing Planning Drag (Generic)

by [Armonia mailto:armonia.odoo@gmail.com](https://apps.odoo.com/apps/modules/browse?author=Armonia)

Odoo

## $ 145.71

You bought this module and need **support**? [Click here!](https://apps.odoo.com/apps/support/309969)

Overview

## Everything your shop floor needs to plan production

Standard Odoo MRP tells you what to make — this module tells you in what order, where each job stands, and what to do next.

⠿

### Drag & Drop Sequencer

Reorder manufacturing orders by dragging rows. The sequence drives automatic scheduling of all work orders across your full MO tree.

🏭

### Work Center Columns

One column per work center shows real-time WO status with color-coded indicators. Up to 16 work centers visible simultaneously.

⚡

### Rush Priority

Mark one order as Rush to instantly push it to position #1. All its work orders get top scheduling priority across every work center.

🔬

### Micro Planning by WC

Fine-tune the queue within each individual work center — reorder jobs exactly as the operator will execute them.

📊

### Planning Report

Per-work-center dashboard showing planned vs. produced quantities, order count, and today's jobs — filterable by date.

⚙️

### Auto Scheduling

Switch to automatic mode and let a configurable cron re-apply the sequence every 15 minutes, respecting workcenter calendars.

---

Feature 1

## The Planning Sequencer

Your command center. Every open manufacturing order appears as a row — drag to reprioritize, read status without opening a single form.

● Pending

◐ On going

✓ Completed

× Cancelled

— N/A

![Planning Sequencer list view showing MOs with work center status columns](https://apps.odoocdn.com/apps/assets/19.0/planning_drag_generic_19/images/screenshot_sequencer.png?1a7a569)

01

#### Real-time status across all work centers

Each row is a manufacturing order. Each column is a work center. The colored dot shows exactly where that job stands — no drilling into forms required. Drag the handle on the left to reprioritize instantly.

![Drag handles visible on planning rows](https://apps.odoocdn.com/apps/assets/19.0/planning_drag_generic_19/images/screenshot_drag.png?1a7a569)

02

#### Drag to resequence, Apply to reschedule

Grab any row and drop it in the new position. Hit **Apply schedule now** to push dates and queue numbers to all pending work orders following your new sequence.

---

Feature 2

## Rush Priority

When a customer calls and needs their order today, one click makes it happen.

⚡ Rush

### One order. Maximum priority. Instantly.

Mark any open planning row as Rush and it jumps to position #1. The system automatically clears Rush from any previously prioritized order — there can only be one. All work orders in the entire MO tree (including child MOs from multi-level BOMs) are scheduled first.

![Rush button tooltip visible on planning row](https://apps.odoocdn.com/apps/assets/19.0/planning_drag_generic_19/images/screenshot_rush.png?1a7a569)

03

#### One click, one Rush — enforced by the system

The Rush button appears on every row. Setting it on one order automatically removes it from any other, keeping planning unambiguous. The ⚡ icon marks the rush order clearly across all views.

---

Feature 3

## Micro Planning by Work Center

The global sequence tells each work center its priority order. Micro planning lets supervisors fine-tune the queue within their own station.

![Micro planning by work center modal dialog](https://apps.odoocdn.com/apps/assets/19.0/planning_drag_generic_19/images/screenshot_micro.png?1a7a569)

04

#### Per-work-center queue control

Open the Micro Planning wizard, select a work center, and reorder its jobs independently. Apply the micro schedule to stamp precise start/end times on each work order, respecting the workcenter's working calendar.

### Calendar-aware scheduling

Work order dates are calculated using each workcenter's working hours and leave calendar, so planned times are realistic.

### Multi-level MO support

Works across root MO and all linked child MOs (semi-finished products). The full production tree is always considered.

---

Feature 4

## Planning Report

A per-work-center summary that answers the most important question every shift: how much did we plan versus how much did we actually produce?

Per WC

Planned qty

Per WC

Produced qty

Per WC

Order count

Per WC

Today's jobs

![Planning Report kanban view with per-workcenter cards](https://apps.odoocdn.com/apps/assets/19.0/planning_drag_generic_19/images/screenshot_report.png?1a7a569)

05

#### Work center cards — planned vs. produced

Each card shows the work center's planned quantity, produced quantity, active order count, and a breakdown of pending vs. done work orders. Filter by Today, this week, or any date range.

---

Configuration

## Settings

All options are accessible from Manufacturing > Settings. No technical configuration required.

| Setting | Default | Description |
| --- | --- | --- |
| Scheduling Mode | Manual | Manual: apply on demand. Automatic: cron runs every 15 min. |
| Align reservations with sequence | On | Unreserves and re-assigns stock components following planning order so earlier rows consume available stock first. |
| Reservation scope | Root MO + linked MOs | Whether reservation ranking applies to the full MO tree or only the root order. |
| Mark first row as Urgent | On | Sets standard MO priority to Urgent for the first open planning row, Normal for the rest. |
| Use workcenter calendar | On | Computes work order dates respecting each workcenter's attendance and leave calendar. |
| Cron always replans from now | Off | When in auto mode, re-anchors all scheduling from current time on every cron run. |

Get in touch

## Questions or want a live demo?

We're happy to walk you through the module with your own data. No pressure — just a real look at how it works.

✉️

### Contact us

For questions, support requests or custom development inquiries, reach us at:

[armonia.odoo@gmail.com](mailto:armonia.odoo@gmail.com)

📅

### Schedule a demo

See the module live — drag & drop sequencing, Rush priority, micro planning and the report — all in a real Odoo 19 instance.

[Request a demo →](mailto:armonia.odoo@gmail.com?subject=Demo%20request%20-%20Manufacturing%20Planning%20Drag&body=Hi%2C%20I%27d%20like%20to%20schedule%20a%20demo%20of%20the%20Manufacturing%20Planning%20Drag%20module.)

| **Availability** | Odoo Online  Odoo.sh  On Premise |
| --- | --- |
| **Odoo Apps Dependencies** | • Manufacturing (mrp)   • Inventory (stock)   • Discuss (mail) |
| **Lines of code** | 2190 |
| **Technical Name** | `                         planning_drag_generic_19` |
| **License** | OPL-1 |
| **Website** | [mailto:armonia.odoo@gmail.com](mailto:armonia.odoo@gmail.com) |

```
Odoo Proprietary License v1.0

This software and associated files (the "Software") may only be used (executed,
modified, executed after modifications) if you have purchased a valid license
from the authors, typically via Odoo Apps, or if you have received a written
agreement from the authors of the Software (see the COPYRIGHT file).

You may develop Odoo modules that use the Software as a library (typically
by depending on it, importing it and using its resources), but without copying
any source code or material from the Software. You may distribute those
modules under the license of your choice, provided that this license is
compatible with the terms of the Odoo Proprietary License (For example:
LGPL, MIT, or proprietary licenses similar to this one).

It is forbidden to publish, distribute, sublicense, or sell copies of the Software
or modified copies of the Software.

The above copyright notice and this permission notice must be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
```