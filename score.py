# < -- FUNCTIONS -- >

score = 0 
lives = 0

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
for x in range (1,20):
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
    break

print("Score: {}".format (score))
# < -- MAIN ROUTINE -- >