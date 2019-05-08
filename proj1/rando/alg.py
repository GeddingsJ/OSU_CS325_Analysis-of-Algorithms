import random
import timeit
import math

def enum(arr):
	subArr = []
	bestTotal = 0

	if len(arr) == 1:
		return arr, arr[0]

	for i in range(len(arr)):
		for j in range(i, len(arr)):
			total = 0
			for k in range(i, j + 1):
				total = total + arr[k]

			if total > bestTotal:
				bestTotal = total
				subArr = arr[i:(j + 1)]

	return subArr, bestTotal

def betterEnum(arr):
	subArr = []
	bestTotal = 0
	
	if len(arr) == 1:
		return arr, arr[0]

	for i in range(len(arr)):
		total = 0
		for j in range(i, len(arr)):
			total = total + arr[j]
			if total > bestTotal:
				bestTotal = total
				subArr = arr[i:(j + 1)]

	return subArr, bestTotal




arr = []
sortedArr = []
val = 0

varString = input("Enter 'n' values to run: ")
var 	  = int(varString)

temp = 0


#for i in range(0, var):
#	arr.append(random.randint(-100, 100))

#Algorithm 1: Enumeration
#start = timeit.default_timer()
#sortedArr, val = enum(arr)
#stop = timeit.default_timer()

#temp = (stop - start)
#print("Algorithm 1: ", temp)


temp = 0
arr = []
for i in range(0, var):
	arr.append(random.randint(-100, 100))


#Algorithm 2: Better Enumeration
start = timeit.default_timer()
sortedArr, val = betterEnum(arr)
stop = timeit.default_timer()

temp = (stop - start)

print("Algorithm 2: ", temp)
