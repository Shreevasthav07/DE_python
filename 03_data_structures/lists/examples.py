# ============================================

# PYTHON LISTS — EXAMPLES

# Data Engineering Learning

# ============================================

# ============================================

# 1. CREATING LISTS

# ============================================

files = ["customers.csv", "orders.csv", "sales.csv"]

numbers = [10, 20, 30, 40]

empty_list = []

mixed = [101, "Alice", 5000.5, True, None]

print(files)
print(numbers)
print(empty_list)
print(mixed)

# ============================================

# 2. INDEXING

# ============================================

files = ["customers.csv", "orders.csv", "sales.csv"]

print(files[0])
print(files[1])
print(files[2])

# ============================================

# 3. NEGATIVE INDEXING

# ============================================

print(files[-1])
print(files[-2])
print(files[-3])

# ============================================

# 4. SLICING

# ============================================

files = [
"customers.csv",
"orders.csv",
"sales.csv",
"products.csv",
"returns.csv"
]

print(files[1:4])
print(files[:3])
print(files[2:])
print(files[:])

# ============================================

# 5. SLICING WITH STEP

# ============================================

print(files[::2])
print(files[1::2])
print(files[::-1])
print(files[-1::-2])

# ============================================

# 6. MODIFYING ELEMENTS

# ============================================

files = ["customers.csv", "orders.csv", "sales.csv"]

files[1] = "products.csv"

print(files)

# ============================================

# 7. APPEND

# ============================================

files = ["customers.csv", "orders.csv"]

files.append("sales.csv")

print(files)

# ============================================

# 8. APPEND WITH A LIST

# ============================================

files = ["customers.csv", "orders.csv"]

files.append(["sales.csv", "products.csv"])

print(files)

# ============================================

# 9. EXTEND

# ============================================

files = ["customers.csv", "orders.csv"]

files.extend(["sales.csv", "products.csv"])

print(files)

# ============================================

# 10. APPEND VS EXTEND

# ============================================

files_1 = ["customers.csv", "orders.csv"]
files_1.append(["sales.csv", "products.csv"])

files_2 = ["customers.csv", "orders.csv"]
files_2.extend(["sales.csv", "products.csv"])

print("append:", files_1)
print("extend:", files_2)

# ============================================

# 11. INSERT

# ============================================

files = ["customers.csv", "orders.csv", "products.csv"]

files.insert(1, "sales.csv")

print(files)

# ============================================

# 12. REMOVE

# ============================================

files = [
"customers.csv",
"orders.csv",
"sales.csv",
"orders.csv"
]

files.remove("orders.csv")

print(files)

# ============================================

# 13. POP

# ============================================

files = ["customers.csv", "orders.csv", "sales.csv"]

removed = files.pop(1)

print("Removed:", removed)
print("Remaining:", files)

# ============================================

# 14. POP WITHOUT INDEX

# ============================================

files = ["customers.csv", "orders.csv", "sales.csv"]

removed = files.pop()

print("Removed:", removed)
print("Remaining:", files)

# ============================================

# 15. DEL

# ============================================

files = ["customers.csv", "orders.csv", "sales.csv"]

del files[1]

print(files)

# ============================================

# 16. DEL WITH SLICING

# ============================================

files = [
"customers.csv",
"orders.csv",
"sales.csv",
"products.csv"
]

del files[1:3]

print(files)

# ============================================

# 17. CLEAR

# ============================================

files = ["customers.csv", "orders.csv"]

files.clear()

print(files)

# ============================================

# 18. LEN

# ============================================

files = ["customers.csv", "orders.csv", "sales.csv"]

print(len(files))

# ============================================

# 19. COUNT

# ============================================

files = [
"sales.csv",
"orders.csv",
"sales.csv",
"customers.csv",
"sales.csv"
]

print(files.count("sales.csv"))
print(files.count("orders.csv"))

# ============================================

# 20. INDEX

# ============================================

files = [
"sales.csv",
"orders.csv",
"sales.csv"
]

print(files.index("sales.csv"))
print(files.index("orders.csv"))

# ============================================

# 21. MEMBERSHIP TESTING

# ============================================

files = ["sales.csv", "orders.csv"]

print("sales.csv" in files)
print("customers.csv" in files)

print("customers.csv" not in files)

# ============================================

# 22. SORT

# ============================================

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

# ============================================

# 23. SORT DESCENDING

# ============================================

numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)

# ============================================

# 24. SORTED

# ============================================

numbers = [40, 10, 30, 20]

result = sorted(numbers)

print("Original:", numbers)
print("Sorted:", result)

# ============================================

# 25. REVERSE

# ============================================

files = ["customers.csv", "orders.csv", "sales.csv"]

files.reverse()

print(files)

# ============================================

# 26. REVERSE USING SLICING

# ============================================

files = ["customers.csv", "orders.csv", "sales.csv"]

reversed_files = files[::-1]

print("Original:", files)
print("Reversed:", reversed_files)

# ============================================

# 27. ITERATING THROUGH A LIST

# ============================================

files = [
"customers.csv",
"orders.csv",
"sales.csv"
]

for file in files:
    print(file)

# ============================================

# 28. ITERATING — DATA ENGINEERING EXAMPLE

# ============================================

files = [
"customers.csv",
"orders.csv",
"sales.csv"
]

for file in files:
    print(f"Processing {file}")

# ============================================

# 29. FILTERING FILES

# ============================================

files = [
"customers.csv",
"orders.txt",
"sales.csv",
"notes.txt"
]

csv_files = []

for file in files:
    if file.endswith(".csv"):
        csv_files.append(file)

print(csv_files)

# ============================================

# 30. LIST COPY

# ============================================

files = ["customers.csv", "orders.csv"]

backup = files.copy()

backup.append("sales.csv")

print("Original:", files)
print("Backup:", backup)

# ============================================

# 31. ASSIGNMENT IS NOT A COPY

# ============================================

files = ["customers.csv", "orders.csv"]

backup = files

backup.append("sales.csv")

print("Original:", files)
print("Backup:", backup)

# Both contain sales.csv because both variables

# refer to the same list.

# ============================================

# 32. NESTED LISTS

# ============================================

data = [
[101, "Alice", 5000],
[102, "Bob", 6000],
[103, "Charlie", 5500]
]

print(data)
print(data[0])
print(data[0][1])

# ============================================

# 33. PROCESSING NESTED RECORDS

# ============================================

records = [
[101, "Alice", 5000],
[102, "Bob", 6000],
[103, "Charlie", 5500]
]

for record in records:
    print(record)

# ============================================

# 34. EXTRACTING VALUES FROM RECORDS

# ============================================

records = [
[101, "Alice", 5000],
[102, "Bob", 6000],
[103, "Charlie", 5500]
]

for record in records:
    print(record[1])

# ============================================

# 35. SIMPLE FILE PROCESSING PIPELINE

# ============================================

files = [
"customers.csv",
"temp.csv",
"orders.csv",
"sales.csv"
]

for file in files:
    if file == "temp.csv":
        continue
print(f"Processing {file}")

# ============================================

# END OF LIST EXAMPLES

# ============================================
