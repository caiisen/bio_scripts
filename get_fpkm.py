with open('test.txt', 'r') as input_file:
    for line in input_file:
        id = line.split(';')[1].split('"')[1]
        fpkm = line.split(';')[-2].split('"')[1]
        print(id + '\t' + fpkm)