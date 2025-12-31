# Task 2: Demonstrate List Slicing

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
extracted_list = list[ : 5]
reverse_list = extracted_list[ : : -1]

print(f"Original list: {list}\n")

print(f"Extracted first five elements: {extracted_list}\n")

print(f"Reversed extracted elements: {reverse_list}")