# Functions go here

# statement decoration types
def statement_decorator(statement, decoration, dec_type):
    # Set decoration length
    sides = decoration * 5

    # set decoration types
    # add decoration to start and ent of statement
    if dec_type == "sides":
        statement = "{} {} {}".format(sides, statement, sides)
        print(statement)
    # add decoration to top and bottom of statement
    elif dec_type == "tb":
        tb_dec = decoration * len(statement)
        print(tb_dec)
        print(statement)
        print(tb_dec)
    # add decoration all around statement
    else:
        statement = "{} {} {}".format(sides, statement, sides)
        tb_dec = decoration * len(statement)
        print(tb_dec)
        print(statement)
        print(tb_dec)

    return ""


statement_decorator("Unicorn", "*", "tb")
