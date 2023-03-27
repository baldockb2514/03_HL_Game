# HL component 5 - no duplicates

secret = 7
guesses_allowed = 5

already_guessed = []
guesses_left = guesses_allowed
num_won = 0

guess = ""

while guess != secret and guesses_left >= 1:

    guess = int(input("Guess: "))   # replace this with function

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print(f"You already guessed that number! Please try again. You *still* have {guesses_left} guesses left")
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:
        if guess < secret:
            print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

        elif guess > secret:
            print("Too high, try a lower number. Guesses left: {}".format(guesses_left))

    else:
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")

if guess == secret:
    if guesses_left == guesses_allowed - 1:
        print(f"Amazing! You got it in one!")
    else:
        print(f"Well done. You got it in {len(already_guessed)}.")
    num_won += 1

elif guesses_left == 0:
    print("Better luck next time.")


