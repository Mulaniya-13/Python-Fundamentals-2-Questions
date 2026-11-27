secret_Number = 7

guess = int(input("Enter your guess: "))

if guess < secret_Number:
    print("Your guess is too low.")
elif guess > secret_Number:
    print("Your guess is too high.")
else:
    print("Congratulations! You guessed the number.")