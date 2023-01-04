# LAB 10: CONTACT LIST
# Open the CSV, convert the lines of text into a list of dictionaries,
# one dictionary for each user.

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 1

# >>>
def csv_reader(file, mode):
    with open(file, mode) as file:
        lines = file.read().split("\n")
    header = True
    contents = []
    for line in lines:
        if header:
            keys = "".join(line).split(",")
            header = False
        else:
            values = "".join(line).split(",")
            contents.append({keys[i]: values[i] for i in range(len(keys))})
    print(contents)


csv_reader("contacts.csv", "r")
# >>>

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 2
# Implement a CRUD REPL.

# >>>
def main():
    pass
