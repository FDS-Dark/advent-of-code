#Strategy Guide

#A Y - A: Opponent plays Rock - B: You play Paper
#B X - B: Opponent plays Paper - X: You play Rock
#C Z - C: Opponent players Scissors - Z: You play scissors

# A/X - Rock
# B/Y - Paper
# C/Z - Scissors

#Point Values
points = {"AX": 3, "BX": 0, "CX": 6, "AY": 6, "BY": 3, "CY": 0, "AZ": 0, "BZ": 6, "CZ": 3}

#Variables
score = 0
count = 0
maxScore = 0

#Read input and convert to list of rounds
with open("input.txt", 'r') as f:
	data = f.read().replace("\n", "").replace(" ", "")
	n = 2
	data = [data[i:i+n] for i in range(0, len(data), n)]

#Awards points per round based off of shape played + outcome 
for item in data:
	if "X" in item:
		score += 1
	elif "Y" in item:
		score += 2
	elif "Z" in item:
		score += 3

	score += points[item]

#Final answer
print(score)

