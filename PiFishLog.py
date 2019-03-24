import csv
while True:
    operation = raw_input("\nEnter an operation. F = add fish, L = view log, and E = end.: ")

    if operation == 'F':
        species = raw_input("\nSpecies?: ")
        weight = raw_input("Weight?: ")
        length = raw_input("Length?: ")
        temp = raw_input("Air temp?: ")
        baro = raw_input("Barometric pressure?: ")
        humid = raw_input("Humidity?: ")
        appendMe = str('\n'+species+','+weight+','+length+','+temp+','+baro+','+humid)
        appendFile = open('log.csv', 'a')
        appendFile.write(appendMe)
        appendFile.close()


    elif operation == 'L':
        with open('log.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)

    elif operation == 'E':
        break

    else:
        print ('\nInvalid operation')
