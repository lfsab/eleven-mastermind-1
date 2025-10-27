# Main Program
# To be run at start

import login
import registration
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
player_select = input("     Select your option:")

# Open Game
import game

#Testing collaborators commit
# Testing Pull Request