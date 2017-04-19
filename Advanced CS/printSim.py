from stack import Queue
import random

class printTask():
    
    def __init__(self, taskCount, timestamp):
        self.taskCount = taskCount
        self.timestamp = timestamp
        self.pages = random.randint(1,20)
        
    def __repr__(self):
        return 'Task #' + str(self.taskCount) + ' at second ' + str(self.timestamp) + ' with ' + str(self.pages) + ' pages.'
        
def printSim():
    
    taskDict = {}
    taskCount = 0
    printQueue = Queue()
    
    for i in range(5400):
        randInt = random.randint(1,180)
        if randInt == 180:
            taskCount += 1
            timestamp = i
            taskDict['task' + str(timestamp)] = printTask(taskCount, timestamp)
            printQueue.enqueue(taskDict['task' + str(timestamp)])
            
    for i in range(600, 6000, 600):
        for j in taskDict:
            if taskDict[j].timestamp <= i:
                printQueue.rid(j)