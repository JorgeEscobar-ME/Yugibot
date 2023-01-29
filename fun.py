import xlrd
import random
sobre1='sobre1.xlsx'
abrirsobre1=xlrd.open_workbook(sobre1)
hojasobre1=abrirsobre1.sheet_by_index(0)

prompack1='prompack1.xlsx'
abrirprompack1=xlrd.open_workbook(prompack1)
hojaprompack1=abrirprompack1.sheet_by_index(0)
i=0
lists1=[]

while i<3:
    a5=random.randint(1,100)
    if a5<=85:
        o=random.randint(6,20)
    else:
        o=random.randint(0,5)
    i+=1
    lists1.append(hojaprompack1.cell_value(o,0))

print(lists1)