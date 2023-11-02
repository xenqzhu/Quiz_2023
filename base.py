# < -- FUNCTIONS -- >

# [>] STARTER INTRODUCTION: (YES / NO):

score = 0 
lives = 0
round = 0

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
 • MAX questions: 20""")
  print("   <------------------------------> \n")
  return""


# < -- MAIN ROUTINE -- >

# [>] WELCOME INTRODUCTION:
print("   <------------------------------>")
print("         WELCOME TO QUIZITH :P ")
print("   <------------------------------> \n")

# [>] ASK USER INPUT: 'HAVE YOU PLAYED BEFORE?':
played_before = yes_no ("Have you participated in this quiz before?: ")

if played_before == "no":
  instructions()

# < -- FUNCTIONS -- >

# [>] ERROR MESSAGE COMPONENT:
def num_check(question):
  error = "<ERROR>: Invalid input. Please enter a whole number. \n "
  try:
    response = int(input(question))
    return response
  except ValueError: 
    print(error)

# [>] LIVE AMOUNT MAX = 10 CHECKER:
Valid = False
while not Valid:
  lives = num_check("Enter Lives amount: ")
  if lives <= 10:
    valid = True
    break
  else:
    print("<ERROR>: Invalid input. Please enter a number between 0-10. \n")

times = num_check("Enter a Times-Table: ")
print()

# [>] LOOP: CALCULATES QUESTIONS (TIMES X NUMBER):
for x in range (1,21):
  round += 1
  print("Question: {}".format(round))
  answer = times * x
  guess = num_check ("What is {} x {}? = ".format(times,x))

  # [>] GUESS = CORRECT OR INCORRECT:
  if guess == answer:
    print("Correct! :D \n")
    score += 1

  else: 
    print("Incorrect :C \n")
    lives -= 1      

  # [>] LIVES AND SCORE CHECKER:
  if lives == 0:
    print("Game Over! \n")
    break
  if score == 20:
    print("   <------------------------------> \n")
    print("Congrats! You completed the quiz!. \n")
    break

# < -- MAIN ROUTINE -- >

# [>] PRINT USERS END GAME STATS:
print("TOTALS STATS: ")
print("Score: {}".format (score))
print("Remaining Lives: {}".format(lives))

print("Thanks for playing! \n")
print("   <------------------------------> \n")
