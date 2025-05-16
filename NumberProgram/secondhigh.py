numbers = [10, 20, 4, 45, 99, 99, 67]

# Remove duplicates to handle repeated highest values
unique_numbers = list(set(numbers))
# Sort in descending order
unique_numbers.sort(reverse=True)

# Second highest is at index 1
if len(unique_numbers) >= 2:
    print("Second highest number is:", unique_numbers[1])
else:
    print("List doesn't have enough unique elements.")
