#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class
# Prompt the user to enter 5 numbers
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Display the list as entered
print("\nList as entered:", numbers)

# Sort the list from small to large and display
sorted_small_to_large = sorted(numbers)
print("Sorted from small to large:", sorted_small_to_large)

# Sort the list from large to small and display
sorted_large_to_small = sorted(numbers, reverse=True)
print("Sorted from large to small:", sorted_large_to_small)

# Calculate and display the mean
mean = sum(numbers) / len(numbers)
print("Mean:", mean)

# Calculate and display the median
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
if n % 2 == 1:
    median = sorted_numbers[n // 2]
else:
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
print("Median:", median)

