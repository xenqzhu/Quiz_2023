# < -- FUNCTIONS -- >

round = 0

def num_check(question):
  error = "<ERROR> Invalid input. Please enter a whole number. "
  try:
    response = int(input(question))
    return response
  except ValueError: 
    print(error)

times = num_check("Enter a Times-Table: ")
print()

for x in range (1,20):
  round += 1
  print("Question: {}".format(round))
  answer = times * x
  guess = num_check ("What is {} x {}? = ".format(times,x))

  if guess == answer:
    print("Correct! :D \n")
  else: 
    print("Incorrect :C \n")

# < -- MAIN ROUTINE -- >
