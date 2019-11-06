class HumanPlayer:
    def __init__(self, playerNum):
        self.playerNum = playerNum

    def get_move(self, board):
        movelist= board.calc_valid_moves()
        move = input("Enter column number:")


        while move not in movelist:
            print("Invalid move")
            move = input("Enter column number:")
        return int(move)




