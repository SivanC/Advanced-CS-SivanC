class Board:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.boardstate = [[' ' for w in range(width)] for h in range(height)]
    
    def __repr__(self):
        height = self.height
        width = self.width
        boardstate = self.boardstate
        board = ""
        for i in range(0, height):
            for j in range(0, width):
                board += "|" + boardstate[i][j]
            board += "|"
            board += '\n'
        board += '-' * (2*width + 1)
        board += "\n"
        board += " "
        for i in range(0, width):
            board += str(i % 10) + " "
        return board
        
    def addMove(self, column, checkerType):
        """ Puts a checker of the selected type in the selected column and returns the board state
        """
        height = self.height
        width = self.width
        board = self.boardstate
        
        i = height - 1
        
        if column > width or column < 0:
            return False
            
        while board[i][int(column)] != ' ' and i >= 0:
            i -= 1
            
        if i < 0:
            return False
        
        
        board[i][column] = checkerType
        
    def clear(self):
        height = self.height
        width = self.width
        board = self.boardstate
        for i in range(0, height):
            for j in range(0, width):
                board[i][j] = ' '
                
    def setMoves(self, movesString):
        checkerType = 'X'

        if type(movesString) != str:
            print 'You should input your moves as a string! (e.g. \'12314\')'
            return 

        movesStringLength = len(movesString)
        for i in range(movesStringLength):
            self.addMove(int(movesString[i]), checkerType)
            if checkerType == 'X':
                checkerType = 'O'
            elif checkerType == 'O':
                checkerType = 'X'
        
    def fill(self):
        height = self.height
        width = self.width
        movesString = ""
        
        for i in range(height):
            for j in range(width):
                movesString += str(j)
        
        self.setMoves(movesString)
        
    def checkWin(self):                                  #Still working on how i want to check for wins
        width = self.width
        height = self.height
        board = self.boardstate
        xCoords = []
        oCoords = []
        xHeights = []
        oHeights = []
        
        for i in range(height):
            for j in range(width):
                if board[i][j] == 'X':
                    xCoords += '(' + str(i) + ',' + str(j) + ')'
                elif board[i][j] == 'O':
                    oCoords += '(' + str(i) + ',' + str(j) + ')'
                    
        for i in range(len(xCoords)):
            xHeights += xCoords[i][2]
            
        return xHeights