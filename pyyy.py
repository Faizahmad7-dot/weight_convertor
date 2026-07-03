secretNumber = 8
guessCount = 0
guessLimit = 3

while guessCount < guessLimit:
    number = int(input("Enter the secret number: "))
    guessCount += 1
    if number == secretNumber:
        print("You won.")
        break
    elif guessCount == guessLimit:
        print("You've reached the limit.")
    elif number != secretNumber:
        print("try again!")




