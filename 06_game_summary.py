# HL component 6 - scoring system

# rounds won wil be calculated (total - draw - lost - won)
rounds_played = 0
rounds_won = 0
rounds_lost = 0

# results for testing purposes
test_results = ["won", "won", "loss", "loss", "won"]

# Play Game
for item in test_results:
    rounds_played += 1

    # Generate computer choice

    result = item

    if result == "won":
        result = "Won"
        rounds_won += 1
    elif result == "loss":
        result = "Lost"
        rounds_lost += 1


# End of game statements
print()
print("***** End Game Summary *****")
print("Wom: {} \t|\t Lost: {}".format(rounds_won, rounds_lost))
print()
print("Thanks for playing!")
