#Sorting Technique: Merge Sort


#Merge Sort function
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

alist = [54,26,93,55,17,31,44,55,20]
print("Input --> ",alist)
merge_sort(alist)
print("Output --> ",alist)