class TicTacToe:
    
    @staticmethod
    def create_board():
        board = {}
        for x in  range (1, 10):
            board.update({x : " "})

        return board

    @staticmethod
    def print_board(board):

        print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |")
        print("-------------")
        print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |")
        print("-------------")
        print("| " + board[7] + " | " + board[8] + " | " + board[9] + " |")

    @staticmethod
    def check_winner (board):
        winner = False
        if (((board [1] != " ") and (board [1] == board [2] == board [3])) or
        ((board [4] != " ") and (board[4] == board [5] == board [6])) or 
        ((board [7] != " ") and (board[7] == board [8] == board [9])) or
        ((board [1] != " ") and (board[1] == board [4] == board [7])) or
        ((board [2] != " ") and (board[2] == board [5] == board [8])) or 
        ((board [3] != " ") and (board[3] == board [6] == board [9])) or
        ((board [1] != " ") and (board[1] == board [5] == board [9])) or 
        ((board [3] != " ") and (board[3] == board [5] == board [7]))):
            winner = True

        return winner

    @staticmethod 
    def is_board_full(board):
    
        for cell in board.values():
            if cell == " ":
                return False

        return True

    @staticmethod
    def make_move(board, pos, token):
        move_successful = True
        if board[pos] == " ":
            board[pos] = token
        else:
            print("Space is already occupied.")
            move_successful = False
        return board, move_successful

def switch_player(token):
    if token == "O":
        token = "X"
    else:
        token = "O"

    return token

def MiniMax(board):

def main():
    
    print("\n" +"Welcome to Tic-Tac-Toe!" +"\n")
    board = TicTacToe.create_board()
    TicTacToe.print_board(board)
    token = "O"

    while True:
        if not TicTacToe.is_board_full(board):

            print("Player {}'s turn.".format(token))
            position = int(input("Enter a number from 1 to 9 to make your move: "))

            if token == 'O':
                board, move_successful = TicTacToe.make_move(board, position, token)
            else:
                MiniMax(board)

            TicTacToe.print_board(board)
            winner = TicTacToe.check_winner(board)

            if winner:
                print("Player {} has won the game!".format(token))
                break

            if move_successful:
                token = switch_player(token)

        else:
            print("Game ends in a tie")
            break

    restart = input("Play again(y/n)? ")

    if restart == "y" or "Y":
        main()

main()
