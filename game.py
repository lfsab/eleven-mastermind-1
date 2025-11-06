# Game Proper
# Mastermind

# Game safeguard: avoid bypass of user login & registration
# Utilize player_id
# ie def game(player_id)
# exit if player_id = null
# then check player_id exists on player.txt

# Generate the secret key
import secret

# Generate the UI for the game board
import spacing

# Use score.py to retrieve score and manage highscores.txt
import score

# Import os for file and console manipulation
import os
import time # for time delays

def start_game(player_id):
    # Check if user has valid login
    if not player_id:
        print("Error: Invalid player ID. Please login or register.")
        return
    
    # Generate header and user welcome message
    spacing.add_space('-', 30, 1)
    print(f"Hello Player {player_id}.")
    spacing.add_space('-', 30, 1)

    # Generate secret code or winning color combination
    secret_code = secret.secret_code()

    # Map out allowed options in secret.py to accept user input
    convert_colors = {
        "🔴": "R",
        "🟢": "G",
        "🔵": "B",
        "🟡": "Y",
        "⚪": "W",
        "🟠": "O"
    }

    colors_allowed = ["R", "G", "B", "Y", "W", "O"]

    # Set max attempts for the game
    attempts = 0
    max_attempts = 10

    # Initialize attempts
    # Make an attempt -- keep accepting user input until max attempt is reached 
    while attempts < max_attempts:
        guess = input(f"Enter your guess ({attempts}/{max_attempts}): ")

        # Error handling for user attempt
        # if [not a valid attempt], print("Invalid guess. Please try again.")
        
        # Add to attempt count
        attempts += 1

        # Validate player attempt
        # CORRECT GUESS
        # if [guess is correct], print("You won in {attempts} attempts!")

        # WRONG GUESS
        # else: print("Try again!")

    
    

