import pdb

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
    
def isPalindrome(word):
    
    if type(word) != str:
        return
    if len(word) == 1 or len(word) == 0:
        return True
        
    if word[0] == word[-1]:
        word = word[1:len(word) - 1]
    
    isPal = isPalindrome(word)
    
    return isPal
    
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
        
    def addItem(self, item):
        item = Node(item)
        if self.isEmpty():
            self.head = item
        elif not self.isEmpty():
            item.setNext(self.head)
            self.head = item
    
    def size(self):
        currentNode = self.head
        nodeCount = 1
        while currentNode.next != None:
            currentNode = currentNode.next
            nodeCount += 1
            
        return nodeCount
        
    def search(self, value, *p):
        currentNode = self.head
        found = False

        while found == False and currentNode != None:
            previousNode = currentNode
            if currentNode.data == value:
                found = True
            if not found:
                currentNode = currentNode.next
        
        if p == ():        
            return currentNode
        else:
            return [currentNode, previousNode]
        
    def remove(self, value):
        delNode = self.search(value, 'y')[0]
        prevNode = self.search(value, 'y')[1]
        
        prevNode.next = delNode.next
        
        
        
aList = LinkedList()
aList.addItem(31)
aList.addItem(52)
aList.addItem(103)