import csv

def csv_repl(file_path):
    with open (file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        print(*header, sep=' | ')

        for row in csv_reader:
            print(*row, sep=' | ')

csv_repl('movies.csv')