import pdb          #python debugger, allows to go through a function step by step using pdb.Trace()
import random       #used in randListGen()
import cProfile



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

def checkSorted(aList):
    """Checks if a list is sorted by comparing each entry to the next
    """
    index = 0
    while aList[index] != aList[-1] and aList[index] < aList[index + 1]:
        index += 1
    if index == len(aList) - 1: #If every number is lower than or equal to the next number the list is sorted
        return True
    else:
        return False

def quickSort(aList): #Best case is 1 swap needed to sort the list. Worst case is...however many splits of the list are required until there's only one item in each list
    print aList
    print 'pivot is ' + str(aList[0])
    if len(aList) <= 1:   #checking the list isn't unsortable
        return aList
    
    pivotIndex = 0 #setting the default pivot of aList[0]
    smallNum = len(aList) - 1
    bigNum = 1
    
    while bigNum + 1 < smallNum: #If this condition is fulfilled then there are only numbers smaller than the pivot in the first half, and only numbers larger in the second, enabling recursive sorting
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
            swappedVals = swapVal(aList[bigNum], aList[smallNum])
            aList[bigNum] = swappedVals[0]       #swaps the values of aList[bigNum] and aList[smallNum]
            aList[smallNum] = swappedVals[1]
    
    middleNum = aList[0] #assigning the number we will move to the middle of the list
    counter = 1
    print aList
    while aList[counter] < middleNum and counter < len(aList) - 1: #determining the divide between numbers lower than and numbers higher than the pivot
        counter += 1
    counter -= 1 #setting the counter to the number after which we insert the pivot
    swappedVals = swapVal(middleNum, aList[counter]) #swapping the pivot with the last value lower than it
    aList[0] = swappedVals[0]
    aList[counter] = swappedVals[1]
    
    if checkSorted(aList) == True:
        #Splitting the semi-sorted list into two halves
        lowHalf = aList[:counter]
        highHalf = aList[counter:]
        quickSort(lowHalf)
        quickSort(highHalf)
        return aList

#cProfile.run('quickSort(randListGen(10,10))','C:\Users\Sivan\Documents\GitHub\Advanced-CS-SivanC\Advanced CS\sortfunctions_Profile.txt')