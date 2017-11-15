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
    
    Returns None. Prints '|   ' or '| x  ' or '| o ' for each element of
    board_row, if  mark = [' ', 'x', 'o']. If mark has some other values the 
    same are printed. 
    
    >>>print_ver([0,1,0], [' ', 'x', 'o'])
    |   | X |   |
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
    # If we multiply all the elements in a row, if we get 0 then atleast one
    # is empty in that row. If the multiplication is 1 (or 1 to the power of
    # board size) it means that all the elements in the row are 1. Similarly
    # if the multiplication is 8 (for board size of 3) that means that all
    # the elements in the row are 2. Anything else means that row has mixed
    # elements and thus cannot be a winning combination. Same logic can be
    # applied to columns and diagonals. 
    
    # Calculate the multiplication of all elements in rows.
    row = []
    length = len(board)
    for i in range(length):
        temp = 1
        for j in board[i]:
            temp = temp*j
        row.append(temp)

    # Calculate the multiplication of all elements in column.
    col = []
    for i in range(length):
        temp = 1
        for j in range(length):
            temp = temp*board[j][i]
        col.append(temp)

    # Calculate the multiplication of all elements in column.
    dia = []
    temp = 1
    for j in range(length):
        temp = temp * board[j][j]
    dia.append(temp)
    temp = 1
    for j in range(length):
        temp = temp * board[j][-1-j]
    dia.append(temp)        

    for temp in range(1,3):
        if temp**length in row or temp**length in col or temp**length in dia:
            return 'Player '+str(temp)+' wins.'

def get_board(board_size):
    """(int) -> list of lists of int
    
    Returns a list of lists of size board_size x board_size with each element
    as zero
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

    Returns True if and only if the the string inp matches
    the format 'int, int'
    """
    import re
    rex = re.compile('^[0-9], ?[0-9]$')
    if rex.match(inp) is not None:
        return True
    
def main():
    print('Welcome!!\n')        
    board_size = get_board_size()   # Get board size from user
    mark = get_mark()   # Get the marks to be used for game
    board = get_board(board_size) # Generate a list of list for size board
    print('At any point you can enter exit to stop the game.\n'
          'co-ordinates are to be entered as: row,column\n'
          'All the best!!')
    print_board(board, mark)
    user = 0
    while True:
        # get coordinates from user and check if the input is in the range of 
        # board
        usr_inp = input('User%s - Enter your coordinate: ' %(user+1))
        if usr_inp.lower() == 'exit':
            input('Game terminated. Press enter to exit...')
            break
        if not validate_input(usr_inp):
            print('Invalid input. Please try again.')
            continue
        
        # Extract row (i) and column (j) from user input
        usr_inp = usr_inp.split(sep = ',')
        i = int(usr_inp[0].strip()) - 1
        j = int(usr_inp[1].strip()) - 1
        
        # Make sure the input is within the range of board_size
        if i >= board_size or j >= board_size:
            print('Invalid input. Please try again.')
            continue
        
        # Make sure the element at the co-ordinate is 0 and then update it.
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
