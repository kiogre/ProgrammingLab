my_dict={'Trieste': 34100, 'Padova': 35100}
my_dict2={'Trieste': 'TS', 'Padova': 'PD'}
print('Cap di Trieste: {}'.format(my_dict['Trieste']))

def mia_funzione (argomento1, argomento2):
    print("Argomenti: {} e {}".format(argomento1, argomento2))

def eleva_al_quadrato (numero):
    return numero * numero

my_var=10
your_var=1
if (my_var > your_var):
    print("My var is bigger than yours")
    if (my_var - your_var) <= 1:
        print("... but not so much")
    if (my_var - your_var) <= 5:
        print("... quite a bit")
    else:
        print("... a lot")


for i in range(10):
    print(i)

#Stessa cosa

i=0
while i < 10:
    print(i)
    i = i + 1

mylist={"Hello": "World"}
for i, item in enumerate(mylist):
    print("Posizione {}: {}".format(i, item))

#from math import sqrt
#sqrt(numero)

#oppure

#import math
#math.sqrt(numerod)