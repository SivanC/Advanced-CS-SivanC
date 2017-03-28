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

def quickSort(aList): #Best case is 1 swap needed to sort the list. Worst case is...however many splits of the list are required until there's only one item in each list
    print aList
    
    if len(aList) <= 1:   #checking the list isn't unsortable
        return aList
    
    pivotIndex = 0 #setting the default pivot of aList[0]
    smallNum = len(aList) - 1
    bigNum = 1
    
    while bigNum < smallNum: #If this condition is fulfilled then there are only numbers smaller than the pivot in the first half, and only numbers larger in the second, enabling recursive sorting
        pivot = aList[pivotIndex] #Defined inside the while loop in order to be updated if all numbers are larger than the pivot
        print 'Big is less than small'
        print 'pivot is at ' + str(pivotIndex)
        print 'aList[bigNum] is ' + str(aList[bigNum])
        while aList[bigNum] < pivot and  bigNum < smallNum:      #checks for a number greater than or equal to the pivot starting from the first index of the array
            bigNum += 1
            print 'bigNum is ' + str(bigNum) + ' and the value is ' + str(aList[bigNum])
            if bigNum > len(aList):
                print 'bigNum reset'
                pivotIndex += 1
                bigNum = pivotIndex + 1
                break
        
        #about half the time turns into infinite loop between two numbers 
        while aList[smallNum] >= pivot and smallNum > (bigNum + 1):   #checks for a number less than the pivot starting from the last index of the array
            smallNum -= 1
            print 'smallNum is ' + str(smallNum) + ' and the value is ' + str(aList[smallNum])
            if smallNum < 0:
                print 'smallNum reset'
                smallNum = len(aList) - 1
                pivotIndex += 1
                bigNum += 1 # updated to start comparisons with the number in front of the pivot
                break
                  
        swappedVals = swapVal(aList[bigNum], aList[smallNum])
        aList[bigNum] = swappedVals[0]       #swaps the values of aList[bigNum] and aList[smallNum]
        aList[smallNum] = swappedVals[1]
        print 'swapping ' + str(swappedVals)
    return aList
    
#cProfile.run('quickSort(randListGen(10,10))', 'sortfunctions Profile')
 #=======
 #               smallNum = 0
 #             
 #       aList[bigNum] = swapVal(aList[bigNum], aList[smallNum])[0]       #swaps the values of aList[bigNum] and aList[smallNum]
 #       aList[smallNum] = swapVal(aList[bigNum], aList[smallNum])[1]#
 #
 #       print aList[bigNum]
 #       print aList[smallNum]
 #
 #   return aList

#samiList = randListGen(10, 8)
#print "My List: " + str(samiList)

#mergeSort(samiList)

#print "Quick Sorted: " + str(quickSort(samiList))