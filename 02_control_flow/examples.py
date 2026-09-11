
"""
02 - CONTROL FLOW
=================

This file contains essential Python control-flow examples
for Data Engineering.

Topics covered:
1. if
2. if / else
3. if / elif / else
4. Nested if
5. for loops
6. range()
7. break
8. continue
9. while loops
10. pass
11. Combining control-flow concepts
12. Data Engineering-style examples
"""


# ============================================================
# 1. IF STATEMENT
# ============================================================

records = 100

if records > 0:
    print("Data is available")


# ============================================================
# 2. IF / ELSE
# ============================================================

records = 0

if records > 0:
    print("Data is available")
else:
    print("No data available")


# ============================================================
# 3. IF / ELIF / ELSE
# ============================================================

rows = 5000

if rows == 0:
    print("Empty dataset")
elif rows < 100:
    print("Small dataset")
elif rows < 10000:
    print("Medium dataset")
else:
    print("Large dataset")


# ============================================================
# 4. NESTED IF
# ============================================================

file_exists = True
row_count = 500

if file_exists:
    print("File found")

    if row_count > 0:
        print("Process data")
    else:
        print("File is empty")
else:
    print("File not found")


# ============================================================
# 5. FOR LOOP
# ============================================================

files = ["sales.csv", "customers.csv", "orders.csv"]

for file in files:
    print(f"Processing {file}")


# ============================================================
# 6. FOR LOOP WITH RANGE()
# ============================================================

for i in range(5):
    print(i)


# ============================================================
# 7. RANGE(start, stop)
# ============================================================

for i in range(1, 6):
    print(f"Batch {i}")


# ============================================================
# 8. RANGE(start, stop, step)
# ============================================================

for i in range(2, 11, 2):
    print(i)


# ============================================================
# 9. BREAK
# ============================================================

files = ["a.csv", "b.csv", "error.csv", "d.csv"]

for file in files:

    if file == "error.csv":
        print("Critical error. Stopping pipeline.")
        break

    print(f"Processing {file}")


# ============================================================
# 10. CONTINUE
# ============================================================

files = ["sales.csv", "temp.csv", "orders.csv", "temp.csv"]

for file in files:

    if file == "temp.csv":
        continue

    print(f"Processing {file}")


# ============================================================
# 11. WHILE LOOP
# ============================================================

count = 1

while count <= 3:
    print(f"Attempt {count}")
    count += 1


# ============================================================
# 12. WHILE LOOP WITH DATA-STYLE LOGIC
# ============================================================

rows = 1000

while rows > 0:
    print(f"Remaining rows: {rows}")
    rows -= 250


# ============================================================
# 13. PASS
# ============================================================

def validate_data(data):
    pass


# ============================================================
# 14. COMBINING IF + FOR
# ============================================================

records = [100, 0, 250, 0, 500]

for record_count in records:

    if record_count > 0:
        print(f"Processing {record_count} records")
    else:
        print("Skipping empty dataset")


# ============================================================
# 15. COMBINING FOR + CONTINUE
# ============================================================

files = [
    "sales.csv",
    "temp.csv",
    "customers.csv",
    "temp.csv",
    "orders.csv",
]

for file in files:

    if file.startswith("temp"):
        continue

    print(f"Processing {file}")


# ============================================================
# 16. COMBINING FOR + BREAK
# ============================================================

files = [
    "sales.csv",
    "customers.csv",
    "error.csv",
    "orders.csv",
]

for file in files:

    if file == "error.csv":
        print("Critical file error.")
        break

    print(f"Successfully processed {file}")


# ============================================================
# 17. DATA QUALITY CHECK
# ============================================================

records = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": ""},
    {"id": 3, "name": "Charlie"},
]

for record in records:

    if record["name"] == "":
        print(f"Invalid record: {record['id']}")
        continue

    print(f"Valid record: {record['id']}")


# ============================================================
# 18. CLASSIFY DATASET SIZE
# ============================================================

row_count = 25000

if row_count == 0:
    dataset_type = "Empty"
elif row_count < 1000:
    dataset_type = "Small"
elif row_count < 100000:
    dataset_type = "Medium"
else:
    dataset_type = "Large"

print(f"Dataset type: {dataset_type}")


# ============================================================
# 19. PROCESS MULTIPLE FILES
# ============================================================

files = [
    "sales.csv",
    "customers.csv",
    "orders.csv",
]

for file in files:

    if file.endswith(".csv"):
        print(f"Reading CSV file: {file}")
    else:
        print(f"Unsupported file: {file}")


# ============================================================
# 20. PROCESS ONLY VALID RECORDS
# ============================================================

records = [
    {"id": 1, "amount": 500},
    {"id": 2, "amount": 0},
    {"id": 3, "amount": 750},
    {"id": 4, "amount": -100},
]

for record in records:

    if record["amount"] <= 0:
        print(f"Invalid amount for record {record['id']}")
        continue

    print(f"Processing record {record['id']}")


# ============================================================
# 21. RETRY-STYLE WHILE LOOP
# ============================================================

max_attempts = 3
attempt = 1
success = False

while attempt <= max_attempts:

    print(f"Attempt {attempt}")

    # Simulating a successful operation
    if attempt == 2:
        success = True

    if success:
        print("Operation successful")
        break

    attempt += 1

if not success:
    print("Operation failed after maximum attempts")


# ============================================================
# 22. SIMPLE PIPELINE CONTROL FLOW
# ============================================================

file_exists = True
row_count = 500
data_valid = True

if not file_exists:
    print("Pipeline stopped: file not found")

elif row_count == 0:
    print("Pipeline stopped: file is empty")

elif not data_valid:
    print("Pipeline stopped: data validation failed")

else:
    print("All checks passed")
    print("Starting ETL process")


# ============================================================
# 23. COMPLETE FILE-PROCESSING EXAMPLE
# ============================================================

files = [
    "sales.csv",
    "customers.csv",
    "temp.csv",
    "orders.csv",
    "error.csv",
    "products.csv",
]

for file in files:

    # Skip temporary files
    if file.startswith("temp"):
        print(f"Skipping temporary file: {file}")
        continue

    # Stop if a critical file is encountered
    if file == "error.csv":
        print("Critical error detected. Stopping pipeline.")
        break

    # Process valid CSV files
    if file.endswith(".csv"):
        print(f"Processing {file}")

    else:
        print(f"Unsupported file: {file}")


# ============================================================
# 24. CONTROL FLOW WITH NONE
# ============================================================

value = None

if value is None:
    print("No value available")
else:
    print(f"Value: {value}")


# ============================================================
# 25. NESTED DATA PROCESSING
# ============================================================

datasets = [
    {
        "name": "sales",
        "rows": 500,
        "valid": True,
    },
    {
        "name": "customers",
        "rows": 0,
        "valid": True,
    },
    {
        "name": "orders",
        "rows": 1000,
        "valid": False,
    },
]

for dataset in datasets:

    if dataset["rows"] == 0:
        print(f"{dataset['name']}: Empty dataset")
        continue

    if not dataset["valid"]:
        print(f"{dataset['name']}: Validation failed")
        continue

    print(
        f"{dataset['name']}: "
        f"Processing {dataset['rows']} rows"
    )


# ============================================================
# END OF CONTROL FLOW EXAMPLES
# ============================================================

print("Control flow examples completed.")

