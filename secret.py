# Secret Code Module
# randomizer to generate a secret code consisting of 4 colors.
import random

# Red    (R), 
# Green  (G), 
# Blue   (B), 
# Yellow (Y), 
# White  (W),
# Orange (O)

# To use this Secret Code Module in game.py, do either
# import secret 
# or
# from secret import secret_code
def secret_code(to_guess): # add: allow dynamic generation
    code = []
    colors = ["🔴", "🟢", "🔵", "🟡", "⚪", "🟠"]

    # for loop to generate a length of `n`/`to_guess` colors
    for g in range(to_guess):        
        selected_color = random.choice(colors)
        code.append(selected_color)
    return code