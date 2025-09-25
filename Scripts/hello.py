print("Hello, World!")

# Ask user to enter numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Convert input string to a list of integers
numbers = [int(num) for num in user_input.split()]

print ("You entered:", numbers)

# Sort the numbers
sorted_numbers = sorted(numbers)

print("Sorted numbers:", sorted_numbers)