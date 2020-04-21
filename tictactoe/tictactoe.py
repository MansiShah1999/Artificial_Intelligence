"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board==initial_state():
    	return X
    x_count=o_count=0
    for row in board:
    	x_count+=row.count(X)
    	o_count+=row.count(O)

    if o_count==x_count:
    	return X
    else:
    	return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves=[]
    for i in range(3):
    	for j in range(3):
    		if board[i][j]==EMPTY:
    			moves.append([i,j])
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new=copy.deepcopy(board)
    a=action[0]
    b=action[1]
    try:
    	if new[a][b]!=EMPTY:
    		raise IndexError
    	else:
    		new[a][b]=player(new)
    		return new
    except IndexError:
    	print('Cell not EMPTY')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
    	if row.count(X)==3:
    		return X
    	if row.count(O)==3:
    		return O

    new=initial_state()

    for i in range(3):
    	for j in range(3):
    		new[i][j]=board[j][i]
    for row in new:
    	if row.count(X)==3:
    		return X
    	if row.count(O)==3:
    		return O
    	
    if board[0][0]==X and board[1][1]==X and board[2][2]==X:
    	return X
    elif board[0][0]==O and board[1][1]==O and board[2][2]==O:
    	return O
    elif board[0][2]==X and board[1][1]==X and board[2][0]==X:
    	return X
    elif board[0][2]==O and board[1][1]==O and board[2][0]==O:
    	return O
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count=0
    if winner(board)!=EMPTY:
    	return True
    for row in board:
    	count+=row.count(EMPTY)
    if count==0:
    	return True
    else:
    	return False
    
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
    	return 1
    elif winner(board)==O:
    	return -1
    else:
    	return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current=player(board)
    if current==X:
    	v=-100000
    	k=v
    	for action in actions(board):
    		v=minValue(result(board,action))
    		if v>k:
    			k=v
    			move=action
    	print(move)
    else:
    	v=k=100000
    	for action in actions(board):
    		v=maxValue(result(board,action))
    		if v<k:
    			k=v
    			move=action
    	print(move)
    return move

def  maxValue(board):
	if terminal(board):
		return utility(board)
	v=-1000000
	for action in actions(board):
		v=max(v,minValue(result(board,action)))
		#print(v)
	return v

def  minValue(board):
	if terminal(board):
		return utility(board)
	v=1000000
	for action in actions(board):
		v=min(v,maxValue(result(board,action)))
		#print(v)
	return v

