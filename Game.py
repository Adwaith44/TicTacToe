"""
Tic-Tac-Toe Game - Basic Two Player Game
"""

import random

# Set up the game board with 9 empty spaces
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# List of all 8 ways you can win tic-tac-toe
winning_combinations = [
    [0, 1, 2],  # Top row
    [3, 4, 5],  # Middle row
    [6, 7, 8],  # Bottom row
    [0, 3, 6],  # Left column
    [1, 4, 7],  # Middle column
    [2, 5, 8],  # Right column
    [0, 4, 8],  # Diagonal from top-left to bottom-right
    [2, 4, 6]   # Diagonal from top-right to bottom-left
]


def show_board():
    """Display the game board"""
    print("\n")
    print("     1     2     3")
    print("   ╔═════╦═════╦═════╗")
    print(f" 1 ║  {board[0]}  ║  {board[1]}  ║  {board[2]}  ║")
    print("   ╠═════╬═════╬═════╣")
    print(f" 2 ║  {board[3]}  ║  {board[4]}  ║  {board[5]}  ║")
    print("   ╠═════╬═════╬═════╣")
    print(f" 3 ║  {board[6]}  ║  {board[7]}  ║  {board[8]}  ║")
    print("   ╚═════╩═════╩═════╝")
    print("\n")


def check_winner():
    """Check if someone has won"""
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False


def is_board_full():
    """Check if board is full"""
    for spot in board:
        if spot == ' ':
            return False
    return True


def play_game():
    """Main game function"""
    print("\n🎮 TIC-TAC-TOE GAME 🎮")
    print("Player 1 is X, Player 2 is O\n")
    
    current_player = 'X'
    game_over = False
    
    while not game_over:
        show_board()
        
        print(f"Player {current_player}'s turn")
        
        valid_move = False
        while not valid_move:
            row = input("Choose a row (1-3): ")
            col = input("Choose a column (1-3): ")
            
            if not row.isdigit() or not col.isdigit():
                print("❌ Please enter numbers!")
                continue
            
            row = int(row)
            col = int(col)
            
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("❌ Please choose numbers between 1 and 3!")
                continue
            
            position = (row - 1) * 3 + (col - 1)
            
            if board[position] != ' ':
                print("❌ That spot is already taken!")
                continue
            
            board[position] = current_player
            valid_move = True
        
        if check_winner():
            show_board()
            print(f"🎉 Player {current_player} wins! 🎉")
            game_over = True
        elif is_board_full():
            show_board()
            print("🤝 It's a draw! 🤝")
            game_over = True
        else:
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'


# Start the game
play_game()