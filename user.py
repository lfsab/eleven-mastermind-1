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
import render
import time


# To use this function, just call on the function name and pass on the variable 
# containing the plain text of the user's password
def encrypt_text(plain_text, shift):
    # Ensure that only strings will be processed
    plain_text = str(plain_text)

    # UPDATE: Utilized dynamic/computed dictonary for the caesar_cipher
    # To make it easier to create a shift list or re-define shift value instead of hardcoded definition

    # Ensure that only integer will be processed for the shift variable
    shift = int(shift) 
    
    # Define the allowed characters in a password as well as it's position in the cipher using tuple
    characters_array = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]","|","\\",":",";","\"","'","<",">",",",".","?","/"," ","\t")

    #Initialize `caesar_cipher` as dictionary list
    caesar_cipher = dict()

    c_array_size = len(characters_array) #define the array size of the tuple = 92
    for c in range(c_array_size):
        # (c+shift) = compute for the encryption offset (caesar function) of a character within the tuple
        # use modulo `%` to perform a loopback to handle when c+shift is > 92
        # [(70+10) % 94] = 80 => {'*':']'}
        # [(90+10) % 94] = 6 => {'.':'F'}
        caesar_cipher.update({characters_array[c]:characters_array[(c+shift) % c_array_size]})

    # Empty string to serve as container for the concatenated letters per iteration
    coded_text = ""

    for letter in plain_text:
        for k, v in caesar_cipher.items():
            if letter == k:
                coded_text =  coded_text + v

    return coded_text 

# To use this function, just call on the function name and pass on the variable 
# containing the cipher text (encrypted text) of the user's password
def decrypt_text(cipher_text, shift):
    # Ensure that only strings will be processed
    cipher_text = str(cipher_text) 

    # Ensure that only integer will be processed for the shift variable
    shift = int(shift)

    #define the allowed characters in a password as well as it's position in the cipher using tuple
    characters_array = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]","|","\\",":",";","\"","'","<",">",",",".","?","/"," ","\t")

    #Initialize `revered_caesar_cipher` as dictionary list
    reversed_caesar_cipher = dict()

    c_array_size = len(characters_array) #define the array size of the tuple = 92
    for c in range(c_array_size):
        # (c-shift) = compute for the decryption offset (caesar function) of a character within the tuple
        # use modulo `%` to perform a loopback to handle c-shift is < 0, or is a negative value
        # [(18-10) % 94] = 8 => {'R':'H'}
        # [(8-10) % 94] = 92 => {'H':'/'}
        reversed_caesar_cipher.update({characters_array[c]:characters_array[(c-shift) % c_array_size]})

    # Empty string to serve as container for the concatenated letters per iteration
    decoded_text = ""

    for letter in cipher_text:
        for k, v in reversed_caesar_cipher.items():
            if letter == k:
                decoded_text = decoded_text + v

    return decoded_text 


def reg(new_user): # new_user is defined for integrating login module

    shift = 10 # variable: define the number of shifts for the caesar cipher
    # NOTE: must be the same value as defined in login 206
    # if line 156 or 157 was commented out the value above is over-written

    render.menu_ui("custom",0,["PLAYER REGISTRATION","Kindly enter a username"])

    file_path = "players.txt"
    if os.path.exists(file_path):
        print("") # success pass
    else: # players.txt does not exist
        open(file_path, "w").close() # create players.txt
        print("Successfully created players.txt\n")

    username_loop = True
 
    while username_loop:

        if new_user == "":
            # default operation if user prompts registration from the main menu.
            username = input("Input (Case Sensitive): ").strip()
        else: # Registration QoL: if user prompts during registration if the input username does not exists.
            username = new_user # to skip username input since it is already provided on the login function call

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                player_found = False
                for line in file:
                    if not line.strip():
                        continue
                    _ , stored_user, _ = line.strip().split(",")
                    if stored_user == username: # to consider case-senitive username storing
                        player_found = True
                        player_exists = f"Player with username '{username}' already exists."
                        render.menu_ui("custom",0,["PLAYER REGISTRATION",player_exists])
                        while True:
                            choice = input("Do you want to log in instead? (yes/no?) ").strip()
                            if choice == "yes":
                                return login(username)
                            elif choice == "no":                        
                                print("Please try a different username.")
                                time.sleep(1)
                                username = ""
                                username_loop = True
                                break
                            else:
                                print("Invalid Input!")
                        break
                    # no action for unique username
                if not player_found:
                    username_loop = False
    
    # UPDATE: Commented out validation loop since the array now considered special/non-alphanumeric characters
    # # Password validation loop
    # while True:

    password = input("Enter a password: ").strip()
        
    #     # Check if password is alphanumeric using built-in string methon isalnum(). 
    #     # If password is not alphanumeric, it will cause issues with deciphering the cipher text.
    #     if password.isalnum():
    #         break
    #     else:
    #         print("You entered an invalid character. Please use only alphanumeric characters.")
    #         continue

    #generate player id
    player_id = 1
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            if lines:
                last_id = int(lines[-1].split(",")[0])
                player_id = last_id + 1

    #encrypt password
    # shift = len(username) # comment-out if shift is dependent/dynamic to the length of the username
    # shift = len(password) # comment-out if shift is dependent/dynamic to the length of the password
    encrypted_password = encrypt_text(password, shift)

    #save player data
    with open(file_path, "a") as file:
        file.write(f"{player_id},{username},{encrypted_password}\n")

    # confirm decryption
    decrypted_password = decrypt_text(encrypted_password, shift)

    print(f"""registration complete! welcome, {username}#{player_id} \n
              please remeber your password: "{decrypted_password}" """) # password confirmaiton 
    # password review only during registration phase
    
    to_end = False
    
    while not to_end:
        end_reg = input("Continue? (Y/N): ")

        if end_reg.lower() == "y":
            print("Now loading the game...")
            time.sleep(3)
            to_end = bool(True)
        else:
            to_end = bool(False)  

    return (player_id,username,password)


