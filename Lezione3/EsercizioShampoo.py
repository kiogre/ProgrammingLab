def sum_csv(file_name):
    tot = 0;
    file = open(file_name, 'r')
    for line in file:
        elements = line.split(',')
        if elements[0] != 'Date':
            tot = tot + float(elements[0])
    return tot