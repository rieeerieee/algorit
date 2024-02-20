import csv
import time

def binary_search(csv_data, keyword):
    left = 0
    right = len(csv_data) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if csv_data[mid][0] == keyword:
            return mid, csv_data[mid]
        elif csv_data[mid][0] < keyword:
            left = mid + 1
        else:
            right = mid - 1

    return None, None

file_path = r"C:\Users\JAMES\Downloads\words.csv"


with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    sorted_data = sorted(csv_reader)

print("Values in the CSV file after sorting:")
csv_as_str = ' '.join([' '.join(row) for row in sorted_data])
print(csv_as_str)

keyword = input("\nEnter the keyword to search for: ")

start = time.perf_counter()
index, result = binary_search(sorted_data, keyword)

if result:
    print("\nKeyword found at index", index, ":", ' '.join(result))
else:
    print("\nKeyword not found")
end = time.perf_counter()
print("Binary Search Speed: %.6f seconds" % (end - start))
