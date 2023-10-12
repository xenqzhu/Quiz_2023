# < -- FUNCTIONS -- >

# [>] STARTER INTRODUCTION: (YES / NO):

def yes_no(question):
  valid = False 
  while not valid:
    response = input(question).lower()
    if response == "yes" or response == "y":
      return response
      
    elif response == "no" or response == "n":
      return response
      
    else:
      print("<ERROR>: Please enter either 'YES' or 'NO'\n")

        
# [>] INSTRUCTIONS LAYOUT:

def instructions ():
  print()
  print("    <-----| HOW TO USE |----->\n")
  print(" | WELCOME TO THE TIMES-TABLE QUIZ |\n")
  print(""" • You will select a times-table you would like to be tested on (MIN - MAX: 1x-12x) 
 • MAX questions: 50
 • INFO SERVICE \n""")
  return""


# < -- MAIN ROUTINE -- >

# [>] WELCOME INTRODUCTION:
print("Welcome to quizith :P \n")

# [>] ASK USER INPUT: 'HAVE YOU PLAYED BEFORE?':
played = yes_no ("Have you participated in this quiz before?: ").lower()

if played == "no" or "n":
  instructions()

# [>] CONTINUE TO QUIZ:
  input("> CONTINUE TO QUIZ: <PRESS ENTER>")
