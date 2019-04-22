
def shellSort(arr):
	n=len(arr)
	gap=n//2
	while(gap >=1):
		for i in range(gap,n,1):
			temp=arr[i]
			j=i
			while(j-gap >=0 and arr[j-gap] > temp):
				arr[j]=arr[j-gap]
				j=j-gap
			arr[j]=temp
		gap=gap//2

arr=[11,2,11,3,7,5678,11,2121,12123,6789,9,15,5,19]
shellSort(arr)
print(arr)