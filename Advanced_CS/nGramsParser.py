# File: nGramsParser.py
# Versions: Python 2.7.13
# Name: Sivan Cooperman
# Date: 5.1.2017
# Desc: Parses Google nGrams Data to display usage statistics
# Usage: Requires a file to parse path and the word you would like to find as raw input after instantiating the function

import linecache as lc
import matplotlib.pyplot as plt
import numpy as np

def getData(line):
    data = line.split("\t")
    if '_' in data[0]:
        temp = data[0].split("_")
        data[0] = temp[0]
        data[0] = data[0].lower()
        data.insert(1, temp[1])
        del(data[1])
    try:
        temp = data[3].split("\n")
        data[3] = temp[0]
    except IndexError:
        pass
        
    return data

def nGramsParse():
    wordFreqAxis = []
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
    
    print 'Word found! Displaying usage...'
    currentWord = wordData[0]
    dataDict = {}
    
    while wordData[0] == currentWord:
        wordData = getData(lc.getline(fileName, lineCount))
        wordFreqAxis.append(wordData[2])
        yearAxis.append(wordData[1])
        dataDict[str(wordData[1])] = wordData[2]
        lineCount += 1
    
    if wordFreqAxis == [] or yearAxis == []:
        print 'That word is not in our data!'
        return
    
    for i in range(len(yearAxis)):
        yearAxis[i] = int(yearAxis[i])
    for j in range(len(wordFreqAxis)):
        wordFreqAxis[j] = int(wordFreqAxis[j])
    print wordFreqAxis
    print yearAxis
    xCoords = np.arange(len(wordFreqAxis))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(xCoords, wordFreqAxis,1.0, align='center')
    ax.set_xticks(xCoords)
    ax.set_xticklabels(yearAxis)