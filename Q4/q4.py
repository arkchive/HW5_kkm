import csv

def main():

    a, b, c, d = cal(line = '1호선')
    e, f, g, h = cal(line = '2호선')
    j, k, l, m = cal(line = '3호선')
    n, o, p, q = cal(line = '4호선')

    print("*** Subway Report for Seoul on March 2023 ***")
    print("Line1:")
    print("Busiest Station: {0:s} ({1:d})" .format(a, b))
    print("Least used Station: {0:s} ({1:d})" .format(c, d))
    print("Line2:")
    print("Busiest Station: {0:s} ({1:d})" .format(e, f))
    print("Least used Station: {0:s} ({1:d})" .format(g, h))
    print("Line3:")
    print("Busiest Station: {0:s} ({1:d})" .format(j, k))
    print("Least used Station: {0:s} ({1:d})" .format(l, m))
    print("Line4:")
    print("Busiest Station: {0:s} ({1:d})" .format(n, o))
    print("Least used Station: {0:s} ({1:d})" .format(p, q))

def cal(line):
    f = open('q4.csv', 'r', encoding = 'cp949')
    data = csv.reader(f, delimiter = ',')
    header = next(data)
    dic_line = {}
    for row in data:
        if row[1] in line:
            dic_line[row[3]] = int(row[4]) + int(row[5])
    sort = sorted(dic_line.items(), key=lambda x:x[1])

    return (sort[-1][0], sort[-1][1], sort[0][0], sort[0][1])
        

if __name__ == '__main__':
    main()
