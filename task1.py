import csv


with open("boyName.csv","w", encoding = "utf-8") as csvfile:
    fieldnames = ['First Name', 'Count']
    csv_writer = csv.DictWriter(csvfile,fieldnames=fieldnames,delimiter = ",")
    csv_writer.writeheader()
    with open ("2000_BoysNames.txt", encoding = "utf-8") as boynamefile:
        for line in boynamefile:
            a = line.split()
            csv_writer.writerow({'First Name': a[0],'Count':a[1]})



with open("girlName.csv","w",encoding = "utf-8") as csvfile:
    fieldnames = ['First Name', 'Count']
    csv_writer = csv.DictWriter(csvfile,fieldnames=fieldnames,delimiter = ",")
    csv_writer.writeheader()
    with open ("2000_GirlsNames.txt", encoding = "utf-8") as girlnamefile:
        for line in girlnamefile:
            a = line.split()
            csv_writer.writerow({'First Name': a[0],'Count':a[1]})



def program():
    nameofcsvfile = input("Hello please enter the name of the csv-file")
    with open(nameofcsvfile,"r", encoding = "utf-8") as readcsvfile:
        csv_reader = csv.reader(readcsvfile)
        for line in csv_reader:
            print(line)




def generateDictionary():
    dict_temp = {}

    with open('font3.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip()
            k = line.split(' ')[1]
            v = line.split(' ')[0]
            dict_temp[k] = v
    print(dict_temp)




program()

generateDictionary()














        

