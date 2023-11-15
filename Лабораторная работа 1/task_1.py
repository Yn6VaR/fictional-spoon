numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
missing_index = 4
numbers[missing_index] = 0
unique_numbers = set(numbers)
sum_of_numbers = sum(set(numbers))
count_of_numbers = len(numbers)

average_of_numbers = sum(set(numbers)) / len(numbers)

numbers[missing_index] = average_of_numbers

print("Измененный список:", numbers)
