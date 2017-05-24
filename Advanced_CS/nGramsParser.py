# File: nGramsParser.py
# Versions: Python 2.7.13
# Name: Sivan Cooperman
# Date: 5.1.2017
# Desc: Parses Google nGrams Data to display usage statistics
# Usage: Requires a file to parse path and the word you would like to find as raw input after instantiating the function

import linecache as lc #Memory efficient line reading

import matplotlib.pyplot as plt #Graphing Utility
import numpy as np

import sys #Returning outside a function

import cProfile #Profiler
import pstats

profile = cProfile.Profile()
sortMethod = 'cumtime'
outputPath = '/Users/Sivan/Documents/Github/Advanced-CS-SivanC/Advanced_CS/nGramsParserProfileOutput.txt'
output = open(outputPath, 'w')
profile.enable() #Begin tracking

def getData(line):
    data = line.split("\t") #Split the data into word, year, number of times used, and across how many books in nGrams database
    if '_' in data[0]:
        temp = data[0].split("_")
        data[0] = temp[0]
        data[0] = data[0].lower() #Removing any part of speech indicators
        data.insert(1, temp[1])
        del(data[1])
    try:
        temp = data[3].split("\n") #Remove the newline at the end of a line unless it is the last line
        data[3] = temp[0]
    except IndexError:
        pass
        
    return data

wordFreqAxis = []
yearAxis = []
quit = False

print '\n Thank you for using the Sivan Cooperman nGrams Parser! All data has been downloaded from Google\'s nGram Database. \n'
validFile = False
while not validFile:
    fileName = str(raw_input('Please enter the path of the file you would like to parse (or \'quit\' to exit): \n')) #Receiving the file path and opening the file
    if fileName == 'quit': #quit comand to exit the program
        quit = True
    try:    
        open(fileName, 'r')
        validFile = True
    except IOError or AttributeError:
        print 'That is not a valid file! Please try again'
    
word = str(raw_input('Please enter the word you would like to display (or \'quit\' to exit): \n')).lower() #Receiving the word to search for

if word == 'quit':
    quit = True

if quit:
    sys.exit()
       
wordFound = False
lineCount = 0

initProfile()

while not wordFound: #Continue to analyze lines using linecache until the function reaches a blank line or finds the word detailed by the raw input
    print 'Searching...'
    lineCount += 1
    wordData = getData(lc.getline(fileName, lineCount))
    wordData.append(lineCount)
    if wordData[0] == '':
        break
    print 'Current word: ' + str(wordData)
    if word == wordData[0]:
        wordFound = True
    
if not wordFound: #If the word isn't found end the function
    print 'That word is not in our data!'
    sys.exit()

print 'Word found! Displaying usage...'
currentWord = wordData[0]
dataDict = {}

while wordData[0] == currentWord: #Creating a data dictionary for text analysis and the two lists for graphing
    wordData = getData(lc.getline(fileName, lineCount))
    wordFreqAxis.append(wordData[2])
    yearAxis.append(wordData[1])
    dataDict[str(wordData[1])] = wordData[2]
    lineCount += 1
    wordData = getData(lc.getline(fileName, lineCount))

if wordFreqAxis == [] or yearAxis == []: #Double checking that we have found the word
    print 'That word is not in our data!'
    sys.exit()

for i in range(len(yearAxis)):
    yearAxis[i] = int(yearAxis[i])
    wordFreqAxis[i] = int(wordFreqAxis[i])

word = getData(lc.getline(fileName, lineCount - 1))[0] #Formatting
word = word.capitalize()

xCoords = np.arange(len(wordFreqAxis)) #Graphing of the two lists as a bar graph of frequency over time
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('Time (Years)')
ax.set_ylabel('Frequency (# Times Used)')
ax.set_title('Frequency of use of ' + word)
ax.bar(xCoords, wordFreqAxis,width=1.0, align='center')
#ax.set_xticks(xCoords)
ax.set_xticklabels(yearAxis, fontsize = 8)
plt.show()
profile.disable() #Stop tracking performance