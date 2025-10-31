"""
Tic-Tac-Toe Game - With Menu and Leaderboard
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

# Leaderboard dictionary
leaderboard = {}


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


def get_empty_positions():
    """Get list of empty positions"""
    empty_spots = []
    for i in range(9):
        if board[i] == ' ':
            empty_spots.append(i)
    return empty_spots


def computer_move():
    """Computer makes a random move"""
    available_positions = get_empty_positions()
    position = random.choice(available_positions)
    board[position] = 'O'
    row = (position // 3) + 1
    col = (position % 3) + 1
    print(f"🤖 Computer chose row {row}, column {col}")


def add_win(player_name):
    """Add win to leaderboard"""
    player_name = player_name.lower()
    if player_name in leaderboard:
        leaderboard[player_name] += 1
    else:
        leaderboard[player_name] = 1


def show_leaderboard():
    """Display leaderboard"""
    print("\n" + "=" * 40)
    print("           📊 LEADERBOARD 📊")
    print("=" * 40)
    
    if len(leaderboard) == 0:
        print("  No games played yet!")
    else:
        sorted_players = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        for name, wins in sorted_players:
            print(f"  {name.capitalize()}: {wins} wins")
    
    print("=" * 40 + "\n")


def reset_board():
    """Clear the board"""
    for i in range(9):
        board[i] = ' '


def show_menu():
    """Display main menu"""
    print("\n" + "=" * 40)
    print("     🎮 TIC-TAC-TOE GAME 🎮")
    print("=" * 40)
    print("\n  MAIN MENU:")
    print("  1 - Play Game")
    print("  2 - View Leaderboard")
    print("  3 - Quit")
    print("=" * 40)
    
    while True:
        choice = input("\nEnter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            return choice
        print("❌ Please enter 1, 2, or 3")


def play_game():
    """Main game function"""
    print("\n" + "=" * 40)
    print("Choose game mode:")
    print("1 - One player (vs Computer)")
    print("2 - Two players (vs Friend)")
    print("=" * 40)
    
    while True:
        mode = input("\nEnter 1 or 2: ")
        if mode == '1' or mode == '2':
            break
        print("❌ Please enter 1 or 2")
    
    if mode == '1':
        player1_name = input("\nEnter your name: ")
        player2_name = "computer"
        print(f"\n✓ One player mode - {player1_name} is X, Computer is O")
        is_single_player = True
    else:
        player1_name = input("\nEnter Player 1 name: ")
        player2_name = input("Enter Player 2 name: ")
        print(f"\n✓ Two player mode - {player1_name} is X, {player2_name} is O")
        is_single_player = False
    
    input("Press ENTER to start playing... ")
    print("\n")
    
    current_player = 'X'
    game_over = False
    
    while not game_over:
        show_board()
        
        if is_single_player and current_player == 'O':
            print("Computer's turn...")
            computer_move()
        else:
            valid_move = False
            while not valid_move:
                if current_player == 'X':
                    print(f"{player1_name}'s turn (X)")
                else:
                    print(f"{player2_name}'s turn (O)")
                
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
            if current_player == 'X':
                winner_name = player1_name
            else:
                winner_name = player2_name
            print(f"🎉 {winner_name} wins! 🎉")
            add_win(winner_name)
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


def main():
    """Main programme loop"""
    while True:
        choice = show_menu()
        
        if choice == '1':
            reset_board()
            play_game()
            input("\nPress ENTER to return to menu...")
        elif choice == '2':
            show_leaderboard()
            input("Press ENTER to return to menu...")
        elif choice == '3':
            print("\nThanks for playing! 👋\n")
            break


# Start the game
main()