import csv


def program():
    nameofcsvfile = input("Hello please enter the name of the csv-file")
    with open(nameofcsvfile,"r", encoding = "utf-8") as readcsvfile:
        csv_reader = csv.reader(readcsvfile)
        for line in csv_reader:
            print(line)

program()