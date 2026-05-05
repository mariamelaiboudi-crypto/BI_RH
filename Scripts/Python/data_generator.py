import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_hr_data(num_records=500):
    departments = ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance', 'Operations']
    job_roles = {
        'HR': ['HR Manager', 'HR Specialist', 'Recruiter'],
        'Engineering': ['Software Engineer', 'QA Engineer', 'DevOps Engineer', 'Technical Lead'],
        'Sales': ['Account Manager', 'Sales Representative', 'Sales Executive'],
        'Marketing': ['Marketing Manager', 'Content Writer', 'SEO Specialist'],
        'Finance': ['Accountant', 'Financial Analyst', 'Finance Manager'],
        'Operations': ['Operations Manager', 'Project Manager', 'Coordinator']
    }
    genders = ['Male', 'Female', 'Non-binary']
    
    data = []
    start_date = datetime(2018, 1, 1)
    end_date = datetime(2023, 12, 31)

    for i in range(1, num_records + 1):
        dept = random.choice(departments)
        role = random.choice(job_roles[dept])
        gender = random.choice(genders)
        age = random.randint(22, 60)
        
        # Hire Date
        hire_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        
        # Exit Date (random attrition)
        exit_date = None
        if random.random() < 0.2: # 20% attrition rate
            exit_days = random.randint(30, 1500)
            potential_exit = hire_date + timedelta(days=exit_days)
            if potential_exit < datetime.now():
                exit_date = potential_exit.strftime('%Y-%m-%d')
        
        salary = random.randint(40000, 120000)
        perf_rating = random.randint(1, 5)
        
        data.append({
            'EmployeeID': f'EMP{i:03}',
            'Name': f'Employee_{i}',
            'Age': age,
            'Gender': gender,
            'Department': dept,
            'JobRole': role,
            'Salary': salary,
            'HireDate': hire_date.strftime('%Y-%m-%d'),
            'ExitDate': exit_date,
            'PerformanceRating': perf_rating
        })
    
    df = pd.DataFrame(data)
    df.to_csv('Data/Raw/hr_data_raw.csv', index=False)
    print(f"Generated {num_records} records in Data/Raw/hr_data_raw.csv")

if __name__ == "__main__":
    generate_hr_data(600)
