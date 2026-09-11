# Python Control Flow

## 1. What is Control Flow?

Control flow determines **which code runs, when it runs, and how many times it runs**.

In Data Engineering, control flow is used for things like:

* Checking whether a file exists
* Checking whether data is available
* Validating records
* Processing multiple files
* Retrying operations
* Skipping invalid data
* Stopping a pipeline when a critical error occurs

---

# 2. `if` Statement

The `if` statement executes code only when a condition is `True`.

### Syntax

```python
if condition:
    # code to execute
```

### Example

```python
records = 100

if records > 0:
    print("Data is available")
```

Output:

```text
Data is available
```

The condition:

```python
records > 0
```

evaluates to `True`, so the indented code executes.

### Important

Python uses **indentation** to determine which statements belong to the `if` block.

```python
if records > 0:
    print("Data is available")
```

Usually, Python code uses **4 spaces** for indentation.

---

# 3. `if / else`

Use `if / else` when there are **two possible paths**.

### Syntax

```python
if condition:
    # runs when condition is True
else:
    # runs when condition is False
```

### Example

```python
records = 0

if records > 0:
    print("Data is available")
else:
    print("No data available")
```

Output:

```text
No data available
```

With `if / else`, exactly **one branch** executes.

---

# 4. `if / elif / else`

Use `elif` when there are **multiple possible conditions**.

### Syntax

```python
if condition1:
    # code
elif condition2:
    # code
elif condition3:
    # code
else:
    # code
```

### Example

```python
rows = 5000

if rows == 0:
    print("Empty dataset")
elif rows < 100:
    print("Small dataset")
elif rows < 10000:
    print("Medium dataset")
else:
    print("Large dataset")
```

Output:

```text
Medium dataset
```

### Important rule

Python evaluates conditions **from top to bottom**.

As soon as it finds a condition that is `True`, it executes that block and skips the remaining `elif` and `else` blocks.

---

# 5. Nested `if`

A nested `if` is an `if` statement inside another `if` statement.

### Example

```python
file_exists = True
row_count = 500

if file_exists:
    if row_count > 0:
        print("Process file")
```

The second condition is checked only if the first condition is `True`.

### Data Engineering example

```python
file_exists = True
row_count = 0

if file_exists:
    print("File found")

    if row_count > 0:
        print("Process data")
    else:
        print("File is empty")
else:
    print("File not found")
```

Output:

```text
File found
File is empty
```

---

# 6. `for` Loop

A `for` loop is used to iterate over a collection of items.

### Syntax

```python
for item in collection:
    # code
```

### Example

```python
files = ["sales.csv", "customers.csv", "orders.csv"]

for file in files:
    print(file)
```

Output:

```text
sales.csv
customers.csv
orders.csv
```

The loop processes one item at a time.

Conceptually:

```text
file = "sales.csv"
file = "customers.csv"
file = "orders.csv"
```

---

# 7. Loop Variable

In:

```python
for file in files:
    print(file)
```

`file` is the **loop variable**.

It temporarily contains the current item being processed.

The name can technically be anything:

```python
for x in files:
    print(x)
```

However, meaningful names are preferred:

```python
for file in files:
    print(file)
```

This makes the code easier to understand.

---

# 8. `range()`

`range()` generates a sequence of numbers, commonly used with `for` loops.

### `range(stop)`

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

The stop value (`5`) is **not included**.

### `range(start, stop)`

```python
for i in range(1, 4):
    print(i)
```

Output:

```text
1
2
3
```

Again, the stop value (`4`) is not included.

### `range(start, stop, step)`

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```text
2
4
6
8
10
```

Here:

* `2` → starting value
* `11` → stopping point, not included
* `2` → step size

### Common patterns

```python
range(5)
# 0, 1, 2, 3, 4
```

```python
range(1, 5)
# 1, 2, 3, 4
```

```python
range(2, 10, 2)
# 2, 4, 6, 8
```

---

# 9. `for` Loop in Data Engineering

A common Data Engineering pattern is processing multiple files.

```python
files = ["sales.csv", "customers.csv", "orders.csv"]

for file in files:
    print(f"Processing {file}")
```

Output:

```text
Processing sales.csv
Processing customers.csv
Processing orders.csv
```

Another example is processing API pages:

```python
for page in range(1, 6):
    print(f"Fetching API page {page}")
```

Output:

```text
Fetching API page 1
Fetching API page 2
Fetching API page 3
Fetching API page 4
Fetching API page 5
```

---

# 10. `break`

`break` immediately **stops the entire loop**.

### Example

```python
files = ["a.csv", "b.csv", "c.csv", "d.csv"]

for file in files:
    if file == "c.csv":
        break

    print(f"Processing {file}")
```

Output:

```text
Processing a.csv
Processing b.csv
```

