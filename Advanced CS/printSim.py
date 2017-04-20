import stack
import random

reload(stack)

class printTask():
    
    def __init__(self, taskCount, timestamp):
        self.taskCount = taskCount
        self.timestamp = timestamp
        self.pages = random.randint(1,20)
        
    def __repr__(self):
        return 'Task #' + str(self.taskCount) + ' at second ' + str(self.timestamp) + ' with ' + str(self.pages) + ' pages.'
        
    def getAsList(self):
        return [self.taskCount, self.timestamp, self.pages]
        
def printSim():
    
    taskDict = {}
    taskCount = 0
    printQueue = stack.Queue()
    
    for i in range(1,5401): #Every second determine if a task is created
        randInt = random.randint(1,180)
        if randInt == 180: #Approximately every two "minutes", create a new task with its place in line, number of pages, and timestamp, and add it to the print queue
            taskCount += 1
            timestamp = i
            taskDict['task' + str(timestamp)] = printTask(taskCount, timestamp) #Add this task to the dictionary with its timestamp
            printQueue.enqueue(taskDict['task' + str(timestamp)].getAsList())
            
    for j in range(60, 5460, 60):
        minute = j/60
        pageCount = 0
        for task in printQueue:
            if pageCount + task[2] <= 10:
                pageCount += task[2]
                printQueue.deleteIndex[taskCount[0] - 1]
            elif task[2] >= 10:
                task[2] -= 10