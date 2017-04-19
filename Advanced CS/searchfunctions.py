def sequentialSearch(aList, element):
    """Performs a sequential search for an item,
    returning true if found and false otherwise
    """
    found = False
    for i in aList:
        if i == element:
            found = True
                
    return found
    
def binarySearch(aList, element):
    if len(aList) == 1:
        return element == aList[0]
    elif len(aList) == 0:
        return
        
    midNum = len(aList)//2
    found = False
    
    if aList[midNum] == element:
        found = True
        return found
        
    else:
        bList = aList[:midNum]
        cList = aList[midNum:]
        b = binarySearch(bList, element)
        c = binarySearch(cList, element)
 
    if b == True:
        found = b
    if c == True:
        found = c
           
    return found