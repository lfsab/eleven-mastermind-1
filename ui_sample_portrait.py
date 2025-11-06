import os
import time
import secret

border_en = "╚════════════════════════════════════════════════════════╝"

border_br = "╠════════════════════════════════════════════════════════╣"

border_mb = "╠════╦════╦════╦════╦════╦════╦════╦════╦════╦════╦══════╣"

border_mm = "╠════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬══════╣"

border_mt = "╠════╩════╩════╩════╩════╩════╩════╩════╩════╩════╩══════╣"

score = 40

secret_code_grid = ["❔","❔","❔","❔"]


guess_grid = ["🔘","🔘","🔘","🔘",
              "🔘","🔘","🔘","🔘",
              "🔘","🔘","🔘","🔘",
              "🔘","🔘","🔘","🔘",
              "🔘","🔘","🔘","🔘",
              "🔘","🔘","🔘","🔘",
              "🔘","🔘","🔘","🔘",
              "🔘","🔘","🔘","🔘",
              "🔘","🔘","🔘","🔘",
              "🔘","🔘","🔘","🔘"]   # row 10 [36,...,39]
result_grid = ["🔳","🔳","🔳","🔳",
               "🔳","🔳","🔳","🔳",
               "🔳","🔳","🔳","🔳",
               "🔳","🔳","🔳","🔳",
               "🔳","🔳","🔳","🔳",
               "🔳","🔳","🔳","🔳",
               "🔳","🔳","🔳","🔳",
               "🔳","🔳","🔳","🔳",
               "🔳","🔳","🔳","🔳",
               "🔳","🔳","🔳","🔳"]   # row 10 [36,...,39]

pointer_grid = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"] # row 1 [0,...9]

def render (delay):
    #clear console using os module
    os.system('cls' if os.name == 'nt' else 'clear')

    #UI Rendering
    #ROW 1
    ui_r0 = []
    ui_r0.append(f"║ {pointer_grid[0]}  ║║") # pointer grid
    for i in range (0,4):
          ui_r0.append(f" {guess_grid[i] } ") # guess grid #emoji with spaces in-between
          ui_r0.append(f"║") #closing bracket
          continue
    ui_r0.append("║")
    for i in range (0,4):
          ui_r0.append(f" {result_grid[i] } ") # result #emoji with spaces in-between
          ui_r0.append(f"║") #closing bracket
          continue 
    ui_r0.append(f"  {secret_code_grid[0]}  ║")

    print("".join(ui_r0))
    
    return

# Set max attempts for the game
attempts = 0
max_attempts = 10

#print the initital UI render with delay 0.15 seconds
render(0.15)

while attempts < max_attempts:
      guess = [] # initialize/reset the attempt guess input list

      # Reset the previous column back to default
      pointer_grid[attempts-1] = "⬛"
      # Set the pointer to the current column using the attempt integer to map
      pointer_grid[attempts] = "▶️"
      render(0) # call a render here so that the changes made for the new attempt is accounted for

      for c in range(0,4):
            while True:
                  order = ["first", "second", "third", "fourth"] # for numerical to word conversion
                  g = input(f"[Attempt {attempts+1}/{max_attempts}] Input your {order[c]} color: ")

                  if g.lower() == "r":
                        g = "🔴"
                        break
                  elif g.lower() == "g":
                        g = "🟢"
                        break
                  elif g.lower() == "b":
                        g = "🔵"
                        break
                  elif g.lower() == "y":
                        g = "🟡"
                        break
                  elif g.lower() == "w":
                        g = "⚪"
                        break
                  elif g.lower() == "o":
                        g = "🟠"
                        break
                  else:
                        render(0)
                        print("Invalid color. Please choose again.")
                        continue # loop back

            guess.append(g) # append to this attempt guess input list

            #Join c and attempt digit to map where on the list to replace
            #Convert integers to strings
            c_str = str(c)
            attempts_str = str(attempts)

            g_map = c_str + attempts_str # string addition causes the digit to concatenate

            #convert `g_map` to string and use it to pin-point where to insert the guess to the guess_grid
            guess_grid[int(g_map)] = g 

            render(0)
      
      attempts += 1