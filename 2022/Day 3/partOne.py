#Guide

#Each input is a list of contents from one rucksack
#The sack will be deviced into two compartments, exactly in half
#After splitting in half, check each compartment for an item in both compartments
#The item in both compartments will have a priority value based on the capitalization
#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.
#The answer is the sum of the priorities at the end of the input list

#Variables
priorities = []

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#List of inputs
with open('input.txt', 'r') as f:
	data = f.read().strip().split("\n")

score = 0

for item in data: #Split the lists in half
	similarities = []
	splitVal = int(((len(item))/2))
	halfOne = item[0:splitVal]
	halfTwo = item[splitVal:len(item)]
	for letter in halfOne: #Check for duplicate letters in the two strings
		if letter in halfTwo:
			similarities.append(letter)
	nodupes = [*set(similarities)] #Remove duplicates from similarities list (using set as order does not matter)
	for letter in nodupes: #Append letters in nodupes list to the master priorities list
		priorities.append(letter)

#Add points for each letter in the priorities list
for item in priorities:
	if item.isupper(): #If letter is uppercase
		print(f"{item} - {uppercase.index(item) + 27}")
		score += uppercase.index(item) + 27 
	else: #If letter is lowercase
		print(f"{item} - {lowercase.index(item) + 1}")
		score += lowercase.index(item) + 1

print(score)
		