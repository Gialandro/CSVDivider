import csv
import math
import os
import time

asciimoji = ('ᕦ( ͡° ͜ʖ ͡°)ᕤ', '╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ', '(╯°□°)╯︵ ┻━┻', 'ヽ(｀Д´)ﾉ')
os.system('cls||clear')
print('PyDivider Alpha0.2')
while True:
    try:
        csvLocation = str(input('Ingresa el nombre del archivo CSV a abrir como "nombre.csv": '))
        rowsPerFile = int(input('Ingresa el numero de filas por archivo: '))
        csvToDivide = open(csvLocation, newline = '', encoding='utf-8')
        break
    except IOError:
        os.system('cls||clear')
        print('Archivo no encontrado, intenta de nuevo. {0}'.format(asciimoji[2]))
    except ValueError:
        os.system('cls||clear')
        print('Numero de filas invalido, intenta de nuevo. {0}'.format(asciimoji[3]))

nameCSV = csvLocation.split('.')[0]
readHeader = csv.reader(csvToDivide)
bodyLst = list() #Lista de elementos
head = list() #Lista del encabezado

for row in readHeader:
    if readHeader.line_num == 1:
        head.append(row)
    else:
        bodyLst.append(row)
header = head[0]
numFiles = math.ceil(int(len(bodyLst)) / rowsPerFile) #Numero de archivos a crear
files = 0
os.system('cls||clear')
print('{0} Archivos...'.format(asciimoji[0]))
time.sleep(0.7)

for element in range(0, numFiles):
    nameF = (nameCSV + 'Hijo {0}' + '.csv').format(element) #Nombre automatico
    with open(nameF, 'w') as fileCSV:
        fileWriter = csv.writer(fileCSV, quoting = csv.QUOTE_ALL, lineterminator='\n')
        fileWriter.writerow(header)
        for row in range(0, rowsPerFile):
            if len(bodyLst) > 0:
                fileWriter.writerow(bodyLst.pop())
    files +=1

os.system('cls||clear')
print('{0} Creados!'.format(asciimoji[1]))
time.sleep(1)
os.system('cls||clear')
print('Hecho. {0} archivos creados ＼(＾O＾)／'.format(files))
csvToDivide.close()
