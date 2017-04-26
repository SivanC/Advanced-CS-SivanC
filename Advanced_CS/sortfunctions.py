import pdb, random, cProfile, pstats          #python debugger, allows to go through a function step by step using pdb.set_trace()

def swapVal(value1, value2):
    """ Swaps the values held in two variables and returns a list with the two swapped values
    """
    tempVal = 0
    tempVal = value1
    value1 = value2
    value2 = tempVal
    return value1, value2
    
def randListGen(listLength, listRange):
    """ Creates a list with random integers in range listRange and length listLength
    """
    randList = []
    for i in range(listLength):
        randList.append((random.randint(0, listRange)))
    return randList

def splitList(aList):
    """Separates all items in a list
    """
    if len(aList) <= 1:
        return aList #if the list is one index long return it

    elif len(aList) > 1:
        bList = aList[0:len(aList)/2]
        cList = aList[len(aList)/2:]
        
    return splitList(bList), splitList(cList)
    
def mergeSort(alist):       #trinket version
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print alist

def isSorted(aList):
    """Checks if a list is sorted by comparing each entry to the next
    """
    index = 0
    while index != len(aList) - 1 and aList[index] <= aList[index + 1]:
        index += 1
    if index == len(aList) - 1: #If every number is lower than or equal to the next number the list is sorted
        return True
    else:
        return False

def quickSort(aList): #Best case is 1 swap needed to sort the list. Worst case is...however many splits of the list are required until there's only one item in each list
    #print aList
    
    if aList == []: #Checking for empty array, unsortable array, and sorted array
        return
    if len(aList) == 1:
        return aList
    if isSorted(aList):
        return aList
        
    pivotIndex = 0 #setting the default pivot of aList[0]
    smallNum = len(aList) - 1
    bigNum = 1
    #pdb.set_trace()
    while bigNum < smallNum: #If this condition is fulfilled then there are only numbers smaller than the pivot in the first half, and only numbers larger in the second, enabling recursive sorting
        pivot = aList[pivotIndex] #Defined inside the while loop in order to be updated if all numbers are larger than the pivot
        swapAllowSmall = False    #resetting prerequisites for swapping
        swapAllowBig = False
        
        while aList[bigNum] < pivot:      #checks for a number greater than or equal to the pivot starting from the first index of the array
            bigNum += 1
            if bigNum >= len(aList):
                #print 'bigNum reset'
                pivotIndex += 1
                bigNum = pivotIndex + 1
                break
            #print 'bigNum is ' + str(bigNum) + ' and the value is ' + str(aList[bigNum])
        if aList[bigNum] >= pivot: #swapAllowBig inside a conditional so that it is not triggered by the break if bigNum > len(aList)
            swapAllowBig = True
            
        while aList[smallNum] >= pivot:   #checks for a number less than the pivot starting from the last index of the array
            if smallNum > bigNum + 1:               
                smallNum -= 1
                #print 'smallNum is ' + str(smallNum) + ' and the value is ' + str(aList[smallNum])
            else:
                #print 'No numbers smaller than pivot found! Adjusting pivot...'
                smallNum = len(aList) - 1
                pivotIndex += 1
                bigNum = pivotIndex
                break
        if aList[smallNum] < pivot:
            swapAllowSmall = True
            
        if swapAllowBig == True and swapAllowSmall == True:
            swapListA = swapVal(aList[bigNum], aList[smallNum])
            aList[bigNum] = swapListA[0]       #swaps the values of aList[bigNum] and aList[smallNum]
            aList[smallNum] = swapListA[1]
    middleNum = aList[0]
    swapIndex = 1
    swapFound = False #temp(?) workaround var for while loop  |
    while swapIndex < len(aList) and swapFound == False:# <--
        if aList[swapIndex] < middleNum:
            swapIndex += 1
        else:
            swapFound = True
    swapIndex -= 1 #setting swapIndex to the number with the highest index that is lower than the pivot
    swapListB = swapVal(middleNum, aList[swapIndex])
    aList[0] = swapListB[0]
    aList[swapIndex] = swapListB[1]
    #print 'swapped list: ' + str(aList)
    if isSorted(aList) == False:
        #Splitting the semi-sorted list into two halves
        lowHalf = aList[:swapIndex]
        highHalf = aList[swapIndex:]
        bList = quickSort(lowHalf)
        cList = quickSort(highHalf)
        return bList + cList
    else:
        return aList

