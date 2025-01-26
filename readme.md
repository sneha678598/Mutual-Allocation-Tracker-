# Mutual Fund Allocation Tracker

## Overview

The **Mutual Fund Allocation Tracker** is a Python framework designed to monitor and analyze changes in mutual fund allocations. The system allows users to process large datasets, filter data by fund name and date range, and view results categorized by fund and month. This tool is useful for financial analysts and investors seeking insights into mutual fund trends.

---

## Features

- **Data Preprocessing**: Cleans and structures raw mutual fund datasets for analysis.
- **Flexible Filtering**: Users can select specific funds and date ranges for targeted analysis.
- **Monthly Allocation Analysis**: Outputs are displayed by fund and month for better insights.
- **User-Friendly Interface**: Simple command-line prompts for fund selection and date input.

---

## Installation

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/yourusername/mutual-fund-tracker.git
   cd mutual-fund-tracker
2. **Install Dependencies**:
  Ensure you have Python installed (version 3.7+ recommended). Install required packages using pip:

  ```bash
  pip install pandas matplotlib openpyxl

3. **Prepare Dataset**:

  Place your dataset in the project folder. Update the file_path in the code to point to your dataset file.

4. **Usage**

  Run the Script:
  Execute the program using Python:
  ```bash
  python main.py

5. **Input Details**:

  Enter the fund name (e.g., Lupin Limited).
  Enter the start and end dates in YYYY-MM-DD format.

6. **View Results**:

  If data is available for the selected range, the system will display allocation details by fund and month.
  If no data matches the criteria, the system will notify you.