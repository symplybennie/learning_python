#1
# Initialize data and total
x = [2.71, 3.14, 1.41, 1.62]
total = 0
# Total the values in data
for value in x:
    total = total + value
# Display the total
print("The total is", total)
 
 #2
# Initialize data and largest pos
data = [1.62, 1.41, 3.14, 2.71]
largest_pos = 0
# Find the position of the largest element
for i in range(1, len(data)):
  if data[i] > data[largest_pos]:
    largest_pos = i
# Display the result
print("The largest value is", data[largest_pos], \
"which is at index", largest_pos)

#3
# Initialize data
data = [0, -1, 4, 1, 0]
# Loop while i is a valid index and the value at index i is not a positive value
i=0
while i < len(data) and data[i] <= 0:
  i=i+1
# If i is less than the length of data then the loop terminated because a positive number was
# found. Otherwise i will be equal to the length of data, indicating that a positive number
# was not found.
if i < len(data):
   print("The first positive number is at index", i)
else:
   print("The list does not contain a positive number")

data = [2.71, 3.14, 1.41, 1.62]
data.append(2.30)
print(data)

data.insert(2, 2.30)
print(data)

data = [2.71, 3.14, 1.41, 1.62]
data.remove(1.62) # Remove 1.62 from the list
last = data.pop() # Remove the last element from the list
print(data)
print(last)