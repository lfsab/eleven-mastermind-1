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
    # Set max attempts for the game
    attempts = 0 # intitialization | DO NOT EDIT 
    userscore = 0 # score initialization | DO NOT EDIT

    max_attempts = 10 # parameter: how many tries a player will have
    to_guess = 4 # parameter: how many colors to guess in the game

    # Generate secret code or winning color combination with the length depends on the `to_guess` parameter
    secret_code = secret.secret_code(to_guess)

    # adapt a new grid generation to account to dynamic parameters
    guess_grid = [["🔘" for i in range(to_guess)] for n in range (max_attempts)]
    result_grid = [["🔳" for i in range(to_guess)] for n in range (max_attempts)]
    pointer_grid = [f"⬛" for i in range(max_attempts)]
    secret_code_grid = [f"❔" for i in range(to_guess)]

    def render (delay):
        #clear console using os module
        os.system('cls' if os.name == 'nt' else 'clear')

        #UI Rendering

        time.sleep(delay) # graphical adjustments, allow delay rendering row-by-row

        spacing.border("╔", "═", "╗",max_attempts)
        print(f"║             Welcome Player# {player_id} to Mastermind!           ║")
        print(f"║  Guess the {to_guess}-color combination in {max_attempts} attempts or less  ║")

        #spacing module to dynamically add borders based on the game `max_attempts` instead of hardcoded string
        spacing.border("╠","╦","╣",max_attempts)

        #GUESS GRID#
        for e in range(to_guess):
                row = ["║"]
                for i in range(max_attempts):
                    row.append(f" {guess_grid[i][e]} ") #emoji with spaces in-between
                    row.append(f"║") #closing bracket
                row.append(f"  {secret_code_grid[e]}  ║") #append secret code
                print("".join(row))
                time.sleep(delay)
        ###

        # DIVIDER #
        spacing.border("╠","╬","╣",max_attempts)
        time.sleep(delay)

        #RESULT GRID#
        for e in range(to_guess):
                row = ["║"]
                for i in range(max_attempts):
                    row.append(f" {result_grid[i][e]} ") #emoji with spaces in-between
                    row.append(f"║") #closing bracket

                if e == 0:
                    row.append("GUESS:║")
                elif e == 1:
                    row.append(f"{attempts+1:02d}    ║")
                elif e == 2:
                    row.append(f"--of--║")
                elif e == 3:
                    row.append(f"    {max_attempts:02d}║")
                else:
                    row.append(f"      ║")

                print("".join(row))
                time.sleep(delay)

        #DIVIDER
        spacing.border("╠","╬","╣",max_attempts)
        time.sleep(delay)  

        ui_pt = ["║"]
        for i in range(max_attempts):
                ui_pt.append(f" {pointer_grid[i]} ")
                ui_pt.append("║")
        ui_pt.append("      ║")

        time.sleep(delay)
        print("".join(ui_pt))
        spacing.border("╠","╩","╣",max_attempts)

        time.sleep(delay)
        print("║      [R]🔴  [G]🟢  [B]🔵   [Y]🟡   [W]⚪   [O]🟠" + ("     "*(max_attempts-10)) + "       ║")

        time.sleep(delay)
        spacing.border("╚","═","╝",max_attempts)

        return

    #print the initital UI render with delay 0.15 seconds
    render(0.15)

    while attempts < max_attempts:
            guess = [] # initialize/reset the attempt guess input list
            # Update pointer to indicate the previous attempt fails
            # with safety net to avoid underflow/wrap-arround error on 0 minus 1
            if attempts !=0:
                    pointer_grid[attempts-1] = "❌"
            # Set the pointer to the current column using the attempt integer to map
            pointer_grid[attempts] = "🔼"
            render(0) # call a render here so that the changes made for the new attempt is accounted for
            
            # Print `try again` except on the initial attempts=0
            if attempts > 0:
                    print("Try again!")

            for c in range(to_guess):
                    while True:
                        g = input(f"[Attempt {attempts+1}/{max_attempts}] Input your color #{c+1}: ")

                        if g.lower() == "r":
                                g = "🔴"
                                break
                        elif g.lower() == "g":
                                g = "🟢"
                                break
                        elif g.lower() == "b":
                                g = "🔵"
                                break
                        elif g.lower() == "y":
                                g = "🟡"
                                break
                        elif g.lower() == "w":
                                g = "⚪"
                                break
                        elif g.lower() == "o":
                                g = "🟠"
                                break
                        else:
                                render(0)
                                print("Invalid color. Please choose again.")
                                continue # loop back

                    guess.append(g) # append to this attempt guess input list

                    # simplified and improved mapping to account to dynamic parameters
                    guess_grid[attempts][c] = g 

                    render(0)
            
            # Confirm User Input
            while True:
                    print("-".join(guess))
                    confirm = input("Are you sure of this combination [Y/N]? ")
                    confirm = confirm.lower()
                    if confirm == "y":
                        secret_code_string = "".join(secret_code)
                        secret_code_check = list(secret_code_string)
                        correctness = 0
                        # Perform checks
                        #copy secret_code to an editable list
                        for i in range (to_guess):
                                result_grid[attempts][i] = "🕚"
                                render(0)
                                time.sleep(1)
                                #check first if current guess[i] is found in the array
                                if guess[i] in secret_code_check:
                                    # perform another check if the index of found color match current `i`
                                    if int(i) == secret_code_check.index(guess[i]):
                                            # Correct color in the correct position.
                                            result_grid[attempts][i] = "⚫"
                                            correctness += 1 # increment to indicate that one guess is correct
                                            #prevent the next check to account an already correct color
                                            secret_code_check[i] = " "
                                            render(0)
                                            time.sleep(1)
                                    else: 
                                            #Correct color in the wrong position.
                                            result_grid[attempts][i] = "⚪"
                                            #prevent the next check to account an already checked color
                                            secret_code_check[int(secret_code_check.index(guess[i]))] = " "
                                            render(0)
                                            time.sleep(1)
                                else: # guess it not found
                                    result_grid[attempts][i] = "🔳"
                                    render(0)
                                    time.sleep(1)
                        
                        # Check for correctness
                        if correctness == int(to_guess):
                                # this means that all colors has been guessed
                                pointer_grid[attempts] = "✅"
                                # reveal the hidden code
                                for r in range (to_guess):
                                    secret_code_grid[r] = secret_code[r]
                                render(0)
                                print(f"You won in {attempts} attempts!")
                                userscore = 10-attempts #compute userscore from the attempts
                                attempts = 10 # set attempt value to 10 to exit the loop
                                break
                        else:
                                # any value (lower) than the requirement means this attempt failed
                                # Increment attempts for failed guess
                                userscore = 0
                                attempts += 1
                        # break and loop back to the next attempt
                        break
                    elif confirm == "n":
                        # resets the guess attempt
                        for x in range(to_guess):
                                guess_grid[attempts][x] = "🔘"
                                render(0) 
                        # break and loop back to the current attempt
                        break
                    else:
                        print("Invalid Input")
                        # loop back

    print(f"User Score: {userscore}")      
      
    # Casting userscore to int to make sure it records properly with the function in scores.py
    return int(userscore)

    

