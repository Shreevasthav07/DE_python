# Variables
A variable is a name that refers to a value/object in Python.
For example:

```
name = "Shree"
age = 21
salary = 45000.50
is_employed = False
```
Python doesn't require you to explicitly declare the data type:
```
age = 21
```
You don't write:
```
int age = 21
```

That's different from languages such as Java or C.

## Variable naming
Python variable names can contain:
- letters
- numbers
- _

But they cannot start with a number.

For Python, the standard readable style is snake_case.

Variables can be reassigned.

```
record_count = 100

record_count = 200

print(record_count)

output:

200
```

You can even assign a different type. 
```
data = 100
data = "sales.csv"
```
Python allows this because it is dynamically typed.

- use type() function to find type of each variable.

## Data Types

- str | String
- int | Integer
- float | Floating-point number
- bool | Boolean - True / False
- None | No value - NoneType

String

```
pipeline_name = "sales_pipeline"
source_file = "sales.csv"
```

Integer
```
record_count = 10000
batch_size = 1000
```
Float
```
success_rate = 98.5
processing_time = 12.75
```
Boolean
```
pipeline_active = True
pipeline_failed = False
```
Notice that True and False do not have quotation marks.
```
True       # bool
"True"     # str
```
These are different.

None - Used when there is currently no value:
```
last_run = None
```
It's Type is:
```
type(last_run)

output
<class 'NoneType'>
```
## Type Conversion

Now let's say your pipeline receives this from an API:
```
records = "50000"
```
Python sees it as str

but you want to perform a calculation:
```
records + 1000
```
That won't work as you might expect because you're trying to combine a string and an integer.

You can convert it:
```
records = int("50000")

print(records)
print(type(records))
```
Output:
```
50000
<class 'int'>
```

Other common conversions:
```
int("100")
float("98.5")
str(50000)
bool(1)
```

## Explicit vs Implicit Conversion

You tell python to convert - Explicit
```
record_count = int("50000")
```
Python can sometimes automatically convert a value when the operator is safe.
```
records = 50000
processing_factor = 1.5
result = records * processing_factor
print(result)
print(type(result))

Output:
75000.0
<class 'float'>
```
The int value participates in an operation with a float, and the result becomes a float.

/ → true division → returns a float

// → floor division → returns an int when both operands are integers

## Operators

Arithmetic
- \+
- \-
- \*
- /
- //
- %
- **

Comparison
- ==
- !=
- \>
- <
- \>=
- <=

Logical
- and
- or
- not

| Operator | Meaning        |  Example |     Result |
| -------- | -------------- | -------: | ---------: |
| `+`      | Addition       |  `a + b` |       `13` |
| `-`      | Subtraction    |  `a - b` |        `7` |
| `*`      | Multiplication |  `a * b` |       `30` |
| `/`      | Division       |  `a / b` | `3.333...` |
| `//`     | Floor division | `a // b` |        `3` |
| `%`      | Remainder      |  `a % b` |        `1` |
| `**`     | Power          | `a ** b` |     `1000` |

Comparision Operators are:
| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | equal to                 |
| `!=`     | not equal to             |
| `>`      | greater than             |
| `<`      | less than                |
| `>=`     | greater than or equal to |
| `<=`     | less than or equal to    |


They produce a Boolean

Logical Operators are:
- and
- or
- not

Ex:
```
record_count = 50000
pipeline_active = True

ask - 
record_count > 0 and pipeline_active == True
```
means - Are there records and is the pipeline active

1 And

and - requires both conditions to be True

or - requires atleast one condition to be True

not - reverses a Boolean value

## Input/Output

There are Two Functions
- print()
- input()

print()

Ex:
```
pipeline_name = "customer_etl"
record_count = 50000

print("Pipeline:", pipeline_name)
print("Records processed:", record_count)
```

input()

input() allows the user to enter something
```
name = input("Enter your name:")
print("Hello", name)
```
**input() always returns a str**

type conversion becomes useful.
```
record_count = int(input("Enter record count: "))
```

**a Boolean can behave like an integer in Python:**

**True  → 1 False → 0**

## None

None represents the absence of a value

Ex: `last_run = None`

It is different from `last_run = 0` and `last_run = ""` and `last_run = False`

None has its own type `<class 'NoneType'>`

## Mutable vs Immutable

**Mutable** --> an object can be changed after it is created.

**Immutable** --> an object cannot be changed after it is created.

**Immutable Objects**

Immutable Types include:
- int
- float
- str
- bool
- tuple
- None
```
record_count = 50000
```
You cant change the existing integer object from 50000 to 60000

When you do:
```
record_count = 60000
```
Python creates/refers to a different integer value.

Similarly, Strings are immutable:
```
pipeline_name = "customer_etl"
# cant modify one character of that string
# this wont work
pipeline_name[0] = 'X'
# will get a TypeError.
# instead we create a new string:
pipeline_name = 'X' + pipeline_name[1:]
```
## Mutable Objects

- list
- dict
- set

```
records = ['customer_1', 'customer_2']
# can be modified
records.append("customer_3")
# will become
# ["customer_1", "customer_2", "customer_3"]
```
**The List itself was Changed**

**Note - Variable is simply a name referring to an Object, that object can be mutable or immutable**

## type() vs isinstance()

`type()` tells you the exact type of an object.

```
record_count = 50000

print(type(record_count) == int)
```
Output: True

```
isinstance(record_count, int)
```
- Is this Object an instance of int?
- useful when you are validating input

type() - What is the object's type?

isinstance() - Is this object an instance of this type? / always checks the type and returns a boolean value

## == vs is

`==` - compare values

Do these two objects have the same value

```
a = 100
b = 100

print(a == b)
```
Result: True

`is` - compares identity

Are these two variables referring to the exact same object
```
a = None
b = None
print(a is b)
```
Output: `True`

Both refers to the same `None` object

**Key Difference**
```
==  → same VALUE?
is  → same OBJECT?
```
Ex:
```
list1 = ["A", "B", "C"]
list2 = ["A", "B", "C"]

print(list1 == list2)
# True - their values/content are the same

print(list1 is list2)
# False - they are two seperate list objects
```
```
list1 = ["A","B","C"]
list2 = list1
print(list1 == list2)
print(list1 is list2)
# Both are True - Both names point to the same list
# And because they're the same mutable object:
list2.append("D")

print(list1)
# we get
["A", "B", "C", "D"]
```
Even though you modified list2, list1 also changed because they're pointing to the same object.

**Note - Since None means "this is the actual absence-of-value object", use is None for validation/checking.**
```
if record is None:
    print("No record found")
if record is not None:
    print("Record exists")
```
Dont use == , use is instead.






