# Read the name from the user
first = input("Enter your first name: ")
# Compute its length
num_chars = len(first)
# Display the result
print("Your first name contains", num_chars, "characters")

# Read the user’s name
first = input("Enter your first name: ")
middle = input("Enter your middle name: ")
last = input("Enter your last name: ")
# Extract the first character from each string and concatenate them
initials = first[len(first)-1] + middle[len(middle)-1] + last[len(last)-1]
# Display the initials
print("Your initials are", initials)