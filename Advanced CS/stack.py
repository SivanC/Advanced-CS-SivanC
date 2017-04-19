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
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self, index):
        del(self.items[index])
        
    def rid(self, element):
        for i in self.items:
            if element == self.items[i]:
                del(self.items[i])

def parChecker(aString):
    """Checks if a set of brackets is identical when reversed. Returns True or False
    """
    
    stack = []
    invertStack = []
    
    for i in range(len(aString)):
        stack.append(aString[i])
        
    for j in stack:
        tempVal = stack.pop()
        invertStack.append(tempVal)
        
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
    
    for j in range(num):
        popped = queue.dequeue()
        queue.enqueue(popped)
        print names[potatoCounter]
        potatoCounter += 1
        if potatoCounter > len(names) - 1:
            potatoCounter = 0
        
    return    