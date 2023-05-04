import csv

def main():
    a, b = large()
    c, d = small()
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Day with the Largest Temperature Variation: {0:s}".format(a))
    print("Maximum Temperature Difference: {0:.1f} Celsius".format(b))
    print("Day with the Smallest Temperature Variation: {0:s}".format(c))
    print("Minimum Temperature Difference: {0:.1f} Celsius".format(d))

def large():
    f = open('q2.csv', 'r', encoding = 'cp949')
    data = csv.reader(f, delimiter = ',')
    header = next(data)
    variation = 10
    max_date = ''
    max_temp = 0
    
    for row in data:
        if row[-1] == '' or row[-2] == '':
            continue
        if variation < float(row[-1])-float(row[-2]):
            variation = float(row[-1])-float(row[-2])
            max_date = row[0]
            max_temp = variation
    return(max_date, max_temp)

def small():
    f = open('q2.csv', 'r', encoding = 'cp949')
    data = csv.reader(f, delimiter = ',')
    header = next(data)
    variation = 10
    min_date = ''
    min_temp = 0
    
    for row in data:
        if row[-1] == '' or row[-2] == '':
            continue
        if variation > float(row[-1])-float(row[-2]):
            variation = float(row[-1])-float(row[-2])
            min_date = row[0]
            min_temp = variation
    return(min_date, min_temp)

if __name__ == '__main__':
    main()
