"""

 This program sorts a list of numbers choosing from various 
 Sorting Algorithms : 
 - Bubble Sort
 - Insertion Sort 
 - Selection Sort
 - Merge Sort 
 - Quick Sort 

"""

#Bubble Sort
# Takes O(n^2) worst-case running time
def BubbleSort(alist):
	for i in range(0,len(alist)):
		min = alist[i]
		for j in range(i+1,len(alist)):
			if alist[j] < min:
				min = alist[j]
				alist[i],alist[j] = alist[j],alist[i]
		print(alist)   #prints every line after swapping is complete in one round

#end of bubble sort 

#Insertion sort function
# Takes O(n^2) worst-case running time 

def insertion_sort(ls):
	for i in range(1,len(ls)):
		key = ls[i]
		j = i - 1
		while j >= 0 and ls[j] > key :
			ls[j+1] = ls[j]
			j = j - 1
		ls[j+1] = key
	print(" Output -> ", ls)

#End of insertion sort


# Selection Sort function 
# Takes O(n^2) worst case running time 

def SelectionSort(alist):
	for fillAt in range(len(alist) - 1, 0, -1):
		positionOfMax = 0

		for location in range(1,fillAt + 1):
			if alist[location] > alist[positionOfMax]:
				positionOfMax = location

		alist[fillAt],alist[positionOfMax] = alist[positionOfMax],alist[fillAt]

# End of Selection Sort 

# Merge Sort function
# Takes O(nlgn) worst-case running time  

def merge(ls,lefthalf,righthalf):
	k = 0
	i = 0
	j = 0


	while i < len(lefthalf) and j < len(righthalf):
		if lefthalf[i] <= righthalf[j]:
			ls[k] = lefthalf[i]
			i = i + 1
		elif righthalf[j] < lefthalf[i]:
			ls[k] = righthalf[j]
			j = j + 1
		k = k + 1

	while i < len(lefthalf):
		ls[k] = lefthalf[i]
		i = i + 1
		k = k + 1

	while j < len(righthalf):
		ls[k] = righthalf[j]
		j = j + 1
		k = k + 1


def merge_sort(ls):
	if len(ls) > 1:
		mid = (len(ls))//2
		lefthalf = ls[:mid]
		righthalf = ls[mid:]
		merge_sort(lefthalf)
		merge_sort(righthalf)
		merge(ls,lefthalf,righthalf)

# End of Merge sort 

# Quick Sort function
# Best case takes O(nlgn), worst case takes O(n^2)
# Advantage of Quick sort over Merge sort it doesn't take as much memory as Merge does
# Using variations of Quick sort we can always get O(nlgn) eg. Three Median technique

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

def QuickSortRecurse(alist,first,last):
	if first < last:
		pivot = partition(alist,first,last)
		QuickSortRecurse(alist,first,pivot - 1)
		QuickSortRecurse(alist,pivot + 1,last)

def QuickSort(alist):
	QuickSortRecurse(alist,0,len(alist) - 1)

# End of quick sort function 


a = input("Enter the list to be sorted (eg. 24 98 56 73 55 12): ")

ans = 'no'	
while ans == 'no':
	print("Choose the Method to sort the numbers : ")
	print("1. Insertion Sort")
	print("2. Merge Sort")
	print("3. Bubble Sort")
	print("4. Selection Sort")
	print("5. Quick Sort ")
	print("6. Exit")
	choice = int(input("Enter your choice: "))

	print(" Input -> ", list(map(int,a.split(" "))))

	if choice == 1:
		#Insertion Sort
		toSort = list(map(int,a.split(" ")))
		insertion_sort(toSort)
	elif choice == 2:
		#Merge Sort
		toSort = list(map(int,a.split(" ")))
		merge_sort(toSort)
		print(" Output - > ", toSort)
	elif choice == 3:
		#Bubble Sort 
		toSort = list(map(int,a.split(" ")))
		BubbleSort(toSort)
		print("Output -> ", toSort)
	elif choice == 4:
		#Selection Sort 
		toSort = list(map(int,a.split(" ")))
		SelectionSort(toSort)
		print("Output -> ", toSort)
	elif choice == 5:
		#Quick Sort 
		toSort = list(map(int,a.split(" ")))
		QuickSort(toSort)
	elif choice == 6:
		ans = input("Are you sure you want to exit ? (yes/no) : ")

		if ans != 'yes' or ans != 'YES' or ans != 'no' or ans != 'NO':
			ans = input("Wrong input ! Try again \n Are you sure you want to exit ? (yes/no) : ")
	