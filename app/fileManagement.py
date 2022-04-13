import os
import csv
import time
from pathlib import Path


date = time.strftime("%Y%m%d-%H%M%S")
fileName = 'import-me-to-cardsphere.' + str(date) + '.csv'
folder = 'import-to-cardsphere'

def getParentDirectory():
    return Path(os.path.dirname(os.getcwd()))

def getFiles():
    return getParentDirectory().glob('*.csv')    

def cleanFile(file):
    filteredFile = []
    for line in file:
        filteredFile.append(line.replace('\x00', ''))
    return parseCsv(filteredFile)

def parseCsv(filteredData):
    return csv.reader(filteredData, delimiter = ',', quotechar = '"')

def createCardSphereCsv(data):
    try:
        os.mkdir(folder)
    except:
        pass
    with open(os.path.join(getParentDirectory(), folder, fileName), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    return fileName

def printResults(debug, duplicates, missing, filename, totalCounted):
    # Alert user that the file has been generated
    # Alert user which cards will have to be added manually
    print("=============================================================\n")
    print("| These cards were not found in the databse (mostly tokens) |\n")
    print("=============================================================\n")
    for d in debug:
        # print(d[0] + ' || ' + d[1])
        print(d)
    print("=============================================================")
    # ---- For Debugging puproses ---- #
    # print("These cards had duplicate entries and not caught:")
    # for dup in duplicates:
    #     print(dup)
    # print("=============================================================")
    # print("These cards have been missed--they have no valid edition")
    # for miss in missing:
    #     print(miss)
    # print("=============================================================")
    print("Created csv: " + filename)
    print("Created " + str(totalCounted) + " entires successfully")

