import random
name = input("What is your name? ")
print("Good Luck ! ", name)
word = []
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = input()
    # adding the element
    word.append(ele) 
 
print(word)
# Function will choose one random word from this list of words
word = random.choice(word)
print("Guess the characters")
guesses = ''
turns = 12
while turns > 0:
	# counts the number of times a user fails
	failed = 0
	for char in word:
		# comparing that character with
		# the character in guesses
		if char in guesses:
			print(char, end=" ")
		else:
			print("_",end=" ")
			# for every failure 1 will be incremented in failure
			failed += 1
	if failed == 0:
		# user will win the game if failure is 0
		# and 'You Win' will be given as output
		print("\n You Win")
		print("The word is: ", word)
		break

	# if user has input the wrong alphabet then
	# it will ask user to enter another alphabet
	print()
	guess = input("guess a character:")

	# every input character will be stored in guesses
	guesses += guess

	# check input with the character in word
	if guess not in word:
		turns -= 1
		# if the character doesn’t match the word then “Wrong” will be given as output
		print("Wrong")
		# this will print the number of turns left for the user
		print("You have", + turns, 'more guesses')
		if turns == 0:
			print("You Loose")
