import csv
import time

def linear_search(csv_reader, keyword):
    for index, row in enumerate(csv_reader):
        if keyword in row:
            return index, row
    return None, None


file_path = r"C:\Users\JAMES\Downloads\words.csv"


with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    print("Values in the CSV file:")
    for row in csv_reader:
        print(row)


with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    keyword = input("\nEnter the keyword to search for: ")

    start = time.perf_counter()
    index, result = linear_search(csv_reader, keyword)

    if result:
        print("Keyword found at index", index, ":", result)
    else:
        print("Keyword not found")
    end = time.perf_counter()
    print("Linear Search Speed: %.6f seconds" % (end - start))
