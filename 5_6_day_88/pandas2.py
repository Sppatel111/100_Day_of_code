
# Given string and list
string = "PYTHONISPGML"
list1 = [6, 2, 4]

# Convert the string to lowercase
lower_string = string.lower()

# Create a new string with spaces
result = ""
last_index = 0

for index in list1:
    result += lower_string[last_index:last_index+index] + " "
    last_index = last_index+index

# Add the remaining part of the string
result += lower_string[last_index:]

# Print the result
print(result.strip())