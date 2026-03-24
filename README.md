# Driver-Based Cost Signal Engine

A FinOps operating engine that converts raw cloud usage and billing signals into standardized cost drivers, baseline comparisons, ownership attribution, recommended actions, and economic insights.

---

## 🚀 Why this exists

Most FinOps practices detect **cost spikes by service**.

This creates reactive workflows:
- “Lambda cost increased”
- “EC2 spend is high”

But it does not answer:
👉 *What is actually driving cost behavior?*

This project standardizes detection using **cost drivers**.

---

## 🧠 Core Concept

Instead of analyzing services directly, we normalize cloud usage into drivers:

- Compute Time (EC2 hours, Lambda duration)
- Request Count (API calls, invocations)
- Storage Volume (S3, EBS)
- Capacity Units (DynamoDB RCU/WCU)
- Throughput (data transfer)

Then we detect:

> **Driver Delta = Current Usage – Baseline**

---

## ⚙️ What the Engine Does

### 1. Normalize Usage → Drivers
Convert raw cloud metrics into standard driver categories.

### 2. Detect Driver Deltas
Compare current driver behavior to baseline.

### 3. Attribute Ownership
Map signals to:
- workload
- team
- technical owner

### 4. Generate Actions
Translate drivers into actionable recommendations.

### 5. Enable Economics
- Cost per driver
- Cost per transaction
- Forecasting

---

## 🏗️ Architecture

Raw Usage Data
↓
Driver Normalization
↓
Driver Detection (Delta Analysis)
↓
Ownership Attribution
↓
Action Routing
↓
Economic Insights


---

## 🧪 Example Output
[ALERT] payments-handler | Request_Count | +150% | Owner: Checkout Team
Action: Check for traffic spike or recursive invocation
Estimated Cost Impact: $4,200

---

## 📂 Project Structure
drivers/ → driver normalization, detection, attribution
economics/ → unit cost, forecasting
data/ → sample datasets
outputs/ → generated results
core/ → shared utilities


---

## 🔥 What This Unlocks

- Standardized cost detection across all services
- Faster root cause analysis
- Automated action routing (Jira/Slack ready)
- Driver-based forecasting
- Unit economics (cost per transaction)

---

## 💡 Key Insight

**Cost is not a service problem.  
It’s a driver behavior problem.**
