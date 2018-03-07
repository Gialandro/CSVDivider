import csv
import math

print('PyDivider v0.1')
while True:
    try:
        csvLocation = str(input('Ingresa el nombre del archivo CSV a abrir como "nombre.csv": '))
        rowsPerFile = int(input('Ingresa el numero de filas por archivo: '))
        csvToDivide = open(csvLocation, newline = '', encoding='utf-8')
        break
    except IOError:
        print('Archivo no encontrado, intenta de nuevo.')
    except ValueError:
        print('Numero de filas invalido, intenta de nuevo.')
nameCSV = 'Archivo'
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

for element in range(0, numFiles):
    nameF = (nameCSV + ' {0}' + '.csv').format(element) #Nombre automatico
    with open(nameF, 'w') as fileCSV:
        fileWriter = csv.writer(fileCSV, lineterminator='\n')
        fileWriter.writerow(header)
        for row in range(0, rowsPerFile):
            if len(bodyLst) > 0:
                fileWriter.writerow(bodyLst.pop())
csvToDivide.close()