def insertSort(aList):
    """Compares each item in a list to the next and swaps if one value is lower, first from left to right and then from right to left. Returns a sorted list
    """
    print aList
    if len(aList) <= 1:    #checking for unsortable and too short lists
        return aList
    elif isSorted(aList):
        return aList
    
    if aList[0] > aList[1]:
        swapListA = swapVal(aList[0], aList[1])
        aList[0] = swapListA[0]
        aList[1] = swapListA[1]
    for i in range(1, len(aList) - 1): #Looping through the list starting at the second/pivot index
        if aList[i] > aList[i + 1]:
            swapListB = swapVal(aList[i], aList[i + 1])
            aList[i] = swapListB[0]
            aList[i + 1] = swapListB[1]
    for j in range(len(aList) - 2, 0, -1): #Looping through the list starting at the second to last entry of the list going backwards
        if aList[j] < aList[j - 1]:
            swapListC = swapVal(aList[j], aList[j - 1])
            aList[j] = swapListC[0]
            aList[j - 1] = swapListC[1]
            
    if isSorted(aList):
        return aList
    else:
        sortedList = insertSort(aList)
    return sortedList
    
def shellSort(aList, *gap):
    """Splits a list into numLists using increments of gap to select items from aList, and then uses insertion sort to sort the individual lists before combination. Returns the sorted list.
    """
    print aList
    if len(aList) <= 1:    #checking for unsortable and too short lists
        return aList
    elif isSorted(aList):
        return aList
    
    if gap != ():
        gap = gap[0]
    else:
        gap = 3
        
    listDict = {}
    intQuotient = len(aList)//gap
    remainder = len(aList) % gap
    sortedList = []
    longListList = []
    
    for i in range(gap): #setting up our arrays
        listDict['list' + str(i)] = []

    for j in range(gap): #Adding numbers to our sublists
        gapCounter = j
        while gapCounter <= len(aList):
            if gapCounter != 0:
                listDict['list' + str(j)] += [aList[gapCounter - 1]]
            gapCounter += gap
            
    for k in listDict: #sorting all lists within the dictionary
        listDict[k] = insertSort(listDict[k])
        
    for l in range(1, remainder + 1): #Appending lists to our list of large lists
        longListList.append('list' + str(l))
        
    for m in range(intQuotient): #At index m in all lists listn add to sortedList
        for n in range(gap):
            sortedList.append(listDict['list' + str(n)][m])
    print 'sorted list:'
    print sortedList
    for o in longListList: #Add the last value of all large lists to the end of the sortedList
        sortedList.append(listDict[o][-1])
        print remainder
    print longListList
    print listDict
    sortedList = insertSort(sortedList)
    return sortedList

def selectionSort(aList):
    """Repeatedly finds the smallest value in aList and puts it behind the previous smallest value. Returns a list.
    """
    print aList
    if len(aList) <= 1:    #checking for unsortable and too short lists
        return aList
    elif isSorted(aList):
        return aList
        
    swapIndex = 0      #setting index of the number to be swapped with the smallest number found
    smallNumIndex = 0
    
    while not isSorted(aList): #Repeat until the list is sorted
        swapAllow = False    #Added to insure that if no smaller number than the number at aList[swapIndex] is found it will not swap with the index of the last known small number
        smallNum = aList[swapIndex]
        
        for i in range(swapIndex, len(aList)): #Check whether each number is lower than the pivot at aList[swapIndex], and if it is update smallNum and smallNumIndex
            if aList[i] < smallNum:
                smallNum = aList[i]
                smallNumIndex = i
                swapAllow = True
                
        if swapAllow == True:  #Swapping the values
            swapListA = swapVal(smallNum, aList[swapIndex])
            aList[smallNumIndex] = swapListA[0]
            aList[swapIndex] = swapListA[1]
            
        if swapIndex < len(aList) - 1: #Checking that the swap index doesn't go out of bounds
            swapIndex += 1
        else:
            break

    return aList
    
def bubbleSort(aList):
    """Sorts a list by checking the order of two elements and swapping it if they are wrong from left to right, starting over until the list is sorted. Returns a list.
    """
    print aList
    if len(aList) <= 1:    #checking for unsortable and too short lists
        return aList
    elif isSorted(aList):
        return aList
    
    while not isSorted(aList):  #Repeat until sorted
        for i in range(len(aList) - 1):
            if aList[i] > aList[i + 1]:  #If the larger value is earlier in the list than the shorter one swap them
                swapList = swapVal(aList[i], aList[i + 1])
                aList[i] = swapList[0]
                aList[i + 1] = swapList[1]
    
    return aList


def sortTest(function):  #See profiletesting.py for comments
    profile = cProfile.Profile()
    sortType = 'cumtime'
    
    profile.enable()
    
    for i in range(1000):
        function(randListGen(10,10))
        
    profile.disable()
    
    outputFile = open('/Users/Sivan/Advanced-CS-SivanC/Advanced CS/sortfunctions_Profile.txt', 'ab')
    outputFile.write('Results of 1000 executions of ' + str(function) + '\n' * 2)
    stats = pstats.Stats(profile, stream = outputFile).strip_dirs().sort_stats(sortType).print_stats()
    
    outputFile.close()
    
    return