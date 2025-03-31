################################TASK 2
#READ A CSV FILE
import csv
import traceback
import os
import custom_module

def read_employees():
    
    try:
        #empty dictionary and list to store data
        employees_dict = {}
        rows_list = []  #stores rows 
        
        #open/read/close CSV file
        with open('../csv/employees.csv', 'r') as csvfile:
            #create CSV reader
            csv_reader = csv.reader(csvfile)
            
            #read 1st row of headers, then store in dictionary
            headers = next(csv_reader)
            employees_dict['fields'] = headers
            
            #read remaining rows and add to list
            for row in csv_reader:
                rows_list.append(row)
            
            # add rows to dictionary
            employees_dict['rows'] = rows_list # add the list of rows (list of lists) to the dict using the key "rows"
            
        return employees_dict #return the dict
    
    #ERROR HANDLING TASK 2
    except Exception as e:

        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back: #loop 
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        #exit program on error
        exit(1)

#function call, store result in global variable
employees = read_employees()
print(employees)  # For verification


################################TASK 3
#FIND COLUMN INDEX
#takes a column name ("first_name") as input
#finds its position i.e index in the employees["fields"] list
#returns position number



def column_index(column_name):
    #find the position of a column in the employees data
    #and return the index of the column name in the fields list
    return employees["fields"].index(column_name)

#call fnc to find where employee_id is stored
employee_id_column = column_index("employee_id")  #global variable employee_id_column 


################################TASK 4
#FIND EMPLOYEE FIRST NAME
#fnc takes a row number (like 0 for the first employee)
#fnc finds where the "first_name" column is located using our column_index function
#returns the first name from that row

def first_name(row_number):

    #find column with first names
    first_name_column = column_index("first_name")

    #grab row
    employee_row = employees["rows"][row_number] #employees["rows"] has all emplooyee data, [row_number] selects specific employee

    #return the first name from employee_row
    return employee_row[first_name_column]

#testing
print("First employee name:", first_name(0)) 
print("Second employee name:", first_name(1)) 


################################TASK 5
#FIND THE EMPLOYEE: FNC IN A FNC
#fnc takes an employee ID number as input
#then finds all rows that match that ID
#then uses filter() to do the searching
#returns the matching rows
#We use int() because CSV files store everything as text


def employee_find(employee_id):
    #fnc checks if a row matches ID
    def employee_match(row):
        #convert ID (string to number) and compare
        return int(row[employee_id_column]) == employee_id
    
    #filter() to find all matching rows
    matched = list(filter(employee_match, employees["rows"]))
    
    return matched

#test
print("Employee with ID 1:", employee_find(1))
print("Employee with ID 2:", employee_find(2))


################################TASK 6
#FIND THE EMPLOYEE USING LAMBDA
#basically this does the same job as employee_find() from T5
#use a lambda
#finds employees by their ID number

def employee_find_2(employee_id):

    matched = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"])) #lambda takes 2 arguments, fnc and employees["rows"]
    return matched

#test
print("Lambda ID 1:", employee_find_2(1))
print("Lambda ID 2:", employee_find_2(2))


################################TASK 7
#SORT THE ROWS BY last_name USING A LAMBDA
#fnc sorts all employee rows alphabetically (last name)
#then uses a lambda fnc to sort
#update the employees dictionary with sorted list
#returns sorted rows

def sort_by_last_name():
    #grab column index for last names to find where last names stored
    last_name_column = column_index("last_name")
    
    #sort rows w lambda: for each employee row → look at just the last name → use this for sorting
    #employees["rows"].sort <---sorts the list
    #key=lambda row: row[last_name_col], for each row use the last name value for sorting
    employees["rows"].sort(key=lambda row: row[last_name_column])
    
    #return sorted rows
    return employees["rows"]

#call fnc and print
sort_by_last_name()
print("Sorted employees:", employees)


################################TASK 8
#CREATE A DICT FOR AN EMPLOYEE
#fnc takes one employees data row
#then creates a dictionary where
#   -keys are the field names ("first_name", "last_name")
#   -values are the employees data from that row
#   -skips the employee_id field
#returns the new dictionary

def employee_dict(row):
    #grab all field names (headers)
    fields = employees["fields"]
    
    #create empty dictionary
    employee = {}
    
    #loop thru each field, then add to dictionary
    for i in range(len(fields)):
        field_name = fields[i]
        #skip employee_id
        if field_name != "employee_id":
            employee[field_name] = row[i]
    
    return employee

#test
first_employee = employees["rows"][0]
second_employee = employees["rows"][1]
print("Employee dictionary1:", employee_dict(first_employee))
print("Employee dictionary2:", employee_dict(second_employee))


################################TASK 9
#A DICT OF DICTS, FOR ALL EMPLOYEES
#makes a big dictionary of all employees
#uses employee IDs as the keys
#each keys value is the employee dictionary made in T8
#returns this big dictionary containing all employees

