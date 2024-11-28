def player_input(board, marker):
    while True: 
        try:
            printBoard(board)
            row_position = int(input(f"Please enter the row position (0-2) for {marker}: "))
            column_position = int(input(f"Please enter the column position (0-2) for {marker}: "))
            # if no empty positin : 
                # then it should mention that the game is draw . 
            # how to check whether the position is going to be empty or not . 


            if(row_position >=0 and row_position <3):
                if(column_position >= 0 and column_position < 3):
                    if(board[row_position][column_position] == '-'):
                        board[row_position][column_position] = marker
                        break
                    else: 
                        print("Position is already occupied.Please try again.")
                else:
                    print("Column out of range . Please try again .")
            else:
                print("Row out of range. Please try again.")
        except ValueError:
                print("Invalid input, please enter a number")
    return board

def endGame(board): 
    result =0
    for i in range(3):
        for j in range(3):
            if(board[i][j]=='-'):
                result = 1
                break
    if result == 0:
        print("The game is draw")
        return False
    return True

def printBoard(board):
    for i in range(3):
        for j in range(3):
            if (j == 2):
                print(board[i][j], end=" ")
            else:    
                print(board[i][j], end=" | ")
        if(i ==2):
            print()
        else:
            print("\n-- --- --")   
def checkWinnerRow(board, marker):
    for i in range(3):
        counter = 0
        for j in range(3):
            if (board[i][j] != marker):
                break
            else:
                counter +=1
                if (counter == 3):
                    return True
    return False

def checkWinnerColumn(board, marker):
    for j in range(3):
        counter = 0
        for i in range(3):
            if (board[i][j] != marker):
                break
            else:
                counter+=1
                if (counter == 3):
                    return True
    return False


def checkWinnerDiagonalFirst(board, marker):
    counter = 0
    for i in range(3):
        if (board[i][i] != marker):
            break
        else:
            counter+=1
            if (counter == 3):
                return True
    return False        


def checkWinnerDiagonalSecond(board, marker):
    counter = 0
    for i in range(3):
        if (board[i][2-i] != marker):
            break
        else:
            counter+=1
            if (counter == 3):
                return True
    return False      
#main function is defined below 

def main():
    #game on variable is set to True
    game_on = True
    #formation of board
    board = [[ '-' for _ in range(3)] for _ in range(3)]
    playerTurn = 0
    playerOneMarker = 'X'
    playerTwoMarker = 'O'

    while game_on:
        if (playerTurn %2 == 0):
            marker = playerOneMarker
        else:
            marker = playerTwoMarker
        playerTurn+=1

        board = player_input(board,marker)
        game_on = endGame(board)
        if(checkWinnerRow(board,marker) or checkWinnerColumn(board,marker)or checkWinnerDiagonalFirst(board,marker)or checkWinnerDiagonalSecond(board, marker)):
            print(f"Congratulaitons! {marker} on winning.")
            game_on = False
        

main()