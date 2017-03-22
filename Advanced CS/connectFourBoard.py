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
        board = self.boardstate
        
        i = height - 1
        
        while board[i][int(column)] != ' ':
            i -= 1
        
        board[i][column] = checkerType
        
    def clear(self):
        height = self.height
        width = self.width
        board = self.boardstate
        for i in range(0, height):
            for j in range(0, width):
                board[i][j] = ' '
                
    def setMoves(self, movesString):
        height = self.height
        width = self.width
        board = Board(height, width)
        checkerType = 'X'

        if type(movesString) != str:
            print 'You should input your moves as a string! (e.g. \'12314\')'
            return 
            
        movesStringLength = len(movesString)
        for i in range(movesStringLength):
            board.addMove(int(movesString[i]), checkerType)
            if checkerType == 'X':
                checkerType = 'O'
            elif checkerType == 'O':
                checkerType = 'X'
        print 'moves have been set'
        return board
        
    def fill(self):
        height = self.height
        width = self.width
        board = Board(height, width)
        movesString = ""
        
        for i in range(height):
            for j in range(width):
                movesString += str(j)
        
        board.setMoves(movesString)

        return board                      #movesString works when manually input into
                                          #setMoves, but not when used by fill()