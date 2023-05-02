# get and check user input
def int_check(question, low=None, high=None):
    situation = ""

    # if low and high
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # checks guess input is not too high or low if both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high}.")
                    continue

            # checks high number is not too low
            elif situation == "low only":
                if response < low:
                    print(f"Please enter a number that is higher than (or equal to) {low}")
                    continue

            return response

        # checks input is an integer
        except ValueError:
            print("Please enter a integer. ")
            continue


lowest = int_check("Lower Parameter: ")
highest = int_check("Higher Parameter: ", lowest + 1)
guess = int_check("Between Parameters: ", lowest, highest)
print("Program continues")
