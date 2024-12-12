from player import HumanPlayer,RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        #self.board = [[ '-' for _ in range(3)] for _ in range(3)] # we will use a array of single list to rep 3*3 board
        self.board = [ i.__str__() for i in range(9)]
        self.current_winner = None # Keep track of winner!
    def print_board_nums(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    # it is going to return a list of indices 
    def available_spaces(self):
        return [i for i in range(9) if self.board[i]!= 'X' and self.board[i]!='O']
    def empty_squares(self):
        return any(spot not in ['X', 'O'] for spot in self.board)
    def empty_squares_num(self):
        return sum(1 for i in range(9) if self.board[i] not in ['X','O'] )
            
    def winner(self, square, letter):
        #winner if 3 in a row anywhere but we have to check the possiblility for all the rows and columns . 
        row_index = square//3
        row = self.board[row_index*3: (row_index+1)*3]
        if all([spot == letter  for spot in row]):
            return True
        
        col_index = square % 3
        column = [self.board[(col_index + (i*3))] for i in range(3)]
        if all ([spot == letter for spot in column]):
            return True

        #0,2,4,6,8
        if square % 2 == 0:
            print("diagonal check ")
            diagonal1 = [0,4,8]
            diagonal2 = [2,4,6]
            if all (self.board[i] == letter for i in diagonal1):
                return True
            if all (self.board[i] == letter for i in diagonal2):
                return True
        return False
    def make_move(self,square,letter):
        if self.board[square] !='X' and self.board[square] != 'O':
            self.board[square] = letter
            if self.winner(square ,letter):
                self.current_winner = letter
            return True
        return False

def play(game : TicTacToe, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()
    letter = 'X'
    while game.empty_squares():
        if letter =='X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        if game.make_move(square,letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board_nums()
                print('')
            if game.current_winner :
                if print_game:
                    print(f"{game.current_winner} wins! ")
                break
        letter = 'O' if letter == 'X' else 'X'
    
    if not game.empty_squares() and not game.current_winner:
        if print_game:
            print("It's a tie.")

        #but wait what if anybody has won 


if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    
    game = TicTacToe()
    play(game, x_player , o_player , True)
