import csv
import math

print('PyDivider Alpha0.1')
while True:
    try:
        csvLocation = str(input('Enter the name of CSV to open like "file.csv": '))
        rowsPerFile = int(input('Enter number of rows per file: '))
        csvToDivide = open(csvLocation, newline = '', encoding='utf-8')
        break
    except IOError:
        print('File not found, try again. (╯°□°)╯︵ ┻━┻')
    except ValueError:
        print('Invalid number of rows, try again. ヽ(｀Д´)ﾉ')
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
# if (header[0] == 'Id' or header[0] == 'ID'):
#     header[0] = '"{0}"'.format(header[0])
numFiles = math.ceil(int(len(bodyLst)) / rowsPerFile) #Number of files to create
print('Working... ヽ(｀Д´)⊃━☆ﾟ. * ･ ｡ﾟ,')
for element in range(0, numFiles):
    nameF = (nameCSV + 'Child {0}' + '.csv').format(element) #Automatic name
    with open(nameF, 'w') as fileCSV:
        fileWriter = csv.writer(fileCSV, quoting = csv.QUOTE_ALL, lineterminator='\n')
        fileWriter.writerow(header)
        for row in range(0, rowsPerFile):
            if len(bodyLst) > 0:
                fileWriter.writerow(bodyLst.pop())
print('Done. ＼(＾O＾)／')
csvToDivide.close()
