num_string = '88'
num_float = 43.7
print("Data type of num_string before Type Casting:", type(num_string))
num_string = int(num_string)
print("Data type of num_string after Type Casting:", type(num_string))
num_sum = num_float + num_string
print("Sum:", num_sum)
print("Data type of num_sum:", type(num_sum))
num_sum = complex(num_sum)
print("Data type of num_sum after Type Casting:", type(num_sum))
print("Complex num_sum:", num_sum)