#insertion sort 


def insertion_sort(ls):
	for i in range(1,len(ls)):
		key = ls[i]
		j = i - 1
		while j >= 0 and ls[j] > key :
			ls[j+1] = ls[j]
			j = j - 1
		ls[j+1] = key
	print(" Output -> ", ls)

if __name__ == '__main__':
	a = input("Enter the list to be sorted : ")
	a = list(map(int,a.split(" ")))

	print(" Input -> ", a)
	insertion_sort(a)	