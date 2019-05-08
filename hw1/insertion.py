import timeit
import random

def insertionSort(array):
	for i in range(1, len(array)):
		val = array[i]
		position = i - 1

		while (position >= 0) and (array[position] > val):
			array[position + 1] = array[position]
			position = position - 1

		array[position + 1] = val


arr = []

varString = input("Enter 'n' values to run: ")
var = int(varString)

for i in range(0, var):
	arr.append(random.randint(0, 10000))

start = timeit.default_timer()	
insertionSort(arr)
stop = timeit.default_timer()

print stop - start
	

