import pandas as pd
import numpy as np
import os

def run_etl():
    # 1. Extract
    raw_path = 'Data/Raw/hr_data_raw.csv'
    if not os.path.exists(raw_path):
        print("Raw data file not found!")
        return
    
    df = pd.read_csv(raw_path)
    
    # 2. Transform
    # Fill missing ExitDate with a placeholder or handle it
    df['ExitDate'] = df['ExitDate'].fillna('Active')
    df['HireDate'] = pd.to_datetime(df['HireDate'])
    
    # Create Dim_Employee
    dim_employee = df[['EmployeeID', 'Name', 'Age', 'Gender']].drop_duplicates()
    
    # Create Dim_Department
    # Assign unique IDs to departments and roles
    dept_info = df[['Department', 'JobRole']].drop_duplicates().reset_index(drop=True)
    dept_info['DeptID'] = dept_info.index + 1
    dim_department = dept_info[['DeptID', 'Department', 'JobRole']]
    
    # Merge DeptID back to main dataframe
    df = df.merge(dim_department, on=['Department', 'JobRole'])
    
    # Create Dim_Date
    all_dates = pd.to_datetime(df['HireDate']).tolist()
    # Also include exit dates if they are not 'Active'
    exit_dates = pd.to_datetime(df[df['ExitDate'] != 'Active']['ExitDate']).tolist()
    date_range = pd.date_range(start=min(all_dates), end=max(all_dates + exit_dates))
    dim_date = pd.DataFrame({
        'Date': date_range,
        'Year': date_range.year,
        'Month': date_range.month,
        'Quarter': date_range.quarter,
        'Day': date_range.day,
        'Weekday': date_range.day_name()
    })
    
    # Create Fact_EmployeeRecords
    # Tenure calculation (in days)
    today = pd.to_datetime(datetime.now().strftime('%Y-%m-%d'))
    df['TenureDays'] = df.apply(
        lambda row: (pd.to_datetime(row['ExitDate']) - row['HireDate']).days 
        if row['ExitDate'] != 'Active' 
        else (today - row['HireDate']).days, axis=1
    )
    df['IsActive'] = df['ExitDate'].apply(lambda x: 1 if x == 'Active' else 0)
    
    fact_employee_records = df[[
        'EmployeeID', 'DeptID', 'HireDate', 'ExitDate', 
        'Salary', 'PerformanceRating', 'TenureDays', 'IsActive'
    ]]
    
    # 3. Load
    os.makedirs('Data/Processed', exist_ok=True)
    dim_employee.to_csv('Data/Processed/dim_employee.csv', index=False)
    dim_department.to_csv('Data/Processed/dim_department.csv', index=False)
    dim_date.to_csv('Data/Processed/dim_date.csv', index=False)
    fact_employee_records.to_csv('Data/Processed/fact_employee_records.csv', index=False)
    
    print("ETL complete. Processed tables saved to Data/Processed/")

from datetime import datetime
if __name__ == "__main__":
    run_etl()
