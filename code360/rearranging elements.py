# Create a list
data = [2.71, 3.14, 1.41, 1.62]
# Swap the element at index 1 with the element at index 3
temp = data[1]
data[1] = data[3]
data[3] = temp
# Display the modified list
print(data)

# Create a new, empty list
values = []
# Read values from the user and store them in a list until a blank line is entered
line = input("Enter a number (blank line to quit): ")
while line != "":
 num = float(line)
values.append(num)
line = input("Enter a number (blank line to quit): ")
# Sort the values into ascending order
values.sort()
# Display the values
for v in values:
 print(v)