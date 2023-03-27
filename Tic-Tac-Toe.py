import math

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
    def is_board_full(board):
    
        for cell in board.values():
            if cell == " ":
                return False

        return True

    @staticmethod
    def make_human_move(board, pos, token):
        move_successful = True
        if board[pos] == " ":
            board[pos] = token
        else:
            print("Space is already occupied.")
            move_successful = False
        return board, move_successful

    @staticmethod
    def evaluate(board):

        for i in range(1, 8, 3): #1, 4, 7

            if ((board [i] != " ") and (board [i] == board [i+1] == board [i+2])):
                if board[i] == "O":
                    return 10
                elif board[i] == "X":
                    return -10

        for i in range(1, 4):
            if ((board [i] != " ") and (board[i] == board [i+3] == board [i+6])):
                if board[i] == "O":
                    return 10
                elif board[i] == "X":
                    return -10

        if (((board [5] != " ") and (board[1] == board [5] == board [9])) or
        ((board[3] == board [5] == board [7]))):
            if board[5] == "O":
                return 10
            elif board[5] == "X":
                return -10 

        return 0

def switch_player(token):
    if token == "O":
        token = "X"
    else:
        token = "O"

    return token

def MiniMax(board, maximisingPlayer):

    player = "O"
    opponent = "X"

    # if node is a terminal node then return value of board
    score = TicTacToe.evaluate(board)
    if  score == 10:
        return 10 

    if score == -10:
        return -10 

    if TicTacToe.is_board_full(board):
        return 0
    
    if maximisingPlayer:
        max_value = -math.inf
        for i in board:
            if board[i] == " ":
                child = board.copy()
                child[i] = player
                max_value = max(max_value, MiniMax(child, False))
        return max_value

    else:
        min_value = math.inf
        for i in board:
            if board[i] == " ":
                child = board.copy()
                child[i] = opponent
                min_value = min(min_value, MiniMax(child, True))
        return min_value


def find_best_move(board):
    bestVal = -math.inf 
    bestMove = -1
    
    for x in range(1, 10):
        if board[x] == " ":
            board[x] = "O"
            value = MiniMax(board, False)
            #print("Val: " +str(value) )
            board[x] = " "
            if value > bestVal:
                bestVal = value
                bestMove = x

    return bestMove

def main():
    
    print("\n" +"Welcome to Tic-Tac-Toe!" +"\n")
    board = TicTacToe.create_board()
    TicTacToe.print_board(board)
    token = "X"

    while True:
        if not TicTacToe.is_board_full(board):

            print("Player {}'s turn.".format(token))

            if token == 'X':
                position = int(input("Enter a number from 1 to 9 to make your move: "))
                board, move_successful = TicTacToe.make_human_move(board, position, token)
            else:
                position = find_best_move(board)
                board[position] = token

            TicTacToe.print_board(board)
            score = TicTacToe.evaluate(board)
            #print("Score" + str(score))

            if (score > 0 or score < 0):
                print("Player {} has won the game!".format(token))
                break

            if move_successful:
                token = switch_player(token)

        else:
            print("Game ends in a tie")
            break

    restart = input("Play again(y/n)? ")

    if restart == 'y':
        main()

main()
