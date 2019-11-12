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











        

