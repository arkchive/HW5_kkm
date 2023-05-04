import csv

def main():
    f = open('q3.csv', 'r', encoding = 'cp949')
    data = csv.reader(f, delimiter = ',')
    header = next(data)
    dic_line = {'1호선':0, '2호선':0, '3호선':0, '4호선':0, '5호선':0, '6호선':0, '7호선':0, '8호선':0, '9호선':0}

    for row in data:
        if row[1] in list(dic_line.keys()):
            dic_line[row[1]] = dic_line[row[1]] + int(row[4]) + int(row[5])

    sort = sorted(dic_line.items(), key=lambda x:x[1])

    print("*** Subway Report for Seoul on March 2023 ***")
    print("1st Busiest Line: {0:s} ({1:d})" .format(sort[-1][0], sort[-1][1]))
    print("2nd Busiest Line: {0:s} ({1:d})" .format(sort[-2][0], sort[-2][1]))
    print("1st Least used Line: {0:s} ({1:d})" .format(sort[0][0], sort[0][1]))
    print("2nd Least used Line: {0:s} ({1:d})" .format(sort[1][0], sort[1][1]))


if __name__ == '__main__':
    main()
