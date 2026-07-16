# 🚀 Enterprise Automated Reporting System

![Python](https://img.shields.io/badge/Python-3.12-blue)
![SQL Server](https://img.shields.io/badge/SQL%20Server-2019-red)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-orange)
![Pandas](https://img.shields.io/badge/Pandas-ETL-green)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

## 📌 Project Overview

The **Enterprise Automated Reporting System** is an end-to-end ETL and Business Intelligence solution built using **Python, SQL Server, Pandas, and Tableau**.

The application extracts business data from SQL Server, performs data transformation using Python, generates processed CSV and Excel reports, and visualizes key business insights through interactive Tableau dashboards.

This project simulates a real-world enterprise reporting workflow used in banking, retail, and corporate environments.

---

# 🏗 Project Architecture

```
                  SQL Server
                       │
                       ▼
              Python ETL Pipeline
        ┌─────────────────────────┐
        │ Extract │ Transform │ Load │
        └─────────────────────────┘
                       │
             Raw & Processed CSV
                       │
                       ▼
             Enterprise_Report.xlsx
                       │
                       ▼
             Tableau Dashboard
```

---

# 💻 Technology Stack

- Python 3.12
- SQL Server
- SQLAlchemy
- Pandas
- OpenPyXL
- PyODBC
- Tableau Public
- Git & GitHub

---

# 📂 Project Structure

```
Enterprise-Automated-Reporting-System
│
├── config
├── data
│   ├── raw
│   └── processed
├── database
├── logs
├── python
├── reports
├── scheduler
├── screenshots
├── sql
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ✨ Features

- SQL Server Integration
- Automated ETL Pipeline
- Data Cleaning
- CSV Export
- Excel Report Generation
- Interactive Tableau Dashboard
- Logging
- Modular Python Code
- Business KPI Reporting

---

# 📊 Database Design

Tables included:

- Customers
- Products
- Employees
- Orders
- Transactions

Relationships:

```
Customers
     │
     ▼
Orders
 ├────────► Products
 │
 ▼
Employees

Orders
   │
   ▼
Transactions
```

---

# 🔄 ETL Workflow

### Extract

- Connect to SQL Server
- Read business tables
- Export Raw CSV

### Transform

- Remove duplicates
- Handle missing values
- Generate calculated columns
- Business KPI calculations

### Load

- Save Processed CSV
- Generate Excel Report
- Prepare Tableau Dataset

---

# 📈 Dashboard KPIs

The Tableau dashboard displays:

- Total Revenue
- Total Orders
- Total Customers
- Average Order Value
- Success Rate
- Daily Sales Trend
- Top Products
- Top Customers
- Payment Mode Analysis
- Failed Transactions

---



<img width="958" height="625" alt="image" src="https://github.com/user-attachments/assets/9029425b-fdf5-4433-b905-fbe3acbac745" />


---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Enterprise-Automated-Reporting-System.git
```

Go inside the project

```bash
cd Enterprise-Automated-Reporting-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the ETL Pipeline

```bash
python python/main.py
```

---

# 📋 Sample SQL Reports

- Daily Sales
- Monthly Revenue
- Top Customers
- Top Products
- Payment Mode Analysis
- Failed Transactions

---

# 📌 Future Improvements

- Scheduled ETL Jobs
- Email Notifications
- Power BI Dashboard
- REST API
- Cloud Deployment
- Docker Support

---

# 👨‍💻 Author

**Dev Ram**

Python | SQL Server | Tableau | ETL | Data Analytics

GitHub: https://github.com/Devram0799/Enterprise-Automated-Reporting-System/

LinkedIn: https://www.linkedin.com/in/devram-ram/

---

# ⭐ If you found this project useful, please give it a Star.
