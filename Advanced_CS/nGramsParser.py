import linecache as lc
import matplotlib.pyplot as plt
import pdb

def nGramsParse():
    wordFreq = []
    yearAxis = []
    
    validFile = False
    #pdb.set_trace()
    while not validFile:
        try:
            fileName = str(raw_input('Please enter the path of the file you would like to parse: \n'))
            validFile = True
        except IOError:
            print 'That is not a valid file! Please try again'
        
    parseFile = open(fileName, 'r')
    
    word = str(raw_input('Please enter the word you would like to display \n'))
    
    wordFound = False
    lineCount = 0
    while not wordFound: 
        lineCount += 1
        wordData = lc.getline(parseFile.__file__, lineCount).split("    ")
        if word == wordData[0]:
            wordFound = True
            
    if not wordFound:
        print 'That word is not in our data!'
        return
    
    currentYear = wordData[1]
    
    while wordData[1] <= currentYear:
        wordData = lc.getline(parseFile, lineCount).split("    ")
        wordFreq.append(wordData[2])
        yearAxis.append(wordData[1])
        lineCount += 1
        
    plt.plot(wordFreq, yearAxis)
    plt.show(block=True)