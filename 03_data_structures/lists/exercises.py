# ============================================

# PYTHON LISTS — EXERCISES

# Data Engineering Learning

#

# IMPORTANT:

# Try solving these yourself.

# Do not look for solutions immediately.

# ============================================

# ============================================

# LEVEL 1 — BASICS

# ============================================

# Exercise 1

# Create a list containing:

# "customers.csv", "orders.csv", "sales.csv"
list = ['customers.csv', 'orders.csv', 'sales.csv']
print(list)

# Print the list.

# Exercise 2
print("Exercise 2")

# Create a list of five integers.
integers = [1,2,3,4,5]

# Print the first element.
print(integers[0])

# Exercise 3

# Using the list below, print the last element

# using negative indexing.

files = ["customers.csv", "orders.csv", "sales.csv"]
print("Exercise 3")
print(files[-1])

# Exercise 4

# Using the same list, print the second element

# using negative indexing.
print("Exercise 4")
print(files[-2])

# Exercise 5

# Find the number of elements in the list.
print("Exercise 5")
print(len(files))

# ============================================


# LEVEL 2 — SLICING

# ============================================

# Exercise 6

# Given:

files = [
"customers.csv",
"orders.csv",
"sales.csv",
"products.csv",
"returns.csv"
]
print("Exercise 6")
# Print:

# a) First three elements
print(files[:3])

# b) Last two elements
print(files[-2:])
# c) Elements from index 1 to index 3
print(files[1:4])
# d) Every second element
print(files[::2])
# Exercise 7
print("Exercise 7")
# Reverse the list using slicing.
print(files[-1::-1])
# Exercise 8

# Using slicing, create a new list containing:

# "orders.csv", "sales.csv", "products.csv"
print("Exercise 8")
new_list = files[1:4]
print(new_list)
# ============================================

# LEVEL 3 — MODIFYING LISTS

# ============================================

# Exercise 9

# Add "products.csv" to the end of this list

# using append().

files = ["customers.csv", "orders.csv"]
print("Exercise 9")
files.append("products.csv")
print(files)

# Exercise 10

# Add both "sales.csv" and "products.csv"

# using extend().
print("Exercise 9")
files.extend(["sales.csv", "products.csv"])
print(files)

# Exercise 11

# Insert "sales.csv" at index 1.

files = ["customers.csv", "orders.csv", "products.csv"]
print("Exercise 11")
files.insert(1,"sales.csv")
print(files)

# Exercise 12

# Change "orders.csv" to "purchase_orders.csv".
print("Exercise 12")
files = ["customers.csv", "orders.csv", "sales.csv"]
files[1] = "purchase_orders.csv"
print(files)

# ============================================

# LEVEL 4 — REMOVING ELEMENTS

# ============================================

# Exercise 13

# Remove "temp.csv" using remove().
print("Exercise 13")

files = [
"customers.csv",
"temp.csv",
"orders.csv",
"sales.csv",
]

files.remove("temp.csv") # removes only first occurence of temp.csv
print(files)
# Exercise 14

# Remove the element at index 2 using pop().
print("Exercise 14")

# Store the removed element in a variable called removed.
removed = files.pop(2)
print(removed)
print(files)

# Exercise 15
print("Exercise 15")
# Remove the first element using del.
del files[0]
print(files)

# Exercise 16
print("Exercise 16")
# Remove all elements using clear().
files.clear()
print(files)


# ============================================

# LEVEL 5 — SEARCHING AND COUNTING

# ============================================

# Exercise 17

# Count how many times "sales.csv" appears.

files = [
"sales.csv",
"orders.csv",
"sales.csv",
"customers.csv",
"sales.csv"
]
print("Exercise 17")

print(f'sales.csv Appeared:{files.count("sales.csv")} times')

# Exercise 18

# Find the index of the first "orders.csv".
print("Exercise 18")
print(files.index("orders.csv"))

# Exercise 19

