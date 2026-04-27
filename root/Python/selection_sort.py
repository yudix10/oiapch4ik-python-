def find_smallest_index(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selection_sort(arr):
	NewArr = []
	for i in range(len(arr)):
		smallest = find_smallest_index(arr)
		NewArr.append(arr.pop(smallest))
	return NewArr

print (selection_sort([100, 2, 61, 201, 101]))