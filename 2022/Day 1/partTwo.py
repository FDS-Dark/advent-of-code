with open('input.txt', 'r') as f:
	data = f.read().strip().split('\n')

count = 0
max = 0
max2 = 0
max3 = 0

for item in data:
	if item == '':
		count = 0
	else:
		count += int(item)

	if count > max:
		max3 = max2
		max2 = max
		max = count
	elif count > max2:
		max3 = max2
		max2 = count
	elif count > max3:
		max3 = count

print(max+max2+max3)
