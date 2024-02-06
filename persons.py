import csv


# TO DO: Define Person Class
class Person:
    def __init__(self, id, first_name, middle_name, last_name, birthday, gender, address):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.address = address

    def __str__(self):
        return (f"ID: {self.id}, Fullname: {self.first_name} {self.middle_name} {self.last_name},"
                f" Birthday: {self.birthday}, Gender: {self.gender}, Address: {self.address}")


def load_csv(file_path):
    persons = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row if present
        for row in reader:
            id, first_name, middle_name, last_name, birthday, gender, address = row

            # TO DO: Create an object for each row and append to your list
            person = Person(id, first_name, middle_name, last_name, birthday, gender, address)
            persons.append(person)

    return persons


def search_persons(persons, keyword):
    results = [person for person in persons if keyword.lower() in person.first_name.lower()
               or keyword.lower() in person.middle_name.lower()
               or keyword.lower() in person.last_name.lower()]
    return results


# TO DO: Create the main program
if __name__ == "__main__":

    file_path = r"C:\Users\JAMES\Downloads\persons.csv"
    person_list = load_csv(file_path)

    while True:
        search_keyword = input("\nSearch for a person (type 'exit' to end): ")

        if search_keyword.lower() == 'exit':
            break

        search_results = search_persons(person_list, search_keyword)

        if search_results:
            print("Results:")
            for result in search_results:
                print(result)
        else:
            print("No results.")
