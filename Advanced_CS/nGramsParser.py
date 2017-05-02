# File: nGramsParser.py
# Versions: Python 2.7.13
# Name: Sivan Cooperman
# Date: 5.1.2017
# Desc: Parses Google nGrams Data to display usage statistics
# Usage: Requires a file to parse path and the word you would like to find as raw input after instantiating the function

import linecache as lc
import matplotlib.pyplot as plt
import pdb

def getData(line):
    data = line.split("\t")
    if '_' in data:
        temp = data[0].split("_")
        data[0] = temp[0]
        data[0].lower()
        data.insert(1, temp[1])
        del(data[1])
    if '\n' in data[3]:
        temp = data[3].split("\n")
        data[3] = temp[0]
    
    return data

def nGramsParse():
    wordFreq = []
    yearAxis = []
    
    validFile = False
    #pdb.set_trace()
    while not validFile:
        fileName = str(raw_input('Please enter the path of the file you would like to parse: \n'))
        if fileName.lower() == 'quit':
            return
        try:    
            open(fileName, 'r')
            validFile = True
        except IOError or AttributeError:
            print 'That is not a valid file! Please try again'
        
    word = str(raw_input('Please enter the word you would like to display \n')).lower()
    print 'Word to look for: ' + word

    wordFound = False
    lineCount = 0
    while not wordFound: 
        print 'Searching...'
        lineCount += 1
        wordData = getData(lc.getline(fileName, lineCount))
        if wordData[0] == ' ':
            break
        print 'Current word: ' + str(wordData)
        if word == wordData[0]:
            wordFound = True
            
    if not wordFound:
        print 'That word is not in our data!'
        return
    
    print 'Word found! Calculating usage...'
    currentYear = wordData[1]
    currentWord = wordData[0]
    
    while wordData[0] == currentWord:
        wordData = getData(lc.getline(fileName, lineCount))
        wordFreq.append(wordData[2])
        yearAxis.append(wordData[1])
        lineCount += 1
    
    plt.xticks(int(currentYear) - 1, currentYear + lineCount)
    plt.plot(wordFreq, yearAxis)
    plt.show(block=True)