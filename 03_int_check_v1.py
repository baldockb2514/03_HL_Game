# get and check user input
def int_check(question, low=None, high=None):
    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # checks input is not too high or low if both upper and lower bounds are specified
            if situation == "both":
                if response < low or high > high:
                    print(f"Please enter a number between {low} and {high}.")
                    continue

            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print(f"Please enter a number that is lower than (or equal to) {low}")
                    continue


            return response

        # checks input is an integer
        except ValueError:
            print("Please enter a integer. ")
            continue


lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)
guess = int_check("Guess: ", lowest, highest)