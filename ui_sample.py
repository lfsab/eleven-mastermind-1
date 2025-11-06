import os
import time
import secret

border_en = "╚════════════════════════════════════════════════════════╝"

border_br = "╠════════════════════════════════════════════════════════╣"

border_mb = "╠════╦════╦════╦════╦════╦════╦════╦════╦════╦════╦══════╣"

border_mm = "╠════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬══════╣"

border_mt = "╠════╩════╩════╩════╩════╩════╩════╩════╩════╩════╩══════╣"



secret_code_grid = ["❔","❔","❔","❔"]

guess_grid = ["🔘","🔘","🔘","🔘","🔘","🔘","🔘","🔘","🔘","🔘", # row 1 [0,...9]
            "🔘","🔘","🔘","🔘","🔘","🔘","🔘","🔘","🔘","🔘",   # row 2 [10,...,19]
            "🔘","🔘","🔘","🔘","🔘","🔘","🔘","🔘","🔘","🔘",   # row 3 [20,...,29]
            "🔘","🔘","🔘","🔘","🔘","🔘","🔘","🔘","🔘","🔘"]   # row 4 [30,...,39]

result_grid = ["🔳","🔳","🔳","🔳","🔳","🔳","🔳","🔳","🔳","🔳",# row 1 [0,...9]
            "🔳","🔳","🔳","🔳","🔳","🔳","🔳","🔳","🔳","🔳",   # row 2 [10,...,19]
            "🔳","🔳","🔳","🔳","🔳","🔳","🔳","🔳","🔳","🔳",   # row 3 [20,...,29]
            "🔳","🔳","🔳","🔳","🔳","🔳","🔳","🔳","🔳","🔳"]   # row 4 [30,...,39]

def render (delay):
      #clear console using os module
      os.system('cls' if os.name == 'nt' else 'clear')

      #UI Rendering
      ui_g1 = ["║"]
      for i in range(0,10):
            ui_g1.append(f" {guess_grid[i]} ") #emoji with spaces in-between
            ui_g1.append(f"║") #closing bracket
      ui_g1.append(f"  {secret_code_grid[0]}  ║") #append secret code 1 of 4
      ui_g2 = ["║"]
      for i in range(10,20):
            ui_g2.append(f" {guess_grid[i]} ")
            ui_g2.append("║")
      ui_g2.append(f"  {secret_code_grid[1]}  ║") #append secret code 2 of 4
      ui_g3 = ["║"]
      for i in range(20,30):
            ui_g3.append(f" {guess_grid[i]} ")
            ui_g3.append("║")
      ui_g3.append(f"  {secret_code_grid[2]}  ║") #append secret code 3 of 4
      ui_g4 = ["║"]
      for i in range(30,40):
            ui_g4.append(f" {guess_grid[i]} ")
            ui_g4.append("║")
      ui_g4.append(f"  {secret_code_grid[3]}  ║") #append secret code 4 of 4
      ui_r1 = ["║"]
      for i in range(0,10):
            ui_r1.append(f" {result_grid[i]} ")
            ui_r1.append("║")
      
      ui_r2 = ["║"]
      for i in range(10,20):
            ui_r2.append(f" {result_grid[i]} ")
            ui_r2.append("║")
      
      ui_r3 = ["║"]
      for i in range(20,30):
            ui_r3.append(f" {result_grid[i]} ")
            ui_r3.append("║")

      ui_r4 = ["║"]
      for i in range(30,40):
            ui_r4.append(f" {result_grid[i]} ")
            ui_r4.append("║")      

      time.sleep(delay) # graphical adjustments
      print(border_mb)

      time.sleep(delay)
      print("".join(ui_g1))
      time.sleep(delay)
      print("".join(ui_g2))
      time.sleep(delay)
      print("".join(ui_g3)) 
      time.sleep(delay)
      print("".join(ui_g4))   

      time.sleep(delay)
      print(border_mm)

      time.sleep(delay)
      print("".join(ui_r1))
      time.sleep(delay)
      print("".join(ui_r2))
      time.sleep(delay)
      print("".join(ui_r3))
      time.sleep(delay)
      print("".join(ui_r4))

      time.sleep(delay)
      print(border_mt)

      time.sleep(delay)
      print("║      [R]🔴  [G]🟢  [B]🔵   [Y]🟡   [W]⚪   [O]🟠       ║")

      time.sleep(delay)
      print(border_en)

      return

# Set max attempts for the game
attempts = 0
max_attempts = 10

#print the initital UI render with delay 0.15 seconds
render(0.15)

while attempts < max_attempts:
      guess = [] # initialize/reset the attempt guess input list
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