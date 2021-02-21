'''In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
The computer makes guesses, and you give it input - is its guess too high or too low?
Using bisection search, the computer will guess the user's secret number!'''

print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = (low + high )//2
while(True):
    print("Is your secret number " + str(guess) + "?")
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if (user_input != "h" and user_input != "l" and user_input != "c"):
         print("Sorry, I did not understand your input.")

    if (user_input == "h"):
        high = guess
        guess = (low + high)//2

    if (user_input == "l"):
        low = guess
        guess = (low + high) // 2

    if (user_input == "c"):
        print("Game over. Your secret number was: " + str(guess))
        break







