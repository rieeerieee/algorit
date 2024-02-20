import csv
import time

def linear_search(csv_reader, keyword):
    for index, row in enumerate(csv_reader):
        if keyword in row:
            return index, row
    return None, None

file_path = r"C:\Users\JAMES\Downloads\words.csv"

# Read and concatenate CSV data into a single string
csv_data_str = ""
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        csv_data_str += ' '.join(row) + ' '

print("Values in the CSV file after sorting:", csv_data_str)

# Perform linear search
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    keyword = input("\nEnter the keyword to search for: ")
    start = time.perf_counter()
    index, result = linear_search(csv_reader, keyword)
    end = time.perf_counter()

# Print search result
if result:
    print("\nKeyword found at index", index, ":", ' '.join(result))
else:
    print("\nKeyword not found")

# Print timing
print("Linear Search Speed: %.6f seconds" % (end - start))
