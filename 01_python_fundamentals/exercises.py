
# create few variables that potentially be used in DE.
pipeline_name = "customer_etl"
source = "mysql"
destination = "postgresql"
records = 50000
batch_size = 5000
active = True
success_rate = 98.5
last_run = None

print(type(pipeline_name))
print(type(source))
print(type(destination))
print(type(records))
print(type(batch_size))
print(type(active))
print(type(success_rate))
print(type(last_run))

# Type Conversions

record_count = "50000"
success_rate = "98.5"
batch_size = "5000"

record_count = int(record_count)
success_rate = float(success_rate)
batch_size = int(batch_size)
print("After Conversion")
print(type(record_count))
print(type(success_rate))
print(type(batch_size))


#dont just convert values use them
print("Apllication after conversion")
record_count = "50000"
batch_size = "5000"

record_count = int(record_count)
batch_size = int(batch_size)

total_batches = record_count//batch_size
print(total_batches)
print(type(total_batches))

# / → true division → returns a float
# // → floor division → returns an int when both operands are integers

## Operators Exercise
successful_records = 48500
failed_records = 1500

total_processed = successful_records + failed_records
difference = successful_records - failed_records
successful_records_doubled = successful_records * 2
print("operators ex")
print(total_processed)
print(difference)
print(successful_records_doubled)

## Conditional Operators Ex

record_count = 50000
batch_size = 5000
print("conditional OPERATOR EX")
print(record_count > batch_size)
print(record_count == batch_size)
print(record_count != batch_size)
print(record_count <= 5000)

#Logical Operators Ex
print("Logical Operators")
record_count = 50000
batch_size = 5000
pipeline_active = True
print(record_count > 0 and pipeline_active == True)
print(record_count > batch_size or pipeline_active == False)
print(pipeline_active == False)


'''
Instead of pipeline_active == True
We can Write:
    pipeline_active
and instead of pipeline_active == False
We can Write
    not pipeline_active
'''

#Input/Output Ex
pipeline_name = input("Enter Pipeline Name: ")
record_count = int(input("Total No of Records: "))
batch_size = int(input("Enter Batch Size: "))
complete_batches = record_count // batch_size
remaining_records = record_count % batch_size
total_batches = complete_batches + (remaining_records > 0)
print("Pipeline: ",pipeline_name)
print("Records: ",record_count)
print("Batch size: ",batch_size)
print("total batches: ",total_batches)

'''
a Boolean can behave like an integer in Python:

True  → 1
False → 0
'''

# == vs IS
records1 = ["A", "B", "C"]
records2 = ["A", "B", "C"]
records3 = records1
print(records1 == records2)
print(records1 is records2)

print(records1 == records3)
print(records1 is records3)

