#Guide

#Same as part one, but now checking for similar letters between 3 elves (3 lines)

#Variables
priorities = []

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#List of inputs
with open('input.txt', 'r') as f:
	data = f.read().strip().split("\n")

score = 0

for i in range(3, int(((len(data)-1))+3), 3):
	similarities = []
	line1 = data[i-3]
	line2 = data[i-2]
	line3 = data[i-1]
	for letter in line1:
		if letter in line2 and letter in line3:
			similarities.append(letter)
	nodupes = [*set(similarities)]
	for letter in nodupes:
		priorities.append(letter)

print(priorities)

#Add points for each letter in the priorities list
for item in priorities:
	if item.isupper(): #If letter is uppercase
		print(f"{item} - {uppercase.index(item) + 27}")
		score += uppercase.index(item) + 27 
	else: #If letter is lowercase
		print(f"{item} - {lowercase.index(item) + 1}")
		score += lowercase.index(item) + 1

print(score)
