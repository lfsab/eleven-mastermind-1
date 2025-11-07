import os
import time
import secret

border_en = "╚════════════════════════════════════════════════╝"

border_br = "╠════════════════════════════════════════════════╣"

border_mb = "╠════╦═════════════════════╦═════════════════════╣"

border_mm = "╠════╬═════════════════════╬═════════════════════╣"

border_mt = "╠════╩═════════════════════╩═════════════════════╣"

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

# guess_grid_a = [f"{i:02d}" for i in range(40)]

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

# result_grid_a = [f"{i:02d}" for i in range(40)]

pointer_grid = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"] # row 1 [0,...9]

def render (delay):
    #clear console using os module
    os.system('cls' if os.name == 'nt' else 'clear')

    print(border_mm)

    post_header = ["║    ║ "]
    for s in secret_code_grid:
         post_header.append(f" {s}  ")
    post_header.append("║")  
    post_header.append(f"      SCORE: {score}      ║")
    print("".join(post_header))


    print(border_mm)

    #UI Rendering
    #ROW 1
    for e in range (0,10):
        row_array_start = (e*4) # simplified (((e*4)+1)-1)
        row_array_end = ((e*4)+4)

        row = []

        row.append(f"║ {pointer_grid[e]} ║") # pointer grid

        for i in range(row_array_start, row_array_end):
              row.append(f"  {guess_grid[i]} ") # guess grid
              continue
        
        row.append(" ║")

        for i in range(row_array_start, row_array_end):
              row.append(f"  {result_grid[i]} ") # guess grid
              continue        
        
        row.append(" ║")
        print("".join(row))
        time.sleep(delay)

        continue
    
    print(border_mt)
    print("║    [R]🔴  [G]🟢  [B]🔵  [Y]🟡  [W]⚪  [O]🟠    ║")
    print(border_en)



    
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
      pointer_grid[attempts] = "▶️ "
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

            g_map = attempts_str + c_str # string addition causes the digit to concatenate
                    # reversed for portrait orientation 01,02,03,04, 11,12,13,14, 21,22,23,24, ..., 91,92,93,94

            # mapping offset to convert the code from landscape to portrait
            p_offset = (6 * int(attempts))

            #convert `g_map` to string and use it to pin-point where to insert the guess to the guess_grid
            guess_grid[(int(g_map) - int(p_offset))] = g 

            render(0)
      
      attempts += 1