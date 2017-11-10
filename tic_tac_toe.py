# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:00:49 2017

@author: Lalit Gupta
"""

def print_hor(board_size = 3):
    """(int) -> None
    
    Returns None. Prints ' ---' times board_size.
    
    >>>print_hor(3)
     --- --- ---
     >>>print_hor(1)
      ---
    """
    print(' ---'*board_size)
    
def print_ver(board_row, mark):
    """(list, list) -> None
    
    Returns None. Prints '|   ' times element of board_row + 1. with mark placed at 
    positions. 
    
    >>>print_ver(3, 'X', 2)
    |   | X |   |
     >>>print_hor(1, 'O', 1)
    | O |
    """
    ver = ''
    for i in board_row:
        ver = ver+'| '+mark[i]+' '  
    ver = ver+'|'
    print(ver)

def print_board(board, mark):
    """(list of lists of int, list of str) -> None
    
    Returns None. Prints a board of size board_size x board_size
    
    >>>print_board(1)
     --- 
    |   |
     ---
     >>>print_board(3)
      --- --- ---
     |   |   |   |
      --- --- ---
     |   |   |   |
      --- --- ---
     |   |   |   |
      --- --- ---
    """
    for row in board:
        print_hor(len(board))
        print_ver(row, mark)
    print_hor(len(board))

def get_result(board = [[2,1,2],
     [1,2,2],
     [2,2,2]]):
    """(list of list of int) -> str
    
    Returns a string specifies which player won or if it is a tie returns none
    
    """  
    row = [] 
    for i in range(len(board)):
        temp = 1
        for j in board[i]:
            temp = temp*j
        row.append(temp)
   
    col = []
    for i in range(len(board[0])):
        temp = 1
        for j in range(len(board)):
            temp = temp*board[j][i]
        col.append(temp)
    
    dia = []
    temp = 1
    for j in range(len(board)):
        temp = temp * board[j][j]
    dia.append(temp)
    temp = 1
    for j in range(len(board)):
        temp = temp * board[j][-1-j]
    dia.append(temp)        
    
    if 1 in row or 1 in col or 1 in dia:
        return 'Player 1 wins.'
    elif 8 in row or 8 in col or 8 in dia:
        return 'Player 2 wins.'

def get_board(board_size):
    """(int) -> list of lists of int
    
    Returns a list of lists of size board_size x board_size    
    """
    return [[0 for i in range(board_size)] for j in range(board_size)]

def get_board_size():
    """() -> int
    Returns board size the user wants to play on

    """
    invalid_input = True
    while invalid_input:
        board_size = input('Please enter the board size: ')
        if board_size.isdigit():
            invalid_input = False
        else:
            print('Invalid input. Please enter a valid number.')
    return int(board_size)

def get_mark():
    """() -> list of characters

    Returns the Marks users want to play with.
    """
    mark=[]
    for i in range(3):
        if i == 0:
            input_string = 'Please enter the blank mark: '
        elif i == 1:
            input_string = 'Please enter the mark for User1: '
        else:
            input_string = 'Please enter the mark for User2: '
        while True:
            inp = input(input_string)
            if len(inp) == 1:
                mark.append(inp)
                break
            else:
                print('Invalid input. Please enter a valid number.')
    return mark

def validate_input(inp):
    """(str) -> bool

    Returns Ture if and only if the the string inp matches
    the format 'int, int'

    """
    import re
    rex = re.compile('^[0-9], ?[0-9]$')
    if rex.match(inp) is not None:
        return True
    
def main():
    print('Welcome!!\n')        
    board_size = get_board_size()
    mark = get_mark()
    board = get_board(board_size)
    print('At any point you can enter exit to stop the game.\n'
          'co-ordinates are to be entered as: 1,1\n'
          'All the best!!')
    print_board(board, mark)
    user = 0
    while True:
        # get input from user1 and check if the input is in array board
        usr_inp = input('User%s - Enter your coordinate: ' %(user+1))
        if usr_inp.lower() == 'exit':
            input('Game terminated. Press enter to exit...')
            break
        if not validate_input(usr_inp):
            print('Invalid input. Please try again')
            continue
        
        usr_inp = usr_inp.split(sep = ',')
        
        i = int(usr_inp[0]) - 1
        j = int(usr_inp[1]) - 1
        
        # make sure the element is 0 and then update it.
        if board[i][j] == 0:
            board[i][j] = user+1
            print_board(board,mark)
            user = (user+1)%2
        else:
            print('This position is already marked.'
                  ' Please enter valid coordinates.')
            continue
            
        # check if anyone won, if not then ask next user for input
        output = get_result(board)
        
        if output is None:
            # check to make sure not all elements are entered. 
            # if they are then it's a tie
            found = False
            for sublist in board:
                if 0 in sublist:
                    found = True
                    break
            if not found:
                print('This game is a tie.')
                input('Press enter to exit...')
                break
        else:
            print(output)
            input('Press enter to exit...')
            break

if __name__ == '__main__':
    main()