# Check whether "customers.csv" exists in the list.
print("Exercise 19")
print({"customers.csv" in files})

files = ["orders.csv", "sales.csv", "products.csv"]

# ============================================

# LEVEL 6 — SORTING

# ============================================

# Exercise 20

# Sort this list in ascending order using sort().

numbers = [50, 10, 40, 20, 30]
numbers.sort()
print("Exercise 20")
print(numbers)

# Exercise 21

# Sort the list in descending order.
print("Exercise 21")
numbers.sort(reverse = True)
print(numbers)
# Exercise 22

# Use sorted() to create a new sorted list.

# Keep the original list unchanged.
print("Exercise 22")
numbers = [70, 20, 50, 10, 40]
sorted_list = sorted(numbers)
print(sorted_list)
print(numbers)

# ============================================

# LEVEL 7 — ITERATION

# ============================================

# Exercise 23

# Print every file using a for loop.
print("Exercise 23")

files = [
"customers.csv",
"orders.csv",
"sales.csv"
]
for file in files:
    print(file)
# Exercise 24

# Print:
print("Exercise 24")
# Processing customers.csv

# Processing orders.csv

# etc.

for file in files:
    print(f'Processing {file}')

# Use a for loop and f-string.

# Exercise 25

# Given a list of numbers, create a new list

# containing only numbers greater than 50.
print("Exercise 25")
numbers = [10, 75, 20, 90, 45, 60, 30]
big_numbers =[]
for number in numbers:
    if number > 50:
        big_numbers.append(number)
print(big_numbers)

# ============================================

# LEVEL 8 — DATA ENGINEERING EXERCISES

# ============================================

# Exercise 26 — CSV filtering

#

# Given a list containing different file types,

# create a new list containing only .csv files.

files = [
"customers.csv",
"notes.txt",
"orders.csv",
"data.json",
"sales.csv",
"readme.md"
]
print("Exercise 26")
csv_files=[]
for file in files:
    if file.endswith(".csv"):
        csv_files.append(file)
print(csv_files)

# Exercise 27 — Remove temporary files

#

# Given the list below, remove every "temp.csv"

# occurrence.

#

# Think carefully about duplicates.

files = [
"customers.csv",
"temp.csv",
"orders.csv",
"temp.csv",
"sales.csv"
]
print("Exercise 27")
for file in files:
    if file == "temp.csv":
        del files[files.index(file)]
print(files)

# Exercise 28 — Required files

#

# Given:

required_files = [
"customers.csv",
"orders.csv",
"sales.csv"
]

available_files = [
"customers.csv",
"sales.csv",
"products.csv"
]

# Find which required files are missing.

# Store the missing files in a new list.
print("Exercise 28")
missing_files=[]
for file in required_files:
    if file not in available_files:
        missing_files.append(file)
print(missing_files)



# Exercise 29 — File validation

#

# Given a list of files, determine whether

# "customers.csv" exists.

#

# Print:

# "File available"

# or

# "File missing"
files = [
"customers.csv",
"sales.csv",
"products.csv"
]
print("Exercise 29")
if "customers.csv" in files:
    print("File available")
else:
    print("File missing")


# Exercise 30 — Processing pipeline

#

# You are given:

#

files = [

"customers.csv",

"temp.csv",

"orders.csv",

"empty.csv",

"sales.csv"

]

#

# Rules:

#

# 1. Skip "temp.csv"

# 2. Skip "empty.csv"

# 3. Process every other file

#
print("Exercise 30")
for file in files:
    if file == "temp.csv" or file == "empty.csv":
        continue
    print(f'Processing {file}')

# Print an appropriate message for each action.

# ============================================

# LEVEL 9 — CHALLENGE

# ============================================

# Exercise 31 — Duplicate detection

#

# Given:

files = [
"customers.csv",
"orders.csv",
"sales.csv",
"orders.csv",
"customers.csv"
]

# Create a new list containing the files

# that appear more than once.

#

# Expected concept:

# ["customers.csv", "orders.csv"]

