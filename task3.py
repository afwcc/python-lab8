





def generateDictionary():
    dict_temp = {}
    with open('font3.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip()
            k = line.split(' ')[1]
            v = line.split(' ')[0]
            dict_temp[k] = v
    print(dict_temp)
