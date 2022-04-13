from ast import Num
import re
import sys
from tokenize import Number
import multiverseBridgeService as service

neoExtArtIdStart = 428
rVal = []
debug = []
duplicates = []
missing = []
data = []
totalQuantity = 0
totalForProgressBar = 0

class Card:
    pass

def removeUselessData(csvData):
    returnData = []
    global totalForProgressBar
    for row in csvData:
        if len(row) > 10:
            returnData.append([row[1],row[3],row[4],row[5],row[6],row[8],row[9]])
            if not 'Quantity' in row[1]:
                totalForProgressBar += int(row[1])
    return returnData

def processCards(cardList):
    # This is the index of each list item for reference
    # 0: 'Quantity',
    # 1: 'Card Name',
    # 2: 'Set Code',
    # 3: 'Set Name',
    # 4: 'Card Number',
    # 5: 'Printing',
    # 6: 'Language'
    global totalQuantity
    totalQuantity = 0
    for card in cardList[1:]:
        c = Card()
        c.isEtched = False
        c.cardName = card[1]
        c.searchName = c.cardName
        if ' // ' in c.cardName:
            c.removedFlipName = c.cardName.split(" //")
            c.searchName = c.removedFlipName[0]
        c.code = card[2]
        if 'etc' in c.code:
            c.isEtched = True
            c.code = c.code.strip('etc')
        c.condition = 'NM'
        c.language = card[6]
        if c.language == 'jp':
            c.language = 'JA'
        if card[5] == 'Normal':
            c.finish = False
            c.csvFinish = 'N'
        elif card[5] == 'Foil':
            c.finish = True
            c.csvFinish = 'FOIL'
        c.codeId = card[4]
        if not c.codeId.isdecimal():
            c.codeId = re.sub('[^0-9]', '', c.codeId)
        c.quantity = str(card[0])
        # For finding cards not added to the csv
        # This value is not usable by Cardsphere 
        # and is replaced by edition in the data
        c.setName = card[3]

        totalQuantity = addCardToDataCollection(c, totalQuantity)
    
    return totalQuantity

def addCardToDataCollection(card, totalCards):
    global rVal
    rVal = None
    edition = None
    if card.code == 'NEO' and int(card.codeId) > neoExtArtIdStart:
        query = {'name':card.searchName, 'mtgjson_code':card.code, 'is_foil':card.finish}
        rVal = service.getCardData(query)
        edition = getNEOExtendedArtCards(card, rVal)
    else:
        query = {'name':card.searchName, 'mtgjson_code':card.code, 'is_foil':card.finish, 'collector_number':card.codeId}
        rVal = service.getCardData(query)
        if len(rVal) == 0:
            query = {'name': card.searchName, 'collector_number':card.codeId}
            rVal = service.getCardData(query)
            edition = getPromoOrUnsortedCards(card, rVal)

    if len(rVal) > 1 and card.isEtched:
        edition = setEtchedFoils(rVal)

    if edition == None:
        edition = setMiscMissingCards(card, rVal)

    if edition != None:
        totalCards += updateDataCollection(card, edition)
        updateStatusBar(totalCards)

    return totalCards
            
# Get specific card groups...Add to this group as needed
def getNEOExtendedArtCards(card, rVal):
    try:
        for val in rVal:
            if 'Extended Art' in val['edition']:
                return val['edition']
    except:
        debug.append([card.cardName, card.setName, card.code, card.codeId, card.finish])

def getPromoOrUnsortedCards(card, rVal):
    try:
        for val in rVal:
            return val['edition']
    except:
        debug.append([card.cardName, card.setName, card.code, card.codeId, card.finish])
    if len(rVal) == 0:
        return getMiscNEOCards(card)

def getMiscNEOCards(card):
    # NEO Commander Cards
    if card.code == 'NEC':
        return 'Kamigawa: Neon Dynasty Commander Decks'
    # NEO some cards are just misnumbered
    elif card.code == 'NEO':
        edition = 'Kamigawa: Neon Dynasty'
    else:
        debug.append([card.cardName, card.setName, card.code, card.codeId, card.finish])

def setEtchedFoils(rVal):
    for val in rVal:
        if 'Etched Foil' in val['edition']:
            return val['edition']

def setMiscMissingCards(card, rVal):
    if len(rVal) > 1 and card.isEtched == False:
        for val in rVal:
            if card.code == 'NEO':
                return 'Kamigawa: Neon Dynasty'
            else:
                duplicates.append([card.cardName, val['edition'], card.codeId])
    elif len(rVal) == 1:
        try:
            return rVal[0]['edition']
        except:
            missing.append([card.cardName, card.code, card.codeId, card.finish])

def updateDataCollection(card, edition):
    data.append([
        card.quantity,
        card.quantity,
        card.cardName,
        edition,
        card.condition,
        card.language,
        card.csvFinish,
        ""
    ])

    return int(card.quantity)

def getDebug():
    return debug

def getDuplicates():
    return duplicates

def getMissed():
    return missing

def getData():
    return data

def updateStatusBar(ttlQty):
    # Create empty bar
    progressBar = ' ||'
    totalBarIncrements = 20
    progressVal = ttlQty/totalForProgressBar
    progressVal = progressVal * 100
    progressValDisplay = progressVal // 5

    i = 0
    while i < int(progressValDisplay):
        progressBar += '#'
        i += 1

    fillDashes = totalBarIncrements - int(progressValDisplay)
    i = 0
    while i < fillDashes:
        progressBar += '-'
        i += 1

    progressBar += '|| ' + str(round(progressVal, 2)) + '%'
    # Show Progress Bar
    print(progressBar, end="\r")

def reset():
    global debug
    global missing
    global duplicates
    global data
    global totalForProgressBar
    debug = []
    missing = []
    duplicates = []
    data = []
    totalForProgressBar = 0