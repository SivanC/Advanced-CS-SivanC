import stack
import random

class printTask():
    
    def __init__(self, taskCount, timestamp):
        self.taskCount = taskCount
        self.timestamp = timestamp
        self.pages = random.randint(1,20)
        self.timeWaited = 0
        
    def __repr__(self):
        return 'Task #' + str(self.taskCount) + ' at second ' + str(self.timestamp) + ' with ' + str(self.pages) + ' pages, completed after ' + str(self.timeWaited) + ' seconds.'
        
    def getAsList(self):
        return [self.taskCount, self.timestamp, self.pages, self.timeWaited]
        
def printSim(pagePerMin):
    
    taskDict = {}
    taskCount = 0
    printQueue = stack.Queue()
    
    for i in range(1,7201): #Every second determine if a task is created
        randInt = random.randint(1,180)
        if randInt == 180: #Approximately every two "minutes", create a new task with its place in line, number of pages, and timestamp, and add it to the print queue
            taskCount += 1
            timestamp = i
            taskDict['task' + str(timestamp)] = printTask(taskCount, timestamp) #Add this task to the dictionary with its timestamp
            printQueue.enqueue(taskDict['task' + str(timestamp)].getAsList())
          
    for seconds in range(60,7260,60): #Every minute:
        if len(printQueue.items) != 0: #Stop if our queue is empty
            task = printQueue[0] #Look at the first item in the queue
            pageCount = 0
            if task[1] <= seconds: #If the task has been created already:
                if pageCount + task[2] <= pagePerMin: #If it doesn't cause us to go over out page limit add the pages and dequeue the item
                    taskDict['task' + str(task[1])].timeWaited = task[3]
                    printQueue.dequeue(0)
                elif task[2] > pagePerMin: #If the item is more than ten pages do the first ten pages and advance one minute
                    task[2] -= pagePerMin
                    task[3] += 60
                else: #If the item is not more than ten pages but would exceed our current page count, complete pages until we have ten this minute and advance a minute
                    task[2] = (pageCount + task[2]) - pagePerMin
                    task[3] += 60
    
    avgWait = 0 #Calculate that average wait time for an order and return it
    for j in taskDict:
        avgWait += taskDict[j].timeWaited
    avgWait /= len(taskDict)
    
    #Creating a string with relevant information
    returnString = 'Average wait: ' + str(avgWait) + ' seconds\nTotal number of tasks: ' + str(len(taskDict)) + ' tasks' \
    + '\nNumber of unfinished tasks: ' + str(len(printQueue.items)) + ' tasks'
    
    print returnString