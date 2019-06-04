

from math import factorial

def binomial_coefficient(i,j):
    return factorial(i)//(factorial(i-j)*factorial(j))



# def pascal_triangle(n):
#     for i in range(0,n):
#         for j in range(0,i+1):
#             k=binomial_coefficient(i,j)
#             print(k,end=" ")
#         print()
# 



# def pascal_triangle(n):
#     for j in range(0,n):
#         k=binomial_coefficient(n-1,j)
#         print(k,end=" ")
#     print()


# def pascal_triangle(n):
#     ans=[[0]*(50) for i in range(50)]
#     ans[0][0]=1
#     ans[1][0]=1
#     ans[1][1]=1
#     for i in range(2,n):
#         for j in range(i+1):
#             if(j==0 or j==i):
#                 ans[i][j]=1
#             else:
#                 ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
#     for i in range(n):
#         for j in range(n):
#         	print(ans[i][j],end=" ")


def pascal_triangle(n):
    # using property
    # nCr= { (nCr-1)*(n-r+1) }/(r)
    
    for i in range(n):
        prev=1;
        print(prev,end=" ")
        for j in range(1,i+1):
            k=(prev * (i-j+1))//j
            print(k,end=" ")
            prev=k
        print()
        


t=int(input())
while t:
    t-=1
    n=int(input())
    pascal_triangle(n)
    