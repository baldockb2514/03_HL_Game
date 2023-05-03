# checks user response is yes/no to a given question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        response = response.replace(" ", "")

        # If the response is valid, return response
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        # If not, print error
        else:
            print("Please answer yes / no")


while True:
    print()
    check = yes_no("Yes or No? ")

    if check == "yes" or "no":
        print("program continues")

    continue
