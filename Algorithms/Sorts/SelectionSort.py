#sorting technique: selection sort

def SelectionSort(alist):
	for fillAt in range(len(alist) - 1, 0, -1):
		positionOfMax = 0

		for location in range(1,fillAt + 1):
			if alist[location] > alist[positionOfMax]:
				positionOfMax = location

		alist[fillAt],alist[positionOfMax] = alist[positionOfMax],alist[fillAt]


alist = [54,26,93,17,77,31,44,55,20]
SelectionSort(alist)
print(alist)