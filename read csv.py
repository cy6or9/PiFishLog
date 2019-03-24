import csv
with open('testLog.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)

#leave anything above this alone

    speciesL = []
    weightL = []
    lengthL = []
    tempL = []
    baroL = []
    humidL = []
    for row in readCSV:
        species = row[0]
        weight = row[1]
        length = row[2]
        temp = row[3]
        baro = row[4]
        humid = row[5]

        speciesL.append(species)
        weightL.append(weight)
        lengthL.append(length)
        tempL.append(temp)
        baroL.append(baro)
        humidL.append(humid)

    print(speciesL)
    print(weightL)
    print(lengthL)
    print(tempL)
    print(baroL)
    print(humidL)
