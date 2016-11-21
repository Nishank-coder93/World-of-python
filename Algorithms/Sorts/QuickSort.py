#Quick sort 

def partition(alist,first,last):
	pivotValue = alist[first]

	leftmark = first + 1
	rightmark = last

	done = False

	while not done:
		while leftmark <= rightmark and alist[leftmark] < pivotValue :
			leftmark += 1

		while rightmark >= leftmark and alist[rightmark] > pivotValue :
			rightmark -= 1

		if leftmark > rightmark:
			done = True
		else:
			alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]

	alist[rightmark],alist[first] = alist[first],alist[rightmark]

	return rightmark

def QuickSort(alist,first,last):
	if first < last:
		pivot = partition(alist,first,last)
		QuickSort(alist,first,pivot - 1)
		QuickSort(alist,pivot + 1,last)


lst = [54,32,12,55,63,1,33,90,11,7]
print("Before --> ",lst)
QuickSort(lst,0,len(lst) - 1)
print("After --> ", lst)
