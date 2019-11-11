# Connect4\
PEAS:
The performance measure is the result of the game, win, loss, or tie. The number of moves it takes to win the game doesn’t really matter, so the only thing the agent should care about is results. The environment in this case is the game board of Connect 4, a 6 x 7 board. This agent’s actuator is making a move in the game. The sensors in this situation would be the game board, the agent should know the state of the game board at all times.

EAD:
This agent’s environment would be fully observable, as the agent always knows exactly where the pieces are in the game board. This is also a multi-agent competitive environment, as there will be two agents playing against each other. This environment is deterministic, there is no element of randomness to Connect 4. This is a sequential environment, as each move affects the game board going forward, which affects what the possible moves will be in the future. There is also a static environment while deciding an action. It is also a discrete environment, as there are only ever up to 7 options for a move on a given turn. This agent also has discrete percepts, as it only needs to use its percepts and update the game board after the other agent makes a move. There is a known outcome of actions, you know what your move will do, although you do not know what move the opponent will make.



Week 1 Jobs:

Tea: Base agent

Josh: game.py file

Christian:  Human Player(), research some other methods, help out if needed


Agent Interface: The agent has gets access to the board via get_move, the agent can see the game board, and returns the move it wants to make with get_move. Those moves are then made using the boards insert function. The agent should be returning an integer, 0-6 if using a board 7 columns wide.

Simulation Interface: If you want to observe a game, construct the game object with show_status = True, this way the game will print the board before each turn (via print_board), as well as print the winner at the end of the game. The results of many games can be expressed via compare_players.

Unit Testing FrameWork: We made our own functions to test insert as well as checkwin, for the  most part it makes more sense to test the full game manually.

