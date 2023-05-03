# Functions go here

def statement_decorator(statement, decoration):

    # Make string with five characters
    sides = decoration * 5

    # add decoration to start and ent of statement
    statement = "{} {} {}".format(sides, statement, sides)
    print(statement)

    return ""


statement_decorator("Unicorn", "*")
