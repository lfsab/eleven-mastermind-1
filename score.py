#Score Management:
# Implement a scoring system for the game. Fewer guesses should yield to a higher score.
# When the game is won:
# Update the file only if the score is better.

# import the json module.
# all records generated and read by update_user_score and leaderboard will be
# in json format
import json
import user

# REMINDER: Please make sure to cast the return value of start_game() in game.py to int
# before using it as the score parameter of update_user_score().
def update_user_score(username, score, password):

    user.safety_check(username, password)
    
    # Boolean variable to check if highscore.txt needs to be updated.
    scoreboard_needs_update = False

    # Check if a file named highscores.txt exists or if it has a valid json format.
    try:
        # Open the highscores.txt file and store its contents to the variable scoreboard
        with open("highscores.txt", "r") as read_scores:
            scoreboard = json.load(read_scores)
    # If highscores.txt does not exist or if it does not contain a valid json format
    # a new empty highscores.txt is created
    except:
        empty_dictionary = {}
        with open("highscores.txt", "w") as write_scores:
            json.dump(empty_dictionary, write_scores, indent=2)
        # After creating an empty highscores.txt, it is then opened so that its content (or lack of it)
        # is stored in the variable scoreboard so that the data can be manipulated in this function.
        with open("highscores.txt", "r") as read_scores:
            scoreboard = json.load(read_scores)

    # Verify if username already exists
    if username in scoreboard:
        # Check if the current number of guesses is lower than the player's stored best score in highscores.txt.
        if score > scoreboard[username]:
            print(f"You got {score}! Good job! You bested your previous record of {scoreboard[username]}!")
            scoreboard[username] = score
            scoreboard_needs_update = True
        else:
            # highscores.txt is not updated if the current score is not higher than the ones recorded in highscores.txt
            print(f"Your score of {score} is not higher than your record of {scoreboard[username]}.")
            print("Better luck next time.")
    # If not, create a new one together with new score
    else:
        print(f"Hey there {username}! You got {score}!")
        scoreboard.update({username: score})
        scoreboard_needs_update = True


    if scoreboard_needs_update:
        # Section for sorting the scoreboard before writing into highscores.txt
        scoreboard = sorted(scoreboard.items(), key = lambda x: x[1])
        scoreboard = dict(scoreboard)
        # Writes the new content of the scoreboard to highscores.txt
        with open("highscores.txt", "w") as write_scores:
            json.dump(scoreboard, write_scores, indent=2)


# Leaderboard:
# The leaderboard should display the top 5 players (username and best score), sorted by score (ascending).
def leaderboard():

    # Open the highscores.txt file and store its contents to the variable scoreboard
    with open("highscores.txt", "r") as read_scores:
        scoreboard = json.load(read_scores)
    
    ########################################################################################################################
    # Below is a series of statements meant to manipulate the data is variable scoreboard
    # so that it will show the Top 5 players and their records in ascending order.
    # The statement immediately below sorts the first five players in descending order.
    descending_sb = sorted(scoreboard.items(), key = lambda x: x[1], reverse = True)[:5]
    # This statement converts descending_sb back to a dictionary since the sorted() function returns a data type of list
    descending_sb = dict(descending_sb)
    # The top five is then finally sorted in ascending order
    ascending_sb = sorted(descending_sb.items(), key = lambda x: x[1])
    # ascending_sb is a list of tuples. No need to cast into a dictionary since the info can be displayed using 
    # the current data structure.
    ########################################################################################################################
   
    print("===TOP 5===") 
    for k, v in ascending_sb:
        print(f"{k}: {v}")

