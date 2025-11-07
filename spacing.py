def add_space(char, width, spaces):
    # char: character to be printed
    # width: number of times the character is to be printed
    # spaces: number of new lines to add below after printing the character
    print((str(char) * int(width)) + ("\n" * int(spaces)))

    return

def border (left,middle,end,repeat):
      # left: starting border
      # middle: divider in between attempts
      # end: end border 
      # repeat = max_attempts; kindly declare on the module when calling this function:
      # example: border("╠","╦","╣",max_attempts)    
      print((str(left)) + (("════" + str(middle))*repeat) + "══════" + str(end))
      return