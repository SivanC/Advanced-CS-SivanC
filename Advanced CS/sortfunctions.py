import pdb
import random
import cProfile

def swapVal(value1, value2):
    tempVal = 0
    tempVal = value1
    value1 = value2
    value2 = tempVal
    return value1, value2
    
def randListGen(listLength, listRange):
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
   
def quickSort(aList):
    print aList
    if len(aList) <= 1:
        return aList
    
    pivotIndex = 0    
    pivot = aList[pivotIndex]
    smallNum = len(aList) - 1
    bigNum = 0
    
    while bigNum < smallNum:
        print 'Big is less than small'
        print 'pivot is at ' + str(pivotIndex)
        while aList[bigNum] < pivot:      #checks for a number greater than or equal to the pivot starting from the first index of the array
            print 'bigNum is ' + str(bigNum) + ' and the value is ' + str(aList[bigNum])
            bigNum += 1
            if bigNum < len(aList):
                print 'bigNum reset'
                bigNum = 0
                pivotIndex += 1
                break
                
            
        while aList[smallNum] >= pivot:   #checks for a number less than the pivot starting from the last index of the array
            print 'smallNum is ' + str(smallNum) + ' and the value is ' + str(aList[smallNum])
            smallNum -= 1
            if smallNum < 0:
                print 'smallNum reset'
                smallNum = len(aList) - 1
                pivotIndex += 1
                break      
                  
        swappedVals = swapVal(aList[bigNum], aList[smallNum])
        aList[bigNum] = swappedVals[0]       #swaps the values of aList[bigNum] and aList[smallNum]
        aList[smallNum] = swappedVals[1]
        print 'swapping ' + str(swappedVals)
    return aList
    
#cProfile.run('quickSort(randListGen(10,10))', 'sortfunctions Profile')