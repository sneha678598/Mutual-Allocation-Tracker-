import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    data = pd.read_excel(file_path, skiprows=4, header=None)  # Adjust as needed
    data.columns = ['Fund Name', 'ISIN', 'Rating_Industry', 'Quantity', 
                    'Market_Value_Lakhs', 'Percentage_NAV', 'YTM', 'Extra_Column1', 'Extra_Column2']
    return data.iloc[:, :7]  # Retain only necessary columns

def process_data(data, fund_name, start_date, end_date):
    # Ensure 'Fund Name' is a string and clean it
    data['Fund Name'] = data['Fund Name'].fillna('').astype(str).str.strip().str.lower()
    fund_name = fund_name.strip().lower()

    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
        filtered_data = data[(data['Fund Name'] == fund_name) & 
                             (data['Date'] >= start_date) & 
                             (data['Date'] <= end_date)]
    else:
        filtered_data = data[data['Fund Name'] == fund_name]
    return filtered_data

def main():
    file_path = r"C:\Users\acer\New folder (2)/ZN250 - Monthly Portfolio September 2024.xlsx"
    data = load_data(file_path)
    print("Dataset preview:")
    print(data.head())

    fund_name = input('Enter Fund Name: ')
    start_date = input('Enter Start Date (YYYY-MM-DD): ')
    end_date = input('Enter End Date (YYYY-MM-DD): ')

    try:
        filtered_data = process_data(data, fund_name, start_date, end_date)
        if filtered_data.empty:
            print(f"No data found for {fund_name} between {start_date} and {end_date}.")
        else:
            print(f"Filtered Data:\n{filtered_data}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
