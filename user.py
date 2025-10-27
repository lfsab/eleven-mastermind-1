# Encryption: Implement a simple substitution 
# or Caesar cipher for the password (no external libraries allowed).

# New User Registration
# 1. Ask for a username and password for new players.
# 2. Check if the username already exists (case-insensitive) in players.txt. 
# If it exists, deny registration and prompt again.
# 3. Encrypt the password and store the pair in players.txt.


#Suggestion:
# QoL: If players exists from database [players.txt], prompt user and proceed to login
# Data Management: Use player ID for easy tracking on return
# ie. return player_id

import os
import spacing

# def encrypt(password):
#TODO: implement password encryption
#for now, password is as is

def reg(new_user): # new_user is defined for integrating login module

    spacing.add_space(' ', 50, 0)
    spacing.add_space('#', 50, 1)

    print("New Player Registration")

    file_path = "players.txt"
    if os.path.exists(file_path):
        print("") # success pass
    else: # players.txt does not exist
        open(file_path, "w").close() # create players.txt
        print("Successfully created players.txt\n")
    #     choice = input("players already exist. Do you want to log in instead? (yes/no?)").strip()
    #     if choice == "yes":
    #         return login.login()

    if new_user == "":
        # default operation if user prompts registration from the main menu.
        while True:
            username = input("enter a username:").strip()

            taken_username = False
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    for line in file:
                        if not line.strip():
                            continue
                        _ , stored_user, _ = line.strip().split(",")
                        if stored_user.lower() == username.lower():
                            print("Username already exists. Try another one")
                            taken_username = True
                            break
            if not taken_username:
                break

        password = input("enter a password:").strip()

    else: # login QoL: if user prompts for a registration if the input username does not exists.
        username = new_user # to skip username check since it is already checked on the login module
        password = input(f"enter a password for {username}: ").strip()


    #generate player id
    player_id = 1
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            if lines:
                last_id = int(lines[-1].split(",")[0])
                player_id = last_id + 1

    #save player data
    with open(file_path, "a") as file:
        file.write(f"{player_id},{username},{password}\n")

    print(f"registration complete! welcome, {username}. Your player ID is {player_id} ")
    return player_id

# if __name__ == "__main__":
#     registration()


# Login
# 1. Ask for username and password.
# 2. Look up the username in players.txt, 
# decrypt the stored password, 
# and check for a match. 
# 3. Deny access if there isn’t a match.

def login(old_user):
    player_id = old_user
    return player_id

# Suggestion:
# If username not found, initiate new registration