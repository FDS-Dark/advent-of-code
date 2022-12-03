with open('input.txt', 'r') as f:
	data = f.read().strip().split('\n')

count = 0
max = 0

for item in data:
	if item == '':
		count = 0
	else:
		count += int(item)

	if count > max:
		max = count

print(max)