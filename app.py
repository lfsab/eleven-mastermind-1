# Main Program
# To be run at start

import user
import spacing # for efficient border creation on the user interface

# Print Startup Screen
for i in range(1, 2):
    spacing.add_space('#', 50, 0)
    continue

print("     ⚫⚪⚪⚫ Eleven Mastermind 🔴🟢🔵🟡⚪🟠       ")

for i in range(1, 2):
    spacing.add_space('#', 50, 0)
    continue

# Prompt for Returning or New Players

print("        [N] New Player      [L] Login          ")

spacing.add_space(' ', 50, 0)

while True:
    player_select = input("     Select your option: ")
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