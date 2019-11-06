class HumanPlayer:
    def __init__(self, playerNum):
        self.playerNum = playerNum

    def get_move(self, board):
        movelist= board.calc_valid_moves()
        move = input("Enter column number:")
        if move in movelist:
            final = int(move)
            return final
        else:
            print("Invalid move")




