import random

#random.randrange(n, n) finds numbers starting at -5 but will not use the last  number (finds 10 not 11)
#random.randint(n, n) will include the last number you put in (will find 11)


#asking user to input a number to  begin game
top_of_range = input("Please type a whole number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range) #converts input str into int

    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time")
        quit()
else:
    print("Please enter a number next time")
    quit()

random_number = random.randint(1, top_of_range) #puts our user input as the top of the range of the number pool
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a number between 0 and " + str(top_of_range) + ": ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number")
        continue #this works like a DC al coda, with the coda being the beginning of the while statement

    if user_guess == random_number:
        print("Well done, you got it!")
        break #this stops the infinite loop

    elif user_guess > random_number:
        print("You need to guess a lower number")
        print()
    else:
        print("You need to guess a higher number")
        print()




print("You got it in", guesses,"guesses")
#print statement adds spaces for each comma, this line = "in " + str(guesses) + " guesses"
