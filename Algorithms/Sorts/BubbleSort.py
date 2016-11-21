#sorting technique: Bubble Sorting.
"""
it is the worst sorting algorithem to implement 
is not practical at all. 
Takes: O(n^2) worst running time 
"""

def BubbuleSort(alist):
	for i in range(0,len(alist)):
		min = alist[i]
		for j in range(i+1,len(alist)):
			if alist[j] < min:
				min = alist[j]
				alist[i],alist[j] = alist[j],alist[i]
		print(alist)   #prints every line after swapping is complete in one round

alist = [54,26,93,17,31,44,55,20]
BubbuleSort(alist)
print(alist)