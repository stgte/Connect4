# Connect4\
PEAS:
The performance measure is the result of the game, win, loss, or tie. The number of moves it takes to win the game doesn’t really matter, so the only thing the agent should care about is results. The environment in this case is the game board of Connect 4, a 6 x 7 board. This agent’s actuator is making a move in the game. The sensors in this situation would be the game board, the agent should know the state of the game board at all times.

EAD:
This agent’s environment would be fully observable, as the agent always knows exactly where the pieces are in the game board. This is also a multi-agent competitive environment, as there will be two agents playing against each other. This environment is deterministic, there is no element of randomness to Connect 4. This is a sequential environment, as each move affects the game board going forward, which affects what the possible moves will be in the future. There is also a static environment while deciding an action. It is also a discrete environment, as there are only ever up to 7 options for a move on a given turn. This agent also has discrete percepts, as it only needs to use its percepts and update the game board after the other agent makes a move. There is a known outcome of actions, you know what your move will do, although you do not know what move the opponent will make.



Week 1 Jobs:

Tea: Base agent

Josh: game.py file

Christian:  Human Player(), research some other methods, help out if needed

Week 2 Jobs:

Tea:AlphaBeta

Josh: Started setting up Neural Network + tests for currently existent code

Christian: Tests, research


Agent Interface: The agent has gets access to the board via get_move, the agent can see the game board, and returns the move it wants to make with get_move. Those moves are then made using the boards insert function. The agent should be returning an integer, 0-6 if using a board 7 columns wide.

Simulation Interface: If you want to observe a game, construct the game object with show_status = True, this way the game will print the board before each turn (via print_board), as well as print the winner at the end of the game. The results of many games can be expressed via compare_players.

Unit Testing FrameWork: We made our own functions to test insert as well as checkwin, for the  most part it makes more sense to test the full game manually.

Advanced AI:

Reinforcement Learning: Josh

One technique we want to apply is reinforcement learning. The idea is that we will have two agents that start with no idea how to play Connect 4 play many many games against each other, rewarding their moves when they win and punishing them when they lose. Eventually, we should have a highly effective agent, hopefully one that has solved the game. We've mainly been learning about implementation through various tech blogs.

This technique is often used for games, most of the examples I've found are for turn based games like checkers or chess, but I've also seen examples that play the game snake. Obviously if this technique is used a lot for turn based games then it should apply to Connect 4 quite well. The main challenge is probably going to be tuning the exploration rate as we go, so that the agent continues exploring new moves but also holds on to old, effective moves so it doesn't forget the progress it makes.

Primary Resources for Reinforcement Learning - https://skymind.ai/wiki/deep-reinforcement-learning, https://towardsdatascience.com/reinforcement-learning-implement-tictactoe-189582bea542


MCTS: Tea and Christian

Monte Carlo Tree Search - The idea behind this algorithm is to create a game tree, but instead of exploring all the possible games, only the most promising routes are chosen. It is a heuristic driven search algorithm that combines the classic tree search implementations alongside machine learning principles of reinforcement learning. In tree search, there’s always the possibility that the current best action is actually not the most optimal action. In such cases, MCTS algorithm becomes useful as it continues to evaluate other alternatives periodically during the learning phase by executing them, instead of the current perceived optimal strategy.

We want to implement DeepMind's AlphaZero algorithm which would potentially solve the game. It will include Monte Carlo tree search in order to perform search as well as deep convolutional residual neural network. We will try to evaluate neural network and solve the game.

Resources:
https://towardsdatascience.com/from-scratch-implementation-of-alphazero-for-connect4-f73d4554002a


Results:
Both algorithms were very succesful, but MCTS was by far more effective. Through training the reinforcement agent was able to achieve a win rate over 90% against random agents, and a winrate  of around 70% against AB depth 2.
MCTS, with a timeout of only 2 seconds, had a 92.3 winrate against AB depth 4, aand 89.7% against AB depth 8.
Anecdotally, of about a dozen games against people during our demo, MCTS won every time.

How to try it out:
To play against MCTS simply go into the testgame.py file in the MCTS folder and run a game. You can change the timeout of MCTS in the montecarlo.py file. For MCTS, due to changes that had to be made to the game board, assign the symbol as either 1 or 0. To play against the reinforcement agent, simply go into tests.py in the test folder.
 Assign a variable to ReinforcementAgent, with either "R" or "Y" as the symbol. To prevent exploratory moves during your game type yourVariable.change_exp(0) to change the exploration rate. 
 Next, load whatever policy you want with yourVariable.load_policy("policy"). (Unfortunately you cannot use our policies, as the files are too large for github) Finally, just run a game with game = Game(yourVariable, HumanPlayer("symbol"), show_status=True).
In order to train reinforcement agent use the trainAgainst function in game.connect4Game, in order to see results as your agent trains use the displayLearning function in game.test.tests.py.