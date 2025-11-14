import os
import time

# Print Startup Screen
def menu_ui(state, delay, variable):
    # state: current menu
    # delay: time-based row-by-row render
    # variable: custom messages, converted to list for multiple prompt
    app_ui_01 = [""]
    app_ui_01.append("╔═══════════════════════════════════════════════════════╗")
    app_ui_01.append("║ 	┏━╸╻  ┏━╸╻ ╻┏━╸┏┓╻             			║")
    app_ui_01.append("║ 	┣╸ ┃  ┣╸ ┃┏┛┣╸ ┃┗┫ 🔴 🟢 🔵 🟡 ⚪ 🟠         	║")
    app_ui_01.append("║ 	┗━╸┗━╸┗━╸┗┛ ┗━╸╹ ╹       			║")
    app_ui_01.append("║   		 ┏┳┓┏━┓┏━┓╺┳╸┏━╸┏━┓┏┳┓╻┏┓╻╺┳┓  		║")
    app_ui_01.append("║ 	⚫⚪⚪⚫ ┃┃┃┣━┫┗━┓ ┃ ┣╸ ┣┳┛┃┃┃┃┃┗┫ ┃┃  	        ║")
    app_ui_01.append("║   		 ╹ ╹╹ ╹┗━┛ ╹ ┗━╸╹┗╸╹ ╹╹╹ ╹╺┻┛  		║")
    app_ui_01.append("╠═══════════════════════════════════════════════════════╣")
    
    if state == "custom":
        #convert/ensure variable to list
        variable = list(variable)
        for v in variable:
            app_ui_01.append("║"+ v.center(55) +"║")
    else: # default is the main menu
        ui_insert = "[N] New Player          [L] Login"
        app_ui_01.append("║     A Group Project of Group Eleven for CMSC 202 	║")
        app_ui_01.append("║        1st Semester A.Y. 2025-2026  			║")
        app_ui_01.append("╠═══════════════════════════════════════════════════════╣")
        app_ui_01.append("║"+ ui_insert.center(55) +"║")
    
    app_ui_01.append("╚═══════════════════════════════════════════════════════╝")

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(len(app_ui_01)):
        print(app_ui_01[i])
        time.sleep(delay)
        continue