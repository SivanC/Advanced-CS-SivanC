import random

class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []  
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[-1]
        
    def size(self):
        return len(self.items)    

class Queue():
    
    def __init__(self):
        self.items = []
        
    def __repr__(self):
        return str(self.items)
        
    def __getitem__(self, index):
        return self.items[index]
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self, index):
        del(self.items[index])
        
    def deleteElement(self, element):
        for i in range(len(self.items)):
            if element == self.items[i]:
                del(self.items[i])
    
    def deleteIndex(self, index):
        del(self.items[index])

def parChecker(aString):
    """Checks if a set of brackets is identical when reversed. Returns True or False
    """
    
    stack = []
    invertStack = []
    
    for i in range(len(aString)):
        stack.append(aString[i])
        
    for j in stack:
        popped = stack.pop()
        invertStack.append(popped)
        
    return stack == invertStack
    
def binaryConv(num):
    """Converts an integer to it's binary representation through the Divide by Two algorithm. Returns a string containing the binary number.
    """
    
    binaryNum = ''
    stack = []
    
    while num > 0:
        remainder = num % 2
        newNum = num // 2
        num = newNum
        stack.append(remainder)
    
    for i in stack:
        binaryNum += str(i)
        
    return binaryNum
    
def hotPotato(names, num):
    
    queue = Queue()
    
    for i in names:
        queue.enqueue(i)
        
    potatoCounter = 0
    
    while len(names) != 1:
        for j in range(num):
            popped = queue.dequeue(0)
            queue.enqueue(popped)
            print str(names[potatoCounter]) + ' has the hot potato!'
            potatoCounter += 1
            if potatoCounter > len(names) - 1:
                potatoCounter = 0
        print 'Time\'s up! ' + str(names[potatoCounter]) + ' is out!'
        del(names[potatoCounter])
    
    print str(names[0]) + ' is the winner!'
    return names[0]