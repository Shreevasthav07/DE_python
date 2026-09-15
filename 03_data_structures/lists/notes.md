# Python Lists

## 1. What is a List?

A list is an ordered, mutable collection of elements.

```python
files = ["customers.csv", "orders.csv", "sales.csv"]
```

### Characteristics of Lists

* Ordered — elements maintain their position.
* Mutable — elements can be changed after creation.
* Allow duplicates.
* Can contain different data types.
* Use square brackets `[]`.
* Support indexing and slicing.

```python
data = [101, "Alice", 5000.5, True, None]
```

---

## 2. Creating Lists

```python
files = ["customers.csv", "orders.csv", "sales.csv"]

numbers = [10, 20, 30, 40]

empty_list = []

mixed = [101, "Alice", 5000.5, True]
```

---

## 3. Indexing

Python uses zero-based indexing.

```python
files = ["customers.csv", "orders.csv", "sales.csv"]

files[0]    # customers.csv
files[1]    # orders.csv
files[2]    # sales.csv
```

### Negative Indexing

Negative indexing starts from the end.

```python
files[-1]   # sales.csv
files[-2]   # orders.csv
files[-3]   # customers.csv
```

---

## 4. Slicing

Syntax:

```python
list[start:stop]
```

The `start` index is included.

The `stop` index is excluded.

```python
files = [
    "customers.csv",
    "orders.csv",
    "sales.csv",
    "products.csv"
]

files[1:3]
# ['orders.csv', 'sales.csv']

files[:2]
# ['customers.csv', 'orders.csv']

files[2:]
# ['sales.csv', 'products.csv']

files[:]
# entire list
```

### Slicing with a Step

Syntax:

```python
list[start:stop:step]
```

Examples:

```python
files[::2]
files[::-1]
files[1::2]
```

`[::-1]` reverses the list.

---

## 5. Lists are Mutable

Lists can be modified after creation.

```python
files = ["customers.csv", "orders.csv", "sales.csv"]

files[1] = "products.csv"

print(files)
```

Output:

```text
['customers.csv', 'products.csv', 'sales.csv']
```

---

# Adding Elements

## 6. append()

Adds one element to the end of the list.

```python
files = ["customers.csv", "orders.csv"]

files.append("sales.csv")
```

Result:

```text
['customers.csv', 'orders.csv', 'sales.csv']
```

### Important

`append()` adds its argument as **one element**.

```python
files.append(["sales.csv", "products.csv"])
```

Result:

```text
['customers.csv', 'orders.csv', ['sales.csv', 'products.csv']]
```

This creates a nested list.

---

## 7. extend()

Adds the elements of an iterable individually.

```python
files = ["customers.csv", "orders.csv"]

files.extend(["sales.csv", "products.csv"])
```

Result:

```text
['customers.csv', 'orders.csv', 'sales.csv', 'products.csv']
```

### append() vs extend()

| Method      | Behavior                            |
| ----------- | ----------------------------------- |
| `append(x)` | Adds `x` as one element             |
| `extend(x)` | Adds elements from `x` individually |

`extend()` can work with other iterables too.

---

## 8. insert()

Adds an element at a specific index.

Syntax:

```python
list.insert(index, value)
```

Example:

```python
files = ["customers.csv", "orders.csv", "products.csv"]

files.insert(1, "sales.csv")
```

Result:

```text
['customers.csv', 'sales.csv', 'orders.csv', 'products.csv']
```

Existing elements shift to the right.

---

# Removing Elements

## 9. remove()

Removes the first occurrence of a value.

```python
files = ["customers.csv", "orders.csv", "sales.csv", "orders.csv"]

files.remove("orders.csv")
```

Result:

```text
['customers.csv', 'sales.csv', 'orders.csv']
```

### Important

`remove()` works by **value**, not index.

If the value doesn't exist, Python raises `ValueError`.

---

## 10. pop()

Removes an element by index and returns the removed element.

```python
files = ["customers.csv", "orders.csv", "sales.csv"]

removed = files.pop(1)
```

Now:

```python
removed
# 'orders.csv'

files
# ['customers.csv', 'sales.csv']
```

If no index is supplied:

```python
files.pop()
```

the last element is removed.

---

## 11. del

Deletes an element by index.

```python
files = ["customers.csv", "orders.csv", "sales.csv"]

del files[1]
```

Result:

```text
['customers.csv', 'sales.csv']
```

It can also delete a range:

```python
del files[1:3]
```

Unlike `pop()`, `del` does not return the removed element.

---

## 12. clear()

Removes all elements.

```python
files = ["customers.csv", "orders.csv"]

files.clear()

print(files)
```

Output:

```text
[]
```

---

# Searching and Counting

## 13. len()

Returns the number of elements.

```python
files = ["a.csv", "b.csv", "c.csv"]

len(files)
# 3
```

---

## 14. count()

Counts how many times a value appears.

```python
files = ["sales.csv", "orders.csv", "sales.csv"]

files.count("sales.csv")
# 2
```

---

