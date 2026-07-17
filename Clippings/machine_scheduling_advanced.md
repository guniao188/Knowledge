---
title: "machine_scheduling_advanced"
source: "https://apps.odoo.com/apps/modules/19.0/machine_scheduling_advanced"
author:
  - "[[Micra digital]]"
published:
created: 2026-07-15
description:
tags:
  - "clippings"
---
![](https://apps.odoocdn.com/web/image/loempia.module/296577/icon_image/84x84?unique=f1b27a0)

## Advanced Manufacturing Scheduling

by [Micra digital https://www.micra.digital/](https://apps.odoo.com/apps/modules/browse?author=Micra%20digital)

Odoo

## $ 48.57

| **Versions** | [17.0](https://apps.odoo.com/apps/modules/17.0/machine_scheduling_advanced) [18.0](https://apps.odoo.com/apps/modules/18.0/machine_scheduling_advanced) 19.0 |
| --- | --- |

You bought this module and need **support**? [Click here!](https://apps.odoo.com/apps/support/296577)

| **Availability** | Odoo Online  Odoo.sh  On Premise |
| --- | --- |
| **Odoo Apps Dependencies** | • Inventory (stock)   • Manufacturing (mrp)   • Discuss (mail)   • Employees (hr) |
| **Lines of code** | 1026 |
| **Technical Name** | `                         machine_scheduling_advanced` |
| **License** | OPL-1 |
| **Website** | [https://www.micra.digital/](https://www.micra.digital/) |

| **Versions** | [17.0](https://apps.odoo.com/apps/modules/17.0/machine_scheduling_advanced) [18.0](https://apps.odoo.com/apps/modules/18.0/machine_scheduling_advanced) 19.0 |
| --- | --- |

## Advanced Machine Scheduling

Advanced Gantt scheduling, machine optimization, and breakdown handling to improve production visibility, reduce downtime impact, and maximize manufacturing efficiency.

Gantt Scheduling Optimization Breakdown Handling Wait & Repair Tracking

## Quick Preview

### Smart Breakdown Decision System

![](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/8.png?93dd2a1)

**Intelligent Repair vs Relocate Analysis**  
When a machine breaks down, the system does not just stop production. It automatically compares **waiting for repair**, **relocating to another machine**, and **moving produced quantity forward**. The planner can instantly see total delay, estimated production time, and time saved, allowing the best decision within seconds.

![](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/12.png?93dd2a1)

**Automatic Breakdown Tracking & History**  
Every machine failure is recorded automatically with breakdown reason, time, and relocation details. Managers can clearly track machine reliability, maintenance issues, and operator actions directly inside the Workcenter screen. This helps improve maintenance planning and prevents repeated production losses.

![](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/15.png?93dd2a1)

**Automatic Production Rescheduling**  
After relocation or conflict, the planning board updates automatically. Operations shift to available machines and the workflow continues without manual re-planning. This ensures uninterrupted production, reduced idle time, and maximum utilization of factory resources.

## Why This Module?

Advanced Machine Scheduling enhances manufacturing planning with intelligent machine scheduling, a real-time Gantt view, optimization tools, and breakdown management to minimize production delays.

### Advanced Gantt View (Machine Scheduling)

- Machine-level scheduling with clear timelines
- Easy visibility of overlaps and delays
- Completion time calculation per machine

### Manual & Automatic Optimization

- Optimize machine allocation to reduce idle time
- Smarter scheduling decisions with real-time view
- Better utilization of work centers

### Breakdown Management & Relocation

- Handle machine failures without losing visibility
- Relocate operations to alternate machines
- Partial quantity movement during breakdown

### Wait & Repair Time Tracking

- Track waiting and repair time for analysis
- Improve maintenance planning
- Reduce downtime impact with data

#### Work Center Enhancements

Each Work Center can show last breakdown time, breakdown reason, and current machine status to support faster decision-making.

#### Key Benefits

- Improved production visibility
- Reduced downtime impact
- Smarter resource allocation
- Better decisions with real-time data
- Higher manufacturing efficiency

### Setup and Guide Steps

This section explains the complete workflow from selecting alternate workcenters to handling breakdowns, relocation, and auto-scheduling using the Machine Schedule (Gantt) view.

![Step 1](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/1.png?93dd2a1)

**Step 1 — Configure Alternate Workcenters:**  
Open **Manufacturing → Configuration → Work Centers**, select a workcenter, and define the **Alternative Workcenter**. This ensures that if the current machine is unavailable (breakdown/busy), the system can relocate operations smoothly without blocking the manufacturing flow.

![Step 2](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/2.png?93dd2a1)

**Step 2 — Confirm the Manufacturing Order:**  
Create and **confirm** a Manufacturing Order so operations are generated. After confirmation, navigate to **Planning → Machine Schedule** to view and manage the live timeline of the operations.

![Step 3](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/3.png?93dd2a1)

**Step 3 — Review the Custom Gantt Flow:**  
The system displays a **custom Gantt view** for Manufacturing Orders. It visualizes the complete sequence of operations, and arrows show the **correct process flow** across machines so planners can instantly understand dependencies and the next operation.

![Step 4](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/4.png?93dd2a1)

**Step 4 — Open the Machine Allocation:**  
In the Gantt view, select the machine block (workcenter operation) and click **Edit**. This is where you can manage scheduling decisions, report issues, or relocate work if required.

![Step 5](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/5.png?93dd2a1)

**Step 5 — Report a Machine Problem:**  
If the selected workcenter (machine) is facing a breakdown or maintenance issue, click **Report Problem**. This starts the breakdown workflow and prevents incorrect production starts on a failed machine.

![Step 6](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/6.png?93dd2a1)

**Step 6 — Fill Breakdown Details in Popup:**  
A popup wizard opens with fields like breakdown reason, notes, and timing details. This ensures the breakdown is properly recorded and visible to planners/operators for quick action.

![Step 7](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/7.png?93dd2a1)

**Step 7 — Relocate Remaining Quantity:**  
Scroll down and enable **Relocate remaining product**. Choose another workcenter (machine) manually, or click **Find Optimum** to let the system suggest the best machine based on availability and efficiency.

![Step 8](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/8.png?93dd2a1)

**Step 8 — Understand the Time Analysis:**  
The system displays a detailed comparison including **waiting time** and **workcenter efficiency**. If you also move produced quantity to the next operation, the wizard shows the **time saved** for the overall process chain.

![Step 9](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/9.png?93dd2a1)

**Step 9 — Confirm the Resolution:**  
Click **Confirm Resolution**. The system relocates the remaining work to the selected workcenter and updates the operation plan without breaking the manufacturing sequence.

![Step 10](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/10.png?93dd2a1)

**Step 10 — Verify Changes in Gantt View:**  
Back in the Gantt view, the MO operation is relocated (example: moved to **Machine D**), and if enabled, produced product is pushed forward to the next operation (example: **Machine B**). Arrows update to keep the correct operation flow.

![Step 11](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/11.png?93dd2a1)

**Step 11 — Verify Inside Manufacturing Order:**  
Open the Manufacturing Order and check operations. You will see the **next operation started** (if moved forward) and the relocated workcenter is displayed so production teams can follow the updated plan.

![Step 12](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/12.png?93dd2a1)

**Step 12 — Breakdown Alert on Workcenter:**  
Open the reported workcenter: an alert confirms breakdown occurred. Details like reason and notes are stored in **Breakdown Info**, keeping a clear history for maintenance and planning audits.

![Step 13](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/13.png?93dd2a1)

**Step 13 — Prevent Start on Broken Machine:**  
If a user tries to start the manufacturing process on a broken machine, the system blocks the action and shows a popup message. This prevents wrong production execution and avoids inaccurate reporting.

![Step 14](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/14.png?93dd2a1)

**Step 14 — Handle Allocation Conflicts:**  
When one MO is already scheduled on a machine and the user assigns another MO on the same time slot, a popup appears asking whether to **Auto Schedule** or **Manually Schedule** to a different time.

![Step 15](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/15.png?93dd2a1)

**Step 15 — Auto Schedule the Operation:**  
On selecting **Auto Schedule**, the module automatically finds the next available time slot for the machine and reschedules the operation accordingly, ensuring no overlap and maintaining planning accuracy.

![Step 16](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/16.png?93dd2a1)

**Step 16 — Busy Machine Relocation Prompt:**  
If a user tries to start an operation while the machine is already busy, the system shows a relocation popup suggesting to move the operation to another workcenter. This ensures production continuity and reduces delays.

## Requirements & Compatibility

#### Compatible With

- Odoo (Manufacturing / MRP)
- Work Centers
- Manufacturing Orders (Operations)

#### Core Capabilities

- Machine-level scheduling (Gantt)
- Optimization tools (manual/auto)
- Breakdown handling + relocation

#### Tracking & Insights

- Wait & repair time tracking
- Work center breakdown info
- Improved decision-making

Tip: Use the screenshots tab to show your Gantt view, optimization button, breakdown wizard, and relocation flow clearly.

## Support & Contact

### Email Support

Need help with installation or configuration? Contact our support team.

[support@micradigital.com](mailto:support@yourcompany.com?subject=Advanced%20Machine%20Scheduling%20Support)

![Micra Digital Logo](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/screenshots/logoo.png?93dd2a1)

### Official Website

Explore more Odoo modules, solutions and services from our team.

https://www.micra.digital

If links are not clickable due to Odoo App Store security policy, please copy and paste the URL into your browser.

| **Availability** | Odoo Online  Odoo.sh  On Premise |
| --- | --- |
| **Odoo Apps Dependencies** | • Inventory (stock)   • Manufacturing (mrp)   • Discuss (mail)   • Employees (hr) |
| **Lines of code** | 1026 |
| **Technical Name** | `                         machine_scheduling_advanced` |
| **License** | OPL-1 |
| **Website** | [https://www.micra.digital/](https://www.micra.digital/) |

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