
from game.connect4Game import Game, compare_players, trainPlayers
from game.connect4Players import *
from game.connect4Board import Board
from game.reinforcementTraining import *



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

def boardToStringTest():
    base = Board()
    player = HumanPlayer("R")
    base.insert(1, "R")
    base.insert(0, "Y")
    base.insert(1, "Y'")
    base.insert(1, "R")
    list = board_to_string(base, player)
    print(len(list))
    print(list)

def improvement_demo():
    # compare_players(AlphaBetaPlayer("R", 2), AlphaBetaPlayer("Y", 2), 10)
    # compare_players(AlphaBetaPlayer("R", 2), AlphaBetaPlayer("Y", 4), 10)
    # compare_players(AlphaBetaPlayer("R", 2), AlphaBetaPlayer("Y", 6), 10)
    # compare_players(AlphaBetaPlayer("R", 2), AlphaBetaPlayer("Y", 8), 10)
    #compare_players(AlphaBetaPlayer("R", 2), AlphaBetaPlayer("Y", 10), 10)
    # game = Game(RandomComputerPlayer("R"), AlphaBetaPlayer("Y", 8), show_status=True)
    # game = Game(AlphaBetaPlayer("R", 8), MinimaxPlayer("Y"), show_status=True)
    game = Game(AlphaBetaPlayer("R", 8), HumanPlayer("Y"), show_status=True)

def reinforcement_round(trainerOne, trainerTwo, randomTester, numTrained, numDisplayed, roundComplete):
    trainPlayers(trainerOne, trainerTwo, numTrained)
    print(str((roundComplete + 1) * numTrained) +' games trained')
    compare_players(trainerOne, randomTester, numDisplayed)



#Results should get better each time
def reinforcement_demo():
    trainerOne = ReinforcementAgent("R", lr = .85)
    trainerTwo = ReinforcementAgent("Y")
    randomTester = RandomComputerPlayer("Y")
    print('0 games trained')
    compare_players(trainerOne, randomTester, 100)
    for i in range(20):
        reinforcement_round(trainerOne, trainerTwo, randomTester, 1000, 100, i)


    print("Complete")

def reinforcement_testing():
    trainerOne= ReinforcementAgent("R")
    opp = ReinforcementAgent("Y")
    trainPlayers(trainerOne, opp, 10)
    print(trainerOne.states)
    print(trainerOne.state_vals)
    #Saving states, issue is probably that states from each game carry over, which probably messes up learning
    #States getting carried over fixed, appears to be some change to state_vals but still no meaningful learning




def main():
    reinforcement_demo()




if __name__ == '__main__':
     main()

