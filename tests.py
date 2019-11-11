from game.game import Game
from game.connect4Players import *



def CheckWinTest():
    game = Game(TestAgent0("R"), RandomComputerPlayer("Y"), show_status=True)
    return

def main():
    CheckWinTest()



if __name__ == '__main__':
     main()

