def splitList(aList):
    """Separates all items in a list
    """
    
    if len(aList) <= 1:
        return aList #if the list is one index long return it

    elif len(aList) > 1:
        bList = aList[0:len(aList)/2]
        cList = aList[len(aList)/2:]
        
    return splitList(bList), splitList(cList)