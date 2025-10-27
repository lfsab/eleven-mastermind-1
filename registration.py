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

import login
import os

# def encrypt(password):
#TODO: implement password encryption
#for now, password is as is

def registration():
    print("New Player Registration")

    file_path = "players.txt"
    if os.path.exists(file_path):
        choice = input("players already exist. Do you want to log in instead? (yes/no?)").strip()
        if choice == "yes":
            return login.login()

    while True:
        username = input("enter a username:").strip()
        password = input("enter a password:").strip()

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

if __name__ == "__main__":
    registration()