"""
02 - CONTROL FLOW
=================

PRACTICE EXERCISES

Topics:
- if
- if / else
- if / elif / else
- nested if
- for loops
- range()
- break
- continue
- while loops
- pass
- Data Engineering-style control flow

IMPORTANT:
Try to solve these exercises yourself.
Do not copy solutions from examples.py.
"""


# ============================================================
# LEVEL 1 — BASIC CONDITIONS
# ============================================================


# Exercise 1: Check Row Count
# ---------------------------
# Create a variable called row_count.
#
# If row_count is greater than 0, print:
# "Data available"
#
# Otherwise, print:
# "No data"


# Write your code below:
row_count = 5
if row_count > 0:
    print("Data available")
else:
    print("No data")



# Exercise 2: File Existence
# --------------------------
# Create a variable:
#
# file_exists = True
#
# If the file exists, print:
# "File found"
#
# Otherwise, print:
# "File not found"


# Write your code below:

file_exists = True

if file_exists:
    print("File found")
else:
    print("File not found")


# Exercise 3: Positive / Negative / Zero
# --------------------------------------
# Create a variable called value.
#
# If value is greater than 0:
#     print "Positive"
#
# If value is less than 0:
#     print "Negative"
#
# Otherwise:
#     print "Zero"


# Write your code below:

value = 15
if value > 0:
    print("Positive")
elif value < 0:
    print("Negative")
else:
    print("Zero")



# ============================================================
# LEVEL 2 — IF / ELIF / ELSE
# ============================================================


# Exercise 4: Dataset Size
# -----------------------
# Create a variable called rows.
#
# Classify the dataset:
#
# rows == 0       -> "Empty"
# rows < 100      -> "Small"
# rows < 10000    -> "Medium"
# otherwise       -> "Large"


# Write your code below:
rows = 100
if rows == 0:
    print("Empty")
elif rows < 100:
    print("Small")
elif rows < 10000:
    print("Medium")
else:
    print("Large")



# Exercise 5: Data Quality Score
# -----------------------------
# Create a variable:
#
# quality_score = 85
#
# Classify it:
#
# 90 or above -> "Excellent"
# 75 to 89    -> "Good"
# 50 to 74    -> "Needs Improvement"
# below 50    -> "Poor"


# Write your code below:
quality_score = 85
if quality_score >=90:
    print("Excellent")
elif quality_score >=75 and quality_score <=89:
    print("Good")
elif quality_score >=50 and quality_score <= 74:
    print("Needs Improvement")
else:
    print("Poor")



# Exercise 6: File Type
# ---------------------
# Create:
#
# filename = "sales.csv"
#
# Check the file extension.
#
# If it is ".csv":
#     print "CSV file"
#
# If it is ".json":
#     print "JSON file"
#
# Otherwise:
#     print "Unsupported file"


# Write your code below:
filename = 'sales.csv'
if filename.endswith(".csv"):
    print("CSV file")
elif filename.endswith(".json"):
    print("JSON file")
else:
    print("Unsupported file")



# ============================================================
# LEVEL 3 — NESTED CONDITIONS
# ============================================================


# Exercise 7: Can the Pipeline Run?
# ---------------------------------
# Create:
#
# file_exists = True
# row_count = 500
#
# The pipeline should run only when:
# 1. The file exists
# 2. The file contains at least one row
#
# Expected logic:
#
# If the file exists:
#     If rows > 0:
#         print "Pipeline can run"
#     Otherwise:
#         print "File is empty"
# Otherwise:
#     print "File not found"


# Write your code below:
file_exists = True
row_count = 500
if file_exists:
    if row_count > 0:
        print("Pipeline can run")
    else:
        print("File is empty")
else:
    print("File not found")




# Exercise 8: Data Validation
# ---------------------------
# Create:
#
# record_exists = True
# data_valid = False
#
# If the record exists:
#     check whether the data is valid
#
# Print appropriate messages:
#
# "Record is valid"
# "Record is invalid"
# "Record not found"


# Write your code below:

record_exists = True
data_valid = False
if record_exists:
    if data_valid:
        print("Record is valid")
    else:
        print("Record is invalid")
else:
    print("Record not found")



