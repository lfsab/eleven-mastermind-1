# Main Program
# To be run at start

import user
import render
import score

render.menu_ui("",0.15,[""])

while True:
    player_select = input("Select your option: ")
    if player_select.lower() == 'n':
        player = list(user.reg(""))
        break
    elif player_select.lower() == 'l':
        player = list(user.login(""))
        break
    else:
        print("Invalid option selected.")

# Open Game
import game

result = list(game.start_game(player[0],player[1],player[2]))

# return (player_id,username,password,userscore)
score.update_user_score(result[0],result[1],result[2])

score.leaderboard()

while True:
    play_again = input("Play Again? [Y/N]: ")
    if play_again.lower() == "y":
        result = list(game.start_game(player[0],player[1],player[2]))
        score.update_user_score(result[0],result[1],result[2])
        score.leaderboard()
    else:
        print("Thank you for playing!")
        break
        

#Testing collaborators commit
# Testing Pull Request