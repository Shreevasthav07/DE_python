pipeline_name = "sales_pipeline"
source_file = "sales.csv"
record_count = 10000
batch_size = 1000
pipeline_active = True

print(pipeline_name)
print(source_file)
print(record_count)
print(batch_size)
print(pipeline_active)

#use type() function to find type of each variable

print(type(pipeline_name)) #str
print(type(source_file)) #str
print(type(record_count)) #int
print(type(batch_size)) #int
print(type(pipeline_active)) #bool

# Operators
record_count = 52750
batch_size = 5000
print("Operator Example Use")
complete_batches = record_count // batch_size
remaining_records = record_count % batch_size
print(complete_batches)
print(remaining_records)

# +, -, * Operators

successful_records = 48500
failed_records = 1500
record_count = 50000

# total_records = successful_records + failed_records
# success_records = record_count - failed_records
# records_processed = batch_size * total_batches

#Comparision Operators
print("Comparision Op Ex")
successful_records = 48500
total_records = 50000
success_rate = successful_records/total_records * 100
print(success_rate)
print(success_rate >= 95)

#isinstance()

print("Isinstance usage")
record_count = 50000
pipeline_name = "customer_etl"
pipeline_active = True

print(type(record_count))
print(type(pipeline_name))
print(type(pipeline_active))

print(isinstance(record_count, int))
print(isinstance(pipeline_name, str))
print(isinstance(pipeline_active, bool))