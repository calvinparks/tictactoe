"""
Tic Tac Toe Player
"""
import copy
import math

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
    This function is called by runner.py
    """
 
    X_count = 0
    O_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                X_count +=1    
            if board[i][j] == O:
                O_count +=1   
    
    if X_count > O_count:
        return O
    if X_count < O_count:
        return X
    if O_count == X_count:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set= set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i,j))
    return actions_set    
             

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    This function is called by runner.py
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception

    tmp_board = copy.deepcopy(board)
    x_count = 0
    O_count = 0
    next_player = EMPTY
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count +=1    
            if board[i][j] == O:
                O_count +=1   
    
    if x_count > O_count:
        next_player = O
    else:
        next_player = X

    tmp_board[action[0]][action[1]] = next_player

    return tmp_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    This function is called by runner.py
    """
    return identify_winner(board)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    This function is called by runner.py
    """

    if not board_has_empty_position(board) or identify_winner(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    the_winner = identify_winner(board)
    if the_winner == X:
        return 1
    if the_winner == O:
        return -1

    return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    This function is called by runner.py
    """
    
    def inner_mini_max(board, alpha, beta, maximize_player):
        if terminal(board):
            return utility(board)

        if maximize_player:
            evaluated_maximun_value = -math.inf
            for distinct_action in actions(board):
                tmp_value = inner_mini_max(board_result_for_specific_player(board, distinct_action, True), alpha, beta, False)
                evaluated_maximun_value = max(evaluated_maximun_value, tmp_value)
                alpha = max(alpha, evaluated_maximun_value)
                if beta <= alpha:
                    break
            return evaluated_maximun_value
        else:
            evaluated_minimun_value = math.inf
            for distinct_action in actions(board):
                tmp_value = inner_mini_max(board_result_for_specific_player(board, distinct_action, False), alpha, beta, True)
                evaluated_minimun_value = min(evaluated_minimun_value, tmp_value)
                beta = min(beta, evaluated_minimun_value)
                if beta <= alpha:
                    break
            return evaluated_minimun_value

    
    if  player(board) == X:
         maximize_player = True
    else:
         maximize_player = False
    
    if maximize_player:
        evaluated_maximun_value = -math.inf
        for distinct_action in actions(board):
                tmp_value = inner_mini_max(board_result_for_specific_player(board, distinct_action, True),-math.inf, math.inf, False)
                if tmp_value > evaluated_maximun_value:
                    evaluated_maximun_value = tmp_value
                    chosen_move = distinct_action
    else:
        evaluated_maximun_value = math.inf
        for distinct_action in actions(board):
                tmp_value = inner_mini_max(board_result_for_specific_player(board, distinct_action, False),-math.inf, math.inf, True)
                if tmp_value < evaluated_maximun_value:
                    evaluated_maximun_value = tmp_value
                    chosen_move = distinct_action
    return chosen_move

   
    

    

def identify_winner(board):
    """
    Deterimine which specifc player won the game
    """
    
    # check the columns for a winner
    if board[0][0] == board[1][0] == board[2][0] == X:
        return X

    if board[0][0] == board[1][0] == board[2][0] == O:
        return O     

    if board[0][1] == board[1][1] == board[2][1] == X:
        return X

    if board[0][1] == board[1][1] == board[2][1] == O:
        return O
 

    if board[0][2] == board[1][2] == board[2][2] == X:
       return X

    if board[0][2] == board[1][2] == board[2][2] == O:
        return O


    # check the rows for a winner 
    
    if board[0][0] == board[0][1] == board[0][2] == X:
        return X

    if board[0][0] == board[0][1] == board[0][2] == O:
        return O  

    if board[1][0] == board[1][1] == board[1][2] == X:
        return X

    if board[1][0] == board[1][1] == board[1][2] == O:
        return O 

    if board[2][0] == board[2][1] == board[2][2] == X:
        return X

    if board[2][0] == board[2][1] == board[2][2] == O:
        return O 


    # check the left leaning diagnol for a winner
    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
        return winner

    # check the right leaning diagnol for a winner
    if board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]
        return winner

    return None


def board_has_empty_position(board):
    """
    Figure out are there any available postions left on the board
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return True
    return False

def board_result_for_specific_player(board, action, max_player):
    """
    Returns the board that results from making move (i, j) on the board.
    This function is called by runner.py
    """

    if board[action[0]][action[1]] != EMPTY:
        raise Exception

    tmp_board = copy.deepcopy(board)
    x_count = 0
    O_count = 0
    next_player = EMPTY  
    
    if max_player:
        tmp_board[action[0]][action[1]] = X
    else:
        tmp_board[action[0]][action[1]] = O

    return tmp_board

