import random  # Used for the computer's random moves

# Set up the game board with 9 empty spaces
# The board positions are numbered 0-8 like this:
#  0 | 1 | 2
#  ---------
#  3 | 4 | 5
#  ---------
#  6 | 7 | 8
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# List of all 8 ways you can win tic-tac-toe
# Each inner list shows 3 positions that make a winning line
winning_combinations = [
    [0, 1, 2],  # Top row
    [3, 4, 5],  # Middle row
    [6, 7, 8],  # Bottom row
    [0, 3, 6],  # Left column
    [1, 4, 7],  # Middle column
    [2, 5, 8],  # Right column
    [0, 4, 8],  # Diagonal from top-left to bottom-right
    [2, 4, 6]  # Diagonal from top-right to bottom-left
]

# Leaderboard dictionary to track wins for each player
# Keys are player names (in lowercase), values are win counts
leaderboard = {}


def show_board():
    """Display the game board in a nice format with row and column numbers"""

    print("\n")  # Add blank line for spacing
    print("     1     2     3")  # Show column numbers at the top

    # Print the board using box-drawing characters to make it look nice
    print("   ╔═════╦═════╦═════╗")
    print(f" 1 ║  {board[0]}  ║  {board[1]}  ║  {board[2]}  ║")
    print("   ╠═════╬═════╬═════╣")
    print(f" 2 ║  {board[3]}  ║  {board[4]}  ║  {board[5]}  ║")
    print("   ╠═════╬═════╬═════╣")
    print(f" 3 ║  {board[6]}  ║  {board[7]}  ║  {board[8]}  ║")
    print("   ╚═════╩═════╩═════╝")
    print("\n")  # Add blank line for spacing


def check_winner():
    """
    Check if someone has won the game
    Goes through all winning combinations to see if any player got 3 in a row
    Returns True if there's a winner, False if not
    """

    # Loop through each possible winning combination
    for combo in winning_combinations:
        # Check if all 3 positions in this combination match AND aren't empty
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True  # Found a winner!

    return False  # No winner found


def is_board_full():
    """
    Check if all spaces on the board are filled
    This is used to detect a draw
    Returns True if board is full, False if there are empty spaces
    """

    # Go through each spot on the board
    for spot in board:
        if spot == ' ':  # If I find an empty space
            return False  # Board isn't full yet

    return True  # No empty spaces found - board is full


def get_empty_positions():
    """
    Get a list of all empty positions on the board
    Used by the computer to know where it can place its mark
    Returns a list of position numbers that are empty
    """

    empty_spots = []  # Create an empty list to store positions

    # Check each position on the board
    for i in range(9):
        if board[i] == ' ':  # If this position is empty
            empty_spots.append(i)  # Add it to the list

    return empty_spots