# ============================================================
# LEVEL 4 — FOR LOOPS
# ============================================================


# Exercise 9: Process Files
# -------------------------
# Given:
#
# files = ["sales.csv", "customers.csv", "orders.csv"]
#
# Print:
#
# Processing sales.csv
# Processing customers.csv
# Processing orders.csv


# Write your code below:
files = ["sales.csv", "customers.csv", "orders.csv"]
for file in files:
    print(f'Processing {file}')




# Exercise 10: Process Tables
# ---------------------------
# Given:
#
# tables = ["customers", "orders", "products"]
#
# Print:
#
# Loading customers
# Loading orders
# Loading products


# Write your code below:

tables = ["customers", "orders", "products"]
for table in tables:
    print(f'Loading {table}')



# Exercise 11: Print Numbers
# --------------------------
# Use range() to print numbers from 1 to 10.


# Write your code below:
for i in range(1,11):
    print(i)



# Exercise 12: Batch Processing
# -----------------------------
# Use range() to print:
#
# Batch 1
# Batch 2
# Batch 3
# Batch 4
# Batch 5


# Write your code below:
for i in range(1,6):
    print(f'Batch {i}')



# Exercise 13: Even Numbers
# -------------------------
# Use range() to print all even numbers from 2 through 20.


# Write your code below:
for i in range(2,21):
    if i%2 == 0:
        print(i)



# ============================================================
# LEVEL 5 — FOR + CONDITIONS
# ============================================================


# Exercise 14: Process Non-Empty Datasets
# ---------------------------------------
# Given:
#
# datasets = [100, 0, 500, 0, 1000]
#
# For every dataset:
#
# If rows > 0:
#     print "Processing X rows"
#
# Otherwise:
#     print "Skipping empty dataset"


# Write your code below:
datasets = [100, 0, 500, 0, 1000]
for dataset in datasets:
    if dataset > 0:
        print(f'Processing {dataset} rows')
    else:
        print("Skipping empty dataset")



# Exercise 15: Find Large Datasets
# --------------------------------
# Given:
#
# datasets = [50, 500, 5000, 50000]
#
# Print only datasets having more than 1000 rows.


# Write your code below:
datasets = [50, 500, 5000, 50000]
for dataset in datasets:
    if dataset > 1000:
        print(dataset)



# Exercise 16: Validate File Extensions
# -------------------------------------
# Given:
#
# files = [
#     "sales.csv",
#     "customers.json",
#     "orders.csv",
#     "image.png"
# ]
#
# Print:
#
# "Processing CSV: <filename>"
# "Processing JSON: <filename>"
# "Unsupported file: <filename>"


# Write your code below:
files = ['sales.csv', 'customers.json', 'orders.csv', 'image.png']
for file in files:
    if file.endswith(".csv"):
        print(f'Processing CSV: {file}')
    elif file.endswith(".json"):
        print(f'Processing JSON: {file}')
    else:
        print(f'Unsupported file {file}')



# ============================================================
# LEVEL 6 — BREAK
# ============================================================


# Exercise 17: Stop at Error
# --------------------------
# Given:
#
# files = ["a.csv", "b.csv", "error.csv", "c.csv"]
#
# Process each file.
#
# When "error.csv" is encountered:
#     print "Critical error"
#     stop the loop
#
# Expected:
#
# Processing a.csv
# Processing b.csv
# Critical error


# Write your code below:
files = ["a.csv", "b.csv", "error.csv", "c.csv"]
for file in files:
    if file == 'error.csv':
        print("Critical error")
        break
    print(f'Processing {file}')


# Exercise 18: Find First Large Dataset
# -------------------------------------
# Given:
#
# datasets = [100, 500, 800, 15000, 50000]
#
# Find the first dataset with more than 10000 rows.
#
# Print:
#
# "Large dataset found: 15000"
#
# Then stop the loop.


# Write your code below:
datasets = [100, 500, 800, 15000, 50000]

for dataset in datasets:
    if dataset > 10000:
        print(f'Large dataset found: {dataset}')
        break
    


# ============================================================
# LEVEL 7 — CONTINUE
# ============================================================


