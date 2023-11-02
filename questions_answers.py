# < -- FUNCTIONS -- >

# [>] ERROR MESSAGE COMPONENT:
def num_check(question):
  error = "<ERROR> Invalid input. Please enter a whole number. "
  try:
    response = int(input(question))
    return response
  except ValueError: 
    print(error)

times = num_check("Enter a Times-Table: ")
print()

# [>] LOOP: CALCULATES QUESTIONS (TIMES X NUMBER):
for x in range (1,20):
  answer = times * x
  guess = num_check ("What is {} x {}? = ".format(times,x))

  # [>] ANSWER CHECKER:
  if guess == answer:
    print("Correct! :D \n")
  else: 
    print("Incorrect :C \n")

# < -- MAIN ROUTINE -- >

