#Basic connect 4 game setup

import operator, numpy

class Connect4:

    # Constants
    ROWS = 6
    COLUMNS = 7
    DIRECTIONS = { # for convenience
        'n' :   (-1, 0),
        'ne':   (-1, 1),
        'e' :   ( 0, 1),
        'se':   ( 1, 1),
        's' :   ( 1, 0),
        'sw':   ( 1,-1),
        'w' :   ( 0,-1),
        'nw':   (-1,-1)
    }

    # Make an empty board
    board = numpy.zeros(shape=(ROWS,COLUMNS),dtype=int)

    def print_board(self):

        # Flip the board upside down, so 0,0 is bottom left instead of top left, then print each row
        for line in reversed(self.board):
            print ("|"),
            for cell in line:
                print ("X") if cell == 1 else "O" if cell else ".",
            print ("|")

    def add_disc(self, column, player):

        # Validate column and player numbers
        if not column < self.COLUMNS:
            print ("Invalid column number! Try again.")
            return False
        if player > 2:
            print ("Invalid player!")
            return False

        # Swap the dimensions to make it easier to loop through
        sBoard = numpy.swapaxes(self.board, 0, 1)

        # Put the piece in the first available spot in the specified column
        for row, cell in enumerate(sBoard[column]):
            if not cell:
                sBoard[column, row] = player
                self.board = numpy.swapaxes(sBoard,0,1)
                return True

        # If we get here, then it should be because nothing can be placed here
        return False

    # Returns the player no. if someone has won
    def check_win(self):
        # Only time multiple wins are found should be when a token is placed in a spot
        # that completes two sequences, provided this function is called after every move
        # This means it should be fine to just take the first item in the 'wins' list to
        # determine the winner
        # TODO: win message
        wins = self.check_sequence(4)
        return wins[0]['player'] if wins else None



    def get_next_in_sequence(self, sequence):
        (x, y) = tuple( map(
            operator.add,
            (sequence['row'], sequence['column']),
            tuple( map(
                operator.mul,
                (sequence['length'], sequence['length']),
                self.DIRECTIONS[sequence['direction']])
            )
        ))
        return self.board[x][y]

    def check_sequence(self, length):
        sequences = []
        for x,column in enumerate(self.board):
            for y,cell in enumerate(self.board[x]):
                if cell:
                    adjacentCells = self.get_next_values(x,y)
                    for direction,value in adjacentCells.iteritems():

                        # The function will check every spot, so no need to look upwards or backwards
                        if value and direction not in ("nw", "n", "ne", "w", "x"):

                            # Check if the same value is in the next cell, and that it's not already part of a sequence
                            # that has already been checked
                            (prevX, prevY) = tuple(map(operator.add, tuple(map(operator.mul, (-1,-1), self.DIRECTIONS[direction])), (x,y)))
                            if value == cell and self.board[prevX,prevY] != cell:
                                sLength = self.follow_sequence(x, y, direction)
                                if sLength >= length:
                                    sequences.append({"row": x, "column":y, "player": value, "direction": direction, "length": sLength})
        return sequences

    # Returns the length of sequence in the direction specified
    def follow_sequence(self, row, column, direction):
        if direction not in self.DIRECTIONS:
            print ("Invalid direction in follow_sequence")
            return False

        if not (row < self.COLUMNS and column < self.ROWS):
            print ("Invalid row/column.")
            return False

        player = self.board[row,column]
        v = player
        length = 0
        (x2, y2) = tuple(map(operator.add, (row,column), self.DIRECTIONS[direction]))
        while v == player:
            v = self.board[x2,y2]
            length += 1
            (x2, y2) = tuple(map(operator.add, (x2,y2), self.DIRECTIONS[direction]))
        return length


    # Returns a dictionary with the values of the surrounding points
    def get_next_values(self, column, row):
        if not (column < self.COLUMNS and row < self.ROWS):
            print ("Invalid row/column.")
            return False

        # Pad board with -1, so we don't get any index errors
        paddedBoard = numpy.empty((self.ROWS+2, self.COLUMNS+2), dtype=int)
        paddedBoard[:,:] = -1
        paddedBoard[1:self.ROWS+1, 1:self.COLUMNS+1] = self.board.reshape(self.ROWS, self.COLUMNS)

        # Get the surrounding cells
        return dict(zip(["nw", "n", "ne", "w", "x", "e", "sw", "s", "se"], (paddedBoard[column:column+3, row:row+3]).ravel()))
