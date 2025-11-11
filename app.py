# Main Program
# To be run at start

import user
import spacing # for efficient border creation on the user interface
import time
import os

# Print Startup Screen
app_ui_01 = [""]
app_ui_01.append("╔═══════════════════════════════════════════════════════╗")
app_ui_01.append("║ 	┏━╸╻  ┏━╸╻ ╻┏━╸┏┓╻             			║")
app_ui_01.append("║ 	┣╸ ┃  ┣╸ ┃┏┛┣╸ ┃┗┫ 🔴 🟢 🔵 🟡 ⚪ 🟠         	║")
app_ui_01.append("║ 	┗━╸┗━╸┗━╸┗┛ ┗━╸╹ ╹       			║")
app_ui_01.append("║   		 ┏┳┓┏━┓┏━┓╺┳╸┏━╸┏━┓┏┳┓╻┏┓╻╺┳┓  		║")
app_ui_01.append("║ 	⚫⚪⚪⚫ ┃┃┃┣━┫┗━┓ ┃ ┣╸ ┣┳┛┃┃┃┃┃┗┫ ┃┃  	        ║")
app_ui_01.append("║   		 ╹ ╹╹ ╹┗━┛ ╹ ┗━╸╹┗╸╹ ╹╹╹ ╹╺┻┛  		║")
app_ui_01.append("╠═══════════════════════════════════════════════════════╣")
app_ui_01.append("║     A Group Project of Group Eleven for CMSC 202 	║")
app_ui_01.append("║        1st Semester A.Y. 2025-2026  			║")
app_ui_01.append("╠═══════════════════════════════════════════════════════╣")
app_ui_01.append("║	    [N] New Player    	 [L] Login  		║")
app_ui_01.append("╚═══════════════════════════════════════════════════════╝")

for i in range(len(app_ui_01)):
    print(app_ui_01[i])
    time.sleep(0.25)
    continue


while True:
    player_select = input("Select your option: ")
    if player_select.lower() == 'n':
        player_id = user.reg("")
        break
    elif player_select.lower() == 'l':
        player_id = user.login("")
        break
    else:
        print("Invalid option selected.")

# Open Game
import game

game.start_game(player_id)

#Testing collaborators commit
# Testing Pull Request