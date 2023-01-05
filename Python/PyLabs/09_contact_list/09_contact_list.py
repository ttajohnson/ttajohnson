# LAB 10: CONTACT LIST
# Open the CSV, convert the lines of text into a list of dictionaries,
# one dictionary for each user.

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 1

# >>>
# def csv_reader(file, mode):
#     with open(file, mode) as file:
#         lines = file.read().split("\n")
#     header = True
#     contents = []
#     for line in lines:
#         if header:
#             keys = "".join(line).split(",")
#             header = False
#         else:
#             values = "".join(line).split(",")
#             contents.append({keys[i]: values[i] for i in range(len(keys))})


# >>>

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 2
# Implement a CRUD REPL.

# >>>
class CSV_REPL:
    def __init__(self):
        self.name = input("CSV Filename: ")
        self.mode = input("Mode: ")
        self.contents = []
        self.keys = []
        self.values = []
        with open(self.name, self.mode) as file:
            lines = file.read().split("\n")
        header = True
        for line in lines:
            if header:
                self.keys = "".join(line).split(",")
                header = False
            else:
                self.values = "".join(line).split(",")
                self.contents.append(
                    {self.keys[i]: self.values[i] for i in range(len(self.keys))}
                )

    def display_contacts(self):
        listed = self.contents
        print(*listed, sep="\n")

    def create_contact(self):
        nc_name = input("Name: ")
        nc_fruit = input("Favorite Fruit: ")
        nc_color = input("Favorite Color: ")
        self.values.extend((nc_name, nc_fruit, nc_color))
        print(self.values)
        self.contents.append(
            {self.keys[i]: self.values[i] for i in range(len(self.keys))}
        )
        print(self.contents)


def main():
    open = CSV_REPL()
    while True:
        choice = input(
            "1. Display Contacts\n2. Create New Contact\n3. View Contact by Name\n4. Update Contact by Name\n5. Delete Contact by Name\n6. Exit\n"
        )
        if choice == "1":
            open.display_contacts()
        elif choice == "2":
            open.create_contact()


main()
