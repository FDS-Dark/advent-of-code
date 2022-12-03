#Strategy Guide

#A Y - A: Opponent plays Rock - Y: You have to make the round a draw by playing paper
#B X - B: Opponent plays Paper - X: You have to make the round a loss by playing rock
#C Z - C: Opponent players Scissors - Z: You have to make the round a win by playing rock

# A/X - Rock
# B/Y - Paper
# C/Z - Scissors

#Values
points = {"X": 1, "Y": 2, "Z": 3}

outcomes = {"X": "LOSE", "Y": "DRAW", "Z": "WIN"}

losses = {"A": "Z", "B": "X", "C": "Y"}

wins = {"A": "Y", "B": "Z", "C": "X"}

draws = {"A": "X", "B": "Y", "C": "Z"}
#Variables
score = 0
count = 0
maxScore = 0

#Read input and convert to list of rounds
with open("input.txt", 'r') as f:
	data = f.read().replace("\n", "").replace(" ", "")
	n = 2
	data = [data[i:i+n] for i in range(0, len(data), n)]

#Awards points per round based off of shape played + outcome determined by the 2nd character in the round 
for item in data:
	print(item)
	if item[1] == "X":
		score += points[losses[item[0]]]
	if item[1] == "Y":
		score += 3 + points[draws[item[0]]]
	if item[1] == "Z":
		score += 6 + points[wins[item[0]]]
	print(f"new score: {score}")

#Final answer
print(score)

