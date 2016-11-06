#sort my things 

#Insertion sort function
# Takes O(n^2) worst-time 

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


#Merge Sort function
# Takes O(nlgn) worst-time algorithm 

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
ans = 'yes'	
while choice == 'yes':
	a = input("Enter the list to be sorted : ")
	a = list(map(int,a.split(" ")))
	print("Choose the Method to sort the numbers : ")
	print("1. Insertion Sort")
	print("2. Merge Sort")
	print("3. Exit")
	choice = int(input("Enter your choice: "))

	print(" Input -> ", a)

	if choice == 1:
		insertion_sort(a)
	elif choice == 2:
		merge_sort(a)
		print(" Output - > ", a)

	ans = input("Do you want to continue ? (yes/no) : ")
	