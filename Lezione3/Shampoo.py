def sum_csv(file_name):
    tot = 0;
    file = open(file_name, 'r')
    for a in file:
        elements = a.split(',')
        if elements[0] != 'Date' or elements[1] == None:
            tot = tot + float(elements[1])
    return tot