# < -- FUNCTIONS -- >

# [>] STARTER INTRODUCTION: (YES / NO):

def yes_no(question):
  valid = False 
  while not valid:
      response = input(question).lower()
      
      if response == "yes" or response == "y" or response == "yef":
        response = "yes"
        return response
        
      elif response == "no" or response == "n" or response == "noh":
        response = "no"
        return response
        
      else:
        print("<ERROR>: Please enter either 'YES' or 'NO'\n")
  
        
# [>] INSTRUCTIONS LAYOUT:

def instructions ():
  print()
  print("    <-----| HOW TO USE |----->\n")
  print(" | WELCOME TO THE TIMES-TABLE QUIZ |\n")
  print(""" • You will select a times-table you would like to 
   be tested on (MIN - MAX: 1x-12x) 
 • MAX questions: 50
 • Enter "STATS", at any given time throughout the quiz for information (current Score, remaining Lives, Quit game) \n""")
  return""


# < -- MAIN ROUTINE -- >

# [>] WELCOME INTRODUCTION:
print("Welcome to quizith :P \n")

# [>] ASK USER INPUT: 'HAVE YOU PLAYED BEFORE?':
played_before = yes_no ("Have you participated in this quiz before?: ")

if played_before == "no":
  instructions()

# [>] CONTINUE TO QUIZ:
  print("       --------------------       ")
  input("""> CONTINUE TO QUIZ: <PRESS ENTER>
       --------------------       """)


