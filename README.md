# 🛡️ Social Media Sentinel: Enterprise Text Analytics Pipeline & Dashboard

An end-to-end, code-driven data analysis application that ingests raw, unstructured consumer feedback data, processes it through a localized Natural Language Processing (NLP) transformation pipeline, and renders business intelligence metrics via an interactive web dashboard.

---

## 🎯 Business Case & Objective
Large enterprise multinational corporations (MNCs) process hundreds of thousands of customer text interactions daily across support portals, product reviews, and social channels. Reviewing this data manually is operationally impossible, leading to delayed escalations for critical bugs, shipping failures, or billing discrepancies.

**The Solution:** This project replaces traditional tabular data analytics with a modern text-data pipeline. It automatically reads a flat data store of **1,000 real-world customer entries**, maps structural attributes programmatically using heuristic text analytics, and populates executive decision-making visual dashboards in real time.

---

## 🧠 Key Features & Technical Architecture

### 1. Interactive Model Sandbox (For Stakeholder Testing)
* Features a live text-ingestion module built in Python where interviewers can pass dynamic, multi-sentence operational complaints.
* On form submission, the pipeline instantly sanitizes the data, runs the classification engine, and surfaces high-level target variables back to the UI.

### 2. High-Performance Local NLP Transform Layer
* Optimized completely inside pure Python, avoiding external cloud latency and subscription costs.
* Programmatically parses text strings to generate three net-new database columns:
  * **Sentiment Categorization:** Maps positive/negative emotional weights to route user feedback.
  * **Operational Department Routing:** Dynamically scans textual patterns to auto-assign rows to **Technical, Pricing, Shipping, or Support** departments.
  * **Severity Matrix Index:** Assigns an emergency weight from 1 to 5 based on key urgency markers.

### 3. State-Managed Analytical Dashboard
* Built using a code-first visualization architecture with **Streamlit** and **Pandas**.
* Utilizes **Streamlit Session States (`st.session_state`)** to cache processed data frames securely in application memory, preventing computational redundancies during user filtering.
* Features aggregate metric KPI summary cards alongside native graphical charts plotting macro operational bottlenecks.

---

## 💻 Tech Stack & Tools
* **Programming Language:** Python 3.10+
* **Data Manipulation & Ingestion:** Pandas, OS File Systems, CSV 
* **User Interface & App Hosting:** Streamlit Framework
* **Development Workspace:** Visual Studio Code (VS Code)

---

## 📊 Database Schema Transformations
The pipeline targets a raw two-column dataset (`dataset.csv`) and transforms it into an optimized analytical data frame structure:

| Column Name | Data Type | Description / Constraints | Source Generation |
| :--- | :--- | :--- | :--- |
| **Review_ID** | Integer | Unique identifier for row indexing | Original Dataset |
| **Review_Text** | String | Raw, messy user-submitted commentary | Original Dataset |
| **Sentiment** | String | Categorical variable: `Positive`, `Negative`, `Neutral` | Pipeline Computed |
| **Category** | String | Operational routing: `Technical`, `Pricing`, `Shipping`, `Support` | Pipeline Computed |
| **Severity** | Integer | Scale of 1 (Low Action Required) to 5 (Critical Escalation) | Pipeline Computed |

---

## 🚀 Local Installation & Deployment

To run this data application on your local workstation, run the following sequential commands in your terminal:

```bash
# 1. Clone or open your project directory
cd social_media_sentinel

# 2. Install core visualization and data structures libraries
python -m pip install pandas streamlit

# 3. Launch the reactive Streamlit application server
python -m streamlit run app.py
```
Once executed, your terminal will deploy a local web application host address. Your browser will instantly open the functional platform at `http://localhost:8501`.
