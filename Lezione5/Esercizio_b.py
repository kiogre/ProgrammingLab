class CSVFile():
    def __init__(self, name):
        self.name = name
        self.lista = []
    def get_data(self):
        try:
            file = open(self.name, 'r')
        except Exception as e:
            print("Errore:{}".format(e))
        for line in file:
            elements = line.split(',')
            lista.append(elements)

class NumericalCSVFile(CSVFile):
    def get_data_original(self):
        super().get_data()
        for elemento in self.lista:
            tmp = True
            for Dentro in elemento:
                if tmp:
                    try:
                        