def all_employees_dict():
    #find column that has employee_id
    id_column = column_index("employee_id")

    #empty big dictionary
    all_employees = {}

    #go thru each employee row
    for row in employees["rows"]:
        #get employee_id, convert
        emp_id = row[id_column]

        #create employee dictionary using T8 fnc
        emp_dict = employee_dict(row)

        # add to big dicitonary
        all_employees[emp_id] = emp_dict

    return all_employees

#test
employees_big = all_employees_dict()
print("All employees dict: ", employees_big)


########################################TASK 10
#set an environment variable in our terminal called THISVALUE
#create fnc that can read this value from inside Python
#return whatever value set in the terminal

#NOTES ON ENV VARIABLE: like a sticky note on computer that programs can read
#exists only during current terminal session

def get_this_value():
    return os.getenv("THISVALUE")

#test
print("Environment value is:", get_this_value())


########################################TASK 11
#store a secret value
#change secret from our main program
#share secret between files
#secret in custom_module.py

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

#test
set_that_secret(" shazam shazoom")
print("New secret: ", custom_module.secret)


########################################TASK 12
#READ minutes1.csv and minutes2.csv
#create two dictionaries (like we did with employees)
#convert each row to a tuple (instead of list)
#return both dicts
#store them in global variables

#fnc read CSV return dict
def read_csv_file(filepath):
    try: 
        #open file 'with' automatically closes when done
        with open(filepath, 'r') as csvfile:
            #create csv reader object
            reader = csv.reader(csvfile)

            #create data dictionary
            headers= next(reader)  #grab first row
            headers_tuple = tuple(headers)  #convert to tuple
            
            #read DATA ROWS, remaining lines
            all_rows = []  #empty list store rows
            
            for row in reader:  #loop thru each row
                row_tuple = tuple(row)  #convert row to tuple
                all_rows.append(row_tuple)  # add to our list
            
            #put all into dict
            data = {
                'fields': headers_tuple,  #column headers
                'rows': all_rows          #all data rows
            }
        return data
    except Exception as e: 
        print(f"Error reading  {filepath}: {e}")
        return None
    
#read both minutes files and return 2 dicts
def read_minutes():
    minutes1 = read_csv_file("../csv/minutes1.csv")
    minutes2 = read_csv_file("../csv/minutes2.csv")
    return minutes1, minutes2

#call fnc, store results
minutes1, minutes2 = read_minutes()

#test
print("Minutes 1: ", minutes1)
print("Minutes 2: ", minutes2)


########################################TASK 13
#CREATE MINUTES_SET
#take the two dictionaries in T12(minutes1 and minutes2)
#convert their rows into sets (which automatically removes duplicates)
#combine both sets into one master set of unique meeting records
#store the result in a global variable called minutes_set

def create_minutes_set():
    #convert minutes1's rows to a set
    meetings_from_file1 = set(minutes1['rows'])
    
    #convert minutes2's rows to a set 
    meetings_from_file2 = set(minutes2['rows'])
    
    #combine both
    all_meetings = meetings_from_file1.union(meetings_from_file2)
    
    return all_meetings

#store results
minutes_set = create_minutes_set()

#test
print(f"We got {len(minutes_set)} unique meetings")


########################################TASK 14
#CONVERT TO DATETIME
#convert (minutes_set) to a list
#transform each record so dates become datetime objects
#keep the chairperson
#store result in global variabl minutes_list

from datetime import datetime

def create_minutes_list():

    #convert set to list
    original_list = list(minutes_set)
    
    #transform each item w/ map()
    processed_list = list(map(
        lambda meeting: (
            meeting[0],   #chairperson kept
            datetime.strptime(meeting[1], "%B %d, %Y")  #convert date string
        ),
        original_list
    ))
    
    return processed_list

#store the result globally
minutes_list = create_minutes_list()

#test
print("First 3 converted meetings:")
for i, meeting in enumerate(minutes_list[:3]):
    print(f"{i+1}. {meeting[0]} - {meeting[1]}")

#Sort our meeting records by date (earliest to latest)


########################################TASK 15
#sort meetings by date earliest --> latest
#convert the dates back to strings
#save everything to a new CSV file w/ headers
#ekep the chairpersons

#from datetime import datetime
# def write_sorted_list():

  #  sorted(minutes_list, key=lambda x: x[1])
  #  final_list = []
  #  for name, date_obj in minutes_list: 
       
   #     the_date = date_obj.strftime("%B/%d/%Y") 
   #     final_list.append(name, the_date)  
        
   # with open('./minutes.csv', 'w', newline='') as f:
   #     writer.writerow(minutes1['fields'])
   #     writer.writerow(final_list) 

# write_sorted_list() 

