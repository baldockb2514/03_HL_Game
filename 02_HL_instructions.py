# Functions go here...
def yes_no(question):

    valid = False
    while not valid:
        response = input(question).lower()
        response = response.replace(" ", "")

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


# Main routine goes here...
print()
see_instructions = yes_no("Would you like to see the instructions? ")

if see_instructions == "yes":
    instructions()

print("Program continues")

