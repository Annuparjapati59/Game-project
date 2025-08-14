while True:
  import random
  Cnumber=random.randrange(1,101)
  userInput=int(input("enter your number:---"))
  if userInput>Cnumber:
     print("computer number",Cnumber)
     print("your guess number is too high")
  elif Cnumber>userInput:
     print("computer number",Cnumber)
     print("your guess number is too low")
  else:
     print("computer number",Cnumber)
     print("your guess number is equal")

    
    
