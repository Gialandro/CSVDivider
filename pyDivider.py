import csv
import math
import os
import time

asciimoji = ('ᕦ( ͡° ͜ʖ ͡°)ᕤ', '╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ', '(╯°□°)╯︵ ┻━┻', 'ヽ(｀Д´)ﾉ')
os.system('cls||clear')
print('PyDivider Alpha0.1')
while True:
    try:
        csvLocation = str(input('Enter the name of CSV to open like "file.csv": '))
        rowsPerFile = int(input('Enter number of rows per file: '))
        csvToDivide = open(csvLocation, newline = '', encoding='utf-8')
        break
    except IOError:
        print('File not found, try again. {0}'.format(asciimoji[2]))
    except ValueError:
        print('Invalid number of rows, try again. {0}'.format(asciimoji[3]))

nameCSV = csvLocation.split('.')[0]
readHeader = csv.reader(csvToDivide)
bodyLst = list() #List of elements
head = list() #List of header

for row in readHeader:
    if readHeader.line_num == 1:
        head.append(row)
    else:
        bodyLst.append(row)

header = head[0]
files = 0
numFiles = math.ceil(int(len(bodyLst)) / rowsPerFile) #Number of files to create

for element in range(0, numFiles):
    os.system('cls||clear')
    print('{} File...'.format(asciimoji[0]))
    time.sleep(0.7)
    nameF = (nameCSV + 'Child {0}' + '.csv').format(element) #Automatic name
    with open(nameF, 'w') as fileCSV:
        fileWriter = csv.writer(fileCSV, quoting = csv.QUOTE_ALL, lineterminator='\n')
        fileWriter.writerow(header)
        for row in range(0, rowsPerFile):
            if len(bodyLst) > 0:
                fileWriter.writerow(bodyLst.pop())
    os.system('cls||clear')
    print('{} Created!'.format(asciimoji[1]))
    files +=1
    time.sleep(0.9)

os.system('cls||clear')
print('Done. {0} files created ＼(＾O＾)／'.format(files))
csvToDivide.close()
