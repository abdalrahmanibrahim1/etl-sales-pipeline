# ETL Sales Pipeline

A Python ETL project that generates synthetic sales data, cleans and validates it, loads it into a SQLite database, and runs business reporting queries.

## Project Overview

This project simulates a small business sales pipeline. It starts with raw CSV files for customers, products, and sales, applies data quality checks, loads the cleaned data into a relational SQLite database, and produces SQL-based business reports.

The goal of this project is to practice core data engineering fundamentals:

* Data generation
* CSV extraction
* Data validation
* Data cleaning
* Relational database design
* SQLite loading
* SQL reporting
* Git/GitHub project structure

## ETL Flow

```text
Synthetic Data Generation
        ↓
Raw CSV Files
        ↓
Extract
        ↓
Transform / Clean / Validate
        ↓
Load into SQLite
        ↓
SQL Reports
```

## Features

* Generates synthetic customer, product, and sales datasets
* Intentionally adds messy data to simulate real-world data quality issues
* Cleans missing values, duplicates, invalid dates, invalid prices, and invalid quantities
* Validates relationships between sales, customers, and products
* Loads cleaned data into a SQLite database
* Creates relational tables with primary keys and foreign keys
* Runs SQL reports for business analysis

## Data Quality Rules

### Customers

* Missing customer names are replaced with `Unknown`
* Blank customer names are replaced with `Unknown`
* Customers with missing IDs are removed
* Customers with invalid signup dates are removed
* Duplicate customer IDs are removed

### Products

* Blank product names are replaced with `Unknown`
* Duplicate product IDs are removed
* Non-numeric prices are removed
* Prices less than or equal to zero are removed

### Sales

* Duplicate sale IDs are removed
* Sales with missing key fields are removed
* Invalid quantities are removed
* Quantities less than or equal to zero are removed
* Invalid sale dates are removed
* Sales referencing missing customers are removed
* Sales referencing missing products are removed

## Business Reports

The project includes SQL reports such as:

* Best-selling product by units sold
* Top product by revenue
* Revenue by city
* Revenue by product category
* Monthly sales trend
* Top customer by spending

## Project Structure

```text
etl-sales-pipeline/
│
├── data/
│   └── raw/
│       ├── customers.csv
│       ├── products.csv
│       └── sales.csv
│
├── src/
│   ├── generate_data.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── report.py
│   └── main.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Tech Stack

* Python
* Pandas
* SQLite
* SQL
* Git / GitHub

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/abdalrahmanibrahim1/etl-sales-pipeline.git
cd etl-sales-pipeline
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate raw CSV data

```bash
python src/generate_data.py
```

### 5. Run the full pipeline

```bash
python src/main.py
```

This will load the cleaned data into SQLite and run the reporting queries.

## Database Schema

### customers

| Column      | Type | Description   |
| ----------- | ---- | ------------- |
| customer_id | TEXT | Primary key   |
| name        | TEXT | Customer name |
| city        | TEXT | Customer city |
| signup_date | TEXT | Signup date   |

### products

| Column       | Type | Description      |
| ------------ | ---- | ---------------- |
| product_id   | TEXT | Primary key      |
| product_name | TEXT | Product name     |
| category     | TEXT | Product category |
| price        | REAL | Product price    |

### sales

| Column      | Type    | Description              |
| ----------- | ------- | ------------------------ |
| sale_id     | TEXT    | Primary key              |
| customer_id | TEXT    | Foreign key to customers |
| product_id  | TEXT    | Foreign key to products  |
| quantity    | INTEGER | Quantity sold            |
| sale_date   | TEXT    | Date of sale             |

## What I Learned

Through this project, I practiced:

* Structuring a Python data project
* Using virtual environments
* Generating synthetic datasets
* Reading CSV files with pandas
* Cleaning and validating data
* Handling missing values, duplicates, and invalid records
* Using SQLite with Python
* Creating database schemas manually
* Loading cleaned data into relational tables
* Writing SQL joins and aggregation queries
* Building a reproducible ETL workflow

## Future Improvements

Possible improvements include:

* Export reports into CSV or text files
* Add logging instead of print statements
* Add automated tests for transformation rules
* Add command-line arguments for running specific pipeline stages
* Replace SQLite with PostgreSQL
* Containerize the project with Docker
* Schedule the pipeline with Airflow or cron
