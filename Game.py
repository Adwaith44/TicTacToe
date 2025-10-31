"""
Tic-Tac-Toe Game - Initial Setup
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


# Test the board display
show_board()