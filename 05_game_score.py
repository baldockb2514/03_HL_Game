game_summary = []
round_score = []

rounds_lost = 0
rounds_won = 0
rounds_played = 5
outcome = ()
score = 0
result = ""

for item in range(0, 5):

    round_result = input("choose result: ")

    if round_result == "lost":
        result = "Lost"
        rounds_lost += 1
    elif round_result == "won":
        result = "Won"
        rounds_won += 1
        score = int(input("choose score: "))

    outcome = "Round {}:\n Result: {} Score: {}".format(item, result, score)
    game_summary.append(outcome)
    round_score.append(score)

# Calculate game stats
percent_win = rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100
highest_score = min(round_score)
lowest_score = max(round_score)
ave_score = (sum(round_score)) / len(round_score)


print()
print("***** Game History *****")
for outcome in game_summary:
    print(outcome)

print()

# displays game stats with % values to the nearest whole number
print("******* Game Statistics *******")
print("Win: {}, ({:.0f}%)\nLoss: {}, "
      "({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lost))
print(f"Best Score: {highest_score:.0f}\nWorst Score: {lowest_score:.0f}\nAverage Score: {ave_score:.2f}")
print()
