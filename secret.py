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
def secret_code():
    colors = ["🔴", "🟢", "🔵", "🟡", "⚪", "🟠"]
    code = [random.choice(colors), random.choice(colors), random.choice(colors), random.choice(colors)]

    return code