#

# Try to solve this without using a set.
print("Exercise 31")
duplicate_files=[]
for file in files:
    if files.count(file) >1 and file not in duplicate_files:
        duplicate_files.append(file)
print(duplicate_files)
# Exercise 32 — Clean a file list

#

# Given:

files = [
"customers.csv",
"temp.csv",
"orders.csv",
"customers.csv",
"sales.txt",
"sales.csv",
"temp.csv"
]

#
print("Exercise 32")
# Create a cleaned list that:

#

# 1. Contains only .csv files

# 2. Removes "temp.csv"

# 3. Removes duplicates

#
# stage wise problem solving - easy to debug and used when intermediate results are useful / required
csv_files=[]
filtered_files=[]
for file in files:
    if file.endswith(".csv"):
       csv_files.append(file)
for file in csv_files:
    if file == "temp.csv":
        continue
    filtered_files.append(file)
cleaned_files=[]
for file in filtered_files:
    if file not in cleaned_files:
        cleaned_files.append(file)
print(cleaned_files)

# single loop version - better for a simple transformation
'''
cleaned_files = []

for file in files:

    if not file.endswith(".csv"):
        continue

    if file == "temp.csv":
        continue

    if file in cleaned_files:
        continue

    cleaned_files.append(file)

print(cleaned_files)
'''
# Preserve the original order.

# Exercise 33 — Batch processing

#

# Given:

files = [
"file_01.csv",
"file_02.csv",
"file_03.csv",
"file_04.csv",
"file_05.csv",
"file_06.csv",
"file_07.csv"
]

#
print("Exercise 33")
total_files= len(files)
batch_size = 2
total_batches = total_files//batch_size + int(total_files%batch_size > 0)

for batch in range(total_batches):
    print(f'Batch {batch+1}')
    fetched_files =[]
    for file_number in range(batch_size):
        if not files:
            break
        fetched_files.append(files.pop(0))
    for file in fetched_files:
        print(f'Processing {file}')
    fetched_files.clear()
# Process files in batches of two.

#

# Expected batches:

#

# Batch 1:

# file_01.csv

# file_02.csv

#

# Batch 2:

# file_03.csv

# file_04.csv

#

# Batch 3:

# file_05.csv

# file_06.csv

# Exercise 34 — Simple ETL list

#

# raw_data contains customer records:

#

# Each record is:

# [customer_id, name, country, status]

#

# Create a new list containing only active

# customers from India.
raw_data =[
    [1, "shree", "India","active"],
    [2,"ronak", "Australia","active"],
    [3,"aman", "India", "idle"]
]
print("Exercise 34")

potential_customers = []
for record in raw_data:
    if record[2] == "India" and record[3] =="active":
        potential_customers.append(record)
print(potential_customers)

# Exercise 35 — Mini Data Engineering Challenge

#

# You receive:

#

files = [

"customers.csv",

"temp.csv",

"orders.csv",

"empty.csv",

"sales.csv",

"customers.csv",

"error.csv",

"products.txt"

]

#

# Requirements:

#

# 1. Ignore non-CSV files.
files_to_be_processed=[]

for file in files:
    if not file.endswith(".csv"):
        continue

# 2. Ignore temp.csv.
    if file == 'temp.csv':
        continue
# 3. Ignore empty.csv.
    if file == 'empty.csv':
        continue
# 4. Remove duplicate filenames.
    if file not in files_to_be_processed:
        files_to_be_processed.append(file)
# 5. If error.csv exists, report it.
final_list=[]
if "error.csv" in files_to_be_processed:
    print("Error Found")
    for file in files_to_be_processed:
        if file == "error.csv":
            continue
        else:
            final_list.append(file)
print(final_list)
        

    


    
# 6. Create a final list of files that should be processed.

# 7. Preserve the original order.

#

# Print:

#

# - Final files to process

#

# Do not use sets for this exercise.

#

# ============================================

# END OF EXERCISES

# ============================================
