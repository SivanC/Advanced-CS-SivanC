positives = ['good', 'fast', 'easy', 'fun']
negatives = ['bad', 'slow', 'difficult', 'boring']

def runStateMachine(inString):
    startState(inString)
    
def startState(inString):
    newString = inString.split(' ')
    if newString[0] == 'Python':
        isTransitionState(newString)
    else:
        errorTransitionState('start')
        
def isTransitionState(inString):
    if inString[1] == 'is':
        notTransitionState(inString)
    else:
        errorTransitionState('isState')

def notTransitionState(inString):
    if inString[2] == 'not':
        if inString[3] in positives:
            badTransitionState()
        elif inString[3] in negatives:
            goodTransitionState()
    elif inString[2] in positives:
        goodTransitionState()
    elif inString[2] in negatives:
        badTransitionState()
    else:
        errorTransitionState('notState')
        
def goodTransitionState():
    print 'Thanks! That\'s kind of you to say.'
    
def badTransitionState():
    print 'Hey! That\'s not very nice'
    
def errorTransitionState(state):
    print 'Sorry, you didn\'t enter a proper string! State reached: ' + state