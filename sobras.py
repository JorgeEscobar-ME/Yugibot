import random
import xlrd
excel='prueba.xlsx'
wb = xlrd.open_workbook(excel) 
sheet = wb.sheet_by_index(0)
#las posiciones inician en 0,0.
print(sheet.cell_value(0, 0)) 


#Número aleatorio entre 0 y 1
print(random.random())
#número aleatorio entre [950,1000).
print(random.randint(950, 1000))
lista=[]
for i in range(10):
    lista.append(random.randint(50,70))
print(lista)
a=lista[4]
print(a)

#Definir función:
def sumar(a,b):
    return a/b

b=15
y=sumar(a,b)
print(y)