# Exercise 19: Skip Temporary Files
# ---------------------------------
# Given:
#
# files = [
#     "sales.csv",
#     "temp.csv",
#     "customers.csv",
#     "temp.csv",
#     "orders.csv"
# ]
#
# Skip every "temp.csv".
#
# Process everything else.


# Write your code below:
files = ['sales.csv', 'temp.csv', 'customers.csv', 'temp.csv', 'orders.csv']
for file in files:
    if file == 'temp.csv':
        continue
    print(f'Processing {file}')


# Exercise 20: Skip Invalid Records
# ---------------------------------
# Given:
#
# records = [
#     {"id": 1, "valid": True},
#     {"id": 2, "valid": False},
#     {"id": 3, "valid": True},
#     {"id": 4, "valid": False},
# ]
#
# Skip invalid records.
#
# Print:
# "Processing record X"
#
# only for valid records.


# Write your code below:
records = [
    {"id": 1, "valid": True},
    {"id": 2, "valid": False},
    {"id": 3, "valid": True},
     {"id": 4, "valid": False},
 ]
for record in records:
    if record["valid"] == False:
        continue
    print(f'Processing record {record["id"]}')






# ============================================================
# LEVEL 8 — WHILE LOOPS
# ============================================================


# Exercise 21: Count Attempts
# ---------------------------
# Use a while loop to print:
#
# Attempt 1
# Attempt 2
# Attempt 3
# Attempt 4
# Attempt 5


# Write your code below:
i=1
while i <=5:
    print(f'Attempt {i}')
    i=i+1



# Exercise 22: Countdown
# ----------------------
# Create:
#
# count = 10
#
# Use a while loop to print:
#
# 10
# 9
# 8
# ...
# 1


# Write your code below:
count = 10
while count>=1:
    print(count)
    count=count-1




# Exercise 23: Process Batches
# ----------------------------
# Assume:
#
# rows = 1000
#
# Each iteration processes 200 rows.
#
# Use a while loop to print the remaining rows.
#
# Expected sequence:
#
# 1000
# 800
# 600
# 400
# 200


# Write your code below:
rows = 1000
while rows >=200:
    print(rows)
    rows= rows - 200



# ============================================================
# LEVEL 9 — BREAK + WHILE
# ============================================================


# Exercise 24: Retry Operation
# ---------------------------
# Create:
#
# max_attempts = 3
# attempt = 1
#
# Use a while loop.
#
# Simulate success when attempt == 2.
#
# If successful:
#     print "Operation successful"
#     stop the loop
#
# If all attempts fail:
#     print "Operation failed"


# Write your code below:

max_attempts = 3
attempt =1
success = False

while attempt <= max_attempts:
    if attempt ==2:
        print("Operation Successful")
        success = True
        break
    attempt += 1
if not success:
    print("Operation failed")



# ============================================================
# LEVEL 10 — PASS
# ============================================================


# Exercise 25: Placeholder Function
# ---------------------------------
# Create a function called:
#
# validate_data()
#
# Use pass as the function body for now.


# Write your code below:
def validate_data():
    pass


# ============================================================
# LEVEL 11 — DATA ENGINEERING PRACTICE
# ============================================================


# Exercise 26: File Processing Pipeline
# -------------------------------------
# Given:
#
# files = [
#     "sales.csv",
#     "temp.csv",
#     "customers.csv",
#     "error.csv",
#     "orders.csv"
# ]
#
# Rules:
#
# 1. Skip files beginning with "temp".
# 2. If "error.csv" is found:
#       print "Critical error"
#       stop processing.
# 3. Process all other CSV files.
#
# Use:
# - for
# - if
# - continue
# - break


# Write your code below:
files =['sales.csv', 'temp.csv', 'customers.csv', 'error.csv', 'orders.csv']
for file in files:
    if file.startswith("temp"):
        continue
    if file == "error.csv":
        print("Critical error")
        break
    print(f'Processing {file}')



# Exercise 27: Data Quality Filter
# -------------------------------
# Given:
#
# records = [
#     {"id": 1, "amount": 500},
#     {"id": 2, "amount": 0},
#     {"id": 3, "amount": 750},
#     {"id": 4, "amount": -100},
#     {"id": 5, "amount": 1200},
# ]
#
# Rules:
#
# - Skip records where amount <= 0.
# - Process valid records.
#
# Print:
#
# "Processing record X"
#
# for valid records only.


