class CSVFile():
    def __init__(self, name):
        self.name = name
    def get_data(self):
        file = open(self.name, 'r')
        lista = []
        for line in file:
            elements = line.split(',')
            if elements[0] != 'Date':
                prova = [elements[0], elements[1]]
                lista.append(prova)