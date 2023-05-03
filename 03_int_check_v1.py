# Check if a number is an Integer within specified bounds
def int_check(question, low=None, high=None, exit_code=None):
    situation = ""

    # set the situation depending on what parameters were entered
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        # Allow "" and the exit code to be a valid input
        response = input(question)
        if exit_code is not None:
            if response == "":
                return response
            if response == exit_code:
                return response

        try:
            response = int(response)

            # checks guess input is not too high or low if both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high}.")
                    continue

            # checks if a number is higher than low if only lower bounds are specified
            elif situation == "low only":
                if response < low:
                    print(f"Please enter a number that is higher than (or equal to) {low}")
                    continue

            return response

        # If input it not an integer, print error and ask question again
        except ValueError:
            print("Please enter a integer. ")
            continue


lowest = int_check("Lower Parameter: ")
highest = int_check("Higher Parameter: ", lowest + 1)
guess = int_check("Between Parameters: ", lowest, highest)
print("Program continues")