When Python reaches:

```python
break
```

the loop terminates.

`c.csv` and `d.csv` are not processed.

### Data Engineering use

`break` can be useful when a **critical condition** occurs and processing should stop.

```python
for file in files:
    if critical_error:
        break
```

---

# 11. `continue`

`continue` skips the **current iteration** and moves to the next iteration.

### Example

```python
files = ["a.csv", "error.csv", "b.csv"]

for file in files:
    if file == "error.csv":
        continue

    print(f"Processing {file}")
```

Output:

```text
Processing a.csv
Processing b.csv
```

The loop does **not** stop.

It simply skips `error.csv`.

### Data Engineering use

`continue` can be useful when a particular record or file should be skipped while allowing the rest of the pipeline to continue.

---

# 12. `break` vs `continue`

| Keyword    | Behavior                                   |
| ---------- | ------------------------------------------ |
| `break`    | Stops the entire loop                      |
| `continue` | Skips the current iteration                |
| `pass`     | Does nothing; execution continues normally |

### Example

```text
break
↓
STOP LOOP
```

```text
continue
↓
SKIP CURRENT ITEM
↓
NEXT ITERATION
```

---

# 13. `while` Loop

A `while` loop repeatedly executes code **as long as its condition is `True`**.

### Syntax

```python
while condition:
    # code
```

### Example

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

Output:

```text
1
2
3
```

The value of `count` changes during each iteration.

Eventually:

```text
count = 4
```

and:

```python
count <= 3
```

becomes `False`.

The loop stops.

---

# 14. Avoiding Infinite Loops

A `while` loop must eventually make its condition `False`.

### Correct

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

### Infinite loop

```python
count = 1

while count <= 3:
    print(count)
```

Here, `count` never changes.

Therefore:

```text
count = 1
count = 1
count = 1
...
```

The condition always remains `True`.

---

# 15. `while` in Data Engineering

A `while` loop can be useful when the number of iterations depends on a condition.

For example:

```python
rows = 1000

while rows > 0:
    print(rows)
    rows -= 250
```

Output:

```text
1000
750
500
250
```

The loop continues until `rows` becomes `0`.

---

# 16. `for` vs `while`

### `for`

Use a `for` loop when you are iterating over a collection or known sequence.

```python
files = ["a.csv", "b.csv", "c.csv"]

for file in files:
    print(file)
```

Think:

> "Process each item."

### `while`

Use a `while` loop when repetition depends primarily on a condition.

```python
while rows > 0:
    process_data()
    rows -= 100
```

Think:

> "Keep doing this while the condition is true."

---

# 17. `pass`

`pass` means **do nothing**.

It is commonly used as a placeholder when code needs a statement but implementation is not ready yet.

### Example

```python
def validate_data(data):
    pass
```

The function is syntactically valid but currently does nothing.

Another example:

```python
if rows == 0:
    pass
else:
    print("Process data")
```

`pass` does not stop the loop and does not skip an iteration.

---

# 18. Control Flow Keywords Summary

| Keyword    | Purpose                                    |
| ---------- | ------------------------------------------ |
| `if`       | Execute code when a condition is true      |
| `elif`     | Check another condition                    |
| `else`     | Execute when previous conditions are false |
| `for`      | Iterate over a collection/sequence         |
| `while`    | Repeat while a condition is true           |
| `break`    | Stop the loop completely                   |
| `continue` | Skip the current iteration                 |
| `pass`     | Do nothing / placeholder                   |
| `range()`  | Generate a sequence of numbers             |

---

# 19. Data Engineering Example

Control flow can be combined to build pipeline logic:

```python
files = ["sales.csv", "temp.csv", "error.csv", "orders.csv"]

for file in files:

    if file == "temp.csv":
        continue

    if file == "error.csv":
        print("Critical error")
        break

    print(f"Processing {file}")
```

Output:

```text
Processing sales.csv
Critical error
```

Execution:

```text
sales.csv
    ↓
process

temp.csv
    ↓
continue → skip

error.csv
    ↓
critical error
    ↓
break → stop loop

orders.csv
    ↓
never reached
```

---

# 20. Key Takeaways

Remember these rules:

```text
if
→ make a decision

elif
→ check another condition

else
→ fallback when conditions are false

for
→ process items in a sequence

while
→ repeat while a condition is true

break
→ stop the loop

continue
→ skip the current iteration

pass
→ do nothing

range()
→ generate a sequence of numbers
```

## Control Flow Checklist

* [x] `if`
* [x] `if / else`
* [x] `if / elif / else`
* [x] Nested conditions
* [x] `for` loops
* [x] `range()`
* [x] `break`
* [x] `continue`
* [x] `while` loops
* [x] `pass`

**Status:** Practiced
