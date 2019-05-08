import math
import timeit
import random

#def stooge(arr, lo, hi):
def stooge(arr):
	if arr[0] > arr[-1] and len(arr) == 2:				#If first is greater than last
		arr[0], arr[-1] = arr[-1], arr[0]	#Swap first and last element
		
	if len(arr) > 2:
		m = int(math.ceil((len(arr) / 3))) 	#Get ceiling of 1/3 position
		n = len(arr) - m			#Get 2/3 position

		arr[:n] = stooge(arr[:n])		#Store in position [0 .. n] and recursive call
		arr[m:] = stooge(arr[m:])		#Store in position [m .. end] and recursive call
		arr[:n] = stooge(arr[:n])
	return arr

array = []
finalArr = []

varString = input("Enter 'n' values to run: ")
var 	  = int(varString)

for i in range(0, var):
	array.append(random.randint(0, 10000))

start = timeit.default_timer()
finalArr = stooge(array);
stop  = timeit.default_timer()

print stop - start
