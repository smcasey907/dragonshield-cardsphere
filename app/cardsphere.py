import processData as pd
import multiverseBridgeService as service
import fileManagement as fm


csvFileCollection = fm.getFiles()

data = []
debug = []
duplicates = []
missed = []
totalCounted = 0

print("Welcome to the Dragon Shield Collection Export\nto Cardsphere csv importer. Be patient\nwhile the kobolds eat...er, massage your data...\n")

for csvFile in csvFileCollection:
    with open(csvFile) as csvf:

        print('Getting data from binder:')
        print(str(csvFile.name).replace('.csv', ''))

        csvData = fm.cleanFile(csvf)
        
        cardList = []
        cardList = pd.removeUselessData(csvData)
        totalCounted += pd.processCards(cardList)

        debugVal = pd.getDebug()
        for dv in debugVal:
            debug.append(dv)
        dupVal = pd.getDuplicates()
        for duv in dupVal:
            duplicates.append(duv)
        missingVal = pd.getMissed()
        for mv in missingVal:
            missed.append(mv)
        finishedData = pd.getData()
        for fd in finishedData:
            data.append(fd)
        pd.reset()
        

# Generate the csv file
data.insert(0, ['Count', 'Tradelist Count', 'Name', 'Edition', 'Condition', 'Language', 'Foil'])

savedFileName = fm.createCardSphereCsv(data)
fm.printResults(debug, duplicates, missed, savedFileName, totalCounted)



# # TODO: 
# # 1. handle Tokens
# # 2. handle two sided cards...may need to call a seperate API