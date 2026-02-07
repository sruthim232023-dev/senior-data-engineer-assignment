# Data Engineer Assignment - Company XYZ

## Overview
This project analyzes sales data to target specific age groups (18-35) for marketing strategy. It extracts total quantities purchased per item, excluding items with no purchases.

## Project Structure

* `main.py`: Python script to execute the data pipeline.
* `queries.sql`: Raw SQL logic for data extraction.
* `output.csv`: The final semicolon-delimited result.
* `requirements.txt`: Python dependencies.
* `.gitignore`: Files to exclude from version control.

## How to Run

1. Place the `company_xyz.db` in the root directory.
2. Install dependencies: `pip install pandas`.
3. Run the script: `python main.py`.

## Business Rules

- Target customers aged 18-35
- Aggregate quantities per customer and item
- Exclude items with zero quantity
- Output format: semicolon-delimited CSV

## Output

The script generates `output.csv` with the following columns:
- Customer (customer_id)
- Age
- Item (item_name)
- Quantity (integer sum)
