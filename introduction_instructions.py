# < -- FUNCTIONS -- >

def yes_no (question):
  valid = False 
  while not valid:
      response = input(question).lower()
        
      # [>] YES / NO / MAYBE INPUT LOOP:
      if response == "yes" or response == "y":
        print("[CONTINUE TO PROGRAM]\n")
       
      elif response == "no" or response == "n":
        print("[DISPLAY INSTRUCTIONS]\n")
    
      else:
        print("<ERROR>: Please enter either 'YES' or 'NO'\n")
  
  
# < -- MAIN ROUTINE -- >

# [>] PROGRAM INTRODUCTION:
print("Welcome to quizith :P \n")

# [>] ASK USER INPUT: 'HAVE YOU PLAYED BEFORE?'
played = yes_no ("Have you participated in this quiz before?: ").lower()




