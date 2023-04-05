game_summary = []
round_score = []

rounds_lost = 0
rounds_won = 0
rounds_played = 5

for item in range(0, 5):

    result = input("choose result: ")

    if result == "lost":
        rounds_lost += 1
    elif result == "won":
        rounds_won += 1

    round_result = int(input("choose score: "))
    outcome = "Round {}: {}\n Score: {}".format(item, result, round_result)
    game_summary.append(outcome)
    round_score.append(round_result)

# Calculate game stats
percent_win = rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100
highest_score = min(round_score)
lowest_score = max(round_score)
ave_score = (sum(round_score)) / len(round_score)


print()
print("***** Game History *****")
for game in game_summary:
    print(game)

print()

# displays game stats with % values to the nearest whole number
print("******* Game Statistics *******")
print("Win: {}, ({:.0f}%)\nLoss: {}, "
      "({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lost))
print(f"Best Score: {highest_score:.0f}\nWorst Score: {lowest_score:.0f}\nAverage Score: {ave_score:.2f}")
print()
