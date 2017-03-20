def sequentialSearch(list, element):
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