## 15. index()

Returns the index of the first matching value.

```python
files = ["sales.csv", "orders.csv", "sales.csv"]

files.index("sales.csv")
# 0
```

---

## 16. Membership Testing

Use `in` and `not in`.

```python
files = ["sales.csv", "orders.csv"]

"sales.csv" in files
# True

"customers.csv" in files
# False
```

```python
"customers.csv" not in files
# True
```

This is useful when checking whether a file, column, ID, or other value exists.

---

# Sorting

## 17. sort()

`sort()` modifies the original list.

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

### Descending order

```python
numbers.sort(reverse=True)
```

Result:

```text
[40, 30, 20, 10]
```

---

## 18. sorted()

`sorted()` creates and returns a new sorted list.

```python
numbers = [40, 10, 30, 20]

result = sorted(numbers)

print(numbers)
print(result)
```

Output:

```text
[40, 10, 30, 20]
[10, 20, 30, 40]
```

### Key difference

| `sort()`               | `sorted()`          |
| ---------------------- | ------------------- |
| Modifies original list | Creates a new list  |
| Returns `None`         | Returns sorted list |
| Method of list         | Built-in function   |

---

# Reversing

## 19. reverse()

`reverse()` reverses the original list.

```python
files = ["a.csv", "b.csv", "c.csv"]

files.reverse()
```

Result:

```text
['c.csv', 'b.csv', 'a.csv']
```

You can also reverse using slicing:

```python
reversed_files = files[::-1]
```

Remember that `[::-1]` creates a reversed list rather than modifying the original list.

---

# Iterating Through Lists

## 20. for Loop

```python
files = ["customers.csv", "orders.csv", "sales.csv"]

for file in files:
    print(file)
```

Output:

```text
customers.csv
orders.csv
sales.csv
```

This is extremely common in Data Engineering.

Example:

```python
for file in files:
    print(f"Processing {file}")
```

---

# Copying Lists

## 21. Assignment vs Copy

This does NOT create an independent list:

```python
files = ["a.csv", "b.csv"]

backup = files
```

Both variables refer to the same list.

Use:

```python
backup = files.copy()
```

or:

```python
backup = files[:]
```

to create a separate shallow copy.

---

# Nested Lists

A list can contain another list.

```python
data = [
    [101, "Alice", 5000],
    [102, "Bob", 6000]
]
```

Accessing nested data:

```python
data[0]
# [101, 'Alice', 5000]

data[0][1]
# 'Alice'
```

Nested structures become especially important when processing structured data such as API responses and JSON.

---

# Lists in Data Engineering

Lists are commonly used for:

### File collections

```python
files = [
    "customers.csv",
    "orders.csv",
    "sales.csv"
]
```

### Column collections

```python
columns = [
    "customer_id",
    "name",
    "email",
    "created_at"
]
```

### Records

```python
record = [101, "Alice", "India", 5000]
```

### Pipeline processing

```python
for file in files:
    print(f"Processing {file}")
```

### Filtering

```python
csv_files = []

for file in files:
    if file.endswith(".csv"):
        csv_files.append(file)
```

---

# Common Mistakes

### Mistake 1 — Forgetting zero-based indexing

```python
files[0]
```

is the first element, not the second.

### Mistake 2 — Confusing append and extend

```python
append(["a", "b"])
```

adds one nested element.

```python
extend(["a", "b"])
```

adds two elements.

### Mistake 3 — Confusing remove and pop

```python
remove("sales.csv")  # value
pop(2)               # index
```

### Mistake 4 — Forgetting that sort() modifies the list

```python
numbers.sort()
```

changes `numbers`.

### Mistake 5 — Assuming assignment creates a copy

```python
backup = files
```

does not create an independent list.

---

# Quick Reference

| Operation           | Purpose                     |
| ------------------- | --------------------------- |
| `list[index]`       | Access element              |
| `list[start:stop]`  | Slice                       |
| `list.append(x)`    | Add one element             |
| `list.extend(x)`    | Add multiple elements       |
| `list.insert(i, x)` | Insert at index             |
| `list.remove(x)`    | Remove first matching value |
| `list.pop(i)`       | Remove and return element   |
| `del list[i]`       | Delete by index             |
| `list.clear()`      | Remove everything           |
| `len(list)`         | Number of elements          |
| `list.count(x)`     | Count occurrences           |
| `list.index(x)`     | Find first index            |
| `list.sort()`       | Sort original list          |
| `sorted(list)`      | Return sorted copy          |
| `list.reverse()`    | Reverse original list       |
| `x in list`         | Membership check            |
| `list.copy()`       | Shallow copy                |

---

# Data Engineering Takeaway

For Data Engineering, the most important List skills are:

1. Indexing and slicing
2. Iteration
3. `append()` and `extend()`
4. Filtering
5. Sorting
6. Membership testing
7. Removing unwanted data
8. Working with nested lists
9. Understanding mutability and copying

These skills will later appear naturally in ETL pipelines, API processing, Pandas, and PySpark.
