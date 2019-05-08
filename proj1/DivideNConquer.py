import random
import timeit
import math
import numpy
import time


def DivideNConquer(arr):
    maxLeft = 0
    leftTemp = 0
    maxRight = 0
    rightTemp = 0
    middle = int((len(arr)) / 2)
    midS = 0
    midE = 0

    if len(arr) == 1:
	return arr[0], arr
    if len(arr) == 0:
	return 0, arr
    
    for i in reversed(range(middle)):
	leftTemp = leftTemp + arr[i]
	if leftTemp > maxLeft:
		maxLeft = leftTemp
		midS = i

    for i in range(middle, len(arr) - 1):
	rightTemp = rightTemp + arr[i]
	if rightTemp > maxRight:
		maxRight = rightTemp
		midE = i + 1

    maxMiddle = maxLeft + maxRight
    
    leftMax, leftSub = DivideNConquer(arr[:middle])
    rightMax, rightSub = DivideNConquer(arr[middle:])

    if leftMax >= rightMax and leftMax > maxMiddle:
		return leftMax, leftSub
    elif rightMax >= leftMax and rightMax > maxMiddle:
		return rightMax, rightSub
    else:
		return maxMiddle, arr[midS : midE]

arr = []
sortedArr = []
val = 0


with open('MSS_Problems.txt') as f:
    for line in f:
        arr.append([int(v) for v in line.split()])

fo = open("MSS_TResults.txt", "wb")

#Divide and Conquer File i/o
start_time = time.clock()
fo.writelines("Divide and Conquer:" "\n")
for row in range(0, len(arr)):
    fo.writelines(str(arr[row]) + "\n")
    val, sortedArr = DivideNConquer(arr[row])
    fo.writelines(str(sortedArr))
    #fo.write("\n")
    fo.writelines("Maximum subarray: ")
    fo.writelines(str(val))
    fo.write("\n")

fo.close
