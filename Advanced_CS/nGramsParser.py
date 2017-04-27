def nGramsParse():
    
    validFile = False
    while not validFile:
        try:
            fileName = str(raw_input('Please enter the path of the file you would like to parse: \n'))
            validFile = True
        except IOError:
            print 'That is not a valid file! Please try again'
        
    parseFile = open(fileName, 'r')
    
    word = str(raw_input('Please enter the word you would like to display \n'))
    
    wordFound = False
    for line in parseFile:
        wordData = line.split("    ")
        if word == wordData[0]:
            wordFound = True
            break
            
    if not wordFound:
        print 'That word is not in our data!'
        return
    
    word = [wordData[0], wordData[1], wordData[2], wordData[3]]
    print word