def computer_move():
    """
    Make the computer choose a random empty position
    The computer (playing as O) picks a random available spot
    """

    # Get all the positions that are still empty
    available_positions = get_empty_positions()

    # Pick a random position from the available ones
    position = random.choice(available_positions)

    # Place the computer's mark (O) on the board
    board[position] = 'O'

    # Work out which row and column this was (for display purposes)
    row = (position // 3) + 1  # Get row
    col = (position % 3) + 1  #  Get column

    print(f"🤖 Computer chose row {row}, column {col}")


def add_win(player_name):
    """
    Add a win to the leaderboard for the given player
    If player doesn't exist, create them with 1 win
    If player exists, add 1 to their win count
    """

    # Convert name to lowercase for consistency
    player_name = player_name.lower()

    # Check if this player is already in the leaderboard
    if player_name in leaderboard:
        leaderboard[player_name] += 1  # Add 1 to their existing wins
    else:
        leaderboard[player_name] = 1  # Create new entry with 1 win


def show_leaderboard():
    """Display the current leaderboard sorted by wins (highest first)"""

    print("\n" + "=" * 40)
    print("           📊 LEADERBOARD 📊")
    print("=" * 40)

    # Check if leaderboard is empty
    if len(leaderboard) == 0:
        print("  No games played yet!")
    else:
        # Sort the leaderboard by wins (highest to lowest)
        # Create a list of tuples (name, wins) sorted by wins
        sorted_players = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

        # Display each player and their win count
        for name, wins in sorted_players:
            print(f"  {name.capitalize()}: {wins} wins")

    print("=" * 40 + "\n")


def reset_board():
    """Clear the board for a new game"""

    # Reset all positions to empty spaces
    for i in range(9):
        board[i] = ' '


def show_menu():
    """Display the main menu and get user's choice"""

    print("\n" + "=" * 40)
    print("     🎮 TIC-TAC-TOE GAME 🎮")
    print("=" * 40)
    print("\n  MAIN MENU:")
    print("  1 - Play Game")
    print("  2 - View Leaderboard")
    print("  3 - Quit")
    print("=" * 40)

    # Get menu choice and validate it
    while True:
        choice = input("\nEnter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            return choice  # Return valid choice
        print("❌ Please enter 1, 2, or 3")


def play_game():
    """
    Main function that runs the whole game
    Handles the game mode selection, game loop, and checking for wins/draws
    """

    # Ask player to choose game mode
    print("\n" + "=" * 40)
    print("Choose game mode:")
    print("1 - One player (vs Computer)")
    print("2 - Two players (vs Friend)")
    print("=" * 40)

    # Get game mode choice and validate it
    while True:
        mode = input("\nEnter 1 or 2: ")
        if mode == '1' or mode == '2':
            break  # Valid choice, exit loop
        print("❌ Please enter 1 or 2")

    # Get player names based on game mode
    if mode == '1':
        # Single player mode
        player1_name = input("\nEnter your name: ")
        player2_name = "computer"  # Computer is always player 2
        print(f"\n✓ One player mode - {player1_name} is X, Computer is O")
        is_single_player = True
    else:
        # Two player mode
        player1_name = input("\nEnter Player 1 name: ")
        player2_name = input("Enter Player 2 name: ")
        print(f"\n✓ Two player mode - {player1_name} is X, {player2_name} is O")
        is_single_player = False

    input("Press ENTER to start playing... ")
    print("\n")

    # Set starting variables for the game
    current_player = 'X'  # X always goes first
    game_over = False  # Flag to control when the game ends

    # Main game loop - keeps running until someone wins or it's a draw
    while not game_over:

        # Show the current state of the board
        show_board()

        # Check if it's the computer's turn (in single player mode)
        if is_single_player and current_player == 'O':
            print("Computer's turn...")
            computer_move()  # Computer makes its move

        else:
            # Human player's turn - keep asking until valid move
            valid_move = False

            while not valid_move:
                # Tell the player whose turn it is
                if current_player == 'X':
                    print(f"{player1_name}'s turn (X)")
                else:
                    print(f"{player2_name}'s turn (O)")

                # Get the player's move - ask for row and column
                row = input("Choose a row (1-3): ")
                col = input("Choose a column (1-3): ")

                # Validate input - check if they entered numbers
                if not row.isdigit() or not col.isdigit():
                    print("❌ Please enter numbers!")
                    continue  # Ask again

                # Convert the input strings to integers
                row = int(row)
                col = int(col)

                # Check if the numbers are in the valid range (1-3)
                if row < 1 or row > 3 or col < 1 or col > 3:
                    print("❌ Please choose numbers between 1 and 3!")
                    continue  # Ask again

                # Convert row and column to board position (0-8)
                # Formula: (row - 1) * 3 + (col - 1)
                # Subtract 1 because lists start at 0, not 1
                position = (row - 1) * 3 + (col - 1)

                # Check if the chosen position is already taken
                if board[position] != ' ':
                    print("❌ That spot is already taken!")
                    continue  # Ask again

                # Valid move - place the mark and exit the input loop
                board[position] = current_player
                valid_move = True

        # Check if the current player won after this move
        if check_winner():
            show_board()  # Display the final board

            # Work out who won and update leaderboard
            if current_player == 'X':
                winner_name = player1_name
            else:
                winner_name = player2_name

            # Display winning message
            print(f"🎉 {winner_name} wins! 🎉")

            # Add win to leaderboard
            add_win(winner_name)

            game_over = True  # Set flag to end the game loop

        # Check if the board is full with no winner (draw)
        elif is_board_full():
            show_board()  # Display the final board
            print("🤝 It's a draw! 🤝")
            game_over = True  # Set flag to end the game loop

        # Game continues - switch to the other player
        else:
            # Use if/else to swap between X and O
            if current_player == 'X':
                current_player = 'O'  # Switch from X to O
            else:
                current_player = 'X'  # Switch from O to X


def main():
    """Main programme loop that shows menu and handles user choices"""

    # Keep showing menu until user chooses to quit
    while True:
        choice = show_menu()  # Display menu choices

        if choice == '1':
            # Play a game
            reset_board()  # Clear the board for a new game
            play_game()
            input("\nPress ENTER to return to menu...")

        elif choice == '2':
            # Show leaderboard
            show_leaderboard()
            input("Press ENTER to return to menu...")

        elif choice == '3':
            # Quit the programme
            print("\nThanks for playing! 👋\n")
            break  # Exit the game


# Starts the game and shows the menu
main()