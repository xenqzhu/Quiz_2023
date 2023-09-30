# < -- FUNCTIONS -- >

# [>] PROGRAM INTRODUCTION:
print("Welcome to quizith :P \n")

valid = False 
while not valid:
    
    
    # [>] ASK USER INPUT: 'HAVE YOU PLAYED BEFORE?'
    played = input("Have you participated in this quiz before?: ").lower()
    
    
    # [>] YES / NO / MAYBE INPUT LOOP:
    if played == "yes":
      print("[PROGRAM CONTINUES]\n")
  
    elif played == "no":
      print("[DISPLAY INSTRUCTIONS]\n")
  
    else:
      print("<ERROR>: Please enter either 'YES' or 'NO'\n")

    
    # < -- MAIN ROUTINE -- >

