def sequentialSearch(alist, element):
    """Performs a sequential search for an item,
    returning true if found and false otherwise
    """
    found = False
    while found != True:
        for i in list:
            if i == element:
                found = True
            elif i != element:
                found = False
                
    return found
    
def binarySearch(alist, num):
    found = False
    newListLength = len(alist)
    print 'running'
    while found == False:
        if alist[newListLength/2] == num:
            found = True
            print 'found 9'
        else:
            newListlength = newListLength/2
            print 'didnt find 9'
        if newListLength <= 1:
            found = True
            print 'list too small'
    return found