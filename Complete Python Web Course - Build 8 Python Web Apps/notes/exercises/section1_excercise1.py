# Create a variable that holds a "magic number" between 0 and 10
# Tell the user to pick a number between 0 and 10
# If the user picks the "magic number", tell them they've won
# Else, tell them to run the program again

magic_number = 5

def user_number():
	number = input("Pick a number between 0 and 10: ")
	return int(number)


def decision():
  #print(magic_number) ~ was a test to make sure this was the magic_number

  if (user_number() == magic_number) == True:
    print("You've won!") 
  else:
    print("Run the program again")
		

decision()