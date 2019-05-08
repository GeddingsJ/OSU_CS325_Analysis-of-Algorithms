def insertionSort(array):
	for i in range(1, len(array)):
		val = array[i]
		position = i - 1

		while (position >= 0) and (array[position] > val):
			array[position + 1] = array[position]
			position = position - 1

		array[position + 1] = val


arr = []

with open('data.txt') as f:
	for line in f:
		arr.append([int(v) for v in line.split()])

fo = open("insertion.out", "wb")
for sub in range(0, len(arr)):
	insertionSort(arr[sub])
	fo.writelines(str(arr[sub]))
	fo.write("\n")

fo.close()
