import timeit
import random

def merge(l, r):
	arr = []
	while len(l) != 0 and len(r) != 0:
		if l[0] < r[0]:
			arr.append(l[0])
			l.remove(l[0])
		else:
			arr.append(r[0])
			r.remove(r[0])
	if len(l) == 0:
		arr += r
	else:
		arr += l
	return arr
	

def mergeSort(arr):
	if len(arr) == 0 or len(arr) == 1:
		return arr
	else:
		mid = len(arr)/2
		l = mergeSort(arr[:mid])
		r = mergeSort(arr[mid:])
	return merge(l, r)


arr = []
varString = input("Enter 'n' values to run: ")
var = int(varString)

for i in range(0, var):
	arr.append(random.randint(0, 10000))

final = []
start = timeit.default_timer()
final = mergeSort(arr)
stop = timeit.default_timer()

print stop - start
	
