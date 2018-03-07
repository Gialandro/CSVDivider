import csv
import math

print('PyDivider v0.1')
while True:
    try:
        csvLocation = str(input('Enter the name of CSV to open like "file.csv"a: '))
        rowsPerFile = int(input('Enter number of rows per file: '))
        csvToDivide = open(csvLocation, newline = '', encoding='utf-8')
        break
    except IOError:
        print('File not found, try again.')
    except ValueError:
        print('Invalid number of rows, try again.')
nameCSV = 'File'
readHeader = csv.reader(csvToDivide)
bodyLst = list() #List of elements
head = list() #List of header
for row in readHeader:
    if readHeader.line_num == 1:
        head.append(row)
    else:
        bodyLst.append(row)
header = head[0]
numFiles = math.ceil(int(len(bodyLst)) / rowsPerFile) #Number of files to create

for element in range(0, numFiles):
    nameF = (nameCSV + ' {0}' + '.csv').format(element) #Automatic name
    with open(nameF, 'w') as fileCSV:
        fileWriter = csv.writer(fileCSV, lineterminator='\n')
        fileWriter.writerow(header)
        for row in range(0, rowsPerFile):
            if len(bodyLst) > 0:
                fileWriter.writerow(bodyLst.pop())
csvToDivide.close()
