# File: nGramsParser.py
# Versions: Python 2.7.13
# Name: Sivan Cooperman
# Date: 5.1.2017
# Desc: Parses Google nGrams Data to display usage statistics
# Usage: Requires a file to parse path and the word you would like to find as raw input after instantiating the func
import linecache as lc #Memory efficient line reading

import matplotlib.pyplot as plt #Graphing Utility
import numpy as np

import sys #Returning outside a function

import cProfile #Profiler
import pstats

filename = ''
profile = cProfile.Profile()
sortMethod = 'cumtime'
outputPath = '/Users/Sivan/Documents/Github/Advanced-CS-SivanC/Advanced_CS/nGramsParserProfileOutput.txt'
    
profile.enable() #Begin tracking

def getData(line):
    data = line.split("\t") #Split the data into word, year, number of times used, and across how many books in nGrams database
    if '_' in data[0]:
        data[0] = data[0].replace(data[0], data[0].split('_')[0])
    try:
        temp = data[3].split("\n") #Remove the newline at the end of a line unless it is the last line
        data[3] = temp[0]
    except IndexError:
        pass
    data[0] = data[0].lower()    
    return data

wordFreqAxis = []
yearAxis = []
quit = False

print '\n Thank you for using the Sivan Cooperman nGrams Parser! All data has been downloaded from Google\'s nGram Database. \n'
validFile = False
while not validFile:
    fileName = str(raw_input('Please enter the path of the file you would like to parse (or \'quit\' to exit): \n')) #Receiving the file path and opening the file
    
    if fileName == 'default':
        fileName = 'C:\Users\Sivan\Documents\GitHub\Advanced-CS-SivanC\Advanced_CS\googleagramsdatabaseaa.txt'
        
    elif fileName == 'quit': #quit comand to exit the program
        quit = True
    try:    
        with open(fileName, 'r+') as openFile:
            if not openFile.read(1):
                print 'This file is empty!'
                sys.exit()
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
        
initLineCount = lineCount 
 
if not wordFound: #If the word isn't found end the script
    print 'The word' + word + ' is not in our data!'
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

profile.disable() #Stop tracking performance

if wordFreqAxis == [] or yearAxis == []: #Double checking that we have found the word
    print 'Error: One or both lists of graphing coordinates are empty!'
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

with open(outputPath, 'a') as output:
    output.write('\n')
    output.write('\t \t Stats for the word ' + word + ' at line ' + str(initLineCount))
    output.write('\n')
    stats = pstats.Stats(profile, stream=output).strip_dirs().sort_stats(sortMethod).print_stats()
print 'Writing stats to file...'