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

with open('data.txt') as f:
	for line in f:
		arr.append([int(v) for v in line.split()])

fo = open("merge.out", "wb")
for sub in range(0, len(arr)):
	final = []
	final = mergeSort(arr[sub])
	fo.writelines(str(final))
	fo.write("\n")

fo.close()
