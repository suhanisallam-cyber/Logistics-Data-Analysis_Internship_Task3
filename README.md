# Advanced Data Analysis & Visualization in Logistics

##  Project Overview

This project focuses on performing advanced Exploratory Data Analysis (EDA) and data visualization on logistics and supply chain shipment data.
The analysis was performed to identify delivery performance patterns, warehouse-level bottlenecks, transportation cost drivers, and the relationship
between shipment weight and transport cost.

The project was completed as **Week 3 Internship Task – Advanced EDA & Visualization**.

##  Project Objectives

- Perform Exploratory Data Analysis (EDA) on logistics shipment data.
- Analyze delivery time and shipment performance.
- Compare on-time and delayed shipments across warehouses.
- Analyze transportation cost patterns.
- Study the relationship between shipment weight and transportation cost.
- Create meaningful visualizations for logistics performance analysis.
- Generate operational insights from the analytical results.

##  Technologies & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

##  Dataset Overview
The project uses a simulated logistics dataset containing **500 shipment transactions** across different regional warehouse origins.

### Key Variables

| Variable | Description |
|---|---|
| `Shipment_ID` | Unique tracking identifier for each shipment |
| `Warehouse_Origin` | Regional warehouse from which the shipment was dispatched |
| `Transport_Mode` | Transportation mode such as Road, Air, Rail, or Maritime |
| `Shipment_Weight_KG` | Weight of the shipment in kilograms |
| `Delivery_Time_Days` | Shipment transit/delivery duration |
| `Transport_Cost_USD` | Transportation cost of the shipment |
| `On_Time_Status` | Indicates whether the shipment was On-Time or Delayed |

The report defines shipments with transit time greater than 6 days as delayed. :contentReference[oaicite:1]{index=1}

##  Exploratory Data Analysis

The project performs analysis of:

- Delivery time distribution
- Warehouse performance
- On-time vs delayed shipments
- Transportation cost
- Shipment weight
- Relationship between shipment weight and transportation cost
- Transportation mode performance

##  Visualizations

The analysis includes visualizations such as:

### 1. Delivery Time Distribution

A distribution visualization was created to understand the spread of shipment delivery times and identify potentially delayed shipments.

### 2. Warehouse Performance

Warehouse-level performance was visualized by comparing on-time and delayed shipments across regional warehouses.

### 3. Cost & Weight Analysis

The relationship between shipment weight and transportation cost was analyzed to identify major cost drivers.

The Python implementation uses Matplotlib and Seaborn for generating the logistics visualizations. :contentReference[oaicite:2]{index=2}

##  Key Analytical Insights
### Warehouse Performance

The analysis identified the **East Warehouse** as having a comparatively high delay rate, with more than 45% of shipments delayed.

This indicates a potential operational bottleneck that may be related to regional dispatch processes, carrier capacity, or staging congestion. :contentReference[oaicite:3]{index=3}

### Shipment Weight & Transportation Cost

Correlation analysis showed a strong positive relationship between shipment weight and transportation cost:

**Correlation coefficient: r = +0.78**

This indicates that transportation cost tends to increase as shipment weight increases.

The analysis also showed that Air freight has a higher cost gradient per kilogram, while Maritime and Rail
are comparatively more cost-efficient for heavier shipments. :contentReference[oaicite:4]{index=4}

##  Business / Operational Insights
The analysis can help logistics teams to:

- Identify warehouses with higher delivery delays.
- Monitor regional operational bottlenecks.
- Understand major transportation cost drivers.
- Evaluate transportation modes based on shipment weight.
- Improve freight mode selection.
- Support data-driven logistics planning.

## 📄 Project Report

[View Detailed Project Report](Week%203%20Task%20-%20Advanced%20Data%20Analysis%20and%20Visualization%20in%20Logisticsnewpdffile.pdf)

##  Skills Demonstrated

- Python
- Pandas
- NumPy
- Exploratory Data Analysis (EDA)
- Data Visualization
- Statistical Analysis
- Correlation Analysis
- Logistics Analytics
- Supply Chain Analytics
- Matplotlib
- Seaborn
- Business Insight Generation

## 👩‍💻 Author

**Suhani Sallam**

B.Tech IT | Aspiring Data Analyst & SQL Developer