# Login
# 1. Ask for username and password.
# 2. Look up the username in players.txt, 
# decrypt the stored password, 
# and check for a match. 
# 3. Deny access if there isn’t a match.

def login(old_user):

    shift = 10 # variable: define the number of shifts for the caesar cipher
    # NOTE: must be the same value as defined in login on line 10
    # if line 220 or 221 was commented out the value above is over-written

    render.menu_ui("custom",0,["PLAYER LOGIN","Kindly your username"])
    

    file_path = "players.txt"
    if not os.path.exists(file_path):
        # assumes that no players are registered yet since players.txt does not exist
        print("players.txt not found. Kindly register first.")
        return reg("")

    while True:
        if old_user == "":
            # default operation if user prompts login from the main menu.
            username = input("Input (Case Sensitive): ").strip()
        else: # for login QoL: if user prompts during registration if the input username already exists.
            username = old_user # to skip username input since it is already checked on the registration module

        with open(file_path, "r") as file:
            for line in file:
                if not line.strip():
                    continue
                player_id, stored_username, stored_password = line.strip().split(",") # mapping the data
                if username == stored_username: # case sensitive check
                    decrypted_password = decrypt_text(stored_password, shift)
                    welcome_player = f"Welcome back, {username} ! Enter your password below."
                    render.menu_ui("custom",0,["PLAYER LOGIN", welcome_player])
                    password = input("Input: ").strip()
                    # shift = len(username) # comment-out if shift is dependent/dynamic to the length of the username
                    # shift = len(password) # comment-out if shift is dependent/dynamic to the length of the password
                    
                    if decrypted_password == password:
                        print(f"login successful! welcome back, {username} - Player #{player_id}.")
                        time.sleep(1)
                        print("Now loading the game...")
                        time.sleep(3)
                        return (player_id,username,password)
                    else:
                        print("Incorrect password. Access denied.")
                        # loop back to login
                        return login(username)

        player_none = f"There is no player with username '{username}'."
        render.menu_ui("custom",0,["PLAYER LOGIN", player_none])
        choice = input("Would you like to register instead? (Y/N?)").strip()
        if choice.lower() == 'y':
            return reg(username)
        else:
            print("Please double-check your login credentials.")


# Safety check: simply a quick login verification during game start to prevent login bypass
def safety_check(username, password):
    shift = 10
    file_path = "players.txt"
    with open(file_path, "r") as file:
        for line in file:
            if not line.strip():
                continue
            player_id, stored_username, stored_password = line.strip().split(",") # mapping the data
            if username == stored_username: # case sensitive check
                # shift = len(username) # comment-out if shift is dependent/dynamic to the length of the username
                # shift = len(password) # comment-out if shift is dependent/dynamic to the length of the password
                decrypted_password = decrypt_text(stored_password, shift)
                
                if decrypted_password == password:
                    return 0
                else:
                    print("Safety Check failed. Access denied!")
                    import sys
                    sys.exit()
