
from game.connect4Game import Game
from game.connect4Players import *
from game.connect4Board import Board



def CheckWinTest():
    game = Game(TestAgent0("R"), RandomComputerPlayer("Y"), show_status=True)
    return

def insertTest():
    testBoard = Board()
    try:
        print("Regular insert, shouldn't get an exception")
        testBoard.insert(1, "R")
    except Exception as exc:
        print("Exception Raised: ", exc)
    try:
        print("Negative insert, should get an exception")
        testBoard.insert(-1, "Y")
    except Exception as exc:
        print("Exception Raised: ", exc)
    try:
        print("Too large insert, shoould get an exception")
        testBoard.insert(9, "R")
    except Exception as exc:
        print("Exception Raised: ", exc)
    try:
        print("Wrong data type, should get an exception")
        testBoard.insert(str(1), "R")
    except Exception as exc:
        print("Exception Raised: ", exc)

    return


def main():
    insertTest()




if __name__ == '__main__':
     main()

