def countingSort(A):
	k=-1000000
	n=len(A)
	for i in range(n):
		if k < A[i]:
			k=A[i]

	k=k+1
	# auxiliary arrays
	B=[0]*n
	C=[0]*k

	#store frequency (count of each element) 
	for i in range(n):
		C[A[i]]=C[A[i]]+1

	# store commulative frequency (current_count + previous_count)
	# after this loop execution , C[i] = total number of elements which are less than or equal to i is C[i]
	for i in range(1,k):
		C[i]+=C[i-1]

	# fill array B as soted array
	for i in range(n):
		B[C[A[i]]-1]=A[i]
		C[A[i]]-=1

	return B


arr=[1,1,8,1,2,11,6,6,3,9,3,2,11,4,12,7,2,0,0]

output_arr=countingSort(arr)
print(output_arr)
