import pdb          #python debugger, allows to go through a function step by step using pdb.Trace()
import random       #used in randListGen()
import cProfile
import pstats

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
    
def shellSort(aList, gap, numLists): #ignore this for now!
    """Splits a list into numLists using increments of gap to select items from aList, and then uses insertion sort to sort the individual lists before combination. Returns the sorted list.
    """
    gapCounter = 0
    for i in range(numLists):
        listName = 'list'
        while gapCounter <= len(aList) - 1:
            listName + str(i) = aList[gapCounter]
            gapCounter += gap
        return 
    
def sortTest(function):
    for i in range(1000):
        function(randListGen(10,10))
        
#pdb.set_trace()
#sortFile = 'C:\Users\Sivan\Documents\GitHub\Advanced-CS-SivanC\Advanced CS\sortfunctions_Profile.txt'
#statsInstance = cProfile.run('insertSort([0, 10, 9, 8, 9, 5, 3, 0, 8, 4])')
#stream = open(sortFile, 'w')
#stats = pstats.Stats(statsInstance, stream = stream)
#stats = pstats.Stats('C:\Users\Sivan\Documents\GitHub\Advanced-CS-SivanC\Advanced CS\sortfunctions.py', stream = stream)
#stats.print_stats()