# < -- FUNCTIONS -- >

from random import randint

while True:
  num1 = randint(2,9)
  num2 = randint(2,9)   
  product = num1 * num2
  response = int(input(f"{num1} x {num2}?: "))
  if not response:
    break
 
  ans = int(response)
  print('Correct! :D \n' if ans == product else 'Incorrect...:C \n')

  # < -- MAIN ROUTINE -- >

