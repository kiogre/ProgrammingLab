class CSVFile():
    def __init__(self, name):
        self.name = name
    def get_data(self):
        try:
            file = open(self.name, 'r')
        except Exception as e:
            print("Errore:{}".format(e))
        lista = []
        for line in file:
            elements = line.split(',')
            lista.append(elements)