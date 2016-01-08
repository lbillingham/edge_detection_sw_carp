def count_rings(array):
	"""
	Input: Line (as array) through 2D edge array
	Output: Number of rings (not edges)
	count=0
	"""
	for i in range(array.size-1):
		if array[i]==1 and array[i+1]==0:
			count=count+1
	if (count%2)==1:
		count=count+1
	return count
	
	
