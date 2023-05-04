import csv

def main():
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Average Temperature: {0:.2f} Celsius".format(avg_temp()))
    print("Average Minimum Temperature: {0:.2f} Celsius".format(avg_min()))
    print("Average Maximum Temperature: {0:.2f} Celsius".format(avg_max()))

def avg_temp():
    f= open('q1.csv', 'r', encoding = 'cp949')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    result = 0
    count = 0
    for row in data:
        if row[0] == '' or row[1] == '' or row[2] == '' or row[3] == '' or row[4] == '' :
            continue
        result += float(row[2])
        count += 1
    f.close()
    return result / count

def avg_max():
    f= open('q1.csv', 'r', encoding = 'cp949')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    result = 0
    count = 0
    for row in data:
        if row[0] == '' or row[1] == '' or row[2] == '' or row[3] == '' or row[4] == '' :
            continue
        result += float(row[-1])
        count += 1
    f.close()
    return result / count

def avg_min():
    f= open('q1.csv', 'r', encoding = 'cp949')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    result = 0
    count = 0
    for row in data:
        if row[0] == '' or row[1] == '' or row[2] == '' or row[3] == '' or row[4] == '' :
            continue
        result += float(row[-2])
        count += 1
    f.close()
    return result / count
    
    
if __name__ == '__main__':
    main()
