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

with open('MSS_Problems.txt') as f:
	for line in f:
		arr.append([int(v) for v in line.split()])

fo = open("MSS_Results.txt", "wb")

#Algorithm 1: Enumeration
fo.writelines("Aglorithm 1: Enumeration" + "\n")
for row in range(0, len(arr)):
	fo.writelines(str(arr[row]) + "\n")
	sortedArr, val = enum(arr[row])
	fo.writelines(str(sortedArr))
	fo.write("\n")
	fo.writelines(str(val))
	fo.write("\n")

#Algorithm 2: Better Enumeration
fo.writelines("Algorithm 2: Better Enumeration" + "\n")
for row in range(len(arr)):
	fo.writelines(str(arr[row]) + "\n")
	sortedArr, val = enum(arr[row])
	fo.writelines(str(sortedArr))
	fo.write("\n")
	fo.writelines(str(val))
	fo.write("\n")

	
fo.close
