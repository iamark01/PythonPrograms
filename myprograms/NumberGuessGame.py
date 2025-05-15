import random
print("Welcome to Number guessing game.\nRules: You have to guess any number between 1 and 100\nLet's play!!")
lucky_number = random.randint(1, 100)
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if (guess >= 1 and guess <= 100):
        break
    else:
        print("Invalid input. Please enter a number within the specified range.")
if guess == lucky_number:
    print("Congratulations!! Your guess ",guess, "is the lucky number")
else:
    print("Sorry, your guess",guess,"is incorrect. The lucky number was ",lucky_number)