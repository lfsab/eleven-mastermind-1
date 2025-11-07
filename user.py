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

# To use this function, just call on the function name and pass on the variable 
# containing the plain text of the user's password
def encrypt_text(plain_text):
    # Ensure that only strings will be processed
    plain_text = str(plain_text) 

    # Shift by 10
    caesar_cipher = {"A": "K", "B": "L", "C": "M", "D": "N", "E": "O", "F": "P",
        "G": "Q", "H": "R", "I": "S", "J": "T", "K": "U", "L": "V", "M": "W",
        "N": "X", "O": "Y", "P": "Z", "Q": "a", "R": "b", "S": "c", "T": "d",
        "U": "e", "V": "f", "W": "g", "X": "h", "Y": "i", "Z": "j", "a": "k",
        "b": "l", "c": "m", "d": "n", "e": "o", "f": "p", "g": "q", "h": "r",
        "i": "s", "j": "t", "k": "u", "l": "v", "m": "w", "n": "x", "o": "y",
        "p": "z", "q": "1", "r": "2", "s": "3", "t": "4", "u": "5", "v": "6",
        "w": "7", "x": "8", "y": "9", "z": "0", "1": "A", "2": "B", "3": "C",
        "4": "D", "5": "E", "6": "F", "7": "G", "8": "H", "9": "I", "0": "J",
    }

    # Empty string to serve as container for the concatenated letters per iteration
    coded_text = ""

    for letter in plain_text:
        for k, v in caesar_cipher.items():
            if letter == k:
                coded_text =  coded_text + v

    return coded_text 

# To use this function, just call on the function name and pass on the variable 
# containing the cipher text (encrypted text) of the user's password
def decrypt_text(cipher_text):
    # Ensure that only strings will be processed
    cipher_text = str(cipher_text) 

    # Shift by 10
    reversed_caesar_cipher = {"K": "A", "L": "B", "M": "C", "N": "D", "O": "E",
        "P": "F", "Q": "G", "R": "H", "S": "I", "T": "J", "U": "K", "V": "L",
        "W": "M", "X": "N", "Y": "O", "Z": "P", "a": "Q", "b": "R", "c": "S",
        "d": "T", "e": "U", "f": "V", "g": "W", "h": "X", "i": "Y", "j": "Z",
        "k": "a", "l": "b", "m": "c", "n": "d", "o": "e", "p": "f", "q": "g",
        "r": "h", "s": "i", "t": "j", "u": "k", "v": "l", "w": "m", "x": "n",
        "y": "o", "z": "p", "1": "q", "2": "r", "3": "s", "4": "t", "5": "u",
        "6": "v", "7": "w", "8": "x", "9": "y", "0": "z", "A": "1", "B": "2",
        "C": "3", "D": "4", "E": "5", "F": "6", "G": "7", "H": "8", "I": "9",
        "J": "0",
    }

    # Empty string to serve as container for the concatenated letters per iteration
    decoded_text = ""

    for letter in cipher_text:
        for k, v in reversed_caesar_cipher.items():
            if letter == k:
                decoded_text = decoded_text + v

    return decoded_text 


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

    if new_user == "":
        # default operation if user prompts registration from the main menu.
        username = input("Enter a UserName (Case Sensitive):").strip()
    else: # Registration QoL: if user prompts during registration if the input username does not exists.
        username = new_user # to skip username input since it is already provided on the login function call
    
    while True:
        taken_username = False
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                for line in file:
                    if not line.strip():
                        continue
                    _ , stored_user, _ = line.strip().split(",")
                    if stored_user.lower() == username.lower():
                        choice = input("players already exist. Do you want to log in instead? (yes/no?)").strip()
                        if choice == "yes":
                            return login(username) # proceed to login module
                        else:
                            print("please try a different username.")
                            taken_username = True
                            break # loop back to username input
        if not taken_username:
            break

    password = input("enter a password: ").strip()


    #generate player id
    player_id = 1
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            if lines:
                last_id = int(lines[-1].split(",")[0])
                player_id = last_id + 1

    #encrypt password
    password = encrypt_text(password)

    #save player data
    with open(file_path, "a") as file:
        file.write(f"{player_id},{username},{password}\n")

    print(f"registration complete! welcome, {username}#{player_id} ")
    return player_id


# Login
# 1. Ask for username and password.
# 2. Look up the username in players.txt, 
# decrypt the stored password, 
# and check for a match. 
# 3. Deny access if there isn’t a match.

def login(old_user):
    spacing.add_space(' ', 50, 0)
    spacing.add_space('#', 50, 1)

    print("Player Login")

    file_path = "players.txt"
    if not os.path.exists(file_path):
        # assumes that no players are registered yet since players.txt does not exist
        print("players.txt not found. Kindly register first.")
        return reg("")

    if old_user == "":
        # default operation if user prompts login from the main menu.
        username = input("Enter your UserName (Case Sensitive): ").strip()
    else: # for login QoL: if user prompts during registration if the input username already exists.
        username = old_user # to skip username input since it is already checked on the registration module

    with open(file_path, "r") as file:
        for line in file:
            if not line.strip():
                continue
            player_id, stored_username, stored_password = line.strip().split(",") # mapping the data
            if username == stored_username: # case sensitive check
                decrypted_password = decrypt_text(stored_password)
                password = input("Enter your Password: ").strip()
                if decrypted_password == password:
                    print(f"login successful! welcome back, {username}#{player_id}.")
                    return int(player_id)
                else:
                    print("Incorrect password. Access denied.")
                    # loop back to login
                    return login(username)

    print(f"Player {username} not found. Would you like to register instead? (Y/N?)")
    choice = input().strip()
    if choice.lower() == 'y':
        return reg(username)
    else:
        return login("") # loop back to login


# Safety check: simply a quick login verification during game start to prevent login bypass
def safety_check(player_id, password):
    # To do...
    return True