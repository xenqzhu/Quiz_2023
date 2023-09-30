# < -- FUNCTIONS -- >

def yes_no (question):
  valid = False 
  while not valid:
    response = input(question).lower()
      
    # [>] YES / NO / MAYBE INPUT LOOP:
    if response == "yes" or response == "y" or response == "yef":
      response = "yes"
      return response

    elif response == "no" or response == "n" or response == "neh":
      response = "no"
      return response 

    else:
      print("<ERROR>: Please enter either 'YES' or 'NO'\n")

  
    # < -- MAIN ROUTINE -- >

# [>] PROGRAM INTRODUCTION:
print("Welcome to quizith :P \n")

# [>] ASK USER INPUT: 'HAVE YOU PLAYED BEFORE?'
played = input("Have you participated in this quiz before?: ").lower()