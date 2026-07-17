---
title: "advanced_mrp_ai"
source: "https://apps.odoo.com/apps/modules/19.0/advanced_mrp_ai"
author:
  - "[[Pokutsoft]]"
published:
created: 2026-07-15
description:
tags:
  - "clippings"
---
![](https://apps.odoocdn.com/web/image/loempia.module/317356/icon_image/84x84?unique=ceb80ac)

## MRP AI: Scheduling, Forecast, OEE & IoT

by [Pokutsoft https://pokutsoft.com/](https://apps.odoo.com/apps/modules/browse?author=Pokutsoft)

Odoo

## $ 159.12

| **Versions** | [18.0](https://apps.odoo.com/apps/modules/18.0/advanced_mrp_ai) 19.0 |
| --- | --- |

You bought this module and need **support**? [Click here!](https://apps.odoo.com/apps/support/317356)

| **Availability** | Odoo Online  Odoo.sh  On Premise |
| --- | --- |
| **Odoo Apps Dependencies** | • Inventory (stock)   • Manufacturing (mrp)   • Discuss (mail) |
| **Lines of code** | 1258 |
| **Technical Name** | `                         advanced_mrp_ai` |
| **License** | OPL-1 |
| **Website** | [https://pokutsoft.com/](https://pokutsoft.com/) |

| **Versions** | [18.0](https://apps.odoo.com/apps/modules/18.0/advanced_mrp_ai) 19.0 |
| --- | --- |

![MRP AI for Odoo banner](https://apps.odoocdn.com/apps/assets/19.0/advanced_mrp_ai/banner.png?a4830c0)

## MRP AI for Odoo

Plan, forecast and measure your shop floor: a **finite-capacity scheduler**, a real **statistical demand-forecasting** engine, **OEE / MTBF / MTTR** analytics and a working **shop-floor IoT** telemetry endpoint — all built on the standard **mrp** app, multi-plant aware.

Finite-Capacity SchedulingDemand Forecasting OEE / MTBF / MTTRShop-floor IoTOdoo 18 & 19

## What It Does

MRP AI adds four advanced manufacturing capabilities to Odoo, each implemented as real working software. The finite-capacity scheduler forward-loads your work orders against each work centre's working-time calendar and parallel capacity using a critical-ratio or priority dispatch rule, so planned start/finish dates never exceed real capacity. The forecasting engine trains genuine statistical models on your sales or production history per product. The analytics layer computes OEE and reliability metrics directly from work-order durations and downtime logs. The IoT endpoint ingests and processes machine telemetry end to end.

## Finite-Capacity Scheduler

Forward finite-loading packs operations into the real availability windows of each work centre, respecting the number of parallel lanes. Two dispatch rules are built in: **Critical Ratio** (time-remaining / processing-time, so jobs at risk of being late go first) and **Priority**. Each run writes planned start/finish back to the work orders and produces a per-work-centre load and bottleneck report. Scope a run to one plant or run it across all sites.

## Statistical Demand Forecasting

A dependency-free forecasting engine with three real models: **linear-trend regression** (ordinary least squares), **simple exponential smoothing** with automatic smoothing-constant selection, and **additive Holt-Winters** triple exponential smoothing for seasonal demand. History is aggregated into monthly buckets from your `sale.order.line` or `mrp.production` data per product; the engine picks the right model for the data, trains it, projects a horizon and reports MAE / RMSE / MAPE accuracy.

## OEE / MTBF / MTTR Analytics

Overall Equipment Effectiveness — Availability × Performance × Quality — is computed per work centre from work-order durations and `mrp.workcenter.productivity` logs. Reliability metrics MTBF (mean time between failures) and MTTR (mean time to repair) are derived from the failure/repair intervals, and from `maintenance.request` when the Maintenance app is installed.

## Shop-floor IoT Integration

A real HTTP JSON endpoint — `POST /mrp_iot/telemetry` — ingests machine telemetry into an `mrp.iot.reading` log and processes it end to end: a **fault** reading blocks the work centre and opens a downtime record; a **recovery** reading unblocks it and closes the record. The endpoint is secured by an optional shared-key header, and an MQTT broker can forward messages to it via a thin bridge. Physical hardware is out of scope; the software ingestion and processing pipeline is complete and testable with a simulated payload.

## Key Features

- Finite-capacity forward-loading scheduler (critical-ratio / priority rules)
- Per-work-centre parallel capacity and ideal cycle time
- Work-centre load & bottleneck report per scheduling run
- Holt-Winters, linear-regression and exponential-smoothing demand forecasting
- Forecast accuracy metrics (MAE / RMSE / MAPE)
- OEE = Availability × Performance × Quality from real logs
- MTBF / MTTR reliability metrics
- HTTP JSON shop-floor IoT telemetry endpoint with fault/recovery handling
- Multi-plant / multi-warehouse scoping and cross-plant capacity view
- Pure-Python, fully unit-tested calculation engines (no scikit-learn dependency)

## Requirements & Notes

Built on the standard Odoo **mrp** and **stock** apps; no Enterprise dependency. Maintenance integration activates automatically when the Maintenance app is installed. The forecasting maths use only the Python standard library. Compatible with Odoo 18 & 19.

## Screenshots

**Finite-Capacity Scheduling run** — per-work-centre available vs loaded minutes, utilisation and bottleneck flag.

![MRP AI for Odoo — finite-capacity scheduling run with work-centre load and utilisation](https://apps.odoocdn.com/apps/assets/19.0/advanced_mrp_ai/screenshot_1.png?a4830c0)

**Statistical Demand Forecast** — selected model, MAPE / RMSE accuracy and the projected monthly horizon.

![MRP AI for Odoo — demand forecast with model, MAPE, RMSE and forecast lines](https://apps.odoocdn.com/apps/assets/19.0/advanced_mrp_ai/screenshot_2.png?a4830c0)

**OEE / MTBF / MTTR analytics** — Availability × Performance × Quality and reliability metrics per work centre.

![MRP AI for Odoo — OEE, availability, performance, quality, MTBF and MTTR per work centre](https://apps.odoocdn.com/apps/assets/19.0/advanced_mrp_ai/screenshot_3.png?a4830c0)

**Shop-floor IoT readings** — ingested telemetry with fault / recovery / heartbeat / metric kinds, all processed.

![MRP AI for Odoo — shop-floor IoT telemetry readings with fault and recovery processing](https://apps.odoocdn.com/apps/assets/19.0/advanced_mrp_ai/screenshot_4.png?a4830c0)

**MRP AI menu** — one place for scheduling, forecasting, OEE analytics and IoT, inside the standard Manufacturing app.

![MRP AI for Odoo — MRP AI menu inside the Manufacturing app](https://apps.odoocdn.com/apps/assets/19.0/advanced_mrp_ai/screenshot_5.png?a4830c0)

Update date: 2026-07-02

| **Availability** | Odoo Online  Odoo.sh  On Premise |
| --- | --- |
| **Odoo Apps Dependencies** | • Inventory (stock)   • Manufacturing (mrp)   • Discuss (mail) |
| **Lines of code** | 1258 |
| **Technical Name** | `                         advanced_mrp_ai` |
| **License** | OPL-1 |
| **Website** | [https://pokutsoft.com/](https://pokutsoft.com/) |

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