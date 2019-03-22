'''
Maximise the sum
Send Feedback
Given 2 sorted arrays (in increasing order), find a path through the intersections that produces maximum sum and return the maximum sum.
That is, we can switch from one array to another array only at common elements.
If no intersection element is present, we need to take sum of all elements from the array with greater sum.
Input Format :
 Line 1 : An integer M i.e. size of first array
 Line 2 : M integers which are elements of first array, separated by spaces
 Line 3 : An integer N i.e. size of second array
 Line 4 : N integers which are elements of second array, separated by spaces
Output Format :
Maximum sum value
Constraints :
1 <= M, N <= 10^6
Sample Input :
6
1 5 10 15 20 25
5
2 4 5 9 15
Sample Output :
81
Sample Output Explanation :
We start from array 2 and take sum till 5 (sum = 11). Then we'll switch to array at element 10 and take till 15. So sum = 36. Now, no elements left in array after 15, so we'll continue in array 1. Hence sum is 81
'''


m=int(input())
a=[int(x) for x in input().split()]
n=int(input())
b=[int(x) for x in input().split()]

#approach is similar to merge two sorted array
max_sum,s1,s2,i,j=0,0,0,0,0

while(i<m and j<n):
    if(a[i]<b[j]):
        s1+=a[i]
        i+=1
    elif a[i]>b[j]:
        s2+=b[j]
        j+=1
    else:
        if(s1 > s2):
            max_sum+=s1
        else:
            max_sum+=s2
            max_sum+=a[i]
            (s1,s2)=(0,0)
            (i,j)=(i+1,j+1)
    
while(i<m):
    s1+=a[i]
    i+=1
while(j<n):
    s2+=b[j]
    j+=1
if(s1 >s2):
    max_sum+=s1
else:
    max_sum+=s2
print(max_sum)
      
