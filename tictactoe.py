print("Welcome to Tic Tac Toe!!!")
print("Let the luck be on your side!!!")

def main():
    player = player_one("")
    board = make_board()
    while not (winner(board) or draw(board)):
        display_board(board)
        make_move(player, board)
        player = player_one(player)
    display_board(board)
    print("Thank you for playing. Hope to see you soon!!!") 

def make_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(".:.:.:.")
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print(".:.:.:.")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print(".:.:.:.")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print(".:.:.:.")
    print()
    
def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player}'s please choose your next square: "))
    board[square - 1] = player

def player_one(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
    else:
        print("Please try again!")



if __name__ == "__main__":
    main()