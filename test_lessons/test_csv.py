import csv, os

current_path = os.path.join('../resources/new_csv.csv')


def test_csv_1():
    with open(current_path, 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        assert csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        assert csvwriter.writerow(['Alex', 'Serj', 'Yana'])


def test_csv_2():
    with open(current_path, newline='') as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')
        for row in csvreader:
            print(row)
        assert row == ['Alex', 'Serj', 'Yana']
