import pandas as pd
import json
import numpy as np


################TASK1
#create DF from dict
data = {
    'Name': ['Alice', 'Bob', 'charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

#create data_frame
task1_data_frame = pd.DataFrame(data)
print("Original: ")
print(task1_data_frame)

#Salary Column
#copy
task1_with_salary = task1_data_frame.copy()

#salary column data
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("DataFrame with Salary Column: ")
print(task1_with_salary)

#Age column we increment by 1
#copy of salary
task1_older = task1_with_salary.copy()

#+1 to age
task1_older['Age'] = task1_older['Age'] + 1
print("DataFrame + 1yr: ")
print(task1_older)

#save to CSV without index
task1_older.to_csv('employees.csv', index=False)
print("T1 Dataframe on CSV file: ")
print(pd.read_csv('employees.csv'))


#########################TASK 2
#Load CSV file
task2_employees = pd.read_csv('employees.csv')
print("\nT2- Employees from CSV: ")
print(task2_employees)

#create, load JSON
#create json 
additional_employees = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]

#write to JSON
with open('additional_employees.json', 'w') as f:
    json.dump(additional_employees, f)

#load in JSON
json_employees = pd.read_json('additional_employees.json')
print("\nT2- Additional Employees from JSON: ")
print(json_employees)

#combine DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nT2- Combined Data:")
print(more_employees)

################################TASK 3
#first 3 rows using head
first_three = more_employees.head(3)
print("\nTask 3 - First Three Employees:")
print(first_three)

#last 2 rows using tail
last_two = more_employees.tail(2)
print("\nTask 3 - Last Two Employees:")
print(last_two)

#get shape with .shape
employee_shape = more_employees.shape
print("\nTask 3 - DataFrame Shape:")
print(employee_shape)

#print
print("\nTask 3 - DataFrame Info:")
print(more_employees.info())



###############TASK 4 

#load the data
dirty_data = pd.read_csv('dirty_data.csv')
print("Dirty Data: ")
print(dirty_data)

#create clean copy
clean_data = dirty_data.copy()
print("\nClean Data Copied: ")
print(clean_data)

#remove duplicates
clean_data = clean_data.drop_duplicates()
print("\nRemoval of Duplicates:")
print(clean_data)

#convert Age to numeric
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\nAfter Converting Age to Numeric:")
print(clean_data)

#clean Salary column
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a', 'NaN'], np.nan)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print("\nAfter Cleaning Salary:")
print(clean_data)

#fill missing values
mean_age = clean_data['Age'].mean()
median_salary = clean_data['Salary'].median()
clean_data['Age'] = clean_data['Age'].fillna(mean_age)
clean_data['Salary'] = clean_data['Salary'].fillna(median_salary)
print("\nAfter Filling Missing Values:")
print(clean_data)

#convert Hire Date   ###ERROR:pandas using a standard time format??? #########################################
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print("\nAfter Converting Hire Date:")
print(clean_data)
##########################################################################################################


#clean text columns
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("\nFinal Cleaned Data:")
print(clean_data)