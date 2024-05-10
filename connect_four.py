no_winner = True



def print_board(board):
    """
    board = [
        ['-', '-'. '-'],
        ['-', '-', '-']
        ['-', '-', '-']
    ]
    :return: None
    :print
    - - -
    - - -
    - - -
    """
    for row in board:
        for element in row:
            print(element, end=" ")
        print()


def initialize_board(num_rows, num_cols):
    """ return: board = [
        ['-', '-'. '-'],
        ['-', '-', '-']
        ['-', '-', '-']
    ]
        """
    board = [
        ['-' for i in range(num_cols)]
        for j in range(num_rows)
    ]
    return board


def insert_chip(board, col, chip_type):
    turn = 0
    """ checks whether the element at the specified row and column is equal to -. """
    """ if it is true than the space is available, if it is not true than the 
        space is not available. """
    """ initializes & declares the variable num_rows since it is not a global 
        variable so that it is within the scope of the insert_chip function"""
    for i in reversed(range(len(board))):
        if board[i][col] == '-':
            board[i][col] = chip_type
            return i
    return -1

def check_if_winner(board, col, row, chip_type):

    """ finds the number of columns in the array - len(board[0])"""
    """ checks to see if there is a winner in the horizontal direction(rows)."""
    count = 0
    """ initializes & declares count to the value zero"""
    for i in range(len(board[0])):
        if board[row][i] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    """checks to see if there is a winner in the vertical direction(columns)."""
    count = 0
    for j in range(len(board)):
        if board[j][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    return False


def main():
    turn = 0
    """ asks for and accepts an integer input from the user that
    dictates the number of rows on the board """
    num_rows = int(input("What would you like the height of the board to be?"))
    """ asks for and accepts an integer input from the user that 
        dictates the number of columns on the board """
    num_cols = int(input("What would you like the length of the board to be?"))
    """ initializes the board to a function call of initialize board where the 
        number of columns and number of rows that the user indicated that 
        they wanted the board to have is used. """
    board = initialize_board(num_rows, num_cols)
    """ prints the initialized board. """
    print_board(board)
    """ tells the users what their chip type will be"""
    print("Player 1: x")
    print("Player 2: o")

    """ Uses boolean logic to continue to asking the players to insert chips if there is no winner"""
    while no_winner:
        """ if else statement that prompts player one to enter their chip if the turn number is even
        otherwise, asks player two to enter their chip if the turn number is odd."""
        if turn % 2 == 0:
            """ asks the user at which column in the board would they like to place their chip."""
            col = int(input("Player 1: Which column would you like to choose?"))
            """ calls the insert_chip function to check if there is a chip inserted into the 
            board at a position"""
            chip_type = 'x'
            """ inserts the chip into the chosen column"""
            row = insert_chip(board, col, chip_type)
            print()
            """ prints the board after the chip is inserted into the spot that the player 
                        has indicated in the insert_chip method"""
            print_board(board)
            if check_if_winner(board, col, row, chip_type):
                print("Player 1 won the game!")
                return
            else:
                turn += 1


        else:
            """ asks the user at which column in the board would they like to place their chip."""
            col = int(input("Player 2: Which column would you like to choose?"))
            """ calls the insert_chip function to check if there is a chip inserted into the 
            board at a position"""
            chip_type = 'o'
            """ inserts the chip into the chosen column"""
            row = insert_chip(board, col, chip_type)
            print()
            """ prints the board after the chip is inserted into the spot that the player 
                        has indicated in the insert_chip method"""

            print_board(board)

            if check_if_winner(board, col, row, chip_type):
                print("Player 2 won the game!")
                return
            else:
                turn += 1

            if turn == num_rows * num_cols:
                print("Draw. Nobody wins.")
                return


if __name__ == '__main__':
    main()