# Write your code below:
records = [
    {"id": 1, "amount": 500},
    {"id": 2, "amount": 0},
    {"id": 3, "amount": 750},
    {"id": 4, "amount": -100},
    {"id": 5, "amount": 1200},
]


# Exercise 28: Dataset Classification
# -----------------------------------
# Given:
#
# datasets = [
#     {"name": "sales", "rows": 500},
#     {"name": "customers", "rows": 0},
#     {"name": "orders", "rows": 50000},
# ]
#
# Classify every dataset:
#
# 0 rows        -> Empty
# < 1000 rows   -> Small
# < 100000 rows -> Medium
# otherwise     -> Large
#
# Print the dataset name and classification.


# Write your code below:
datasets = [
    {"name": "sales", "rows": 500},
    {"name": "customers", "rows": 0},
    {"name": "orders", "rows": 50000},
]

for dataset in datasets:
    if dataset["rows"] == 0:
        print(f'{dataset["name"]} Empty')
    elif dataset["rows"] < 1000:
        print(f'{dataset["name"]} Small')
    elif dataset["rows"] <100000:
        print(f'{dataset["name"]} Medium')
    else:
        print(f'{dataset["name"]} Large')



# Exercise 29: Pipeline Validation
# --------------------------------
# Create:
#
# file_exists = True
# row_count = 500
# data_valid = True
#
# The pipeline should run only when:
#
# - file exists
# - row count > 0
# - data is valid
#
# Otherwise print the appropriate reason why
# the pipeline cannot run.


# Write your code below:

file_exists = True
row_count = 500
data_valid = True
if file_exists:
    if row_count > 0:
        if data_valid:
            print("Pipeline will run")
        else:
            print("Data not valid")
    else:
        print("row count cant be negative or null")
else:
    print("File Doesnt exit")



# ============================================================
# LEVEL 12 — CHALLENGE
# ============================================================


# Exercise 30: Mini ETL Control Flow
# ----------------------------------
#
# Build a small control-flow program that simulates
# an ETL pipeline.
#
# Input data:
#
# files = [
#     "sales.csv",
#     "temp.csv",
#     "customers.csv",
#     "empty.csv",
#     "orders.csv",
#     "error.csv",
#     "products.csv",
# ]
#
# Create a dictionary containing row counts:
#
# row_counts = {
#     "sales.csv": 500,
#     "temp.csv": 100,
#     "customers.csv": 1000,
#     "empty.csv": 0,
#     "orders.csv": 5000,
#     "error.csv": 100,
#     "products.csv": 250,
# }
#
# Rules:
#
# 1. Skip files beginning with "temp".
#
# 2. If the file has 0 rows:
#       print "Skipping empty file: <filename>"
#       continue
#
# 3. If the file is "error.csv":
#       print "Critical error: <filename>"
#       break
#
# 4. Otherwise:
#       print "Processing <filename>: <rows> rows"
#
# You should use:
#
# - dictionary access
# - for loop
# - if / elif / else
# - continue
# - break
#
# This is your first mini Data Engineering-style
# control-flow problem.


# Write your code below:
files = [
    "sales.csv",
    "temp.csv",
    "customers.csv",
    "empty.csv",
    "orders.csv",
    "error.csv",
    "products.csv",
]

row_counts = {
     "sales.csv": 500,
     "temp.csv": 100,
     "customers.csv": 1000,
     "empty.csv": 0,
     "orders.csv": 5000,
     "error.csv": 100,
     "products.csv": 250,
 }
for file in files:
    if file == 'temp.csv':
        continue
    if row_counts[file] == 0:
        print(f'Skipping empty file: {file}')
        continue
    if file == 'error.csv':
        print(f'Critical error:  {file}')
        break
    print(f'Processing {file}: {row_counts[file]} rows')



# ============================================================
# SELF-CHECK
# ============================================================
#
# Before marking this section as practiced, make sure you can
# explain the difference between:
#
# if
# elif
# else
# for
# while
# break
# continue
# pass
#
# Also make sure you understand:
#
# range(stop)
# range(start, stop)
# range(start, stop, step)
#
# ============================================================

